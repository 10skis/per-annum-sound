# v0.14: Dial arrows, listening timer

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- Desktop dial has ◀ and ▶ buttons either side; each steps one station and plays it.
- Listening timer in the header next to ON AIR: starts when a station starts, restarts on a new station, clears on stop. Shows m:ss, then h:mm:ss past an hour.
- Verified on desktop (arrows step and play, timer ticks and resets) and at 375px (header fits even at 11:02:13).

## Why
- Robert asked for arrows on the web dial and a way to see how long he's been listening.

## Decisions made
- Timer sits with the ON AIR status rather than near the clock, so it reads as playback time, not time of day.
- Ran a survey of modern radio players (NTS, Radio Garden, KEXP, BBC Sounds, lofi.cafe, Poolsuite, Spotify and others) and gave Robert a ranked shortlist. Nothing from it built yet.

## Next steps
- See TODO.md.
