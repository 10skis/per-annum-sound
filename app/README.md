# Pi Radio app

Control service and web app for Pi Radio. See `../SCOPE.md` for the full design.

| File | What it does |
|---|---|
| `server.py` | Control service and web endpoints |
| `player.py` | Playback: MPD, or a silent mock when MPD isn't running |
| `nts.py` | NTS live show info and mixtape details |
| `art.py` | Dithers art to the 128×128 amber image both screens use |
| `stations.yaml` | The station list, in dial order |
| `static/` | The web app |

## Run on the Mac

```
python3 -m venv .venv && .venv/bin/pip install fastapi uvicorn python-mpd2 pyyaml httpx pillow   # first time only
./run.sh
```

Open http://localhost:8080. On the iPhone, on the same Wi-Fi, open http://RW-FlowX.local:8080 in Safari, then Share → Add to Home Screen.

Without MPD the app runs on a mock player with no sound. To hear it, install Homebrew and MPD, then start MPD before `run.sh`:

```
brew install mpd
mpd dev/mpd.conf
```

## Adding a station

Add a line under "Elsewhere" in `stations.yaml` with an id, name, place and stream URL (find streams at radio-browser.info), then restart `run.sh`.
