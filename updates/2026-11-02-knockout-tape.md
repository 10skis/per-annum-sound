# v0.19: Knockout art, clickable tape

**Date:** 2026-11-02
**Project:** Per Annum Sound

## What changed
- **No-art stations.** The name is now cut out of the dot pattern as empty space, with no box. The pattern uses a finer halftone (64 dots across) so the letters read, and it stays dense behind the name, fading back to the open pattern over about 14 px. Same design in the browser and `art.py`.
- **Phones.** Volume sits above the visualizers.
- **Map labels.** Markers and labels are no longer rounded to whole pixels, so they glide with the drifting dots instead of stepping behind them. Each label keeps its position from the last frame while it still fits, so labels stop hopping between sides.
- **Tuning tape.** Tap a tick to tune to it, or drag the tape (left for higher stations, right for lower). It previews with RELEASE TO TUNE and plays on release. Works on the desktop tape under the dial and the phone tape under the tuner.

## Verified
- Phone 375 px: volume above the deck, no overflow, knockout art renders. Tape tap moved to the tapped tick; drag of 50 px left moved 5 stations, 30 px right moved 3 back.

## Decisions made
- More visualizers and a replacement for the crowded glyph dial were questions; answered with options, nothing built yet.

## Next steps
- See TODO.md.
