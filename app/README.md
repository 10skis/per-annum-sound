# Pi Radio app

Control service and web app for Pi Radio. See `../SCOPE.md` for the full design.

| File | What it does |
|---|---|
| `server.py` | Control service and web endpoints |
| `player.py` | Playback: MPD, or a silent mock when MPD isn't running |
| `nts.py` | NTS live show info and mixtape details |
| `art.py` | Dithers art to the 128×128 amber image both screens use |
| `vis.py` | Spectrum analyser reading MPD's FIFO output |
| `stations.yaml` | The station list, in dial order |
| `build_static.py` | Builds the no-server version into `web/` |
| `static/` | The web app |

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

`build_static.py` builds a version of the app that needs no server: the page reads the station list from a file, fetches NTS's public feeds itself, dithers art in the browser (station logos are pre-dithered into the folder), and plays everything on the device. Recently played is kept on each device. There's no RADIO output in this version.

```
.venv/bin/python build_static.py
```

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

Add a line under "Elsewhere" in `stations.yaml` with an id, name, place and stream URL (find streams at radio-browser.info), then restart `run.sh`.
