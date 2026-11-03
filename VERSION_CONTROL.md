# Per Annum Sound: Version Control

**Status:** Active
**Started:** 2026-11-02
**Location:** This folder. Scope in [SCOPE.md](SCOPE.md), code in [app/](app/README.md).
**Start here:** [HANDOFF.md](HANDOFF.md) has the design rules, traps and how to build and test.
**Goal:** A DIY Raspberry Pi radio for NTS and other internet radio on the Edifier speakers, with physical controls and an iPhone/Mac web app as a second remote. Personal project.

## Current version
v0.36: Per Annum Sound web app with 53 stations, console styling, nav map, halftone art, schedule, spectrum and on-device playback, plus a no-server build for a free static host so it works away from home before the Pi, live at https://spiffy-elf-9ebf5d.netlify.app. Radio output still on a mock player until MPD is installed. Hardware not ordered

## History
Newest first. Each entry links to its update file.

| Version | Date | Summary | Update |
|---|---|---|---|
| v0.36 | 2026-11-03 | Radiocult stations show the show's name, not the file name | [link](updates/2026-11-03-radiocult-show-names.md) |
| v0.35 | 2026-11-03 | Profiles for every station, twelve corrected; city codes shared by server and page; FIP logos back | [link](updates/2026-11-03-profiles-city-codes.md) |
| v0.34 | 2026-11-03 | Scroll to tune on the dial | [link](updates/2026-11-03-dial-scroll.md) |
| v0.33 | 2026-11-03 | Art shimmer was hidden under the image since v0.17; now drawn on top | [link](updates/2026-11-03-shimmer-visible.md) |
| v0.32 | 2026-11-02 | Signal panel filled for every station: day and night, nearest stations by distance; shimmer back to 5 to 14 s | [link](updates/2026-11-02-signal-panel-every-station.md) |
| v0.31 | 2026-11-02 | Volume trackpad swipe, five LEVEL displays, live turning sigil with city in the middle | [link](updates/2026-11-02-volume-level-sigil.md) |
| v0.30 | 2026-11-02 | Sigil art for stations without artwork | [link](updates/2026-11-02-sigil.md) |
| v0.29 | 2026-11-02 | Stronger, more frequent art shimmer; mockups of five no-art designs | [link](updates/2026-11-02-shimmer-noart-mockup.md) |
| v0.28 | 2026-11-02 | Dial arrows turn the ring the way they point; drag follows the hand | [link](updates/2026-11-02-dial-arrows-direction.md) |
| v0.27 | 2026-11-02 | Ticker above the board, level panel fitted, nearby and listening stats, About pop-up with 33 profiles | [link](updates/2026-11-02-ticker-about-nearby.md) |
| v0.26 | 2026-11-02 | Header readouts (scrolling when long), level strip under the art, up-next timeline and recent tracks | [link](updates/2026-11-02-readouts-level-upnext.md) |
| v0.25 | 2026-11-02 | Map scrolls sideways unzoomed; mockups of four signal-panel fills | [link](updates/2026-11-02-map-scroll-fill-mockups.md) |
| v0.24 | 2026-11-02 | Pan the zoomed map by drag or two-finger scroll, balanced two-column station board | [link](updates/2026-11-02-map-pan-columns.md) |
| v0.23 | 2026-11-02 | Map click-to-zoom, softer city dots | [link](updates/2026-11-02-map-zoom.md) |
| v0.22 | 2026-11-02 | Map labels on hover, yellow markers, smooth group open and close | [link](updates/2026-11-02-map-hover-groups.md) |
| v0.21 | 2026-11-02 | Dial turns with the hand, trackpad swipe on the tape, orange map markers | [link](updates/2026-11-02-dial-swipe-markers.md) |
| v0.20 | 2026-11-02 | Rotating-window dial, tape tuner, fitted no-art names, five more visualizers | [link](updates/2026-11-02-dial-tape-visualizers.md) |
| v0.19 | 2026-11-02 | Knockout names on no-art stations, volume above visualizers on phones, map labels glide, clickable tuning tape | [link](updates/2026-11-02-knockout-tape.md) |
| v0.18 | 2026-11-02 | Renamed Per Annum Sound, smoother map drift, glyph dial, dot-matrix no-art design, Terrascan FM with Worldwide FM | [link](updates/2026-11-02-per-annum-sound.md) |
| v0.17 | 2026-11-02 | Collapsible board, recent ticker, art shimmer, visualizer modes, map drift, 19 new stations | [link](updates/2026-11-02-board-and-motion.md) |
| v0.16 | 2026-11-02 | Console look, nav map, waterfall, track info, reminders, offline, help panel | [link](updates/2026-11-02-console.md) |
| v0.15 | 2026-11-02 | Presets 1-6, sleep timer, keyboard shortcuts | [link](updates/2026-11-02-presets-sleep-keys.md) |
| v0.14 | 2026-11-02 | Desktop dial arrows, listening timer | [link](updates/2026-11-02-dial-arrows-timer.md) |
| v0.13 | 2026-11-02 | Phone tuner: full-width art, arrows, swipe; dial desktop only | [link](updates/2026-11-02-tuner.md) |
| v0.12 | 2026-11-02 | iPhone volume note, art and dial swapped on phones | [link](updates/2026-11-02-mobile-volume-swap.md) |
| v0.11 | 2026-11-02 | Progress bar fix, station descriptions, Kool FM, WQXR, Chillhop | [link](updates/2026-11-02-stations-progress.md) |
| v0.10 | 2026-11-02 | Halftone art for shows and mixtapes, 1-bit logos, 512px web art | [link](updates/2026-11-02-halftone-art.md) |
| v0.9 | 2026-11-02 | Dial plays on release, touch/mouse fixes, brighter secondary text | [link](updates/2026-11-02-dial-contrast.md) |
| v0.8 | 2026-11-02 | Text cleanup: full descriptions, smaller marquee, ENDING label | [link](updates/2026-11-02-text-cleanup.md) |
| v0.7 | 2026-11-02 | No-server build for static hosting, logo fixes | [link](updates/2026-11-02-static-build.md) |
| v0.6 | 2026-11-02 | Phone-speaker output, Tailscale steps, mobile overflow fix | [link](updates/2026-11-02-phone-output.md) |
| v0.5 | 2026-11-02 | Schedule, show detail, board subtitles, signal readout, recently played, spectrum | [link](updates/2026-11-02-dashboard-fill.md) |
| v0.4 | 2026-11-02 | Desktop dashboard layout, The Lot Radio added | [link](updates/2026-11-02-desktop-dashboard.md) |
| v0.3 | 2026-11-02 | UI restyled flat retro digital | [link](updates/2026-11-02-retro-digital-ui.md) |
| v0.2 | 2026-11-02 | Web app and control service built, 29 stations | [link](updates/2026-11-02-web-app-v1.md) |
| v0.1 | 2026-11-02 | Project created, device and web app scoped | [link](updates/2026-11-02-project-created.md) |

## Open items
Tracked in `~/Documents/claude-workspace/projects/TODO.md`.
