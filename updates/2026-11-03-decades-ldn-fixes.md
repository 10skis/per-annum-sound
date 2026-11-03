# v0.47: Chante France decades, LDN, tree glyph, no play note

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Chante France 70s and 80s added to Genre Radio, after the 60s channel. They are the only other decade streams on Chante France's host (50s, 90s and 2000s return 404). 66 stations.
- London's city code is LDN instead of LON, on the map and the sigils. The `codes:` entry carries a comment saying why.
- The Christmas tree glyph is centred in its dial slot. It sat on the text baseline, which pushed it above the ring when lit at 15 px; it is now positioned at the slot's centre like the text glyphs.
- The blue "TAP PLAY TO START AUDIO" note is gone. Scrolling quickly cut off each play request, which raised it. A play the browser blocks now just shows as stopped; an interrupted one is ignored. The "stream failed" note also ignores loads aborted by the next station.

## Verified
- Tree SVG centre measured equal to its slot centre. Switching through 8 stations 60 ms apart left no note and the last one playing. Both new streams play.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
