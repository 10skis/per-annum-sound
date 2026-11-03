# v0.56: 05 Level on phones, by swiping 03

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- On phones, 03 Spectrum and 05 Level share one spot: swipe sideways to flip between them, with two dots under the panel showing which page is up. It uses the browser's own snap scrolling, so it has the phone's momentum and the page still scrolls up and down. Tapping still steps through the displays on whichever page is showing.
- The level screen gets the full 03 area on a phone (309 × 200 at 375 px wide), more room than the desktop strip, which suits Fluid and Reels.
- Desktop is unchanged: 05 stays under the art. The page moves the panel between the two places when the window crosses 960 px.
- The keys panel lists the new swipe.
- Decided against a separate 05 panel on phones (mocked up in `mockups/level-on-phone.html`): the swipe keeps the page the same length.

## Verified
- 375 px: both pages 309 × 200, the swipe lands exactly on 05, the dots follow both ways, no page overflow.
- 1440 px: 05 back under the art at 301 × 152 as before, dots hidden. `selfTest.core()` and `layout()` clean.
- Not verified: the feel of the swipe on a real iPhone.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
