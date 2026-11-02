"""Playback backends. MPD is the real one (moOde on the Pi, or Homebrew mpd on a Mac).
MockPlayer keeps the same state without making sound, for building the UI without MPD."""

import logging
from typing import Optional

from mpd import MPDClient

log = logging.getLogger("pi-radio")


class MockPlayer:
    name = "mock"

    def __init__(self):
        self._url = None
        self._playing = False
        self._volume = 60

    def play(self, url: str) -> None:
        self._url, self._playing = url, True

    def resume(self) -> None:
        if self._url:
            self._playing = True

    def stop(self) -> None:
        self._playing = False

    def set_volume(self, value: int) -> None:
        self._volume = max(0, min(100, value))

    def status(self) -> dict:
        return {"playing": self._playing, "volume": self._volume, "url": self._url, "title": None,
                "bitrate": None, "audio": None}


class MPDPlayer:
    name = "mpd"

    def __init__(self, host: str = "localhost", port: int = 6600):
        self.host, self.port = host, port

    def _client(self) -> MPDClient:
        # A fresh connection per call: MPD drops idle clients, and calls here are infrequent.
        c = MPDClient()
        c.timeout = 5
        c.connect(self.host, self.port)
        return c

    def _run(self, fn):
        c = self._client()
        try:
            return fn(c)
        finally:
            c.close()
            c.disconnect()

    def play(self, url: str) -> None:
        def go(c):
            c.clear()
            c.add(url)
            c.play(0)
        self._run(go)

    def resume(self) -> None:
        self._run(lambda c: c.play())

    def stop(self) -> None:
        self._run(lambda c: c.stop())

    def set_volume(self, value: int) -> None:
        self._run(lambda c: c.setvol(max(0, min(100, value))))

    def status(self) -> dict:
        def get(c):
            st, song = c.status(), c.currentsong()
            vol = int(st.get("volume", -1))
            return {
                "playing": st.get("state") == "play",
                "volume": vol if vol >= 0 else None,
                "url": song.get("file"),
                "title": song.get("title"),
                "bitrate": st.get("bitrate"),  # kbps, while playing
                "audio": st.get("audio"),      # "samplerate:bits:channels", e.g. "44100:16:2"
            }
        return self._run(get)


def make_player(kind: Optional[str], host: str, port: int):
    """kind 'mpd' or 'mock' forces a backend. Otherwise try MPD and fall back to the mock."""
    if kind == "mock":
        return MockPlayer()
    player = MPDPlayer(host, port)
    try:
        player.status()
        log.info("Using MPD at %s:%s", host, port)
        return player
    except Exception as e:
        if kind == "mpd":
            raise
        log.warning("MPD not reachable at %s:%s (%s). Using the mock player: no sound.", host, port, e)
        return MockPlayer()
