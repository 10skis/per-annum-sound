# v0.53: 3D Fluid, Phosphor side traces, mobile fixes, spectrogram

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Phosphor has LO and HI traces either side, in its glowing-line style: the bass as a slow loop, the treble as a 3:4 figure.
- Fluid is three-dimensional: a tilted disc of dots on a hex mesh, drawn back to front and lit by height, on dim cone rings. A rolling swell carries narrow spikes that shoot up and slump back. They spawn continuously (5 to about 40 a second with the level, plus a burst on each bass kick) rather than only on kicks. Tall spikes ease off before the top of the panel. The LO and HI puddles are 3D too: LO a rolling swell, HI a bed of fast, fine spikes.
- Phones:
  - The header switches to its short form (P·A·S, no clock, no "ON AIR" word) below 560 px instead of 420. Between those widths the full header was 70 px wider than the screen, which widened the whole page and pushed the art and tape out of line.
  - The top padding clears the status bar by 14 px on notched iPhones, and the side padding respects the safe area in landscape.
  - The tape under the phone tuner is as tall as the desktop one, so its numbers no longer sit on the group labels.
- A Spectrogram display on 03, added last in the list so saved choices keep their place. Time scrolls right to left and frequency runs up the side (60 to 16K labels); the bands are blended smoothly, and it glides between columns.

## Verified
- At 375, 458 and 1440 px wide: no header overflow, page exactly the screen width, full brand on desktop. On the phone tape, numbers end at 637 px and the group labels start at 639.
- Frames drawn by hand and saved for Phosphor, Fluid and Spectrogram. Fluid costs about 0.5 ms a frame.
- Not checked: the notch spacing on a real iPhone.

## Next steps
- Re-drag `app/web` to Netlify and check the top of the page on the iPhone. See TODO.md.
