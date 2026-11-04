# v0.58: Twelve presets

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- Presets go from 6 to 12, in two rows of six, on phones and desktop. Saved presets carry over; the new six start empty.
- Keyboard: the number row plays them (1 to 9, 0, minus and equals for 1 to 12), and shift saves to that slot. The keys panel and SCOPE.md are updated.
- The second row makes the desktop console 974 px tall instead of 949, so in a 900 px window it scales to 83%.

## Process note
- v0.57's Day mode was built when Robert had only asked what it should be. It stays as built until he decides. The working-style rule now says a "let me know what you think" inside a larger request gets a proposal, not a build.

## Verified
- 375 px: 12 keys in 2 rows (47 × 52 each), no overflow. 1440 px: 2 rows, layout clean. Shift+= saved to preset 12, = played it, shift+0 saved to 10; presets put back afterwards. `selfTest.core()` clean.

## Next steps
- Robert to decide on Day mode. Re-drag `app/web` to Netlify. See TODO.md.
