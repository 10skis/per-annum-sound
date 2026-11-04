# v0.67: Phosphor fits its panel

**Date:** 2026-11-04
**Project:** Per Annum Sound

## What changed
- In a big window the Level panel gets short and wide. Phosphor then drew a figure about 40 px tall with a glow sized for a bigger one, so it blurred into a tall blob, and the side scopes disappeared because the room check was too strict.
- The diamond now sizes to the height above the correlation bar. The glow and line weight scale with the figure, and the bright beads only show when there's room for them.
- The figure is more balanced: the sideways swing is opened up and the up-and-down one eased, and it shows 25 ms of signal instead of 50, so it reads as a figure rather than a tall streak or a solid block.
- The LO and HI scopes show whenever they'd be at least 8 px across (was 14), and their labels stay clear of the correlation bar.

## Verified
- Before and after frames at 283×141 (phone), 301×110 (desktop) and 520×58 (short full-screen panel). At the short size the side scopes are back and the main figure is drawn to its own scale.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
