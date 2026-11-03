# v0.31: Volume swipe, LEVEL modes, live sigil

**Date:** 2026-11-02
**Project:** Per Annum Sound

## What changed
- **Volume** responds to a two-finger sideways swipe over the bar, like the tuner tape: steps of 5 per ~18 px, swiping left turns it up (same direction as the tape), sent once the swipe settles. Vertical scrolling still scrolls the page.
- **05 LEVEL** cycles through five displays on click (the screen or its label), remembered per device: Trace (L/R over 30 s), Meter (two LED bargraphs with peak hold and a dB scale), Needle (one analog VU), Goniometer (stereo image as a dot cloud), Loudness (a rolling bar every quarter second).
- **Sigil** is now drawn live for stations with no logo: while playing, each ring turns at its own slow speed in alternating directions, and the shimmer's ripples and sweeps light up the dots as they pass (the CSS shimmer is skipped there, since it masks a still image). The middle shows the city code large with the city name under it, instead of the station number (which the dial already shows). Server-side still image updated to match.

## Verified
- Bangkok and KEXP show the live sigil with BKK / BANGKOK and SEA / SEATTLE; rings advance each frame; a ripple draws through the dots. All five LEVEL displays draw without errors and a click steps to the next. Volume swipe moved 80 to 60 in four steps.

## Next steps
- See TODO.md.
