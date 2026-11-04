# v0.59: Presets in one scrolling row, Bright mode replaces Day

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- Presets are back to one row: six show, and a swipe (or a trackpad scroll, or the mouse wheel over them) snaps to 7-12. Two rows made the console taller again, so the bottom was cut off once more. Pressing a preset key, or saving to a preset, brings its page of six into view.
- Day mode (cream chassis) is gone. In its place, **Bright** keeps the night background and turns every amber element up: lettering, lines and glows, displays at 1.5×, and art at 1.25× (more washes it out). The header key cycles NGT, DSK and BRT, and T does the same. Anyone who had Day saved lands on Bright.
- The self test's layout check skips presets 7-12, which sit off to the side on purpose.

## Verified
- 1440×900: one row, and the console back to 944 px and 90% scale. Keys = and 2 move to the right page (an instant scroll lands exactly on page two; the smooth animation needs a visible window, which the hidden browser pane isn't).
- 375 px: one row of six (46 × 52), and page two shows 7-12 after a swipe. Layout clean.
- Bright screenshot at 1100×800. `selfTest.core()` clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
