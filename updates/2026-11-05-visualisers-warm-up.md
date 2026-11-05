# v0.99: Visualisers warm up

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- On play, the Level and spectrum displays warm up with the rest of the console: from faint to full over a second, starting 0.3 s in, at the map's place in the sweep. Before, they snapped straight on.
- They still don't dim when stopped, so NO CARRIER stays readable.

## Why
- Robert said the power-off worked, but the visualisers came back on too fast.

## Verified
- Play adds `.waking`, which runs `warm-up` on all three display canvases with a 0.3 s delay and clears after 1.5 s; a repeat play while already playing doesn't rerun it. No console errors; `selfTest.core()` clean. Needs a look on screen.

## Next steps
- Standby glow on a dimmed PLAY: proposed, waiting on Robert. Re-drag `app/web` to Netlify. See TODO.md.
