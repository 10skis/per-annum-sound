# v0.26: Header readouts, level strip, up next

**Date:** 2026-11-02
**Project:** Per Annum Sound

## What changed
- **Header readouts** (desktop) between PER ANNUM SOUND and the clock: city, position, local time at the station (ticks each minute), distance from New York, and stream format while playing. When they don't fit on one line they scroll like the station title but slower (about 28 px a second, roughly half the title's speed); a minute ticking over doesn't restart the scroll. Hidden on phones. Time zones added for every place (`timezones:` in stations.yaml, loaded by catalog.py); the three Pacific stations have none, so no local time.
- **05 LEVEL strip** under the artwork (desktop): left and right level over the last ~30 s as two dotted traces on a dB scale; NO CARRIER when stopped.
- **Up next** under the description: NTS 1 and 2 show their next shows on a small timeline with a needle at the current time, minutes left, and +CAL on each; stations that publish what's playing show the tracks recently heard there (kept on the device). Hidden for stations with neither; what to show for those is an open question to Robert.

## Verified
- 1440 px: readouts show for London with local time; NTS 1 timeline renders with NOW and minutes left; KEXP shows its recent track list; a mixtape hides the block; the level strip sits under the art (301 × 152). 1000 px: readouts scroll at 17.5 s per loop against the title's 10.9 s, header doesn't overflow.

## Next steps
- See TODO.md.
