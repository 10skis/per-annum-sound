# v0.45: Glyph dial app icon

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- New home-screen icon, option D from `mockups/app-icon-dial.html`: the desktop dial's rotating window, an arc of katakana fading out either side of the lit ｦ with the needle above, on a dark dot-matrix plate. Below it, ｦ again, large, in LED dots (13x13 grid, lit dots glowing, unlit ones dim). Soft glass highlight across the top. No letters.
- Replaces the v0.44 display-window icon. Robert compared it with C (the same arc with PAS in dots) and picked D.
- `dev/icon.js` now draws this; `make_icons.py` only had its description updated.

## Verified
- 180 and 512 px PNGs written and copied into web/static; the 180 px file matches the mockup.

## Next steps
- Re-drag `app/web` to Netlify, then delete and re-add the home-screen shortcut so iOS picks up the icon.
