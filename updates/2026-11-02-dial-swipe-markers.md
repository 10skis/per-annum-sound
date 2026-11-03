# v0.21: Dial direction, trackpad swipe, orange markers

**Date:** 2026-11-02
**Project:** Per Annum Sound

## What changed
- **Dial direction flipped.** Upcoming stations now wait on the left of the ring, so stepping forward (turning clockwise, ▶, right arrow) turns the ring clockwise with the hand, like a knob.
- **Trackpad swipe on the tape.** A two-finger horizontal swipe over the tape scrubs it (about one station per 28 px; swipe left for higher stations), previews with RELEASE TO TUNE, and tunes once the swipe settles (0.38 s). Vertical scrolling over the tape still scrolls the page.
- **Map markers.** Solid orange (#ff7a1a, the playing city brighter #ff9a3c with a stronger glow), slightly larger, with an orange pulse ring. Labels stay amber.

## Verified
- Ring angles: next station at -21°, previous at +21°. Swipe of 120 px moved 4 stations and tuned; 90 px back moved 3; a vertical scroll over the tape was not intercepted. Markers render orange.

## Next steps
- See TODO.md.
