# v0.27: Ticker above the board, About pop-up, nearby and listening

**Date:** 2026-11-02
**Project:** Per Annum Sound

## What changed
- **Recently played ticker** moved above the station columns. Entries behave like station rows: hovering pauses the ticker, lights the entry (box, thicker brighter text) and lights that station's row in the board; clicking plays it.
- **Level panel** now fills just the space under the art. The level canvas had been pushing the whole top row taller (702 px instead of ~470); the art column and signal panel now take the height the right-hand controls set, so the panel sits at about 150 px.
- **Nearby & similar** and **Your listening here** fill the signal panel for stations with no schedule or track info: quick-tune buttons for stations in the same city (other groups) and neighbours in the same group, plus total time, sessions and last visit on that station (kept on the device, saved every 30 s).
- **About pop-up**: click the station name or description for the full profile: history, notable shows or hosts, group, city, founding year, local time, distance, your listening there, the show on now (NTS), and the station's website. Esc, the backdrop or CLOSE dismisses it.
- **Profiles** for 33 stations added to stations.yaml (`profile`, `founded`, `notable`, `site`), researched by a subagent from Wikipedia, station sites and press; every website address checked to load (three replaced with working ones). Hanoi, Bangkok, Chillhop and FIP Jazz have none yet and fall back to their short description. Corrected earlier descriptions: Cashmere is now in Wedding; Chillhop no longer claims a label link that couldn't be confirmed; Folk Alley began at WKSU.

## Verified
- 1371 px: top row 469 px with NTS (timeline) and with a mixtape; level panel 152 px. About opens from the description and closes on Esc. Ticker sits above the columns; hovering an entry lit one station row and cleared on leave. Nearby for a London mixtape lists other London stations.

## Decisions made
- Profiles built on search summaries rather than fetched pages (refuge, noods, alhara, raheem, oroko, mutant, radio80000, stegi, yumi-co, drummer, super45, sleeping-pill) were trimmed to the less contested facts; worth a spot check.

## Next steps
- See TODO.md.
