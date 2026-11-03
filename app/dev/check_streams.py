"""Server-side check of the station list and every stream. Run from app/:

    .venv/bin/python dev/check_streams.py

Checks stations.yaml (duplicate ids, HTTPS, places with coordinates and time zones), then
fetches the first 8 KB of every stream in parallel. HLS playlists are read for an
#EXT-X-ERROR line, which is how a station that is off air (The Lot between shows) answers.
Prints only what needs a look; exit code 1 if anything does. NTS channels and mixtapes have
no genre or profile in the file on purpose (they come live from NTS), and "Online" stations
have no place on the map, so those aren't reported.
"""

import collections
import concurrent.futures
import sys
from pathlib import Path

import httpx
import yaml

HERE = Path(__file__).resolve().parent.parent
data = yaml.safe_load((HERE / "stations.yaml").read_text())
stations = [s for g in data["groups"] for s in g["stations"]]
problems = []

for sid, n in collections.Counter(s["id"] for s in stations).items():
    if n > 1:
        problems.append((sid, f"id used {n} times"))
for s in stations:
    url, place = s.get("url", ""), s.get("place")
    if url and not url.startswith("https://"):
        problems.append((s["id"], "stream is not HTTPS (the Netlify page can't play it)"))
    if place and place != "Online":
        if place not in data.get("places", {}):
            problems.append((s["id"], f"place {place!r} has no coordinates"))
        if place not in data.get("timezones", {}):
            problems.append((s["id"], f"place {place!r} has no time zone"))
    if s.get("kind") == "radio" and not s.get("genre"):
        problems.append((s["id"], "no genre"))


def check(s):
    url = s.get("url")
    if not url:
        return None
    try:
        with httpx.stream("GET", url, timeout=10, follow_redirects=True,
                          headers={"User-Agent": "Mozilla/5.0"}) as r:
            body = b""
            for chunk in r.iter_bytes():
                body += chunk
                if len(body) > 8000:
                    break
        ctype = r.headers.get("content-type", "")
        if r.status_code != 200:
            return f"HTTP {r.status_code}"
        if b"#EXT-X-ERROR" in body:
            line = body.split(b"#EXT-X-ERROR:")[1].split(b"\n")[0].decode(errors="replace").strip()
            return f"playlist refused: {line} (off air?)"
        if "mpegurl" not in ctype.lower() and len(body) < 8000:
            return f"only {len(body)} bytes of {ctype or 'unknown type'}"
    except Exception as e:
        return f"{type(e).__name__}: {e}"[:120]
    return None


with concurrent.futures.ThreadPoolExecutor(16) as ex:
    for s, err in zip(stations, ex.map(check, stations)):
        if err:
            problems.append((s["id"], err))

print(f"{len(stations)} stations checked.")
for sid, msg in problems:
    print(f"  {sid}: {msg}")
print("All clear." if not problems else f"{len(problems)} to look at.")
sys.exit(1 if problems else 0)
