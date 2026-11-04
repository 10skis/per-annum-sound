# Per Annum Sound: Handoff

Start here. Written 2026-11-03 at v0.34, updated at v0.61 so a new session can pick up without re-reading 34 update notes. History lives in `VERSION_CONTROL.md` and `updates/`; this file is the rules and the traps.

## Snapshot

| Field | Value |
|---|---|
| Product | Per Annum Sound (renamed from Pi Radio; folder stays `pi-radio`) |
| Version | v0.61 |
| Owner | Robert |
| Live site | https://perannum.netlify.app (v0.47 live as of 2026-11-03, v0.61 waiting; was spiffy-elf-9ebf5d.netlify.app; Robert re-drags `app/web` to update) |
| Repo | `~/Documents/claude-workspace`, pushed to GitHub |
| Hardware | Raspberry Pi device scoped in `SCOPE.md`; not ordered |
| Open to-dos | `projects/TODO.md`, lines starting "Per Annum Sound:" |

## How it runs

| Thing | How |
|---|---|
| Server version (the Pi later) | `app/run.sh`, port 8080. FastAPI plus MPD; falls back to a silent mock player when MPD isn't running |
| No-server version (Netlify) | `.venv/bin/python build_static.py` writes `app/web/`. Serve locally with `python3 -m http.server 8090` from `app/web` |
| One page, two modes | `app/static/index.html` serves both. The build injects `window.PI_RADIO_STATIC = true`; the `DATA` object switches between the server API and fetching NTS and stations.json directly |
| Station data | `app/stations.yaml`: groups, `places` (lat/lon/label), `timezones`, per-station `about`, `info`, `genre`, `glyph`, `profile`, `founded`, `notable`, `site`, `map`, plus `codes` (airport-style city codes for the map and sigil; London is LDN by choice, not LON). Loaded by `catalog.py` for both server and build |
| Art | `art.py`: 45° halftone for covers, 1-bit for logos, sigil for stations with none. The page has matching JS for the no-server build |
| Map land | `make_map.py` builds `static/worldmap.js` from Natural Earth (`dev/ne_110m_land.geojson`) |
| Offline | `static/sw.js`, copied to the web root by the build |
| App icon | Glyph dial: the rotating-window arc of katakana with the lit ｦ shown large in LED dots, dark dot-matrix plate, glass highlight, no letters (iOS 26/27 style; the sigil and display-window versions were rejected). Drawn by the page (`dev/icon.js`); `make_icons.py` serves web/ and saves what the page posts. Steps in its docstring |

After any change: rebuild `web/`, check in the browser at 1371 or 1440 px and at 375 px, then log (update file, VERSION_CONTROL, PROJECTS, TODO) and push.

## Design rules (Robert's decisions; don't undo)

| Area | Rule |
|---|---|
| Colour | Amber only: `--amber #ffb02e`, `--amber-mid #d08c26`, `--amber-dim #9c6c22`, `--amber-ghost #241907`, `--line #4a3616`. Blue `#4fb4ff` for warnings only (no signal, offline, sleep's last minute). Map city dots yellow `#e8c43a` (hot `#ffe56e`). Nothing else |
| Type | VT323 for data, Saira Condensed for labels, Michroma for the brand only |
| Look | "Cyberpunk alien car dashboard", leaning retro-analog: chamfered panels, inverse code tabs (01 ART, 02 SIGNAL, 03 SPECTRUM, 04 NAV, 05 LEVEL, 06 ABOUT), registration brackets, unlit 88 behind numerals, dot matrix everywhere. Robert reacts badly to over-literal brand references (Braun etc.) |
| Dial (desktop) | No glyphs that read as a known symbol (⌘ was swapped out). A station can set `glyph:` for a drawn one from `GLYPH_ART` (Christmas Vinyl HD has a tree); drawn glyphs use currentColor, never emoji, and are absolutely centred in the slot (inline SVG sits on the baseline and rides high). Rotating window: ring of katakana glyphs, about six either side of the current one, fading. Not the centerpiece (he rejected that mockup). ◀ turns the ring clockwise, ▶ anticlockwise; drag follows the hand; scroll down or right = next |
| Tape tuner | Under the dial (desktop) and under the tuner (phones). Thin 1 px analog ticks, a number every fifth, group bands, needle. Swipe or drag left = higher stations |
| Volume | Two-finger swipe right = louder |
| Phones | Tuner strip instead of the dial; no clock in the header (status bar has it); ? in the header; brand shows P·A·S |
| Level displays | Eight: Trace, Meter, Needle, Goniometer, Loudness, then eye candy (Phosphor, Fluid, Reels). Goniometer is the first version, a random dot cloud with LO and HI clouds; v0.49's trace lives on as Phosphor. Eye candy is welcome here; avoid repeating the spectrum screens' displays. Fluid is a 3D dot surface with spikes; Phosphor, Goniometer and Fluid all have LO and HI side versions |
| Art shimmer | Breathing, not flashing (v0.50): a 5.2 s ring or 4.6 s sweep every 7 to 16 s, dots swelling by up to about 40%, no highlight colour. Cover art and sigils (v0.51). Since v0.49 halftone art swells its own dots (read back from the image onto `#artDots`, image hidden only during the ripple); logos keep the `.shimmer` overlay |
| Hold | Tap the art to hold shimmer and sigil rotation; tap the title to stop its scroll. Tap again resumes; remembered per device. About opens from the line under the title and the description, not the title |
| Sigil (no artwork) | Turning dotted rings, city code large with city name under it (not the station number), faint dot matrix behind. Breathes with the same ripple as cover art |
| Map | Dots only; label wipes out on hover. World view drifts left slowly, pauses on hover. Click empty map = zoom 1.9×, again = out; drag or scroll pans. WORLD and EUROPE ranges |
| Signal panel | Every station gets: what's on (NTS timeline or recent tracks), day and night bar, nearby and similar, your listening |
| Board | Collapsible groups. Columns: NTS Live and Infinite Mixtapes; Terrascan FM and Genre Radio; Deep Cuts and Talk Radio (`GROUP_COL`). Two columns 960–1279 px (third column under the second), three from 1280. Recently played ticker above the columns, hover lights the row |
| Header readouts | City, position, local time, distance from NYC, signal. Scroll slower than the station title when too long |
| Motion | Smooth easing (cubic-bezier(.3,.7,.3,1)), not stepped. Everything off with reduced motion |

## Traps already hit

| Trap | What to do |
|---|---|
| Canvases inflating the layout | A canvas with height 100% in a grid or flex row feeds its own size back. Use `contain: size` on the canvas, and on `.artcol` and `.strip`, so the right-hand controls set the top row's height |
| Class name clashes | It's one 2,500-line file. The ticker once used `.tk`, the tape's tick class, and turned the ticks into a solid line. Grep a class name before using it |
| Phone header | The full header needs about 460 px, so below 960 px (where the unit is at most 420 wide) it shows P·A·S and drops the clock and "ON AIR". Anything wider than the screen widens the whole page on iPhone and knocks the art and tape out of line |
| Off-air stations | The Lot Radio (`lot`) goes off air at times; its playlist then answers #EXT-X-ERROR and the page shows NO SIGNAL under the title. Check their site before calling a stream dead |
| Testing | `dev/check_streams.py` (data and every stream, server-side) and `dev/selftest.js` (run in the page: `selfTest.core()`, `play(from, to)` in slices of 11, `layout()` per width). Neither is shipped in `web/` |
| Display modes | `data-theme` on `<html>`: night, dusk, bright (header key or T, stored as piRadioTheme, set before first paint). Robert rejected a light Day mode: modes change brightness, never the dark background. New colours should be variables, or they'll ignore the mode |
| Smooth motion | Don't slide dot rows by fractions of a pixel: 2 px dots shimmer as they cross pixel lines (Ridges in v0.59). Keep rows fixed and blend values, and round positions. Measure jitter as the share of pixels changing per frame |
| Presets | Twelve in one row: six show, swipe or scroll for 7-12 (snaps by six). Two rows were tried and rejected: too tall for a laptop screen |
| Desktop fit | `fitDesktop()` scales `.note`, `.unit` and `.list` with CSS zoom (floor 70%) until the console fits the window height. Pointer code measuring distances must divide by `scaleOf(el)` |
| 05 Level on phones | Shares 03's spot in `#swipe`: native scroll-snap, dots under it. `placeLevel()` moves the panel there below 960 px and back under the art above. Robert chose this over a separate panel |
| Spectrum screens (03) | New displays go at the end of `VIS_MODES`: the saved choice is an index |
| Layering | The art image's drop-shadow filter paints it as its own layer. Anything meant to sit on top (`.shimmer`) needs a z-index, or it's hidden. The shimmer was invisible from v0.17 to v0.33 because of this |
| `hidden` ignored | `[hidden] { display: none !important }` exists because class display rules override the attribute |
| Patching | Edits are scripted string replacements with `assert count == 1`. Comment markers often appear twice (CSS and JS); match the longer, unique form |
| Streams | Must be HTTPS (Netlify page). HLS is only detected by `.m3u8` in the URL; a playlist at a bare address (wyep.org/stream) fails, so use a direct MP3/AAC stream. More than 70 stations needs more `DIAL_GLYPHS`. BBC Radio 4 is UK-only; World Service plays abroad. Track info only from feeds that allow browser access (KEXP, Airtime, radio.co, Radiocult). Kiosk, alHara and FIP logos block browsers, so the build pre-renders them. No "tap play" note: fast scrolling aborts plays and used to flash it. The browser pane runs no animation frames while hidden, so rAF-timed checks stall; test logic directly, or draw frames by hand and save them. `build_static.py` replaces `web/`, so restart any server running from it |
| Wikimedia art | Needs a descriptive user agent (`UA` in `art.py`) or it returns 429 and the build quietly drops the FIP logos. Check `web/art/` after a build |
| Track titles | Some feeds send file names (250119_0258). `fileLike()` in the page filters them; prefer a feed's show name over its track title |
| iPhone | Pages can't set volume; the bar becomes a "use the volume buttons" note |
| Testing in the built-in browser | It won't register service workers; screenshots right after load can be stale or mid boot animation; a hidden pane pauses requestAnimationFrame. For visuals, freeze animations and look at the frame. "Animation running" is not "visible" |

## Open items

- v0.45 is live. Chrome and iOS keep an installed app's old icon: remove and reinstall it (Chrome: chrome://apps, Remove from Chrome) to see the new one.
- Oroko Radio announced an indefinite hiatus in April 2026; its stream still answers. Robert to decide whether it stays.
- Chillhop Radio is FluxFM's channel, not the Chillhop Music label's own stream of the same name. Possible rename to FluxFM ChillHop.
- MPD install and the hardware build: see TODO.md and SCOPE.md. On hold as of 2026-11-03.
