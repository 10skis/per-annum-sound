# v0.60: Ridges steady

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- v0.57 made every ridge slide back a step between samples, so the whole landscape crept upward by fractions of a pixel and the dots shimmered. Each ridge now stays put and its shape blends from its sample toward the newer one in front: the heights flow back through the rows with no sliding. Dots snap to whole pixels, and samples land on an exact beat so the blend never skips.

## Verified
- 90 frames of each version, counting the pixels that change from one frame to the next:

| Version | Average | Biggest jump | Still frames |
|---|---|---|---|
| v0.56 (original) | 2.6% | 20.8% | 75 of 89 (it moved in jumps) |
| v0.59 (sliding) | 20.2% | 21.8% | 0 |
| v0.60 | 2.2% | about 2% once the rows have filled | 0 (moves steadily) |

- The only bigger changes (about 9%) come in the first 1.5 s after switching to Ridges, while its 14 rows fill in.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
