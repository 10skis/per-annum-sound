# v0.62: Visual guidelines pass

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
Checked against `context/visual-design.md`. The deliberate breaks (detailed console, bordered display windows, halftone, dot font, caps readouts, corner gradients) stay under the project's own spec. Robert approved four fixes:
- **Section numbering (12):** panel tabs show names only (Art, Signal, Spectrum, Nav, Level, About, Keys). The numbers weren't a sequence and read 01, 02, 03, 05, 04 down a phone.
- **Tags (1):** genres are plain text, HOUSE · GARAGE, not bordered boxes.
- **Shades and opacities (7):** every see-through colour in the CSS is now a named token: `--glow`, `--glow-soft`, `--warn-glow`, `--texture`, `--vignette`, `--scanline` and `--scrim`. The 66 and 55 glows merged into one soft glow. Bright mode now just retunes `--glow` and `--glow-soft` instead of restating rules.
- **Dividers (6):** the dashed rule above Up Next is gone; spacing sets it off. The header rule stays as part of the chassis.

## Verified
- The CSS has no see-through colours left outside the token definitions. Bright picks up the stronger glow through the tokens.
- `selfTest.core()` and layout clean at 1100 and 375 px. Screenshot at 1100 px.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
