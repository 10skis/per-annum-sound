# v0.11: Show progress fix, descriptions, new stations

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- Show progress bar fixed. It never actually hid: a CSS display rule overrode the `hidden` attribute, so non-NTS stations kept the last NTS show's times. Added a global `[hidden]` rule.
- NTS keeps listing a show as "now" for a while after it ends. Both versions now skip shows that have ended and pick the one covering the current time, so the bar, title and art switch on the hour.
- The bar redraws every 10 seconds on its own instead of only when new data arrives.
- Every Elsewhere station now has a short description (`about` in stations.yaml), shown in the detail panel. NTS shows and mixtapes already had theirs from NTS.
- Three stations added (33 total): Kool FM (jungle and drum & bass, London), WQXR (classical, New York) and Chillhop Radio (lo-fi hip-hop, via FluxFM Berlin). All three are HTTPS and verified playing on device.

## Why
- Robert flagged the progress bar as not doing anything, asked for descriptions where missing, and asked for classical, lo-fi hip-hop and jungle/DnB stations.

## Decisions made
- Kool FM over Bassdrive and others: it's the original London jungle station and HTTPS on Rinse's infrastructure. Bassdrive only offers plain HTTP, which an HTTPS page can't play.
- WQXR for classical as the local New York station.
- Chillhop via FluxFM over anonymous lo-fi relays, since it's curated by the Chillhop label.

## Next steps
- See TODO.md.
