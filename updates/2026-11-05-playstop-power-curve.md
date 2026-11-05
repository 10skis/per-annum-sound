# v0.97: PLAY/STOP on the power curves

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- PLAY/STOP's amber no longer snaps between the two halves. Pressing PLAY, it warms up over the same slow second as the rest of the console, leading the sweep; pressing STOP, STOP lights in the same half-second fall.
- It still never dims: it's the power switch and stays lit at rest. The press itself still answers at once.

## Why
- Robert asked whether PLAY/STOP should be part of the animation; it joined the motion but not the dim.

## Verified
- Transitions read back: 1 s warm-up curve when playing, 0.5 s fall when stopped; STOP settles on amber. No console errors; `selfTest.core()` clean. The motion needs a look on screen.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
