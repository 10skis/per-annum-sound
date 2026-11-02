# v0.9: Dial and contrast

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- Dial rewritten for touch and mouse. Dragging only moves the dial and shows the station name with RELEASE TO TUNE; the station plays when you let go. Before, every step during a drag played a station, so the NTS keys and PLAY/STOP flickered as you turned, and on iPhone audio could be blocked because it started outside a tap.
- Steps are 24° (was 30°). Movement near the centre of the dial is ignored, since a small finger shift there is a big angle. Tap versus turn is decided by distance moved (8px), not angle.
- Mouse drags no longer select text; the cursor shows grab and grabbing. Polling no longer repaints the dial mid-turn.
- Secondary text and borders brightened: `--amber-dim` #5c3e10 to #9c6c22 (about 2:1 to 4.5:1 contrast), `--amber-mid` #b87a1c to #d08c26, `--line` #3a2a10 to #4a3616.
- Verified with simulated drags: no requests or key changes mid-drag, one play on release, tap toggles, centre wobble does nothing.

## Why
- Robert flagged the dial on Safari touch and Mac (drag affected the keys above) and the dim labels as hard to read.

## Decisions made
- Halftone artwork mocked up (32 cells on a 45° grid, midtone gamma 1.2) against the current dither on live NTS covers; awaiting Robert's pick before it goes in.

## Next steps
- See TODO.md.
