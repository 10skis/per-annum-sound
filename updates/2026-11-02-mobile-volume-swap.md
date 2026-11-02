# v0.12: Phone volume note, art and dial swapped

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- On iPhone the volume bar is replaced by "USE THE PHONE'S VOLUME BUTTONS". iOS ignores volume changes from web pages, so the bar could never work there; it was showing "--" and doing nothing. The bar still shows where volume can be set, and in RADIO mode it controls the Pi.
- On phones the art now sits on the left and the dial on the right (was the reverse). Desktop layout unchanged.

## Why
- Robert found the volume bar non-functional on mobile and asked to swap the dial and image.

## Decisions made
- No Web Audio workaround for volume: it needs the stream hosts to allow cross-origin access, which most don't, and it would silence those streams.
- Robert asked whether a dial is the right digital control at all. Answered with a recommendation; nothing changed yet.

## Next steps
- See TODO.md.
