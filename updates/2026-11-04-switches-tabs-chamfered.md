# v0.69: Switches and tabs chamfered

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- The map range switch reads EUROPE then WORLD.
- Two-way switches (map range, and the radio/phone output switch on the Pi server) are cut like PLAY/STOP: one key in two halves, the left half cut top-left, the right half bottom-right, with the diagonal drawn in the key colour.
- The instrument tabs in each panel's top-right corner (Art, Level, Signal, Spectrum, Nav, About, Keys) have their inner corner cut, so they share the chamfer language of the keys and panels.
- Galaxy mockup puts its key after WORLD to match.

## Verified
- Built and checked at desktop and phone widths: switch order, cuts on both halves and in the lit state, cut tabs on every panel.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
- Galaxy map view still waiting on Robert's call.
