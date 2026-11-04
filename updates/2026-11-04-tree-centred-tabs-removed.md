# v0.77: Tree centred; panel labels removed

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- Robert accepted the text glyphs as centred and pointed at the tree, which was genuinely off: measured from his screenshot, about 1.5 image px left of the caret. The tree is the one SVG glyph. At 1em of the lit 15 px font, centring it put its edge on a half pixel, and the browser snaps drawn images to whole pixels. It now has even sizes (12 px, 16 px lit), so its offset is a whole 8 px.
- Removed the name tabs from every panel (Art, Level, Signal, Spectrum, Nav, About, Keys) and their CSS, per the visual guidelines.

## Verified
- Lit tree: centre equal to the dial's centre, shift -8 px exactly. No `.tab` elements left; desktop screenshot clean.
- Lesson from this run: my 4× check image drew its guide line 2 px off, which made a centred arrow look wrong. Draw guides at the measured centre, not the pixel index.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
