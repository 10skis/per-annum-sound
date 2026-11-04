# Per Annum Sound: restart brief

Paste the block below into a new Claude Code chat (working directory `~/Documents/claude-workspace`) to pick up where we left off.

```
Picking up Per Annum Sound, my internet-radio web app, in projects/pi-radio. Read projects/pi-radio/HANDOFF.md first (rules, traps, open items), then the top of projects/pi-radio/VERSION_CONTROL.md for recent versions. Don't read every update file.

Where it stands: v0.81 is built (app/web) and pushed to GitHub. The live site https://perannum.netlify.app is still on v0.47; I re-drag app/web to Netlify myself, so don't deploy. 79 stations; map ranges USA / EUROPE / TERRA / GALAXY; display modes Lunar / Eclipse (tint slider) / Solar with one brightness setting, in a panel under the header's mode key.

How I want to work: one small change at a time, built, checked in the browser at desktop and phone width, logged and pushed. If I ask a question, answer it and stop. If you're unsure what I mean, ask before building, and when I compare to something existing ("like Terra"), match it exactly. Keep replies short.

First task: [write it here]
```

## Where things are

| Field | Value |
|---|---|
| Version | v0.81 (2026-11-04) |
| Live site | https://perannum.netlify.app, on v0.47 until the next re-drag |
| Rules and traps | `HANDOFF.md` |
| History | `VERSION_CONTROL.md`, `updates/` |
| Open to-dos | `projects/TODO.md`, lines starting "Per Annum Sound:" |
| Local preview | `cd app && .venv/bin/python build_static.py`, then `python3 -m http.server 8091 --directory web` |

## Last run (v0.68 to v0.81, 2026-11-04)

| Version | Change |
|---|---|
| v0.68 | 13 worldwide stations (79 in all); each group sorted by place |
| v0.69 | Map switch order; two-way switches chamfered |
| v0.70 | Map ranges USA, EUROPE, TERRA, GALAXY; galaxy view built in |
| v0.71 | Borders, state lines, rivers and lakes on USA and EUROPE (desktop only since v0.73) |
| v0.72 | NGT is Solarized dark; DSK panel corners fixed |
| v0.73 | Galaxy zooms and pans; no geography on phone maps |
| v0.74 | Signal panel drops the Day & night and listening headings |
| v0.75 to v0.77 | Dial: full-circle ring, caret drawn without pixel rounding, tree centred |
| v0.77 to v0.78 | Panel name tabs removed; padding evened out |
| v0.79 | Lunar, Eclipse and Solar modes, Eclipse tint slider, brightness, display panel |
| v0.80 | Display panel opens without flickering |
| v0.81 | Fluid fits its panel |

## Worth doing next (Robert's call)

- Re-drag `app/web` to Netlify, then check on the iPhone (haptics, notch, Spectrum/Level swipe).
- Nine more dial glyphs so every station has its own.
- Open questions in `HANDOFF.md`: Oroko Radio's hiatus, the Chillhop name.
