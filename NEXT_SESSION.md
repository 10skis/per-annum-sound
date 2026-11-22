# Per Annum Sound: restart brief

Paste the block below into a new Claude Code chat (working directory `~/Documents/per-annum-sound`) to pick up where we left off.

```
Picking up Per Annum Sound, my internet-radio web app, in ~/Documents/per-annum-sound. Read HANDOFF.md first (rules, traps, open items), then the top of VERSION_CONTROL.md for recent versions. Don't read every update file.

Where it stands: v0.103 is live at https://10skis.github.io/per-annum-sound/. Every push to main publishes it through GitHub Actions, so only push what's ready. 79 stations; map ranges USA / EUROPE / TERRA / GALAXY; display modes Lunar / Eclipse / Solar, each with its own tint strip, and one brightness setting and an amber-to-green colour setting, in a panel under the header's mode key.

How I want to work: one small change at a time, built, checked in the browser at desktop and phone width, logged and pushed. If I ask a question, answer it and stop. If you're unsure what I mean, ask before building, and when I compare to something existing ("like Terra"), match it exactly. Keep replies short.

First task: [write it here]
```

## Where things are

| Field | Value |
|---|---|
| Version | v0.101 (2026-11-06) |
| Live site | https://10skis.github.io/per-annum-sound/, deployed on every push to `main` |
| Rules and traps | `HANDOFF.md` |
| History | `VERSION_CONTROL.md`, `updates/` |
| Open to-dos | `TODO.md` |
| Local preview | `cd app && .venv/bin/python build_static.py`, then `python3 -m http.server 8091 --directory web` |

## Last run (v0.68 to v0.101, 2026-11-04 to 06)

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
| v0.82 | Station search |
| v0.83 | Lunar and Solar tint strips |
| v0.84 | Lunar black to grey; taller Level panel |
| v0.85 | Solid controls and board |
| v0.86 to v0.87 | Textured plate behind the controls, in the panels' glass and lined up with them |
| v0.88 | Code review fixes (ten) |
| v0.89 | Power-off dim; Level grid |
| v0.90 to v0.91 | Sparse dots in the now-playing panel; grid behind the spectrum |
| v0.92 | Galaxy matches Terra |
| v0.93, v0.96-0.101 | Power down/up: a flicker, then a smooth fall and warm-up; PLAY/STOP and the visualisers dim and warm up with the rest; PLAY breathes on standby |
| v0.94 | Dots on the station list |
| v0.95 | Amber-to-green colour setting |

## Worth doing next (Robert's call)

- Add the new address to the iPhone Home Screen, then check (haptics, notch, Spectrum/Level swipe).
- Nine more dial glyphs so every station has its own.
- Open questions in `HANDOFF.md`: Oroko Radio's hiatus, the Chillhop name.
