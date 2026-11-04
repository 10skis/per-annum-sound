# Per Annum Sound app

Control service and web app for Per Annum Sound (the Pi Radio project; renamed 2026-11-02). Before changing anything, read `../HANDOFF.md`: the design rules and the traps already hit. See `../SCOPE.md` for the full design.

| File | What it does |
|---|---|
| `server.py` | Control service and web endpoints |
| `player.py` | Playback: MPD, or a silent mock when MPD isn't running |
| `nts.py` | NTS live show info and mixtape details |
| `art.py` | Renders art as an amber halftone (show and mixtape art) or 1-bit (station logos); 512px for the web, 128px for the OLED |
| `vis.py` | Spectrum analyser reading MPD's FIFO output |
| `stations.yaml` | The station list, in groups |
| `catalog.py` | Loads `stations.yaml`, fills in each station's place and map position, and sorts each group by place (then name, Online last), which is also the dial order |
| `make_map.py` | Builds `static/worldmap.js`, the land mask for the map, from Natural Earth data in `dev/` |
| `build_static.py` | Builds the no-server version into `web/` |
| `static/` | The web app; `static/sw.js` keeps the no-server version usable offline |

## Run on the Mac

```
python3 -m venv .venv && .venv/bin/pip install fastapi uvicorn python-mpd2 pyyaml httpx pillow numpy   # first time only
./run.sh
```

Open http://localhost:8080. On the iPhone, on the same Wi-Fi, open http://RW-FlowX.local:8080 in Safari, then Share → Add to Home Screen.

Without MPD the app runs on a mock player with no sound. To hear it, install Homebrew and MPD, then start MPD before `run.sh`:

```
brew install mpd
mpd dev/mpd.conf
```

The spectrum shows LIVE when it's reading MPD's audio (the FIFO output in `dev/mpd.conf`) and SIM when it's simulating. On the Pi, moOde needs the same FIFO output added to its MPD config.

## No-server version (for away from home, until the Pi)

`build_static.py` builds a version of the app that needs no server: the page reads the station list from a file, fetches NTS's public feeds itself, renders the halftone art in the browser (station logos are pre-rendered into the folder), and plays everything on the device. Recently played is kept on each device. There's no RADIO output in this version.

```
.venv/bin/python build_static.py
```

Live at https://perannum.netlify.app (published 2026-11-02; renamed from spiffy-elf-9ebf5d.netlify.app on 2026-11-03).

That writes `web/`. To publish it, go to https://app.netlify.com/drop (free account), drag the `web` folder onto the page, and open the address Netlify gives you on the iPhone, then Share → Add to Home Screen. To update it later, rebuild and drag the folder onto the same site's Deploys page. Cloudflare Pages works the same way.

## Listening away from home with the Pi

The OUTPUT switch at the top of the controls picks where sound comes out. RADIO drives the speakers at home. THIS DEVICE plays the stream on the phone or laptop you're holding, and the radio is left alone. The choice is remembered per device. Lock-screen and headphone controls work in THIS DEVICE mode.

To reach the app from outside the home network, use Tailscale, a free private network between your own devices. Nothing is opened to the internet.

1. Install Tailscale on the machine running the app (the Pi; the Mac for now) and sign in. On the Pi: `curl -fsSL https://tailscale.com/install.sh | sh`, then `sudo tailscale up`.
2. Install the Tailscale app on the iPhone and sign in with the same account.
3. In the Tailscale app, find the machine's name (for example `pi-radio`). On the iPhone, open `http://<that name>:8080` in Safari.
4. Share → Add to Home Screen from that address. It works at home and away, so it replaces any icon made from the `.local` address.

The machine at home has to be on and running `run.sh`.

## Adding a station

Add an entry under "Terrascan FM" (or "Genre Radio", "Deep Cuts" or "Talk Radio") in `stations.yaml` with an id, name, place, stream URL and a short `about` (find streams at radio-browser.info). Where in the group doesn't matter, since the app sorts each group by place. If the place is new, add it under `places:` with its latitude and longitude so it shows on the map, plus `codes:` and `timezones:`. If the station publishes what's playing in a format the app knows (`kexp`, `airtime:`, `radioco:`, `radiocult:`), add an `info:` line. Then restart `run.sh`, and rebuild with `build_static.py` for the Netlify version.
