# v0.103: Own repo, GitHub Pages

**Date:** 2026-11-22
**Project:** Per Annum Sound

## What changed
- The project left the work workspace repo for its own public repo on Robert's personal account: https://github.com/10skis/per-annum-sound, checked out at `~/Documents/per-annum-sound`. History came along through `git subtree split` (128 commits); commit emails rewritten to the account's GitHub noreply address so the work email isn't public.
- Hosting moved from Netlify to GitHub Pages at https://10skis.github.io/per-annum-sound/. `.github/workflows/pages.yml` runs `build_static.py` and publishes `app/web` on every push to `main`. No more drag-and-drop and no Netlify credits.
- The site now lives under a path, so the icon and manifest links in `index.html` and `manifest.webmanifest` are relative. They still work from the server at `/`.
- `app/requirements.txt` added so the build and a fresh `.venv` install the same packages.
- To-dos moved from the workspace `TODO.md` into this repo's `TODO.md`; HANDOFF, NEXT_SESSION, README and SCOPE point here instead of the workspace and Netlify.

## Why
- Robert ran out of Netlify credits, and a personal project shouldn't sit in a work repo that's moving to the FlowX org.

## Verified
- Before publishing, scanned the project's full history for work names, the work email, credentials and local addresses. Only the commit author email needed changing; listening history and state files were never committed.
- Built locally and served under `/per-annum-sound/`: all 79 stations load, no missing files.
- Live: the Actions deploy passed in 31 s. On https://10skis.github.io/per-annum-sound/ every file loads, the service worker registers at the subpath, all 79 stations are there and Mutant Radio played. Not yet checked on the iPhone.
- Pushes from this checkout use the 10skis account through a repo-level credential helper (`gh auth token --user 10skis`); gh's active account stays the work one, so the workspace still pushes as rwitenski-flowx.

## Next steps
- Add the new address to the iPhone Home Screen, and delete the Netlify site. See `TODO.md`.
