# v0.7: No-server build

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- The page now runs in two ways from the same file. With the server it works as before. Built by `build_static.py` into `web/`, it needs no server: station list from `stations.json`, NTS feeds fetched by the browser (NTS allows this), art dithered in the browser, all playback on the device, Recently played stored on the device, and the RADIO output hidden.
- The build pre-dithers station logos into `web/art/`, because Kiosk, alHara and FIP block browsers from reading their logos.
- FIP's logo link was dead (404); replaced with the Wikimedia copy.
- `art.py` now puts transparent logos on white before dithering, so dark logos don't vanish. This applies to the server version too.
- Tested the built folder from a plain file server: NTS data, schedule, taglines, browser-dithered art, Refuge playing on the device and logging to Recently played, no page overflow. Server version re-checked afterwards.

## Why
- The Pi may be months away, and Robert wants his own place for all his stations on his phone away from home, without the work laptop running.

## Decisions made
- Netlify (drag-and-drop, free, personal account) over GitHub Pages, which would sit on the FlowX GitHub account. Robert creates the account and publishes.
- Tailscale moves to the Pi only; it stays off the work Mac.
- One page file for both versions, switched by a flag the build injects, so they can't drift apart.

## Next steps
- See TODO.md.
- Published 2026-11-02 at https://spiffy-elf-9ebf5d.netlify.app. Checked from the live host: 30 stations, NTS schedule, bundled art and KEXP playback all work.
