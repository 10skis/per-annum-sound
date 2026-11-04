# v0.68: Worldwide stations, sorted by place

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- 13 stations added, 79 in all, each from a city not on the map before:

| Group | Station | Place |
|---|---|---|
| Terrascan FM | Triple R | Melbourne |
| Terrascan FM | Operator Radio | Rotterdam |
| Terrascan FM | LYL Radio | Lyon |
| Terrascan FM | Radio Skovoroda | Kyiv |
| Genre Radio | Rádio Batuta | Rio de Janeiro |
| Genre Radio | Radio Nacional Folklórica | Buenos Aires |
| Genre Radio | Irie FM | Ocho Rios |
| Deep Cuts | Rádio Quântica | Lisbon |
| Deep Cuts | Bush Radio | Cape Town |
| Deep Cuts | CKUT | Montreal |
| Deep Cuts | Ibero 90.9 | Mexico City |
| Deep Cuts | Radio Kampus | Warsaw |
| Talk Radio | NHK World Radio Japan | Tokyo |

- Each new place has coordinates, a city code and a time zone. Kyiv is KYV rather than the airport's KBP, for the same reason London is LDN.
- `catalog.py` now sorts each group by place A to Z, then by name, with Online stations last. Server and static build both use it, so the list, dial numbers and next/previous all follow the new order. Presets are saved by station id, so they're unaffected. The NTS mixtapes, all London, are now alphabetical.
- Profiles and founding years are only filled in where they could be stated with confidence; the rest have an `about` line only.

## Verified
- `dev/check_streams.py`: all 13 new streams answer (The Lot timed out, off air as usual).
- In the browser: all 13 play, 1.2 to 7.5 s to sound; NHK's HLS stream works. `selfTest.core()` clean across 79 stations, and every group lists in place order.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
- Galaxy map view: mocked up in `mockups/galaxy-map.html` (serve it beside a build, like the Level mockup). NTS in the core, one arm per group, stations along each arm by longitude, slow spin, the playing star pulses. Waiting on Robert's call.
