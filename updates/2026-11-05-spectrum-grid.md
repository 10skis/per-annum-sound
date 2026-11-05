# v0.91: Grid behind the spectrum

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- The Level panel's faint 12 px graticule now sits behind the spectrum displays too (the two screens beside the map). One rule covers both. Full-frame displays such as the spectrogram cover it, as they should.

## Why
- Robert asked for the grid behind the spectrum as well.

## Verified
- 1440 x 900: grid behind Lissajous and Ridges (screenshot), 12 px on all three canvases. 375 px unaffected. Self test clean in v0.90's run; no layout change here.

## Next steps
- Station list ("add text"): what's meant is being asked. Galaxy vs Terra cohesion: proposal pending. Re-drag `app/web` to Netlify. See TODO.md.
