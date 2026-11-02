# v0.10: Halftone art

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- Show and mixtape art is now an amber halftone: 32 dots across on a 45° grid, dot area tracking brightness, midtones eased slightly darker (gamma 1.2) so highlights stay as separate dots. It replaces the Floyd–Steinberg dither, which turned busy photos into speckle.
- Station logos get a clean 1-bit threshold instead, since a dot grid breaks up their lettering.
- Web art is rendered at 512px with smooth dot edges (was 128px blown up). `art.py` also has a 128px crisp mode for the device's OLED; it renders in about 16ms.
- Same algorithm in `art.py` (server and build) and in the page (no-server version), so both match. Checked side by side on live NTS covers, mixtapes, logos and a no-art station.

## Why
- Robert found the dithered art looked wrong; he picked the 45° halftone from a side-by-side mockup.

## Decisions made
- Logos stay 1-bit, not halftone (flagged to Robert).
- Kiosk's logo is blocky because its source is a small favicon; a bigger source would fix it.

## Next steps
- See TODO.md.
