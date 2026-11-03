# v0.55: Tuning indicator, capped art cache, saved checks

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- From the tap until sound starts, the line under the title blinks TUNING. A stream that hasn't started after 15 s, or whose host refuses it, shows "NO SIGNAL · OFF AIR OR UNREACHABLE" there instead, like a radio on dead air. The blue "stream failed" note no longer fires for a station that never started, and a note from the last station is cleared on the next tap.
- The service worker keeps NTS cover art in its own cache, capped at the newest 60 images. The shell cache moves to v2, so old caches holding every image ever loaded are cleared on update.
- The full check is saved:
  - `dev/check_streams.py` checks stations.yaml and every stream server-side, and reads HLS playlists for an off-air error.
  - `dev/selftest.js` runs in the page: `selfTest.core()` for displays, panels and controls, `selfTest.play(from, to)` for playback, `selfTest.layout()` for overflow.

## Correction
- The Lot Radio isn't locked out, as the v0.54 note said. Their own site showed OFFLINE and their player didn't play either: it's simply off air at times. It stays in the list and now shows NO SIGNAL when off.

## Verified
- Kool FM: TUNING blinks, then the city shows when sound starts at 4.8 s. The Lot (off air): TUNING, then NO SIGNAL at 10 s with no blue note, and the next station starts clean.
- Cap: 75 images in, the newest 60 kept. The browser pane can't register service workers at all (true before this change too), so the trimming was tested against the page's cache storage with the worker's own function.
- `selfTest.core()` clean; the playback slice flags only The Lot; presets put back afterwards. `check_streams.py` flags only The Lot.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
