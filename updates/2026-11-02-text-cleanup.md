# v0.8: Text cleanup

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- Show descriptions are no longer cut at three lines. They show up to six and scroll inside the panel past that.
- The desktop scrolling title is smaller (30 to 36px, was 36 to 56px) and the subtitle with it.
- Scrolling text fades out at both edges instead of being chopped mid-letter, and the repeat has a wider gap with a dot so the loop point is clear.
- When a show's end time has passed but NTS hasn't moved on yet, the panel says ENDING instead of 0 MIN LEFT.
- Checked at 1580px and 375px: no overflow. Rebuilt `web/`; needs re-dragging onto Netlify to go live.

## Why
- Robert flagged cut-off text and an oversized scrolling title on the desktop dashboard.

## Decisions made
- Artwork filter treatment is under discussion; not changed in this version.

## Next steps
- See TODO.md.
