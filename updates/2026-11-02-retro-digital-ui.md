# v0.3: Retro digital UI

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- Restyled the web app from skeuomorphic hardware to flat retro digital: no gradients, keycaps, knurled dial or lever. Keys are outlined cells that invert when active, play/stop is a two-cell switch, the dial is a ring of square LEDs (one per station) around a large station number, volume is a 20-segment bar, and the station list uses a `>` cursor. VT323 dot-matrix type throughout, amber on near-black, scanlines over the page.
- Corrected the station count: 29 (2 NTS live, 16 mixtapes, 11 others), not 31 as the v0.2 log said.

## Why
- Robert asked for less skeuomorphism and a more retro digital look.

## Decisions made
- Dial keeps the same interaction (drag to step, tap to play/stop, arrow keys); only the drawing changed.

## Next steps
- See TODO.md.
