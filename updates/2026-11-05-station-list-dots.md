# v0.94: Dots on the station list

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- The station list on desktop gets the same sparse, faint dot matrix as the now-playing panel (14 px, `--strip-dot`), since both are mostly text. One rule now draws both.
- Phones don't get it: the list has no frame or fill there, so dots would float on the chassis.

## Why
- Robert asked for texture on the station list ("add text" was a typo).

## Verified
- 1440 x 900: dots behind the groups; the playing row's highlight and hover still sit above them. 375 px: no dots, no overflow. `selfTest.core()` and `selfTest.layout()` clean.

## Next steps
- The amber-to-green colour slider. Re-drag `app/web` to Netlify. See TODO.md.
