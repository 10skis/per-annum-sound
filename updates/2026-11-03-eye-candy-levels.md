# v0.52: Phosphor, Fluid and Reels level displays

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- The level screen has eight displays: Trace, Meter, Needle, Goniometer (the dot cloud with LO and HI clouds), Loudness, then three for eye candy.
- **Phosphor:** the goniometer's second version (v0.49's glowing trace with trails and the correlation bar), kept as its own display.
- **Fluid:** cornstarch on a speaker cone. A puddle of dots on dim cone rings, its outline wobbling slowly. Bass kicks throw out fingers that shoot up fast and sag back over about a second, and it leans toward the louder channel. Small LO (swells and rolls) and HI (quivers with fine spikes) puddles sit either side.
- **Reels:** a tape deck's two spools in dots, turning at play speed and nudged by the level. The tape winds left to right over about ten minutes, and the head between them glows with the level.
- Level displays ignore a negative frame time, which would otherwise wreck the reel angle and the meter smoothing.

## Verified
- Frames of all three drawn by hand and saved. Fluid keeps up to nine fingers alive and most of them sagging; Reels shows no radial streaks after each tape ring was started at a different angle.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
