# Per Annum Sound: Version Control

**Status:** Active
**Started:** 2026-11-02
**Location:** This folder. Scope in [SCOPE.md](SCOPE.md), code in [app/](app/README.md).
**Start here:** [HANDOFF.md](HANDOFF.md) has the design rules, traps and how to build and test.
**Goal:** A DIY Raspberry Pi radio for NTS and other internet radio on the Edifier speakers, with physical controls and an iPhone/Mac web app as a second remote. Personal project.

## Current version
v0.99: Per Annum Sound web app with 79 stations, console styling, nav map, halftone art, schedule, spectrum and on-device playback, plus a no-server build for a free static host so it works away from home before the Pi, live at https://perannum.netlify.app. Radio output still on a mock player until MPD is installed. Hardware not ordered

## History
Newest first. Each entry links to its update file.

| Version | Date | Summary | Update |
|---|---|---|---|
| v0.99 | 2026-11-05 | The visualisers warm up on play too | [link](updates/2026-11-05-visualisers-warm-up.md) |
| v0.98 | 2026-11-05 | PLAY/STOP dims with the rest when stopped | [link](updates/2026-11-05-playstop-dims.md) |
| v0.97 | 2026-11-05 | PLAY/STOP's light moves on the power curves | [link](updates/2026-11-05-playstop-power-curve.md) |
| v0.96 | 2026-11-05 | Power down and up as a smooth fall and a warm-up instead of a flicker | [link](updates/2026-11-05-power-warm-up.md) |
| v0.95 | 2026-11-05 | Colour setting: the accents turn from amber to phosphor green | [link](updates/2026-11-05-colour-amber-green.md) |
| v0.94 | 2026-11-05 | Station list gets the now-playing panel's sparse dots (desktop) | [link](updates/2026-11-05-station-list-dots.md) |
| v0.93 | 2026-11-05 | Power down and up: one stepped flicker for everything that dims, in step | [link](updates/2026-11-05-power-animation.md) |
| v0.92 | 2026-11-05 | Galaxy drawn in the maps' palette, so it matches Terra | [link](updates/2026-11-05-galaxy-matches-terra.md) |
| v0.91 | 2026-11-05 | Grid behind the spectrum displays too | [link](updates/2026-11-05-spectrum-grid.md) |
| v0.90 | 2026-11-05 | Sparse dot pattern in the now-playing panel | [link](updates/2026-11-05-now-playing-dots.md) |
| v0.89 | 2026-11-05 | Power off: map and controls dim when stopped; faint grid behind the Level displays | [link](updates/2026-11-05-power-off-level-grid.md) |
| v0.88 | 2026-11-05 | Review fixes: Solar status bar, glows dim with brightness, keys from sliders, canvas glass erased, live search, plate on named areas | [link](updates/2026-11-05-review-fixes.md) |
| v0.87 | 2026-11-04 | Controls plate in the art panel's glass, lined up with the panels beside it | [link](updates/2026-11-04-plate-aligned.md) |
| v0.86 | 2026-11-04 | Textured glass plate behind the desktop controls column | [link](updates/2026-11-04-control-plate.md) |
| v0.85 | 2026-11-04 | Solid controls: glass lifted toward the chassis and every control and the board filled with it | [link](updates/2026-11-04-solid-controls.md) |
| v0.84 | 2026-11-04 | Lunar tint runs black to grey; taller Level panel (option B) back for Fluid | [link](updates/2026-11-04-lunar-grey-taller-level.md) |
| v0.83 | 2026-11-04 | Lunar and Solar get tint strips (cool, neutral or cream, warm); each mode keeps its own tint | [link](updates/2026-11-04-lunar-solar-tints.md) |
| v0.82 | 2026-11-04 | Station search on the board: name, city, code, genre, group or what's on | [link](updates/2026-11-04-station-search.md) |
| v0.81 | 2026-11-04 | Fluid sized to fit its panel, so its spikes no longer run off the top | [link](updates/2026-11-04-fluid-fit.md) |
| v0.80 | 2026-11-04 | Display panel opens without the console's boot flicker | [link](updates/2026-11-04-panel-flicker.md) |
| v0.79 | 2026-11-04 | Display modes Lunar, Eclipse (tint slider) and Solar, one brightness setting, display panel under the mode key | [link](updates/2026-11-04-lunar-eclipse-solar.md) |
| v0.78 | 2026-11-04 | Panel padding evened out now the name tabs are gone | [link](updates/2026-11-04-panels-rebalanced.md) |
| v0.77 | 2026-11-04 | Tree glyph centred under the caret (even SVG sizes); panel name tabs removed | [link](updates/2026-11-04-tree-centred-tabs-removed.md) |
| v0.76 | 2026-11-04 | Dial caret drawn without border rounding, so it sits centred over the lit glyph; ring pulled in to clear it | [link](updates/2026-11-04-dial-caret-centred.md) |
| v0.75 | 2026-11-04 | Dial's visible glyphs spread evenly round the full ring, so it sits centred on the number | [link](updates/2026-11-04-dial-full-ring.md) |
| v0.74 | 2026-11-04 | Signal panel drops the Day & night and Your listening here headings | [link](updates/2026-11-04-signal-labels-trimmed.md) |
| v0.73 | 2026-11-04 | Galaxy zooms and pans like the maps; no borders or geography on phone USA/Europe | [link](updates/2026-11-04-galaxy-zoom-phone-geo.md) |
| v0.72 | 2026-11-04 | NGT is Solarized dark; DSK panel corners drawn again; US state lines drawn like Europe's borders | [link](updates/2026-11-04-solarized-night-dusk-corners.md) |
| v0.71 | 2026-11-04 | Borders, state lines, rivers and lakes on USA and EUROPE | [link](updates/2026-11-04-map-geography.md) |
| v0.70 | 2026-11-04 | Map ranges USA, EUROPE, TERRA, GALAXY; TERRA zooms to USA or EUROPE; galaxy view built in | [link](updates/2026-11-04-map-usa-terra-galaxy.md) |
| v0.69 | 2026-11-04 | Map switch reads EUROPE then WORLD; two-way switches and corner tabs chamfered like the keys | [link](updates/2026-11-04-switches-tabs-chamfered.md) |
| v0.68 | 2026-11-04 | 13 worldwide stations (79 in all); each group sorted by place, A to Z | [link](updates/2026-11-04-worldwide-stations-sorted.md) |
| v0.67 | 2026-11-04 | Phosphor sizes to its panel: scaled glow, balanced figure, side scopes in short panels | [link](updates/2026-11-04-phosphor-scale.md) |
| v0.66 | 2026-11-04 | Dial and tape glyphs centred: even overflow, and each glyph's ink measured and nudged to centre | [link](updates/2026-11-04-glyphs-centred.md) |
| v0.65 | 2026-11-04 | Sigil's background dot grid brighter, with a soft glow (page and server) | [link](updates/2026-11-04-sigil-grid-glow.md) |
| v0.64 | 2026-11-04 | ◀ mirrored like shuffle; 01/66 readout cut at both top corners, so the tuner row is symmetrical | [link](updates/2026-11-04-mirrored-prev-readout.md) |
| v0.63 | 2026-11-04 | Shuffle key mirrored so its notch faces PLAY's | [link](updates/2026-11-04-mirrored-shuffle.md) |
| v0.62 | 2026-11-04 | Visual guidelines pass: panel names without numbers, plain genre text, glow tokens, one divider less | [link](updates/2026-11-04-visual-guidelines-pass.md) |
| v0.61 | 2026-11-04 | Phone header balanced; shuffle and PLAY/STOP chamfered like the other keys | [link](updates/2026-11-04-header-chamfer-keys.md) |
| v0.60 | 2026-11-04 | Ridges steady: fixed rows with blended heights instead of sliding | [link](updates/2026-11-04-ridges-steady.md) |
| v0.59 | 2026-11-04 | Presets in one row of six, swipe for 7-12; Bright mode replaces Day | [link](updates/2026-11-04-preset-row-bright-mode.md) |
| v0.58 | 2026-11-04 | Twelve presets in two rows; keys 1-9, 0, -, = | [link](updates/2026-11-04-twelve-presets.md) |
| v0.57 | 2026-11-04 | Night, dusk and day modes; desktop scales to fit the window; steady Fluid, smooth Lissajous and Ridges | [link](updates/2026-11-04-modes-fit-smoother.md) |
| v0.56 | 2026-11-03 | 05 Level on phones: swipe sideways on 03 Spectrum | [link](updates/2026-11-03-swipe-level-phone.md) |
| v0.55 | 2026-11-03 | TUNING / NO SIGNAL under the title, art cache capped at 60, saved test scripts; The Lot is off air, not dead | [link](updates/2026-11-03-tuning-cache-selftest.md) |
| v0.54 | 2026-11-03 | Full check of streams, displays, controls, layouts and the Pi server; tablet header fix | [link](updates/2026-11-03-full-check.md) |
| v0.53 | 2026-11-03 | 3D Fluid, Phosphor LO/HI, phone header and notch fixes, Spectrogram on 03 | [link](updates/2026-11-03-fluid-3d-mobile-spectrogram.md) |
| v0.52 | 2026-11-03 | Phosphor, Fluid and Reels level displays | [link](updates/2026-11-03-eye-candy-levels.md) |
| v0.51 | 2026-11-03 | Goniometer back to the dot cloud with LO and HI clouds; breathing ripple on sigils | [link](updates/2026-11-03-cloud-gonio-sigil-ripple.md) |
| v0.50 | 2026-11-03 | Slower, softer breathing ripple; analog goniometer with LO and HI side scopes | [link](updates/2026-11-03-breathing-ripple-side-scopes.md) |
| v0.49 | 2026-11-03 | Smoother levels, phosphor goniometer, dot-size ripple, shuffle key, haptics, phone description | [link](updates/2026-11-03-smooth-levels-dot-ripple.md) |
| v0.48 | 2026-11-03 | RND button; middle pane fixed, long descriptions scroll on one line | [link](updates/2026-11-03-random-fixed-pane.md) |
| v0.47 | 2026-11-03 | Chante France 70s and 80s; London code LDN; tree glyph centred; play note removed | [link](updates/2026-11-03-decades-ldn-fixes.md) |
| v0.46 | 2026-11-03 | Site renamed to perannum.netlify.app; v0.45 live; records updated | [link](updates/2026-11-03-new-address.md) |
| v0.45 | 2026-11-03 | App icon is the glyph dial: an arc of katakana with the lit ｦ large in LED dots | [link](updates/2026-11-03-glyph-dial-icon.md) |
| v0.44 | 2026-11-03 | App icon is a dark display window like the site's panels, PAS in the dot font | [link](updates/2026-11-03-display-window-icon.md) |
| v0.43 | 2026-11-03 | App icon is a PAS sigil, drawn by the page's own sigil code | [link](updates/2026-11-03-pas-icon.md) |
| v0.42 | 2026-11-03 | Christmas tree glyph for Christmas Vinyl HD; per-station glyph field | [link](updates/2026-11-03-christmas-tree-glyph.md) |
| v0.41 | 2026-11-03 | Genre Radio under Terrascan FM on the board; command-key glyph swapped | [link](updates/2026-11-03-board-genre-glyph.md) |
| v0.40 | 2026-11-03 | Monocle, ABC Radio National, CBC Radio One, RTÉ Radio 1 and LBC in Talk Radio | [link](updates/2026-11-03-talk-stations.md) |
| v0.39 | 2026-11-03 | Five Pittsburgh stations, BBC World Service, new Talk Radio group | [link](updates/2026-11-03-pittsburgh-talk.md) |
| v0.38 | 2026-11-03 | Genres for the Terrascan FM stations on the board | [link](updates/2026-11-03-terrascan-genres.md) |
| v0.37 | 2026-11-03 | Tap the art or title to hold its motion; tap again to resume | [link](updates/2026-11-03-tap-to-hold.md) |
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
