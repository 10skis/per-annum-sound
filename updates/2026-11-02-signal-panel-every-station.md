# v0.32: A full signal panel for every station

**Date:** 2026-11-02
**Project:** Per Annum Sound

## What changed
- The space under the description is never thin now. Every station gets the same stack: what's on where known (NTS timeline, or the last three tracks heard), **Day & night** where the station is, **Nearby & similar**, and **Your listening here**.
- **Day & night**: a 24-hour strip in the station's local time with daylight lit, a marker at the hour it is there now, and "DAYTIME IN HANOI · SUNSET IN 6H 13M" or "NIGHT IN LONDON · SUNRISE IN 2H 50M". Sun times from the standard solar-position approximation (as in suncalc); polar day or night is named (the North Pole shows POLAR NIGHT); places without a time zone go by longitude.
- **Nearby** now falls back to the closest stations elsewhere, one per city with the distance (Hanoi: Bangkok Community Radio 988 km), when fewer than three share the station's city. NTS 1 and 2 skip nearby, since their timeline takes the room.
- **Art shimmer** back to every 5 to 14 seconds (the 3 to 8 from v0.29 felt too busy); the stronger ring look stays.

## Verified
- Hanoi, Bangkok, NTS 1, Memory Lane, Christmas Vinyl HD and Nightride each show the right sections; top row stays 469 px.

## Next steps
- See TODO.md.

## Follow-up (same version)
- The shimmer itself is slower, not just less frequent: the ripple now takes 4.6 s to cross the art (was 2.4 s) and the sweep 3.6 s (was 1.9 s).
- Shimmer restored exactly to its v0.25 form, on Robert's call: a single ripple ring over 1.8 s, a narrow 1.5 s sweep, every 5 to 14 s. (The stronger echo ring and the slowed 4.6 s version are gone.)
- Volume swipe reversed: swiping right turns it up, toward the full end of the bar.
