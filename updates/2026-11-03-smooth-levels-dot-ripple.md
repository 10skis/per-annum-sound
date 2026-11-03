# v0.49: Smoother levels, phosphor goniometer, dot ripple, haptics

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Level displays run on frame-timed meter ballistics (fast attack, slower release) instead of the raw, noisy levels. Trace and Loudness glide between samples rather than jumping 3 or 4 px at a time; Meter's top segment fades in with the level and the peak falls at a steady rate; Needle is frame-rate independent.
- Goniometer is now a phosphor scope: a short window of stereo signal built from the low, mid and high levels, traced as a glowing line on a buffer that fades each frame, so it swirls and leaves trails. Mid is up, L and R on the diagonals, and a correlation bar runs along the bottom.
- The random key is a shuffle symbol (drawn, currentColor) and sits left of PLAY/STOP.
- Haptics on phones: a tick each time the tuner, tape or dial passes a station, on ◀ ▶ and random, and per volume step. Android uses `navigator.vibrate`; iPhone uses the Safari 18 switch-checkbox tick. Does nothing on desktop.
- Phones show the description as a scrolling line under the title, same pace as desktop; tapping it opens About.
- Shimmer on halftone art now swells the art's own dots: the dots are read back from the image (same 45° grid, size from the ink in each cell) and redrawn as a ring or sweep passes, with faint dots rising in empty cells at the wavefront. Works in both the Netlify and Pi versions. Logos (1-bit, no dots) keep the overlay.
- Scrolling lines re-measure when their width changes. A line that was hidden or zero-width when its text arrived (the phone description, titles after a resize) used to stay unscrolled.

## Verified
- Redrawn dots differ from the original image by 1.5% of ink, so a ripple starts and ends without a jump. Level panel at 62 fps with the goniometer; its figure spans about 120 x 150 px in a 550 x 186 canvas.
- Phone width: RND left of PLAY/STOP, description under the subtitle and scrolling, no page overflow.
- Not verified: haptics need a real phone.

## Next steps
- Re-drag `app/web` to Netlify and try the haptics on the iPhone. See TODO.md.
