# v0.48: Random button, fixed info pane

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- RND key beside PLAY/STOP, on phones and desktop: plays any station but the current one. R does the same on the keyboard (added to the keys panel).
- The middle info pane no longer scrolls. The description is one line; when it's too long it scrolls like the station title, at 0.6 s per character against the title's 0.35. Clicking it still opens About.
- Sections under the description (coming up, day and night, nearby and similar, your listening) drop off from the bottom, whole, when they don't fit, rather than being cut mid-line.
- Fixed a race in the scrolling lines: a frame queued for an earlier text could overwrite the new one, leaving the line blank. It hit the description first but could also blank a title.

## Verified
- Five random presses gave five plays, never repeating the current station. NTS 1's 267-character description scrolls at 160 s per loop and opens About on click. NTS 1, Christmas Vinyl, KEXP and WYEP all fit the pane at 1440 x 900 (NTS 1 drops two sections).

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
