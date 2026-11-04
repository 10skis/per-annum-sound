# v0.72: Solarized NGT, DSK corners

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- NGT is now Solarized dark: base03 chassis (#002b36), darker glass behind the displays, base02 for unlit segments and ghosts, base0 grey for quiet labels and key outlines. Amber stays the accent (lit keys, titles, displays), close to Solarized's own yellow and orange. DSK and BRT keep the original near-black.
- A new `--screen` token holds the glass colour; canvas fills that used a fixed near-black (map labels, lakes and rivers, NO CARRIER plates, the level meter's label strip) now read it, so they match every mode. The map's cached base layer redraws when the mode changes.
- DSK fix: its panel rule set the `background` shorthand, which wiped the diagonal lines drawn across each panel's cut corners, so the art panel's top-left and bottom-right corners looked open. Panels now set only the colour.

## Verified
- Desktop in NGT: chassis, glass, keys, map and tabs all in the Solarized tones with amber accents. Phone in DSK: the art panel's cut corners are drawn.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
