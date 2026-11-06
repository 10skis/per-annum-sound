# v0.101: Standby glow

**Date:** 2026-11-06
**Project:** Per Annum Sound

## What changed
- While stopped, the PLAY half breathes like a standby light: 25% to 45% and back every 4 seconds, with a faint halo at its brightest, starting once the power-down has settled. It stops the moment you press PLAY and hands over to the warm-up. Off with reduced motion.
- PLAY/STOP now dims by its two halves rather than as one key, so PLAY can rise above the dim (a child can't be brighter than a dimmed parent).

## Why
- Robert wanted the dimmed power switch findable with a subtle glow; he picked the breathing PLAY over a standby dot.

## Verified
- Stopped: `standby` running on PLAY only, 4 s; playing: none. No console errors; `selfTest.core()` clean. The breathing needs a look on screen.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
