"""Turns cover art into the 128x128 1-bit dithered image the device's art screen shows.
The web app shows the same image so both screens match."""

import io
import logging
from collections import OrderedDict
from typing import Optional

import httpx
from PIL import Image, ImageDraw, ImageFont, ImageOps

log = logging.getLogger("pi-radio")

SIZE = 128
AMBER = (255, 176, 46, 255)
_cache: "OrderedDict[str, bytes]" = OrderedDict()


def _to_png(img: Image.Image) -> bytes:
    """Lit pixels become amber, unlit pixels transparent, so the page supplies the screen colour."""
    mask = img.convert("1")
    out = Image.new("RGBA", mask.size, (0, 0, 0, 0))
    out.paste(Image.new("RGBA", mask.size, AMBER), mask=mask)
    buf = io.BytesIO()
    out.save(buf, "PNG")
    return buf.getvalue()


def dither(url: str) -> Optional[bytes]:
    if url in _cache:
        _cache.move_to_end(url)
        return _cache[url]
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
    img = ImageOps.fit(img, (SIZE, SIZE), Image.LANCZOS)
    img = ImageOps.autocontrast(img, cutoff=1)
    png = _to_png(img.convert("1"))  # Floyd-Steinberg dithering
    _cache[url] = png
    if len(_cache) > 64:
        _cache.popitem(last=False)
    return png


def placeholder(name: str) -> bytes:
    """Station name in block letters, for stations with no art."""
    img = Image.new("L", (SIZE, SIZE), 0)
    d = ImageDraw.Draw(img)
    words = name.upper().split()
    font = ImageFont.load_default(size=22)
    lines = words if len(words) <= 3 else [" ".join(words[:2]), " ".join(words[2:])]
    h = 26 * len(lines)
    y = (SIZE - h) // 2
    for line in lines:
        w = d.textlength(line, font=font)
        d.text(((SIZE - w) / 2, y), line, fill=255, font=font)
        y += 26
    d.rectangle([2, 2, SIZE - 3, SIZE - 3], outline=255)
    return _to_png(img)
