# Pi Radio: Scope

A DIY take on the Atonemo NTS Radio Player ($179). It's a dedicated box on the Edifier speakers that plays NTS and other internet radio when you switch it on, with no phone required. AirPlay covers Apple Music and podcasts. An iPhone/Mac web app is a second remote for the same box.

| Field | Value |
|---|---|
| Owner | Robert Witenski |
| Status | Scoped, parts not ordered |
| Started | 2026-11-02 |
| Design language | Retro-analog |
| Target cost | ~$140–175 |
| Speakers | Edifier R1280DB (RCA line in, via the included 3.5mm-to-RCA cable) |

## Architecture

One control service runs on the Pi. The physical controls and the web app are two front ends to it, so they always agree on what's playing. Stations live in one file, `stations.yaml`, that both read.

| Layer | Choice |
|---|---|
| OS and player | moOde Audio (radio, AirPlay, MPD player, web settings) |
| Control service | Python: `python-mpd2` for playback, `gpiozero` for buttons and dial, FastAPI for the web app |
| Station list | `stations.yaml`: NTS 1, NTS 2, the 16 Infinite Mixtapes, then other stations |
| Stream sources | NTS public stream URLs; radio-browser.info for everything else |
| Network | Home Wi-Fi, plus Tailscale for access away from home |

## Scope 1: Physical device

### Layout

```
 ┌──────────────────────────────────────┐
 │  [NTS1] [NTS2]              ⏻ toggle │
 │                                      │
 │     ╭──────╮        ┌──────────┐     │
 │     │ DIAL │        │   ART    │     │
 │     ╰──────╯        │ 128×128  │     │
 │                     └──────────┘     │
 │  ┌────────────────────────────────┐  │
 │  │ ▸ NTS 1 · SHOW NAME · HOST     │  │
 │  └────────────────────────────────┘  │
 └──────────────────────────────────────┘
```

### Controls

| Control | Action |
|---|---|
| Key 1 | NTS Channel 1 |
| Key 2 | NTS Channel 2 |
| Dial, turn | Step through the station list |
| Dial, press | Play/stop |
| Toggle switch | Power on and safe shutdown |
| Volume | Speaker knob, plus software volume from the web app |

Switching on boots straight into the last station.

### Displays

Both screens are amber/yellow. The art screen is a color OLED drawing in amber only, so its hue is tuned in software to match the strip.

| Display | Part | Shows |
|---|---|---|
| Art | 1.5" 128×128 color OLED (SSD1351), amber in software | 1-bit amber art: 45° halftone for NTS show, mixtape and AirPlay cover art; clean 1-bit for station logos |
| Text strip | 3.12" 256×64 yellow OLED (SSD1322) | Station, show, song, artist |

### Parts

| Part | Cost |
|---|---|
| Raspberry Pi Zero 2 WH (headers pre-soldered) | $18 |
| DAC board with 3.5mm out (HiFiBerry DAC+ Zero or similar) | $20 |
| 1.5" 128×128 color OLED (SSD1351) | $15–40 |
| 3.12" 256×64 yellow OLED (SSD1322) | $25 |
| Rotary encoder with push switch + aluminum knob | $10 |
| 2 Cherry MX switches + keycaps | $8 |
| Mausberry soft-power board (toggle-switch version) + toggle switch | $20 |
| Official Pi power supply + 32GB microSD | $16 |
| Wiring | $5 |
| 3D-printed enclosure (library printer, PLA) | $0–15 |
| **Total** | **~$140–175** |

### Enclosure

The enclosure is printed on a library printer and modeled in OpenSCAD, a free tool where measurements are numbers in code, so a bad fit is one edit and a reprint. It's split into a front panel and a back shell so each part fits inside a library booking. Labels are printed into the panel. The back holds the 3.5mm out and the power input. The panel is about 120×90mm.

### Build phases

| Phase | Work | Time |
|---|---|---|
| 1. Bench test | Flash moOde, attach the DAC, confirm AirPlay and NTS through the Edifiers | 1–2 hrs |
| 2. Stations | Build `stations.yaml` | 1 hr |
| 3. Controls | Wire keys and dial on a breadboard, write the control service | 2–3 hrs |
| 4. Displays | Drive both OLEDs, halftone art, amber tuning, NTS show info | 3–4 hrs |
| 5. Power | Mausberry and toggle wiring, resume on boot | 1 hr |
| 6. Enclosure | Model, print a cutout test piece, print the final parts, assemble | 4–6 hrs plus print time |

## Scope 2: Web app

A web page served by the Pi and saved to the iPhone home screen (Safari → Share → Add to Home Screen), where it opens full-screen like an app. It also runs in any Mac browser. A native app isn't worth it: it needs Xcode, a $99/yr Apple developer account and upkeep, all for a remote.

### Features

| Feature | Detail |
|---|---|
| NTS keys | NTS 1, NTS 2, play/stop |
| Station list | Tap any station to play |
| Now playing | Station, show, host, track, with the same halftone art as the device |
| Volume | Software volume |
| Sync | Reflects the physical controls live |
| NTS schedule | Now and the next three shows on both channels, tap to tune in |
| Show detail | Description, genres, and a progress bar with time left |
| Station board | Live show under NTS 1/2, tagline under each mixtape, city under other stations |
| Signal readout | Codec, bitrate, sample rate, plus a clock |
| Recently played | Last 50 shows and tracks, logged every 15 s while playing |
| Output switch | RADIO plays on the speakers at home; THIS DEVICE plays the stream on the phone or laptop, with lock-screen controls |
| Away from home | Until the Pi: a no-server build on a free static host (Netlify, live at https://spiffy-elf-9ebf5d.netlify.app). With the Pi: Tailscale private network to it |
| Spectrum | 32-band analyser from MPD's FIFO output; a simulation labelled SIM when that isn't available |
| Presets | Six preset keys, car-radio style: tap to play, hold to save the current station. Kept per device for now; candidates for six physical buttons on the Pi |
| Listening and sleep timers | Time on the current station next to ON AIR; ZZ sets a 15, 30, 60 or 90 minute sleep timer that fades out where the device allows |
| Keyboard | Space play/stop, left/right tune, 1-6 presets, shift+1-6 save, S sleep, M map range, ? help panel |
| Nav map | Dot-matrix world map (Natural Earth land data) with a marker per city; WORLD and EUROPE ranges; tap a city to list its stations |
| Waterfall | A second visualizer under the spectrum: its recent history, scrolling down |
| Track info | Now-playing from stations that publish it to browsers: KEXP (with DJ notes), Dublab, Kiosk, Cashmere, Refuge, Noods |
| Show reminders | +CAL on upcoming NTS shows downloads a calendar event with a 5-minute alert |
| Offline | The no-server version keeps its shell cached and says NO SIGNAL when the connection drops |

The visual style is flat retro digital: amber on near-black, dot-matrix type, an LED-ring dial and a segmented volume bar. Changed from mechanical-looking controls on 2026-11-02.

### Build phases

| Phase | Work | Time |
|---|---|---|
| 1. Trial | Use moOde's built-in web interface for a week to learn what's actually needed | 0 hrs |
| 2. API | Play, stop, next, volume, current state, built on the Scope 1 control service | 2–3 hrs |
| 3. Front end | One HTML page, live updates | 3–5 hrs |
| 4. Polish | Home-screen icon, full-screen mode | 1 hr |

## Build order

Changed 2026-11-02: the web app is built first, on the Mac, then the physical device.

## Unverified assumptions

| Assumption | When it gets checked |
|---|---|
| The Infinite Mixtapes have public stream URLs like NTS 1 and 2 | Confirmed 2026-11-02 |
| NTS's live data feed includes show images | Confirmed 2026-11-02 |
| moOde can resume playback on boot | Scope 1, Phase 5 |
| The color OLED's amber can be matched closely to the yellow strip | Scope 1, Phase 4 |
| Mausberry's toggle version works with a latching switch on the Pi Zero 2 W | Before ordering |
| moOde lets us add a FIFO output to its MPD config for the spectrum | Scope 1, Phase 1 |
| A Pi Zero 2 W runs the spectrum analysis without audio dropouts | Scope 1, Phase 1 |
| iPhone keeps playing in THIS DEVICE mode with the screen locked, from the home-screen icon | First phone test |

## Open items

Tracked in `~/Documents/claude-workspace/projects/TODO.md`.
