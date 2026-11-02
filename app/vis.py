"""Spectrum analyser fed by MPD's FIFO output, the raw audio MPD is playing.
MPD needs an output like the one in dev/mpd.conf writing 44100:16:2 to the FIFO path.
With no FIFO, levels() reports source "none" and the page shows a labelled simulation."""

import logging
import os
import threading
import time

import numpy as np

log = logging.getLogger("pi-radio")

RATE = 44100
FRAMES = 2048
BANDS = 32


class Spectrum:
    def __init__(self, path: str):
        self.path = path
        self._levels = np.zeros(BANDS)
        self._at = 0.0
        self._lock = threading.Lock()
        # Log-spaced band edges from 40 Hz to 16 kHz, as FFT bin indices.
        freqs = np.fft.rfftfreq(FRAMES, 1 / RATE)
        edges = np.geomspace(40, 16000, BANDS + 1)
        self._bins = [np.where((freqs >= lo) & (freqs < hi))[0] for lo, hi in zip(edges[:-1], edges[1:])]
        self._window = np.hanning(FRAMES)
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        while True:
            if not os.path.exists(self.path):
                time.sleep(2)
                continue
            try:
                with open(self.path, "rb") as f:  # blocks until MPD opens the FIFO
                    log.info("Visualizer reading %s", self.path)
                    while True:
                        buf = f.read(FRAMES * 4)
                        if len(buf) < FRAMES * 4:
                            break  # MPD closed the FIFO
                        self._analyse(buf)
            except Exception as e:
                log.warning("Visualizer FIFO error: %s", e)
                time.sleep(2)

    def _analyse(self, buf: bytes):
        samples = np.frombuffer(buf, dtype="<i2").reshape(-1, 2).mean(axis=1) / 32768
        mag = np.abs(np.fft.rfft(samples * self._window))
        bands = np.array([mag[b].max() if len(b) else 0 for b in self._bins])
        db = 20 * np.log10(bands + 1e-9)
        level = np.clip((db + 10) / 50, 0, 1)  # roughly -10 dB..+40 dB onto 0..1
        with self._lock:
            # Rise straight away, fall gradually, like a meter.
            self._levels = np.maximum(level, self._levels * 0.8)
            self._at = time.time()

    def levels(self) -> dict:
        with self._lock:
            if time.time() - self._at > 0.5:
                return {"source": "mpd" if os.path.exists(self.path) else "none", "levels": [0] * BANDS}
            return {"source": "mpd", "levels": [round(float(x), 3) for x in self._levels]}
