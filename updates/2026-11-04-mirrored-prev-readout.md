# v0.64: Mirrored ◀, symmetrical readout

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- The ◀ key is mirrored like shuffle, cut top-right and bottom-left, on the phone tuner and beside the desktop dial.
- The 01/66 readout is cut at both top corners. On the phone tuner row, ◀'s notch meets the readout's top-left, the readout's top-right meets ▶'s top-left, and the outer bottom corners mirror each other, so the row is symmetrical.
- The mirrored corners are now one shared rule (`.key.mirror`) instead of shuffle's own, and pressing a key can't reset them.

## Verified
- 375 px: tuner row symmetrical, layout clean. 1100 px: dial ◀ mirrored. `selfTest.core()` clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
