# v0.84: Lunar black to grey, taller Level panel

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- Lunar's tint strip runs BLACK / GRAPHITE / GREY instead of cool / neutral / warm. The glass and unlit segments step up with the chassis. Lunar starts at BLACK for everyone, since the old notches meant something else.
- The taller Level panel is back (option B in `mockups/level-height.html`): 20 px above and below the dial on desktop, so the top row and the panel under the art are 40 px taller. The console scales to 89% at 1440 x 900 instead of 95%.

## Why
- Robert wanted Lunar as a black to light grey gradient, and Fluid still looked squished at fit-only.

## Decisions made
- GREY stops at #3d3d3d. Lighter greys can't carry amber lettering: the quiet amber is 4.8:1 there, 4.1:1 at #474747 and 1.7:1 at #808080. Going further needs dark lettering, which is what Solar is.

## Verified
- 1440 x 900: Lunar at GREY with the panel open; Fluid canvas 280 x 93, drawn frames stay between rows 28 and 202 of 208; console at 89%. Stored Lunar tint reset to BLACK on first load. 375 px: no overflow. `selfTest.core()` and `selfTest.layout()` clean at both widths.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
