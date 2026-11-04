# v0.78: Panels rebalanced

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- With the name tabs gone (v0.77), the extra top padding that cleared them was left behind. Removed it: Spectrum, Map and Level panels are 12 px all round (were 22 top, 10 bottom); the Signal panel is 18 px top and bottom on desktop (was 28/18) and loses its 22 px top on phones; the Keys pop-up is 18 px top and bottom (was 30/18).

## Verified
- Desktop and phone screenshots: even margins in every panel. Phone layout check clean, no overflow.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
