# v0.4: Desktop dashboard and The Lot Radio

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- At 960px and wider the web app becomes a dashboard: a now-playing deck across the top (large art, large scrolling text, controls on the right) and the station board below, one column per group. The phone layout is unchanged. Tested at 1440, 1024 and phone width.
- Added The Lot Radio (30 stations now).

## Why
- Robert wanted the desktop site to use the width like a dashboard, and The Lot in the station list.

## Decisions made
- The Lot only streams video (HLS, 240p to 1080p). The station uses the lowest version (240p, about 0.4 Mbps), which works without a login token; MPD keeps only the audio. Not yet heard: needs MPD. If The Lot renumbers its versions, the URL in `stations.yaml` needs updating.

## Next steps
- See TODO.md.
