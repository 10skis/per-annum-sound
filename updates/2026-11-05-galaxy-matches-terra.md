# v0.92: Galaxy matches Terra

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- The galaxy is drawn in the maps' own palette: square dots in Terra's land tones (up to its 3 px #86601f squares, brighter where the arms are denser), the same yellow station squares and widening square ring as Terra's cities, dotted arm lines, a dotted graticule outside the disc like the map grid, and plotter text in the dim amber of Terra's corner coordinates. The orbit rings and bearing ticks are gone.
- `MARK` and `MARK_HOT` are now shared by the maps and the galaxy.

## Why
- Robert's screenshots showed Galaxy and Terra as two different styles. The galaxy read the CSS colour tokens, which are already bright; Lunar's canvas filter (brightness 1.6) took them to white, the only white in the app.

## Verified
- 1440 x 900, Lunar GRAPHITE: galaxy and Terra compared side by side at full brightness. No console errors. `selfTest.core()` and `selfTest.layout()` clean.

## Next steps
- Power down/up animation, station list texture, amber-to-green colour slider. Re-drag `app/web` to Netlify. See TODO.md.
