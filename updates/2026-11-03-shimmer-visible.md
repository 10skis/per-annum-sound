# v0.33: Art shimmer actually visible

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- The art shimmer (ripple and sweep) had never been visible since it was added in v0.17. The art image's glow filter (drop-shadow) makes the browser paint it as its own layer, and because it comes after the shimmer in the markup it was drawn on top, hiding every ripple and sweep. The shimmer now sits above it (z-index 1, the panel tab at 2).
- Settings are the v0.25 ones Robert asked for: single ring over 1.8 s, narrow 1.5 s sweep, every 5 to 14 s.

## Verified
- Frozen mid-animation on an NTS cover: the sweep shows as a pale band and the ripple as a pale ring through the dots. Before the fix the same frames showed nothing.

## Decisions made
- The speed and strength changes in v0.29 and v0.32 were tuned without the effect ever being seen, by Robert or by me; earlier checks only confirmed the animation was running, not that it was visible. Visual checks now freeze the frame and look at it.

## Next steps
- See TODO.md.
