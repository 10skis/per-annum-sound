# v0.96: Power warm-up

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- The power animation is now a smooth curve, not a flicker. STOP: everything drops fast and settles at its dimmed level in half a second, like a switch cutting out. PLAY: everything starts slowly and rises to full over a second, like a valve warming, sweeping out from the controls to the title, the art and then the map, 0.1 s apart.
- `setPower()` is now one line; the keyframes and timers are gone.

## Why
- Robert said v0.93's stepped flicker looked more like a glitch than a power-up.

## Verified
- Transition timings read back in both states (map up 1 s after 0.3 s, title 0.1 s, art 0.2 s, controls at once; down 0.5 s, no delays). No console errors; `selfTest.core()` clean. The curve itself needs a look on screen; the hidden pane doesn't run transitions.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
