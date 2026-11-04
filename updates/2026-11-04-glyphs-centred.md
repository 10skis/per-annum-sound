# v0.66: Dial glyphs centred

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- Dial and tape glyphs sat in a box narrower than the wide line-art symbols, and text centring can't centre what overflows, so those symbols spilled to the right (station 51 was the visible one). The boxes now centre their glyph even when it's wider than they are.
- The glyphs come from several fonts that each place their ink differently (line-art runs wide, katakana sits high). The page now measures each glyph's ink once, with the same fonts, and nudges it so the ink's centre is the box's centre. The nudge is in em, so it holds for the 12 px ring glyphs, the 15 px lit one and the 13 px tape glyphs.

## Verified
- A contact sheet of all 66 stations' glyphs in their lit dial style, each on a crosshair: every glyph centres horizontally, and vertically within about a pixel. 12 of the 70 glyphs needed a nudge of more than 5% of their size. The Christmas tree was already centred by v0.47.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
