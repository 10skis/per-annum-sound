# v0.75: Dial glyphs round the full ring

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- Robert saw every dial glyph as off centre. Measured in his screenshot and in the app, each glyph sat exactly on its ring position and was centred in its box: the cause was the shape. The 13 visible glyphs (current station plus six either side) were spaced 21° apart, an arc of about 250° open at the bottom, so the ring looked like it sat high around the station number.
- They now share the whole circle evenly (about 27.7° apart), current station still at the top under the caret, so the ring sits centred on the number.

## Verified
- Dial enlarged 4× in the build: thirteen glyphs evenly round the number, lit station under the caret.

## Next steps
- Robert to judge it in use; if glyphs still look off, get a pointer to which ones.
- Re-drag `app/web` to Netlify. See TODO.md.
