# v0.42: Christmas tree glyph for Christmas Vinyl HD

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Christmas Vinyl HD (44) shows a small outline Christmas tree on the dial and tape instead of ﾛ.
- Unicode has no plain tree, only the colour emoji, which would break the amber-only rule. So it's a drawn SVG in `currentColor`: it dims and lights like the text glyphs, with a drop-shadow glow when current.
- New per-station `glyph:` field in stations.yaml (`glyph: tree`), looked up in `GLYPH_ART` in the page. It follows the station, not the slot number, so adding or moving stations won't hand the tree to another station. The server passes `glyph` through.

## Verified
- Dial and tape render the tree (3 SVGs: dial plus both tapes). At 120 px it reads as a tree at the same stroke weight as ﾛ and ⏀, lit and dim.

## Next steps
- Re-drag `app/web` to Netlify (covers v0.35 to v0.42).
