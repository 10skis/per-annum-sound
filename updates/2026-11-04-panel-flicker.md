# v0.80: Display panel opens without flickering

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- The display panel no longer flickers when it opens. It sits inside the console (`.unit`), so it was picking up the console's boot animation (0.7 s in six steps), and a CSS animation restarts each time an element goes from hidden to shown. The panel now opts out with `animation: none`; the console's own boot is unchanged.

## Why
- Robert saw the menu flicker each time he opened it.

## Decisions made
- The panel opens instantly rather than with a new transition of its own. No ask for one.

## Verified
- 1440 and 375 px: three opens in a row, each with no animation and full opacity at once; the header still runs its boot animation. Page stays 375 wide on phones.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
