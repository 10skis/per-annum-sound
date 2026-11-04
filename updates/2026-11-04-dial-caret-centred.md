# v0.76: Dial caret centred over the glyphs

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- Robert's four close-ups (ｴ, ﾆ, ﾊ and the tree) showed the real fault: every lit glyph sat about 1 px right of the caret, and touched or overlapped it from below. Measured from his screenshots: glyph centre 4.5 image px right of the caret centre in all four, at about 4.6 image px per CSS px.
- Cause: the caret was a CSS border triangle. Browsers round border widths to whole device pixels, so at the desktop fit's zoom (about 0.77) the triangle shrank toward its left edge and sat left of the glyphs, which are placed exactly. It's now a clipped shape (`clip-path`), centred with a transform, which scales without rounding.
- The ring is pulled in (desktop `--ring` 82 to 76 px, default 72 to 66) so the lit 15 px glyph clears the caret.
- v0.75's full-circle ring stays.

## Verified
- Enlarged 8× in the build: the caret and the ink of ｴ, ﾆ, ﾊ and the tree share a centre to within half a pixel, with a clear gap between caret and glyph. The rounding fault itself only shows at the real fit zoom and couldn't be measured in the browser pane, so Robert's eye is the final check.

## Next steps
- Robert to check a few stations at his window size.
- Re-drag `app/web` to Netlify. See TODO.md.
