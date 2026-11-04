# v0.82: Station search

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- A search field at the end of the Recently played row, chamfered like the keys, in the dot font. On phones it takes its own full-width row under the ticker.
- Typing filters the board. Every word must match a station's name, city, place, airport code, genre or group; "NTS" matches every NTS channel, mixtapes included; what's on now (the row's subtitle) counts too. Accents are ignored.
- Groups with a match open for the search and show their match count; their saved open or closed state is untouched. Groups with none hide, the NTS schedule steps aside, and the board's count reads matches/79. No match shows NO STATIONS MATCH.
- / focuses the field, Enter plays the first match, Esc or × clears it. Listed in the ? panel.

## Why
- Robert asked for search by title, location or genre now that there are 79 stations.

## Decisions made
- Placement, keys and behaviour as proposed and approved ("Yes, in order").

## Verified
- Searches: berlin 3, jazz 5, nts 18, LDN 26, mexico 1, "experimental berlin" 2, zzzz 0 with the empty note. / focuses, Esc clears and ends the search.
- 1440 x 900: field at the end of the ticker, matching groups open across the columns. 375 px: full-width field, no page overflow. `selfTest.core()` and `selfTest.layout()` clean.

## Next steps
- Lunar and Solar tint strips (v0.83). Re-drag `app/web` to Netlify. See TODO.md.
