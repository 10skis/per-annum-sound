# v0.87: Controls plate lined up

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- The plate behind the controls is now the same glass as the art panel, instead of v0.86's lighter halfway tone. It keeps the dot matrix.
- Its top and bottom line up with the art and Level panels on the left and the now-playing panel beside it. It no longer runs past them.
- The controls sit 12 px inside it. That inset came out of the space between TURN · PRESS and VOL (the dial's padding went from 20 to 8 px), so the row height, the taller Level panel and the 89% fit are unchanged.

## Why
- Robert saw the plate as lighter than the panels and running too far, with spare space above VOL.

## Verified
- 1440 x 900, Lunar GRAPHITE: plate 80-523 px, the same as the signal panel and the art-to-Level column; `--plate` equals the panels' glass; keys 14 px and VOL 11 px inside it; fit 0.893 as before. 375 px: no change, no overflow. `selfTest.core()` and `selfTest.layout()` clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
