# v0.63: Mirrored shuffle key

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- The shuffle key is cut at the top-right and bottom-left, so its notch faces PLAY's top-left notch across the gap. It's the one mirrored key; every other key keeps top-left and bottom-right.
- Chosen from `mockups/key-row.html`: A was the old key, B joined shuffle, PLAY and STOP into one bar, and C was this one.
- The mirrored corners are set on the key's id, so pressing it can't reset them.

## Verified
- 375 px screenshot: notches top-right and bottom-left, layout clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
