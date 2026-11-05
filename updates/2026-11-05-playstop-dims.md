# v0.98: PLAY/STOP dims

**Date:** 2026-11-05
**Project:** Per Annum Sound

## What changed
- PLAY/STOP now dims to 25% with the rest of the console when stopped, and warms up with the controls on play. Its amber still moves between the halves on the power curves (v0.97).

## Why
- Robert wanted it dimmed; my case for keeping the power switch lit didn't win.

## Verified
- Stopped: 25%, 0.5 s fall; playing: 1 s warm-up with no delay, leading the sweep. `selfTest.core()` clean.

## Next steps
- Re-drag `app/web` to Netlify, then check on the iPhone in sun that a dimmed PLAY is still easy to find. See TODO.md.
