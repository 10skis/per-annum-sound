# v0.100: Visualisers on the power curves

**Date:** 2026-11-06
**Project:** Per Annum Sound

## What changed
- The Level and spectrum displays now dim to 25% when stopped and warm up on play on exactly the map's curve and timing (0.5 s fall; 1 s warm-up starting 0.3 s in). Their labels stay lit, like the map's range switch.
- v0.99's separate warm-up keyframe and the `.waking` timer are gone; `setPower()` is one line again.

## Why
- Robert found the visualisers still incongruent: in v0.99 they stayed at full brightness while stopped, so they stood out at rest and then warmed up on a curve of their own.

## Verified
- Stopped: all three display canvases in the dim list (screenshot shows them dimmed with the map). Timings read back the same as the map's in both states. No console errors; `selfTest.core()` clean.

## Next steps
- Breathing standby glow on PLAY (approved). Re-drag `app/web` to Netlify. See TODO.md.
