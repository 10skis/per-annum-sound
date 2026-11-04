# v0.65: Sigil grid glows

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- The dot grid behind the sigil's rings glows. Each dot is about twice as bright as before, toward the centre, and sits on a soft round halo, so the background reads as an unlit LED panel that's still faintly lit. It still fades toward the corners, and it still swells with the ripple.
- The server's sigil (`art.placeholder`, used in Pi mode and on the lock screen) matches.

## Verified
- Before and after renders of the page's sigil (WYEP, PIT) and the server's: the grid is clearly visible and glowing, and stays behind the rings. About 1.2 ms per sigil frame at 512 px.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
