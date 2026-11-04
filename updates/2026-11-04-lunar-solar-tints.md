# v0.83: Lunar and Solar tint strips

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- The tint strip now shows in every mode, with notches of its own:

| Mode | Notches | Default |
|---|---|---|
| Lunar | COOL (blue-black) / NEUTRAL / WARM (amber-black) | NEUTRAL |
| Eclipse | GREY / GREEN / BLUE / VIOLET / RED | BLUE |
| Solar | COOL (grey-white) / CREAM / WARM (parchment) | CREAM |

- Lunar's and Solar's notches stay in one hue family and move only the chassis, glass, lines and unlit segments. Amber, the lettering and the displays don't change. The middle notch is the v0.79 look.
- Each mode remembers its own tint. A saved Eclipse tint from v0.79-0.82 carries over.
- Solar's painted glass is now a token (`--glass`), so it follows the notch.

## Why
- Robert asked for Lunar and Solar tints on a monochromatic scale, unlike Eclipse's colour wheel.

## Decisions made
- Three notches each, as proposed and approved ("Yes, in order"). Solar's display ink stays the same in every notch, since the Solar filter's contrast takes the canvas glass to near white regardless.

## Verified
- Each mode's strip, names and range; tints remembered per mode across switches; blends between notches (Lunar 1.5 reads ~WARM).
- 1440 x 900: Solar cool and warm, Lunar cool, panel open. 375 px: panel at Solar warm, no page overflow. `selfTest.core()` and `selfTest.layout()` clean.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md. The Lunar and Solar strips are faint by nature (close shades); if they're hard to read, outline the segments in a stronger tone.
