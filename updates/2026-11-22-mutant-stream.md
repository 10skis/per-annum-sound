# v0.102: Mutant Radio stream fix

**Date:** 2026-11-22
**Project:** Per Annum Sound

## What changed
- Mutant Radio's RadioKing stream (`listen.radioking.com/radio/282820/stream/328621`) now returns 404, which Safari showed as a sign-in prompt on PAS. The station has moved to its own HLS stream, the one its site's player uses: `stream.mutantradio.net/memfs/052585f9-….m3u8`. Updated in `stations.yaml` and rebuilt `app/web`.

## Why
- Robert hit the sign-in dialog tuning to Mutant on PAS.

## Verified
- The new stream played in the browser pane from the perannum.netlify.app origin through hls.js: about 12 s of playback in 6 s of waiting, no errors. Not yet checked on the iPhone, where Safari plays HLS natively.
- The stream is a 720p video feed (about 1.2 Mbps), heavier than an audio stream on mobile data. The `memfs` UUID may change if they rebuild their streaming setup.

## Next steps
- Re-drag `app/web` to Netlify. See TODO.md.
