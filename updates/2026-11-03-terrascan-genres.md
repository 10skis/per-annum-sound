# v0.38: Genres for the Terrascan FM stations

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- The 16 Terrascan FM stations had no `genre`, so their board line showed only the city. Each now has one, taken from its description, so the line reads like Genre Radio and Deep Cuts ("Jungle and drum & bass · London", "Freeform · New Jersey"). Kiosk and alHara use "Community radio"; dublab uses its own "Future roots".

## Verified
- Server `/api/stations` and the static board both show genre and city; no row overflows at 1440 px.

## Next steps
- Re-drag `app/web` to Netlify (covers v0.35 to v0.38).
