# v0.95: Amber to green

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- A COLOUR row in the display panel, a strip like the tint strip running AMBER to GREEN. It snaps to each end and blends through yellow-olive between them. One setting for all three modes, remembered per device.
- What turns: lettering, keys, glows, lines, unlit segments, the textures, and every display, the art and the maps. The tokens turn in OKLCH toward one green hue, keeping their lightness, so contrast holds; the canvases and art turn with a CSS hue rotation (70 deg, or 90 for Solar's dark ink). Solar's orange lands on the same green as Lunar's amber.
- What doesn't: the warning blue, Eclipse's chassis tints and cream lettering, Solar's slate lettering and every background.
- The day bar in the signal panel used a hard-coded amber; it's a token now, so it turns too.

## Why
- Robert asked for a UI slider from amber to green.

## Decisions made
- Eclipse GREEN with green lettering is allowed; Robert will avoid that combination himself.
- HANDOFF's colour rule now reads amber by default, green by choice.

## Verified
- Green in all three modes: Lunar amber #ffc24a to #8be78f, Eclipse #ffb84a to #86e08a, Solar #cb4b16 to #19932e; at 0 everything is as before (Lunar #ffc24a). Screenshots at 1440 x 900 (Lunar, Solar) and 375 px (panel). No console errors; `selfTest.core()` and `selfTest.layout()` clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
