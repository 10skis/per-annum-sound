# v0.44: Display-window app icon

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- New home-screen icon, option 2 from `mockups/app-icon-options.html` with a dark background as Robert asked: the site's near-black background with its faint amber dot texture and darker rim; a display window drawn like the site's panels (two chamfered corners, deep black fill, a brown-amber edge, unlit dot matrix inside); PAS glowing in VT323; an inverse "01" code tab on the top-right corner; registration brackets at the two square corners; a soft glass highlight across the top.
- Replaces the v0.43 sigil icon, which didn't fit the iOS 26/27 look.
- `dev/icon.js` now draws this; `make_icons.py` is unchanged apart from its description.

## Verified
- Preview at 280 px and at 60 px on light and dark wallpaper: PAS readable at home-screen size. 180 and 512 px PNGs written and copied into web/static.

## Next steps
- Re-drag `app/web` to Netlify, then delete and re-add the home-screen shortcut so iOS picks up the icon.

## Follow-up (same version)
- Robert still doesn't love the display window and asked about a glyph dial with dot matrix. Mockup `mockups/app-icon-dial.html`: A, full katakana ring with the top glyph lit and a needle, PAS in LED dots in the middle; B, the same ring with ｦ (the dial's first glyph) in LED dots in the middle, no letters; C, the desktop's rotating window as an arc of fading glyphs, PAS in LED dots below. Not built; the display-window icon stays in the code until he picks.
