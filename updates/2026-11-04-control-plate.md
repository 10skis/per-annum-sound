# v0.86: Plate behind the controls

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- On desktop, a borderless glass plate sits behind the controls column, from the Output switch to VOL. It has chamfered corners and no frame, a tone halfway between the controls' glass and the chassis, and the same faint dot matrix that sits behind the art (7 px pitch).
- The controls stay filled with the darker glass on top of it, so each still reads as its own part.
- Phones don't get the plate: there's no side-by-side panel to balance against.

## Why
- Robert wanted option B's plate added to A's solid controls, without the controls looking like they're just sitting on it.

## Decisions made
- Plate tone and dot colour are `DISPLAY` tokens (`--plate`, `--plate-dot`), so they follow every mode and tint. On Lunar BLACK the plate is black and only the dots show.

## Verified
- 1440 x 900: Lunar GRAPHITE, Eclipse and Solar; the display panel still opens over it. 375 px: plate hidden, no overflow. `selfTest.core()` and `selfTest.layout()` clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
