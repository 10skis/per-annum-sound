# v0.50: Breathing ripple, goniometer side scopes

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- The dot ripple is slower and softer: a ring takes 5.2 s and a sweep 4.6 s, up from 1.8 and 1.5. The wave travels at an even pace, dots swell by up to about 40% and ease back slightly smaller just behind it, and its strength fades in and out over the run. The bright highlight colour is gone. The picture breathes rather than flashes.
- Ripples now come every 7 to 16 s, up from 5 to 14, so one never overlaps the next.
- The logo overlay matches: same slower timings, fading in and out at about 40% opacity.
- Goniometer is back to an analog feel: dots instead of a glowing line, the signal window sliding at a fifth of real time, 22 ms of signal per frame so it draws a figure rather than a block, and trails that fade over about a quarter second.
- Small LO and HI scopes fill the space either side of the main one: the bass alone as a slow loop, the treble as a turning 3:4 figure. They only appear where there's room.

## Verified
- Frames drawn by hand and saved (the browser pane runs no animation frames while hidden): the three scopes read as distinct figures, and a mid-run ripple shows a soft band of swollen dots with slightly shrunken ones behind it.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
