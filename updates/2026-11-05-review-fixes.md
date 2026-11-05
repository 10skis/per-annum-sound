# v0.88: Code review fixes

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
A high-effort review of v0.79 to v0.87 found ten issues; all are fixed.

| # | Fix |
|---|---|
| 1 | Solar on the installed iPhone app: a dark strip (#073642, Solarized base02) fills the safe area under the status bar, whose text is white (black-translucent). Standalone mode only |
| 2 | Glows fade with brightness below 100, so halos don't outshine dimmed lettering in a dark room |
| 3 | Keys work while a slider has focus: after dragging tint, brightness or volume, Esc closes the panel and T, [ ], space and / work. Sliders keep only their own arrow keys |
| 4 | Canvas glass is erased to transparent rather than painted with `--screen` (lakes, rivers, map label backings, NO CARRIER, spectrogram labels, Ridges' hidden lines), so the panel's glass shows through. In Solar these were near-white patches |
| 5 | The map base layer's cache key no longer reads a style each frame |
| 6 | Search re-filters when the NTS schedule changes what's on |
| 7 | The controls plate sits on the controls' named grid areas instead of line numbers |
| 8 | Two stale comments corrected (Lunar's black-to-grey strip; every mode has a tint) |
| 9 | `--plate` dropped; the plate uses `--fill` |
| 10 | `store` moved into the head script and shared with `DISPLAY` |

## Verified
- Glow alpha at brightness 40: #ffc24a52 (was cc). From a focused brightness slider: ] stepped to 105, T cycled the mode, Esc closed the panel. Plate still 80-523 px, matching the signal panel. Solar NO CARRIER boxes on the panel glass. Search "jazz" 05/79.
- No console errors. `selfTest.core()` and `selfTest.layout()` clean at 1440 and 375.
- Not verifiable here: the status-bar strip only shows in the installed iPhone app. Added to the iPhone check in TODO.md.

## Next steps
- Re-drag `app/web` to Netlify, then check Solar's status bar on the iPhone. See TODO.md.
