# v0.36: Show names instead of file names on Radiocult stations

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Radiocult stations (Bangkok, Ha Noi, Noods, Oroko) showed the name of the file being played, which on Bangkok is often a recorder's file name ("250119_0258"). Radiocult also sends the scheduled show's name; that now wins ("BCR INTERNATIONAL"). Between shows, when the station runs a default playlist, it shows artist and track ("Ytu - DJ Mix").
- A title with no spaces and a run of four digits or an underscore counts as a file name. It is never shown, never saved to the recent-tracks list, and old ones already saved on a device are hidden from "Recently on".

## Verified
- Live feeds: Bangkok "BCR INTERNATIONAL", Ha Noi "Ytu - DJ Mix", Noods "Jugotek Radio with Sammy Oravec", Oroko blank (on hiatus).
- Bangkok with the two file names from Robert's screenshot in its saved list: the panel shows only the show name.

## Next steps
- Re-drag `app/web` to Netlify (covers v0.35 and v0.36).
