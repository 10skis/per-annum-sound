# v0.85: Solid controls

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- The displays' glass now sits 35% of the way toward the chassis colour in every mode and tint (Solar moves its painted glass; the others move `--screen`, so the canvases match).
- Every control is filled with that glass: keys, presets, PLAY/STOP, the two-way switches, the dial face, the 01/79 readout and the search field. Lit keys keep their amber. The station board is filled inside its frame on desktop; on phones it has no frame, so no fill.

## Why
- Robert saw the controls and the board as hollow next to the filled panels, and didn't want to box the controls column.

## Decisions made
- Option A from `mockups/control-weight.html` (solid controls), over B (one borderless plate behind the column). Both lifted the glass partway, the middle ground Robert asked for between filling the controls and lightening the panels.
- Lunar on BLACK looks as before, since its glass and chassis are both black.

## Verified
- 1440 x 900: Lunar on GRAPHITE, Eclipse and Solar; map glass matches its panel; STOP keeps its amber. 375 px: filled keys, readout and strip, no overflow. `selfTest.core()` and `selfTest.layout()` clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
