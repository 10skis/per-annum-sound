# v0.54: Full check, tablet header fix

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What was checked
| Area | Result |
|---|---|
| stations.yaml | 66 stations, no duplicate ids, every stream HTTPS. Gaps are by design: NTS channels and mixtapes take genre and description live from NTS; three stations are placed "Online" |
| Streams, server side | 65 of 66 answer with audio. The Lot Radio's HLS now replies "session is not allowed to view this stream" even with their site as origin: it's locked to their own player |
| Streams, in the browser | All 65 others play. Kool FM, Drummer and WRCT take 5 to 6 s to start; the rest under 3.6 s |
| Displays | All 12 spectrum displays in both slots, all 8 level displays and both map ranges draw with no errors |
| Per station | About, Up Next, signal readouts and sigil for all 66 stations with no errors; About opens for every one |
| Controls | Arrows, random (button and R), space play/stop, preset save (shift) and recall, sleep timer cycle, map key, help open and Escape, art and title hold: all pass |
| Layout | 320, 375, 414, 458, 600, 768, 960, 1024, 1280, 1440 and 1920 px: no page overflow, middle pane never overflows |
| Pi server | Every endpoint answers (bad ids get 404). Radio mode plays through the mock player; the server's halftone art ripples its own dots; console clean |
| Live site | Serving v0.47 (66 stations, no random key) |

## What changed
- At 600 to 959 px (tablets, iPad portrait) the full header still spilled 70 px past its frame: below 960 the unit is at most 420 wide, so the short header now covers that whole range.

## Not verified
- Haptics and the notch spacing need a real iPhone.

## Next steps
- See TODO.md, and the suggestions in this session.
