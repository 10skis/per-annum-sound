"""Draws the home-screen icon: an amber dial on a dark plate. Run once after changing it."""
import math
from pathlib import Path
from PIL import Image, ImageDraw

HERE = Path(__file__).parent
for size in (180, 512):
    s = size * 4  # draw large, scale down for smooth edges
    img = Image.new("RGB", (s, s), (14, 12, 10))
    d = ImageDraw.Draw(img)
    c, r = s / 2, s * 0.30
    for i in range(24):
        a = math.tau * i / 24
        d.line([(c + math.cos(a) * r * 1.12, c + math.sin(a) * r * 1.12),
                (c + math.cos(a) * r * 1.24, c + math.sin(a) * r * 1.24)], fill=(90, 84, 76), width=s // 120)
    d.ellipse([c - r, c - r, c + r, c + r], fill=(200, 196, 188))
    d.ellipse([c - r * .78, c - r * .78, c + r * .78, c + r * .78], fill=(160, 155, 147))
    w = s * 0.035
    d.rounded_rectangle([c - w / 2, c - r * .95, c + w / 2, c - r * .45], radius=w / 2, fill=(255, 176, 46))
    img.resize((size, size), Image.LANCZOS).save(HERE / "static" / f"icon-{size}.png")
