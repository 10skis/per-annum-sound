# v0.5: Dashboard detail, recently played, spectrum

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- NTS schedule: now and the next three shows on both channels, under NTS Live. Tapping a show tunes to its channel.
- Show detail in the now-playing panel on desktop: description, genres when NTS lists them, and a 30-segment progress bar with start, end and minutes left.
- Station board subtitles: the live show under NTS 1/2, each mixtape's tagline, each other station's city.
- Header: codec, bitrate, sample rate and channels (bitrate and rate need MPD), and a clock.
- Recently played: the server logs each new show or track every 15 s while playing, keeps the last 50 in `history.json`, and the board's fourth column shows the latest 12.
- Spectrum: 32 bands × 14 segments. `vis.py` reads the raw audio from an MPD FIFO output (added to `dev/mpd.conf`) and runs an FFT. Without it, the page shows a simulation labelled SIM; with it, LIVE.
- Fixed the board's empty fourth column (the header row was stretching an extra column). The board is now 4 columns at 1280px and up, 2 between 960 and 1280.
- Fixed the info panel overflowing under the controls.

## Why
- Robert found the desktop dashboard bare and approved all four additions plus recently played and a visualizer.

## Decisions made
- The visualizer reads MPD's actual audio rather than animating for show; the simulation is labelled SIM so it never passes as real.
- Added numpy as a dependency for the spectrum.

## Next steps
- See TODO.md.
