"""NTS public data feeds: what's live on Channel 1/2, the schedule, and the Infinite Mixtapes."""

import html
import logging
import time
from datetime import datetime, timezone

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


def _show(broadcast: dict) -> dict:
    details = broadcast.get("embeds", {}).get("details", {})
    return {
        "title": html.unescape(broadcast.get("broadcast_title", "")).strip(),
        "subtitle": details.get("location_long") or "",
        "description": html.unescape(details.get("description") or "").strip(),
        "genres": [g["value"] for g in details.get("genres", []) if g.get("value")],
        "start": broadcast.get("start_timestamp"),
        "end": broadcast.get("end_timestamp"),
        "art": details.get("media", {}).get("picture_medium"),
    }


def _channel(channel: str) -> dict:
    for ch in _live.get().get("results", []):
        if ch.get("channel_name") == channel:
            return ch
    return {}


def _ended(show: dict) -> bool:
    end = show.get("end")
    try:
        return bool(end) and datetime.fromisoformat(end.replace("Z", "+00:00")) <= datetime.now(timezone.utc)
    except ValueError:
        return False


def schedule(channel: str, count: int = 5) -> list:
    """The current show plus the next count-1, oldest first. NTS keeps listing a show as
    "now" for a while after it ends, so anything already over is skipped."""
    ch = _channel(channel)
    keys = ["now", "next"] + [f"next{i}" for i in range(2, 18)]
    shows = [_show(ch[k]) for k in keys if ch.get(k)]
    return [s for s in shows if not _ended(s)][:count]


def live_now(channel: str) -> dict:
    """Current show on an NTS channel."""
    shows = schedule(channel, 1)
    return shows[0] if shows else {}


def mixtape(alias: str) -> dict:
    for m in _mixtapes.get().get("results", []):
        if m.get("mixtape_alias") == alias:
            return {
                "title": m.get("title", ""),
                "subtitle": m.get("subtitle", ""),
                "description": html.unescape(m.get("description") or "").strip(),
                "art": m.get("media", {}).get("picture_medium"),
            }
    return {}
