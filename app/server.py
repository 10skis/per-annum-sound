"""Pi Radio control service. One source of truth for what's playing; the web app and,
later, the physical controls both drive it through these endpoints.

Run:  .venv/bin/uvicorn server:app --host 0.0.0.0 --port 8080
Env:  PLAYER=mpd|mock (default: MPD if reachable, else mock), MPD_HOST, MPD_PORT
"""

import hashlib
import json
import logging
import os
from pathlib import Path

import yaml
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import art
import nts
from player import make_player

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

HERE = Path(__file__).parent
STATE_FILE = HERE / "state.json"

GROUPS = yaml.safe_load((HERE / "stations.yaml").read_text())["groups"]
STATIONS = [dict(s, group=g["name"]) for g in GROUPS for s in g["stations"]]
BY_ID = {s["id"]: s for s in STATIONS}

player = make_player(os.getenv("PLAYER"), os.getenv("MPD_HOST", "localhost"), int(os.getenv("MPD_PORT", "6600")))


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
        info = nts.mixtape(station["id"])
        info["title"] = info.get("subtitle", "")
        info["subtitle"] = "Infinite Mixtape"
    else:
        info = {"title": stream_title or "", "subtitle": station.get("place", ""), "art": station.get("art")}
    return {"title": info.get("title", ""), "subtitle": info.get("subtitle", ""), "art": info.get("art")}


app = FastAPI(title="Pi Radio")


@app.get("/api/stations")
def stations():
    return [{"name": g["name"], "stations": [{"id": s["id"], "name": s["name"]} for s in g["stations"]]} for g in GROUPS]


@app.get("/api/state")
def state():
    st = player.status()
    # MPD may have been changed by something else (moOde's own UI); follow it if we know the URL.
    if st["url"]:
        match = next((s["id"] for s in STATIONS if s["url"] == st["url"]), None)
        if match and match != current:
            _set_current(match)
    station = BY_ID[current]
    now = now_playing(station, st.get("title"))
    art_key = hashlib.sha1((now["art"] or station["name"]).encode()).hexdigest()[:10]
    return {
        "station": {"id": station["id"], "name": station["name"], "group": station["group"]},
        "playing": st["playing"],
        "volume": st["volume"],
        "player": player.name,
        "now": {"title": now["title"], "subtitle": now["subtitle"]},
        "art": f"/api/art/{station['id']}?v={art_key}",
    }


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
    png = (art.dither(url) if url else None) or art.placeholder(station["name"])
    return Response(png, media_type="image/png", headers={"Cache-Control": "public, max-age=86400"})


app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")


@app.get("/")
def index():
    return FileResponse(HERE / "static" / "index.html")


@app.get("/manifest.webmanifest")
def manifest():
    return FileResponse(HERE / "static" / "manifest.webmanifest", media_type="application/manifest+json")
