# v0.73: Galaxy zoom and pan; plainer phone maps

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- GALAXY zooms and pans like the maps: tap or click empty space to zoom in 2.6× about that point (deeper than the maps' 1.9×, since an arm's stations sit close together), drag or two-finger scroll to move, tap again to come back out. Tapping a star still plays it. The halftone grid stays fixed while the disc grows under it, so it gets finer as you zoom. The corner readout shows ×2.6 when zoomed, and arms whose tip is off-frame drop their label instead of pinning it to the edge.
- The maps' eased zoom and panning moved into `zoomStep()` and `toggleZoom()`, shared by the maps and the galaxy.
- Phones (map narrower than 460 px): USA and EUROPE draw no geography at all, plain dots like TERRA. (First pass kept lakes and a faint border trace; Robert wanted them gone.) Desktop keeps borders, state lines, rivers and lakes.

## Verified
- Galaxy: click zooms to 2.6, drag and wheel pan, click on empty space zooms out, clicking a star plays it; zoomed render checked.
- Phone width: USA and EUROPE renders checked; `selfTest.core()` clean, no layout overflow.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
