# v0.93: Power down and up

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- Pressing STOP runs a power-down: the art, title, map and controls flicker together in the boot animation's stepped style and settle at their dimmed levels in 0.6 s. Pressing PLAY runs the reverse, a warm-up flicker to full in 0.7 s.
- The map and controls no longer fade on their own half-second timer, so nothing lags.
- PLAY/STOP doesn't flicker. Neither runs on page load (the boot animation covers that) or with reduced motion.

## Why
- Robert saw a delay between the art dimming and everything else, and asked for a power down/up animation.

## Verified
- On load: dimmed, no flicker. Play: `power-up` on the map, art and title, cleared after 0.8 s. Stop: `power-down` on the controls and VOL; none on PLAY/STOP. No console errors; `selfTest.core()` and `selfTest.layout()` clean. The flicker itself couldn't be watched here (the hidden pane doesn't run animations); check it on screen.

## Next steps
- Station list texture, then the amber-to-green colour slider. Re-drag `app/web` to Netlify. See TODO.md.
