# v0.89: Power off, Level grid

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- Power off: when stopped, the map (canvas and the line under it) and the controls (presets, shuffle, dial, tape, VOL, and the tuner on phones) dim to 25%, alongside the art and title that already dimmed. PLAY/STOP stays fully lit as the power switch. They fade back up over half a second on play, and stay usable while dimmed.
- A faint 12 px graticule sits behind the Level displays (Fluid and the rest), like a scope's grid. Its colour is a `DISPLAY` token (`--grid`), so it follows every mode.

## Why
- Robert's screenshot showed the map and controls at full brightness while the rest of the console was off. He asked for a grid in the mostly black Level box.

## Decisions made
- 25% rather than the art's 20%, so the dimmed controls stay findable. The map's range switch stays lit, since it's a control you'd use while stopped.
- The VOL row dims through its children: as a direct child of the console, its boot animation holds its own opacity at 1. Recorded in HANDOFF.

## Verified
- 1440 x 900 and 375 px, stopped: map, controls and VOL dimmed, PLAY/STOP lit (screenshots); the grid shows behind Phosphor and Fluid. `selfTest.core()` and `selfTest.layout()` clean. The fade itself couldn't be watched, since the hidden browser pane doesn't run CSS transitions.

## Next steps
- Pattern for the now-playing box: proposal pending. Re-drag `app/web` to Netlify. See TODO.md.
