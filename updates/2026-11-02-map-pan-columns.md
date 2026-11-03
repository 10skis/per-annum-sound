# v0.24: Pan while zoomed, balanced two-column board

**Date:** 2026-11-02
**Project:** Per Annum Sound

## What changed
- **Map panning.** While zoomed, drag the map or use a two-finger scroll to move around. In the world view sideways movement turns the globe (it wraps); up and down, and everything in the Europe view, stops at the map's edges. A drag doesn't count as a click, so it won't zoom back out. On phones a finger drag pans the map instead of the page only while zoomed. Panning eases back to centre when zooming out. When not zoomed, scrolling over the map scrolls the page as before.
- **Station board.** Between 960 and 1279 px wide (two columns), Genre Radio and Deep Cuts sit under Terrascan FM in the right column instead of under NTS. Three columns from 1280 px. Any new group still lands in the third column by default.

## Verified
- Zoomed drag of 60 × 42 px moved London's marker 60 × 36 (stopped at the bottom edge); the click ending the drag didn't zoom out; a two-finger scroll was captured and panned. At 1100 px the third column sits under the second; at 1440 px three columns side by side.

## Next steps
- See TODO.md.
