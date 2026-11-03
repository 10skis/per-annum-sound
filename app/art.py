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
        r = httpx.get(url, timeout=8, follow_redirects=True, headers={"User-Agent": "pi-radio/0.1"})
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


def halftone(gray: Image.Image, size: int = 512) -> Image.Image:
    crisp = size <= N
    ss = 1 if crisp else 2                  # draw at 2x and scale down for smooth dot edges
    canvas = size * ss
    out = Image.new("L", (canvas, canvas), 0)
    d = ImageDraw.Draw(out)
    px = gray.load()
    pitch, k = N / CELLS, canvas / N
    a = math.radians(ANGLE)
    ca, sa = math.cos(a), math.sin(a)
    span = math.ceil(CELLS * 0.75) + 1
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


def placeholder(name: str, size: int = 512) -> bytes:
    """Art for stations with none: ripples from two or three points meeting, seeded by the name,
    as a dim halftone, with the name in dot-matrix letters on a dark band. Mirrors the page's
    placeholderArt()."""
    rng = np.random.default_rng(zlib.crc32(name.encode()))
    yy, xx = np.mgrid[0:N, 0:N]
    srcs = [(rng.random() * N, rng.random() * N, 4 + rng.random() * 7) for _ in range(2 + int(rng.random() * 2))]
    v = sum(np.sin(np.hypot(xx - sx, yy - sy) / wl) for sx, sy, wl in srcs) / len(srcs)
    gray = Image.fromarray(((.5 + .5 * v) ** 1.6 * 150).astype("uint8"), "L")
    mask = halftone(gray, size)
    k = size / N
    d = ImageDraw.Draw(mask)
    words = name.upper().split()
    lines = words if len(words) <= 3 else [" ".join(words[:2]), " ".join(words[2:])]
    lh, top = 20, N / 2 - len(lines) * 20 / 2
    d.rectangle([0, (top - 6) * k, size, (top + len(lines) * lh + 6) * k], fill=0)
    for x in range(2, N, 3):
        for yb in (top - 6, top + len(lines) * lh + 5):
            d.rectangle([x * k, yb * k, (x + .9) * k, (yb + .9) * k], fill=150)
    # Type the name at 128px, then draw each lit pixel as a dot
    t = Image.new("L", (N, N), 0)
    td = ImageDraw.Draw(t)
    font = ImageFont.load_default(size=18)
    for i, line in enumerate(lines):
        w = td.textlength(line, font=font)
        td.text(((N - w) / 2, top + lh * i + 1), line, fill=255, font=font)
    px = t.load()
    r = k * .46
    for y in range(N):
        for x in range(N):
            if px[x, y] > 110:
                cx, cy = (x + .5) * k, (y + .5) * k
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    return _to_png(mask)
