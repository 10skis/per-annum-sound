# v0.90: Dots in the now-playing panel

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- The now-playing panel gets a faint dot matrix, like an unlit display behind the text: the controls plate's dots at twice the pitch (14 px) and about 60% of the strength, so it sits under the station name and schedule without competing.
- It's drawn on a pseudo-element behind the content, since a background image on the panel itself would replace the chamfer's corner diagonals.

## Why
- Robert wanted a subtle pattern in the black now-playing box, and chose sparser dots over repeating the plate's pattern, so the three textured panels stay distinct (plate dots, sparse dots, Level grid).

## Verified
- 1440 x 900: `--strip-dot` set per mode, 14 px pitch, chamfer corners intact. 375 px: no overflow. `selfTest.core()` and `selfTest.layout()` clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
