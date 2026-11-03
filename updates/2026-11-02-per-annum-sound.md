# v0.18: Per Annum Sound

**Date:** 2026-11-02
**Project:** Per Annum Sound (formerly Pi Radio)

## What changed
- **Name.** The app is now Per Annum Sound: page title, header, home-screen name ("Per Annum"), lock-screen album, calendar events, server title. Phones show P·A·S in the header, since the full name doesn't fit beside the timers. The project folder, saved settings and the Netlify address are unchanged.
- **Map drift.** Reversed (content now moves left) and smoothed: the map is drawn at sub-pixel offsets instead of whole pixels, and a long gap between frames no longer jumps it. Land dots are brighter (#86601f, was #5c3e10), grid dots too.
- **Dial.** The ring is now glyphs, one per station (half-width katakana plus a few technical symbols): unlit dim amber, neighbours brighter, the current one lit with a glow. The desktop dial grew slightly (176 px) to fit 53 of them. Not made the centerpiece.
- **No-art stations.** Instead of plain text: a ripple interference pattern seeded by the station's name, drawn as a dim halftone, with the name in dot-matrix letters on a dark band between two dotted rules. Same design in the browser and in `art.py` for the server.
- **Map spots for stations without a city.** Christmas Vinyl HD at the North Pole (pinned to the top edge of the world view); Yumi Co. in the North Pacific, Ambient Sleeping Pill mid-Pacific, Nightride FM at Point Nemo. New `map:` field in stations.yaml for pins that differ from the place.
- **Groups.** "Worldwide FM" group renamed Terrascan FM, and Gilles Peterson's Worldwide FM added to it with now-playing info. 53 stations.

## Verified
- Desktop and 375 px phone: header fits at worst case, glyph ring renders, North Pole and Pacific pins in place, map drift direction and per-frame step, Worldwide FM plays with its track, Radio Raheem shows the new no-art design. Server version restarted.

## Decisions made
- Read "change the name to Terrascan FM" as the station group (the clash flagged last round), since the app was renamed to Per Annum Sound in the same message. Flagged to Robert.

## Next steps
- See TODO.md.
