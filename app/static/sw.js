// Offline shell for the no-server build. Keeps the page, station list, art, fonts and the
// last NTS data so the app still opens with no signal. Network first, so updates show
// straight away; the cached copy is only used offline. Streams are never touched.
const CACHE = "pi-radio-v1";
const SHELL = ["./", "index.html", "stations.json", "manifest.webmanifest",
               "static/worldmap.js", "static/icon-180.png", "static/icon-512.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener("fetch", e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== "GET" || req.headers.has("range") || req.destination === "audio") return;
  const keep = url.origin === location.origin
    || /(^|\.)fonts\.(googleapis|gstatic)\.com$/.test(url.hostname)
    || url.hostname === "www.nts.live" || url.hostname.endsWith(".ntslive.co.uk");
  if (!keep || /\.(m3u8|ts|aac|mp3)$/.test(url.pathname)) return;
  e.respondWith(
    fetch(req).then(res => {
      if (res.ok || res.type === "opaque") {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(req, copy));
      }
      return res;
    }).catch(() => caches.match(req).then(hit => hit || (req.mode === "navigate" ? caches.match("index.html") : Response.error())))
  );
});
