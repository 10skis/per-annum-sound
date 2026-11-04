# v0.71: Geography on USA and Europe

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- USA and EUROPE now show country borders (dashed, amber), US state and Canadian province lines (dotted, dim), and rivers and lakes etched out of the land dots (the Great Lakes, Ladoga, the Danube and so on).
- New `make_geo.py` builds `static/geo.js` (52 KB) from Natural Earth's public-domain 1:50m borders, admin-1 lines, rivers and lakes, clipped to the two ranges and simplified. Sources sit in `dev/`.
- Drawn once into the map's cached base layer, so it costs nothing per frame. The service worker cache moved to v3 so phones pick up the new file.

## Verified
- Renders of both ranges: borders, state lines, Great Lakes and the Baltic lakes all present.
- Two generator bugs found and fixed on the way: closed lake outlines collapsed to a point when simplified, and the size filter dropped rank 0 (the biggest lakes and rivers).

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
