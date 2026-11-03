# v0.17: Board, motion, 19 new stations

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- **Art shimmer.** Every 5 to 14 seconds while playing, a ripple from a random point or a diagonal sweep runs across the art. The art itself is the mask, so only its dots light up.
- **Station rows.** Hover and the playing row get a chamfered highlight box, and the text thickens and brightens over 0.14 s; moving off runs it backwards. Numbers have the unlit 88 behind them.
- **Station board.** Groups collapse and expand (open state remembered per device): NTS Live with the NTS schedule and Infinite Mixtapes in column one, Worldwide FM (renamed from Elsewhere) in two, Genre Radio and Deep Cuts in three. Recently played is now a slow ticker along the bottom with its timestamps; hover pauses it, tapping an entry plays that station.
- **Stations.** 19 added, all streams checked over HTTPS and 5 played in the browser. Genre Radio (7): Chante France 60s, Radio Italia Anni 60, Reprezent Radio, triple j Unearthed, Yumi Co. Radio (city pop), Folk Alley, Christmas Vinyl HD. Deep Cuts (12): Resonance FM, Oroko Radio, Ha Noi Community Radio, Bangkok Community Radio, Mutant Radio, Super45.fm, stegi.radio, Radio 80000, Give the Drummer Radio, Radio Raheem, Ambient Sleeping Pill, Nightride FM. 52 stations total. Seven of them publish now-playing info, wired up. A `genre` field shows with the city in the list.
- **Map.** The world view drifts east (content moving right) at 1.5° a second and stops while the pointer is over it. 20 cities now, each with an airport-style code.
- **Visualizers.** Click either screen (or its label) to step through Spectrum, Waterfall, Scope, VU, Polar and Mirror; choices are remembered. Stopped, both rest on a flat line with NO CARRIER.
- **Play/stop.** One button: a click anywhere toggles; both labels stay, the active one lit.
- **Station name** now leads the signal panel on desktop at 38 to 48 px, with the description under it.
- **Phones.** ? moved into the header. The header clock is hidden on phones (the status bar already shows the time) to make room.
- **Warnings** (NO SIGNAL, offline, mock player, the sleep timer's last minute) are blue (#4fb4ff). Everything else stays amber.
- Mockup of "dial as the centerpiece" in `mockups/dial-centerpiece.html`, for Robert to judge; not built.

## Decisions made
- Stations whose city couldn't be confirmed (Yumi Co., Christmas Vinyl HD, Ambient Sleeping Pill, Nightride FM) are in the list but off the map rather than placed on a guess.
- Robert's highlight box kept for the playing row instead of the inverse fill I'd proposed, so the two designs don't fight.
- The group name "Worldwide FM" is also the name of Gilles Peterson's station; flagged to Robert.
- Spare verified streams kept in the agent report for later: Worldwide FM, LYL Radio, Radio Quântica, Le Mellotron, Radio Meuh, Datafruits, BAGeL Radio.

## Next steps
- See TODO.md.
