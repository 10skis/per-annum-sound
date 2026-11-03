# v0.15: Presets, sleep timer, keyboard

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- Six preset keys replace the NTS 1 / NTS 2 keys. Tap plays a slot; hold (600 ms) saves the current station; tapping an empty slot saves too. Slots 1 and 2 start as NTS 1 and 2. Saved on the device. The playing preset lights up.
- Sleep timer: the ZZ button by the listening timer cycles 15, 30, 60, 90 minutes, off, and shows the countdown. At zero the radio stops; on devices that allow volume the last 10 seconds fade out (not on iPhone).
- Keyboard: space play/stop, left/right tune, 1-6 presets, shift+1-6 save to a slot, S sleep. The volume slider keeps its own arrow keys.
- On phones the header drops the words ON AIR (the lit dot stays) and tightens spacing so both timers fit.
- Verified: number keys, arrows, space, tap-to-play, empty-slot save, hold-to-save without replaying, sleep cycle and stop at zero; header fits at 375px with both timers at their longest.

## Why
- Robert picked presets, sleep timer and keyboard shortcuts from the modern-player survey.

## Decisions made
- Presets replace the NTS keys rather than sit beside them, to save space; NTS stays on 1 and 2 by default.
- Presets are per device for now. When the Pi arrives they should move to the server so the physical buttons and the app share them.

## Next steps
- See TODO.md.
