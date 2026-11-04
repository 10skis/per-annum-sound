# v0.70: Map ranges USA, Europe, Terra, Galaxy

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- The Nav map has four ranges, in this order: USA, EUROPE, TERRA, GALAXY. TERRA is the world view renamed; it is still `world` in code and in the saved setting, so nobody's choice resets.
- USA covers 128°W to 62°W, 24.5°N to 52°N, so Vancouver and Montreal are on it. In TERRA, tapping the North American cluster zooms to USA, the same way the European cluster zooms to EUROPE.
- GALAXY is the mockup made real (`drawGalaxy`): a barred spiral, NTS and the mixtapes round the bulge, one arm per group lit by group size, stations along each arm by longitude and joined like a constellation, orbit rings and bearing ticks, one turn every five minutes (still with reduced motion). Hover a star for its name and city, tap to play. No zoom or pan in this range.
- M steps through all four. Help text updated.
- Below 460 px the map's label gives way so the four keys fill the row.
- `selfTest.core()` draws all four ranges and checks M.

## Verified
- `selfTest.core()` clean (79 stations, 20 displays, all four ranges, controls). USA render shows Vancouver, Seattle, LA, Kent, Pittsburgh, New York and Montreal. Phone width: four keys fit, no overflow.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
