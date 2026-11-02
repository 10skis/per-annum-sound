"""NTS public data feeds: what's live on Channel 1/2, and the Infinite Mixtapes."""

import html
import logging
import time

import httpx

log = logging.getLogger("pi-radio")

LIVE_URL = "https://www.nts.live/api/v2/live"
MIXTAPES_URL = "https://www.nts.live/api/v2/mixtapes"


class _Cached:
    def __init__(self, url: str, ttl: int):
        self.url, self.ttl = url, ttl
        self._data, self._at = None, 0.0

    def get(self):
        if self._data is None or time.time() - self._at > self.ttl:
            try:
                r = httpx.get(self.url, timeout=5, headers={"User-Agent": "pi-radio/0.1"})
                r.raise_for_status()
                self._data, self._at = r.json(), time.time()
            except Exception as e:
                # Keep serving the last good copy rather than blanking the display.
                log.warning("NTS feed failed (%s): %s", self.url, e)
        return self._data or {}


_live = _Cached(LIVE_URL, ttl=60)
_mixtapes = _Cached(MIXTAPES_URL, ttl=6 * 3600)


def live_now(channel: str) -> dict:
    """Current show on an NTS channel: title, location, art URL."""
    for ch in _live.get().get("results", []):
        if ch.get("channel_name") == channel:
            now = ch.get("now", {})
            details = now.get("embeds", {}).get("details", {})
            return {
                "title": html.unescape(now.get("broadcast_title", "")).strip(),
                "subtitle": details.get("location_long") or "",
                "art": details.get("media", {}).get("picture_medium"),
            }
    return {}


def mixtape(alias: str) -> dict:
    for m in _mixtapes.get().get("results", []):
        if m.get("mixtape_alias") == alias:
            return {
                "title": m.get("title", ""),
                "subtitle": m.get("subtitle", ""),
                "art": m.get("media", {}).get("picture_medium"),
            }
    return {}
