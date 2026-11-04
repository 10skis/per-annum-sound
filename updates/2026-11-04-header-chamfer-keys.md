# v0.61: Phone header balanced, chamfered play keys

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- Phones: the header sits P·A·S on the left, with status, mode and help on the right, instead of everything bunched on the left.
- The shuffle key and PLAY/STOP now have chamfered corners like the presets and arrows. PLAY/STOP is one key in two halves, cut as one: PLAY takes the top-left corner, STOP the bottom-right. On the lit half the diagonal turns full amber.
- Fixed while doing it: the lit half's background shorthand reset the corner's size, which drew a diagonal across the whole key. Size and repeat now sit where the lit style can't override them.

## Verified
- 375 px screenshots: header spread edge to edge; keys chamfered with PLAY lit and with STOP lit. 1100 px: same keys, header unchanged. `selfTest.core()` and `layout()` clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
