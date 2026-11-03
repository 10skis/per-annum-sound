# v0.35: Station profiles, shared city codes, Wikimedia art

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Profiles for the four stations that had none: Ha Noi Community Radio, Bangkok Community Radio, Chillhop Radio (FluxFM's channel) and FIP Jazz. Every radio station now has one; NTS mixtapes still don't.
- Spot-checked the twelve profiles written from search summaries against station sites and press, and corrected most of them. Main fixes: Noods only joined DAB+ in August 2026 (it was on DAB from 2019); Refuge co-founded with Richard Akingbehin; full founder lists for alHara, Oroko, Mutant; Radio Raheem left the Triennale for Combo Milano in 2026; Oroko announced an indefinite hiatus in April 2026 (stream still answers, so it stays on the dial); the Bangkok "sounds of Siam" line was unsourced and is replaced. Super45's "since 1996" rests on one directory listing, so `founded` stays blank.
- City codes (LON, NYC, MPC...) moved from the page into `stations.yaml` under `codes:`. `catalog.py` gives every station a `code`, the server sends it and uses it for the sigil, and the page reads it for the map and sigil. Before this the server's sigil used the first three letters (MID for Mid-Pacific).
- Wikimedia started refusing the generic `pi-radio/0.1` user agent with a 429, so the build silently dropped the FIP and FIP Jazz logos. `art.py` now sends a descriptive user agent. The build you deployed earlier today is likely missing both logos.

## Verified
- Server: `/api/stations` codes match the yaml for all 24 cities; server sigil for Ambient Sleeping Pill reads MPC.
- Page (static build): map cities and sigils use the yaml codes; About pop-up shows the new Bangkok profile.
- Build pre-renders fip.png and fip-jazz.png again.

## Next steps
- Re-drag `app/web` to Netlify (FIP logos and profiles).
- Decide whether to keep Oroko while it's on hiatus.
- See TODO.md.
