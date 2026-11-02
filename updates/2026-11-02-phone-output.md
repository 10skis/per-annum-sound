# v0.6: Phone-speaker output and away-from-home access

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- OUTPUT switch (RADIO / THIS DEVICE). In THIS DEVICE mode every control (keys, dial, station list, schedule, play/stop, volume) plays the stream on the device itself, and the server only supplies show info (`/api/now/<station>`). The choice is remembered per device. Lock-screen and headphone controls are wired through the Media Session API.
- Tested in the browser with real audio: NTS 2, The Lot (HLS), and a dial step to Dublab all played; volume, stop, play and switching back to RADIO all worked, and the radio's own state was untouched.
- The Lot uses hls.js from a CDN in browsers without native HLS. That path is untested, because the test browser and iPhone Safari both play HLS natively.
- Fixed a phone layout bug from v0.5: long scrolling titles widened the page past the screen.
- Tailscale setup steps in `app/README.md`.

## Why
- Robert wants to listen on his phone when he's not home.

## Decisions made
- Tailscale over cloud hosting: free, nothing exposed to the internet, one copy of the app. The trade-off is that the machine at home has to be on.
- In THIS DEVICE mode the spectrum is always SIM: the phone has no access to MPD's audio, and most stations block browsers from analysing their streams.
- Plays in THIS DEVICE mode aren't added to Recently played (that log is the radio's).

## Next steps
- See TODO.md.
