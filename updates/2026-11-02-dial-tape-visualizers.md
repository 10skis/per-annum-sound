# v0.20: Rotating dial, tape tuner, 11 visualizers

**Date:** 2026-11-02
**Project:** Per Annum Sound

## What changed
- **Dial (desktop).** Rotating window: the glyph ring turns so the current station sits under a caret at the top; only the six stations either side show, fading with distance. Reads the same at any station count. Turning, arrows and keys work as before.
- **Tape tuner** (under the dial on desktop, under the tuner on phones): a band sliding under a fixed needle, with a glyph and tick per station, a number every fifth, and the five groups marked underneath like MW/FM bands, the current one lit. Tap or drag as before (16 px per station now).
- **No-art names.** Word-wrapped at the largest size that fits (at most three lines), with letter spacing, so long names like Give the Drummer Radio no longer run off the edge and letters no longer run together. Same in the browser and `art.py`.
- **Visualizers.** Five more, 11 in total: Ridges (recent history as stacked lines, front ones hiding those behind), Glyph Rain, Lissajous, Starfield, Tunnel. Click a screen to cycle.
- Mockups for both dial options in `mockups/`.

## Verified
- Desktop: ring shows 13 glyphs with the current one lit at the top; tape band lit for the right group; all 11 visualizer modes draw without errors and render while playing. Phone: tape tuner fits, no overflow. Server-side name layout checked on four long names.

## Decisions made
- Robert chose both: rotating window for the dial and the tape tuner for the tape.

## Next steps
- See TODO.md.
