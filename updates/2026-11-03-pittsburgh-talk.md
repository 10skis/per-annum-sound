# v0.39: Pittsburgh stations and a Talk Radio group

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Five Pittsburgh stations, a new city on the map (PIT):
  - Terrascan FM: WYEP 91.3 (indie and roots, after KEXP), WZUM (the Pittsburgh Jazz Channel, after FIP Jazz), WQED-FM 89.3 (classical, after WQXR).
  - Deep Cuts: WRCT 88.3 (Carnegie Mellon's freeform station, after Give the Drummer Radio).
  - New Talk Radio group at the end: WESA 90.5 (Pittsburgh's NPR news station) and BBC World Service.
- BBC Radio 4 can't be streamed outside the UK any more (its stream address redirects to the BBC homepage), so World Service is the BBC's English talk option. RTÉ Radio 1 also plays from the US if a second European one is wanted.
- Each has a genre, description, profile, founding year and site, checked against Wikipedia, station history pages and CMU, WQED and WYEP pages. None publishes track info to browsers.
- 59 stations now. The dial had 54 glyphs and wrapped, so stations 55 on would have repeated NTS 1's glyph; six more symbols added.
- WYEP's own stream address (wyep.org/stream) is an HLS playlist without `.m3u8` in the name, so the page tried to play it as plain audio and failed. It now uses WYEP's direct MP3 stream on the same CDN as WESA.

## Verified
- All six played in the browser (audio advancing, no error). Board shows the Talk Radio group under Deep Cuts; Pittsburgh marker lists all five local stations; 59 unique dial glyphs.

## Next steps
- Re-drag `app/web` to Netlify (covers v0.35 to v0.39).
