# v0.51: Cloud goniometer back, sigil ripple

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Goniometer is the first version again: a cloud of dots in a diamond, redrawn each frame. Small LO and HI clouds in the same style sit either side, showing the bass and the treble alone, where there's room. The phosphor trace and the correlation bar from v0.49 and v0.50 are gone.
- The breathing ripple now runs on sigil stations too. The ring dots swell on the wave and ease smaller behind it, and the faint background matrix brightens as it passes. Cover art and the sigil share one swell function (`rippleSwell`).

## Verified
- Dublab (sigil) mid-run: the swell runs about +0.3 at the wavefront and down to about -0.13 behind it, and the sigil redraws with it. NTS 1 cover art still ripples its own dots. No new console errors.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
