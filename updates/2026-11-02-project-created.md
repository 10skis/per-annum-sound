# v0.1: Project created

**Date:** 2026-11-02
**Project:** Pi Radio

## What changed
- Compared the Atonemo NTS Radio Player ($179) to a DIY build and wrote both scopes, physical device and web app, into [SCOPE.md](../SCOPE.md).

## Why
- Robert wants a dedicated, phone-free radio on his speakers with stations beyond NTS. The Atonemo locks its controls to NTS.

## Decisions made
- Pi Zero 2 WH with moOde Audio. AirPlay is the only streaming protocol needed.
- One shared control service and `stations.yaml` behind both the physical controls and the web app.
- Analog out through a DAC board to the Edifier R1280DB. USB-C for the phone dropped.
- Two amber/yellow displays: a 1.5" 128×128 art screen (color OLED drawing in amber) and a 3.12" 256×64 yellow OLED text strip. Dithered art over photorealism.
- Cherry MX keys for NTS 1/2, rotary dial for the station list, toggle switch with a Mausberry board for safe power.
- 3D-printed enclosure on a library printer, modeled in OpenSCAD.
- Web app served from the Pi, home Wi-Fi only, with software volume.
- Design language: retro-analog.

## Next steps
- See TODO.md.
