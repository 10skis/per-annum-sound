# v0.46: New site address

**Date:** 2026-11-03
**Project:** Per Annum Sound

## What changed
- Robert renamed the Netlify site to https://perannum.netlify.app and deployed v0.45 (checked: icons and stations.json match the build; index.html differs only by Netlify's injected comment).
- The old address is replaced in HANDOFF, VERSION_CONTROL, SCOPE, the app README and `art.py`'s user agent. The user agent no longer carries a version number, so it won't go stale.
- The re-drag to-do is moved to Done.
- Chrome's "Open in app" kept the old icon because the installed app holds its own copy; removing it at chrome://apps and reinstalling fixes it (noted in HANDOFF).

## Verified
- No other non-history file mentions spiffy-elf. Build still pre-renders all six logos with the new user agent.

## Next steps
- See TODO.md.
