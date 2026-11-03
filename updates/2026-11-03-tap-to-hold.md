# v0.37: Tap to hold the art and title motion

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Tap or click the art to hold its motion: no shimmer on artwork, and the sigil's rings stop turning. Tap again to resume. A swipe on the art still tunes; only a tap (under 10 px of movement) toggles.
- Tap or click the station title to stop it scrolling. It rests at its start with the end faded out on the right. Tap again to resume.
- Both are remembered on the device (`piRadioArtHeld`, `piRadioTitleHeld`).
- The title used to open the About pop-up. Now the line under it (city or show) and the description open About.
- Help panel lists the new tap.

## Verified
- Title: marquee to none to marquee on two clicks, About stays shut; the line under it still opens About.
- Art: tap holds (sigil ring rotation unchanged over 0.8 s while playing), second tap resumes (rotation moves again).
- Phone-width layout: held title shows its start with a right-edge fade.

## Next steps
- Re-drag `app/web` to Netlify (covers v0.35 to v0.37).
