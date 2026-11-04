# v0.79: Lunar, Eclipse and Solar display modes

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- Three display modes replace night, dusk and bright:

| Mode | Look |
|---|---|
| Lunar | The dark mode, from the old BRT: pure black, the brightest amber, strong glows, no vignette or scanlines |
| Eclipse | A painted chassis with cream lettering, amber accents and dark glass. The tint is a slider with five notches (grey, green, blue, violet, red) that snaps to each and blends in OKLab between them |
| Solar | Solarized light: cream chassis, pale glass, dark ink, Solarized orange as the accent. The displays go light too, for phones in the sun |

- One brightness setting, 40 to 140, for everything that carries information: lettering, lines, displays and art. Backgrounds and glass stay put. Low settings cover what dusk did.
- The header key reads LUN, ECL or SOL and opens a display panel under it: a three-way mode switch like the map range, the tint strip like the tape tuner (shown in Eclipse only), and a dot bar like VOL. Full width on phones. T cycles modes, [ and ] step brightness, Esc or a tap outside closes it.
- Every mode's colours now live in one script in `<head>` (`DISPLAY`), applied before first paint, so a saved Eclipse tint doesn't flash. Old night, dusk and bright settings land on Lunar.
- The map's cached base layer redraws when the tint changes its glass.

## Why
- The dark-only modes were unusable on a phone in the sun and tiring on a laptop in daylight, and DSK and BRT were too close to tell apart.

## Decisions made
- Chosen over two mockup rounds in `mockups/light-modes.html`. Solar beat Paper (light chassis, dark displays) and LCD (grey-green, black ink).
- Orange and yellow were tried for a warm Eclipse tint and dropped: they share amber's hue and the keys sank into the chassis. Red stayed; violet was added as amber's opposite.
- Lunar and Solar stay a switch, not one slider with Eclipse: the lettering and Solar's inverted displays can't blend through the middle.
- Solar recolours the displays with a CSS filter rather than new colours in each canvas. The canvases have about 60 hard-coded ambers; the filter keeps them consistent and was what the mockup approved. If a display looks off in Solar, give that canvas `DISPLAY` tokens.

## Verified
- 1440×900: Lunar, Eclipse at blue-to-violet, and Solar, with the panel open; the map glass follows the tint. 375 px: panel full width at red, no page overflow.
- Keys: T cycles to Solar, ] steps to 110 and stops at 140, Esc and an outside tap close the panel, settings persist across reloads. An old saved night setting loads as Lunar.
- `selfTest.core()` clean (79 stations, 20 displays); `selfTest.layout()` clean at 375 and 1440.

## Next steps
- Re-drag `app/web` to Netlify, then try Solar on the iPhone in direct sun. See TODO.md.
