# v0.57: Night, dusk and day modes; desktop fits the window; smoother displays

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- **Display modes**, cycled by a key in the header (NGT, DSK, DAY) or T, and remembered per device. The browser's top bar colour follows the mode.
  - Night: as before.
  - Dusk: everything lifted for a bright room. Lighter chassis and lettering, displays about 30% brighter, softer vignette and scanlines.
  - Day: the console in daylight. A warm cream chassis with ink-brown lettering and a deep amber accent, while every display window stays dark glass with its amber glow, the way real hardware looks in daylight. That also leaves all the visualizers untouched.
- **Desktop fits the window's height.** The console was a fixed 949 px tall, so the map and visualizers ran off the bottom of any laptop browser window. It now scales down, keeping every panel's proportions, until it fits, with a floor of 70%. At full size from about 950 px tall; 84% at 860; 73% at 789. Map clicks, map dragging and the tape correct for the scale.
- **Fluid** stays put (it used to lean with the stereo balance).
- **Lissajous** is smooth: its size eases instead of following raw levels each frame, points no longer snap to whole pixels, and each shape melts into the next instead of jumping.
- **Ridges** is smooth: it keeps its own eased levels, every ridge glides back a step between samples, and a live ridge slides in at the front.

## Verified
- Fit at 1440×789, 1512×860 and 1728×1000 (bottom inside the window). 1280×700 hits the 70% floor and runs 28 px over.
- Screenshots of all three modes at 1100×800. `selfTest.core()` clean; layout clean at 320 and 1440 px; the header fits at 320 px with the new key; T cycles the modes.
- Not checked: the browser pane's size emulation sends no resize events while hidden, so refitting on resize was confirmed by calling it directly. A real window sends them.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
