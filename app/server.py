"""Per Annum Sound control service (the Pi Radio project). One source of truth for what's playing; the web app and,
later, the physical controls both drive it through these endpoints.

Run:  .venv/bin/uvicorn server:app --host 0.0.0.0 --port 8080
Env:  PLAYER=mpd|mock (default: MPD if reachable, else mock), MPD_HOST, MPD_PORT,
      VIS_FIFO (default /tmp/pi-radio.fifo, the FIFO output in dev/mpd.conf)
"""

import hashlib
import json
import logging
import os
import threading
import time
from collections import deque
from datetime import datetime
from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import art
import catalog
import nts
from player import make_player
from vis import Spectrum

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

HERE = Path(__file__).parent
STATE_FILE = HERE / "state.json"
HISTORY_FILE = HERE / "history.json"

GROUPS = catalog.load(HERE / "stations.yaml")["groups"]
STATIONS = [dict(s, group=g["name"]) for g in GROUPS for s in g["stations"]]
BY_ID = {s["id"]: s for s in STATIONS}

player = make_player(os.getenv("PLAYER"), os.getenv("MPD_HOST", "localhost"), int(os.getenv("MPD_PORT", "6600")))
spectrum = Spectrum(os.getenv("VIS_FIFO", "/tmp/pi-radio.fifo"))


def _load_current() -> str:
    try:
        sid = json.loads(STATE_FILE.read_text()).get("station")
        if sid in BY_ID:
            return sid
    except Exception:
        pass
    return STATIONS[0]["id"]


current = _load_current()


def _set_current(sid: str) -> None:
    global current
    current = sid
    STATE_FILE.write_text(json.dumps({"station": sid}))


def now_playing(station: dict, stream_title=None) -> dict:
    kind = station["kind"]
    if kind == "nts_live":
        info = nts.live_now(station["channel"])
    elif kind == "nts_mixtape":
        mix = nts.mixtape(station["id"])
        info = {"title": mix.get("subtitle", ""), "subtitle": "Infinite Mixtape",
                "description": mix.get("description", ""), "art": mix.get("art")}
    else:
        info = {"title": stream_title or "", "subtitle": station.get("place", ""),
                "description": station.get("about", ""), "art": station.get("art")}
    return {
        "title": info.get("title", ""),
        "subtitle": info.get("subtitle", ""),
        "description": info.get("description", ""),
        "genres": info.get("genres", []),
        "start": info.get("start"),
        "end": info.get("end"),
        "art": info.get("art"),
    }


# Stream format, read once per station from the stream's Content-Type.
_codecs = {}


def _codec(station: dict) -> str:
    url = station["url"]
    if url not in _codecs:
        codec = ""
        if ".m3u8" in url:
            codec = "HLS"
        else:
            try:
                with httpx.stream("GET", url, timeout=3, follow_redirects=True) as r:
                    ctype = r.headers.get("content-type", "")
                codec = "MP3" if "mpeg" in ctype else "AAC" if "aac" in ctype else "OGG" if "ogg" in ctype else ""
            except Exception:
                pass
        _codecs[url] = codec
    return _codecs[url]


def _signal(station: dict, st: dict) -> dict:
    rate = bits = channels = None
    if st.get("audio"):
        parts = st["audio"].split(":")
        if len(parts) == 3:
            rate, bits, channels = parts
    return {
        "codec": _codec(station),
        "kbps": int(st["bitrate"]) if st.get("bitrate") and st["bitrate"].isdigit() and st["bitrate"] != "0" else None,
        "khz": round(int(rate) / 1000, 1) if rate and rate.isdigit() else None,
        "channels": int(channels) if channels and channels.isdigit() else None,
    }


# Recently played: a background check every 15 s logs each new show or track while playing.
_history = deque(maxlen=50)
_history_lock = threading.Lock()
try:
    _history.extend(json.loads(HISTORY_FILE.read_text()))
except Exception:
    pass


def _log_history():
    while True:
        try:
            st = player.status()
            if st["playing"]:
                station = BY_ID[current]
                title = now_playing(station, st.get("title"))["title"]
                with _history_lock:
                    last = _history[0] if _history else None
                    if not last or last["station"] != station["name"] or last["title"] != title:
                        _history.appendleft({"at": datetime.now().astimezone().isoformat(timespec="seconds"),
                                             "station": station["name"], "title": title})
                        HISTORY_FILE.write_text(json.dumps(list(_history)))
        except Exception as e:
            logging.warning("History check failed: %s", e)
        time.sleep(15)


threading.Thread(target=_log_history, daemon=True).start()


app = FastAPI(title="Per Annum Sound")


@app.get("/api/stations")
def stations():
    def sub(s):
        if s["kind"] == "nts_mixtape":
            return nts.mixtape(s["id"]).get("subtitle", "")
        if s["kind"] == "radio":
            return " · ".join(x for x in (s.get("genre"), s.get("place")) if x)
        return ""  # NTS live: the page fills this from the schedule
    keep = ("id", "name", "url", "kind", "place", "geo", "city", "info")
    return [{"name": g["name"], "stations": [{**{k: s[k] for k in keep if k in s}, "sub": sub(s)}
                                             for s in g["stations"]]}
            for g in GROUPS]


@app.get("/api/state")
def state():
    st = player.status()
    # MPD may have been changed by something else (moOde's own UI); follow it if we know the URL.
    if st["url"]:
        match = next((s["id"] for s in STATIONS if s["url"] == st["url"]), None)
        if match and match != current:
            _set_current(match)
    return {**_describe(BY_ID[current], st), "playing": st["playing"], "volume": st["volume"], "player": player.name}


def _describe(station: dict, st: dict) -> dict:
    now = now_playing(station, st.get("title"))
    art_key = hashlib.sha1((now["art"] or station["name"]).encode()).hexdigest()[:10]
    return {
        "station": {"id": station["id"], "name": station["name"], "group": station["group"], "url": station["url"]},
        "now": {k: now[k] for k in ("title", "subtitle", "description", "genres", "start", "end")},
        "signal": _signal(station, st),
        "art": f"/api/art/{station['id']}?v={art_key}",
    }


@app.get("/api/now/{sid}")
def now_for(sid: str):
    """What's on a station, without touching the radio. Used when the phone plays the stream itself."""
    if sid not in BY_ID:
        raise HTTPException(404, "Unknown station")
    return _describe(BY_ID[sid], {})


@app.get("/api/schedule")
def schedule():
    return {"NTS 1": nts.schedule("1"), "NTS 2": nts.schedule("2")}


@app.get("/api/history")
def history():
    with _history_lock:
        return list(_history)[:20]


@app.get("/api/spectrum")
def spectrum_levels():
    return spectrum.levels()


@app.post("/api/play/{sid}")
def play(sid: str):
    if sid not in BY_ID:
        raise HTTPException(404, "Unknown station")
    player.play(BY_ID[sid]["url"])
    _set_current(sid)
    return state()


@app.post("/api/toggle")
def toggle():
    if player.status()["playing"]:
        player.stop()
        return state()
    return play(current)


@app.post("/api/stop")
def stop():
    player.stop()
    return state()


@app.post("/api/step/{direction}")
def step(direction: int):
    """The dial: +1 or -1 through the station list, wrapping round."""
    ids = [s["id"] for s in STATIONS]
    i = (ids.index(current) + (1 if direction > 0 else -1)) % len(ids)
    return play(ids[i])


class Volume(BaseModel):
    value: int


@app.post("/api/volume")
def volume(v: Volume):
    player.set_volume(v.value)
    return state()


@app.get("/api/art/{sid}")
def station_art(sid: str):
    station = BY_ID.get(sid)
    if not station:
        raise HTTPException(404, "Unknown station")
    url = now_playing(station)["art"]
    style = "logo" if station["kind"] == "radio" else "halftone"  # radio stations' art is their logo
    png = (art.dither(url, style) if url else None) or art.placeholder(station["name"])
    return Response(png, media_type="image/png", headers={"Cache-Control": "public, max-age=86400"})


app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")


@app.get("/")
def index():
    return FileResponse(HERE / "static" / "index.html")


@app.get("/manifest.webmanifest")
def manifest():
    return FileResponse(HERE / "static" / "manifest.webmanifest", media_type="application/manifest+json")
