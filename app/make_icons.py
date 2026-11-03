"""Writes the home-screen icons: a site-style display window with PAS in it.

The icon is drawn by the page itself (dev/icon.js, in the page so it has the VT323 font), so it
matches the site. To redraw it:
  1. build web/ (build_static.py), then run this script: it serves web/ on localhost:8090
  2. open http://localhost:8090, set window.ICON_POST = true, and run dev/icon.js in the console
It writes static/icon-512.png and static/icon-180.png, then stops. Rebuild to copy them to web/."""
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

HERE = Path(__file__).parent
WANT = {"/icon-512.png", "/icon-180.png"}
got = set()


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path not in WANT:
            self.send_error(404); return
        body = self.rfile.read(int(self.headers["Content-Length"]))
        if body[:8] != b"\x89PNG\r\n\x1a\n":
            self.send_error(400); return
        (HERE / "static" / self.path.lstrip("/")).write_bytes(body)
        got.add(self.path)
        print("wrote", self.path, len(body), "bytes", flush=True)
        self.send_response(200); self.end_headers()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")  # always the fresh build
        super().end_headers()


server = HTTPServer(("localhost", 8090), partial(Handler, directory=str(HERE / "web")))
while got != WANT:
    server.handle_request()
