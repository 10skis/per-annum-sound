"""Turns cover art into the amber images the screens show.

Show and mixtape art becomes a halftone: one dot per cell on a 45° grid, dot area tracking
brightness. Station logos are flat graphics with lettering, which a dot grid breaks up, so they
get a clean 1-bit threshold instead. The web page renders the same halftone in the browser for
the no-server version, so both match.

size=512 is for the web app (anti-aliased dots). size=128 is for the device's 1-bit OLED.
"""

import io
import logging
import math
import zlib
from collections import OrderedDict
from typing import Optional

import httpx
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

# Wikimedia refuses generic user agents with a 429; it wants a name and a way to reach the owner.
UA = "PerAnnumSound (personal radio app; https://10skis.github.io/per-annum-sound)"
log = logging.getLogger("pi-radio")

N = 128                  # working resolution, the art screen's pixel size
CELLS, ANGLE, GAMMA = 32, 45, 1.2
AMBER = (255, 176, 46)
_cache: "OrderedDict[tuple, bytes]" = OrderedDict()


def _to_png(mask: Image.Image) -> bytes:
    """Mask brightness becomes amber opacity, so the page supplies the screen colour."""
    out = Image.new("RGBA", mask.size, AMBER + (0,))
    out.putalpha(mask.convert("L"))
    buf = io.BytesIO()
    out.save(buf, "PNG")
    return buf.getvalue()


def _gray(url: str) -> Optional[Image.Image]:
    try:
        r = httpx.get(url, timeout=8, follow_redirects=True, headers={"User-Agent": UA})
        r.raise_for_status()
        img = Image.open(io.BytesIO(r.content))
        if img.mode in ("RGBA", "LA", "P"):
            # Logos with transparent backgrounds: put them on white, or dark logos vanish.
            img = img.convert("RGBA")
            backed = Image.new("RGBA", img.size, (255, 255, 255, 255))
            backed.alpha_composite(img)
            img = backed
        img = img.convert("L")
    except Exception as e:
        log.warning("Art fetch failed (%s): %s", url, e)
        return None
    img = ImageOps.fit(img, (N, N), Image.LANCZOS)
    return ImageOps.autocontrast(img, cutoff=1)


def halftone(gray: Image.Image, size: int = 512, cells: int = CELLS) -> Image.Image:
    crisp = size <= N
    ss = 1 if crisp else 2                  # draw at 2x and scale down for smooth dot edges
    canvas = size * ss
    out = Image.new("L", (canvas, canvas), 0)
    d = ImageDraw.Draw(out)
    px = gray.load()
    pitch, k = N / cells, canvas / N
    a = math.radians(ANGLE)
    ca, sa = math.cos(a), math.sin(a)
    span = math.ceil(cells * 0.75) + 1
    w = round(pitch)
    for j in range(-span, span):
        for i in range(-span, span):
            u, v = (i + .5) * pitch, (j + .5) * pitch
            x, y = N / 2 + u * ca - v * sa, N / 2 + u * sa + v * ca
            if not (-pitch <= x <= N + pitch and -pitch <= y <= N + pitch):
                continue
            x0, y0 = round(x - pitch / 2), round(y - pitch / 2)
            total = sum(px[min(N - 1, max(0, xx)), min(N - 1, max(0, yy))]
                        for yy in range(y0, y0 + w) for xx in range(x0, x0 + w))
            r = pitch / 2 * math.sqrt((total / (w * w) / 255) ** GAMMA) * 0.98 * k
            if r < (0.6 if crisp else 0.4 * ss):
                continue
            d.ellipse([x * k - r, y * k - r, x * k + r, y * k + r], fill=255)
    if ss > 1:
        out = out.resize((size, size), Image.LANCZOS)
    return out


def _logo(gray: Image.Image, size: int) -> Image.Image:
    mask = gray.point(lambda v: 255 if v >= 128 else 0)
    return mask.resize((size, size), Image.NEAREST)


def dither(url: str, style: str = "halftone", size: int = 512) -> Optional[bytes]:
    """style: "halftone" for show and mixtape art, "logo" for station logos."""
    key = (url, style, size)
    if key in _cache:
        _cache.move_to_end(key)
        return _cache[key]
    gray = _gray(url)
    if gray is None:
        return None
    png = _to_png(halftone(gray, size) if style == "halftone" else _logo(gray, size))
    _cache[key] = png
    if len(_cache) > 64:
        _cache.popitem(last=False)
    return png


def placeholder(name: str, size: int = 512, city: str = "", code: str = "") -> bytes:
    """Art for stations with none: a sigil. Rings of dotted grooves like a record, each ring's arcs
    switched on or off by the station's name; the city code and city name in the middle.
    Mirrors the page's placeholderArt() (same layout, its own random sequence)."""
    rng = np.random.default_rng(zlib.crc32(name.encode()))
    ss = 2                                   # draw at 2x and scale down for smooth dots
    W = size * ss
    S = W / 440
    out = Image.new("L", (W, W), 0)
    d = ImageDraw.Draw(out)
    cx = cy = W / 2
    # A dot matrix behind the rings, glowing faintly, fading toward the corners: a soft halo under
    # each dot, then the dot (the page's sigil draws the same)
    pitch = 11 * S
    y = pitch / 2
    while y < W:
        x = pitch / 2
        while x < W:
            f = 1 - min(1, math.hypot(x - cx, y - cy) / (W * .72))
            a = .09 + f * .17
            h = 1.2 * S * 2.6
            d.ellipse([x - h, y - h, x + h, y + h], fill=int(255 * a * .14))
            d.rectangle([x - 1.2 * S, y - 1.2 * S, x + 1.2 * S, y + 1.2 * S], fill=int(190 * a))
            x += pitch
        y += pitch
    for ring in range(11):
        rad = (60 + ring * 15) * S
        segs = 6 + int(rng.random() * 8)
        dots = int(rad * math.pi * 2 / (9 * S))
        pattern = [rng.random() > .38 for _ in range(segs)]
        rot = rng.random() * math.pi * 2
        for k in range(dots):
            a = rot + k / dots * math.pi * 2
            on = pattern[int(k / dots * segs)]
            r = (3 if on else 2) * S
            x, y = cx + math.cos(a) * rad, cy + math.sin(a) * rad
            d.ellipse([x - r, y - r, x + r, y + r], fill=255 if on else 60)
    if code:
        font = ImageFont.load_default(size=round(46 * S))
        d.text((cx - d.textlength(code, font=font) / 2, cy - 34 * S), code, fill=255, font=font)
    if city:
        font = ImageFont.load_default(size=round(15 * S))
        t = city.upper()
        d.text((cx - d.textlength(t, font=font) / 2, cy + 20 * S), t, fill=150, font=font)
    return _to_png(out.resize((size, size), Image.LANCZOS))
