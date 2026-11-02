"""Builds the no-server version of the app into web/, ready to upload to a static host
(Netlify, Cloudflare Pages). Run after changing stations.yaml or the page:
    .venv/bin/python build_static.py
"""

import json
import shutil
from pathlib import Path

import yaml

import art

HERE = Path(__file__).parent
OUT = HERE / "web"

if OUT.exists():
    shutil.rmtree(OUT)
(OUT / "static").mkdir(parents=True)

stations = yaml.safe_load((HERE / "stations.yaml").read_text())

# Pre-dither station logos into the folder. Some logo hosts block browsers from reading
# their images, so the page can't dither those itself.
(OUT / "art").mkdir()
for group in stations["groups"]:
    for st in group["stations"]:
        if st.get("art"):
            png = art.dither(st["art"])
            if png:
                (OUT / "art" / f"{st['id']}.png").write_bytes(png)
                st["art"] = f"art/{st['id']}.png"

(OUT / "stations.json").write_text(json.dumps(stations, indent=1))

page = (HERE / "static" / "index.html").read_text()
assert "<!-- static-flag -->" in page
page = page.replace("<!-- static-flag -->", "<script>window.PI_RADIO_STATIC = true;</script>")
(OUT / "index.html").write_text(page)

for name in ("icon-180.png", "icon-512.png"):
    shutil.copy(HERE / "static" / name, OUT / "static" / name)
shutil.copy(HERE / "static" / "manifest.webmanifest", OUT / "manifest.webmanifest")

count = sum(len(g["stations"]) for g in stations["groups"])
print(f"Built {OUT} with {count} stations.")
