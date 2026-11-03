# v0.22: Map hover labels, yellow markers, smooth groups

**Date:** 2026-11-02
**Project:** Per Annum Sound

## What changed
- **Map markers** are just dots until the pointer is over one; its label then wipes out from the dot over about 0.2 s and wipes back when the pointer leaves. A selected city keeps its label (inverse). On phones, tapping a city selects it and shows its label and stations.
- **Marker colour** is bright yellow (#ffe23d; hovered, selected or playing #fff59a) with a yellow glow and pulse, so it stands off the amber land.
- **Station groups** open and close with the same smooth easing as the dial and tape (0.42 s) instead of stepped timing; the contents fade and settle in as a group opens, and the chevron turns smoothly. Reduced-motion turns these off.

## Verified
- No labels at rest; hover on London revealed its label in five frames and reversed to zero after leaving. Group transition reads as the new easing. Markers render yellow.

## Next steps
- See TODO.md.
