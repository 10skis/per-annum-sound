// The home-screen icon: the page's own sigil (rings seeded by "Per Annum Sound") with PAS in the
// middle. Run in the app page (served from web/) while make_icons.py serves it; it posts the
// two sizes back and make_icons.py writes them to static/. Returns the 512 px data URL for a look.
(async () => {
  await document.fonts.load('100px "VT323"');
  const N = 1024, big = document.createElement("canvas");
  big.width = big.height = N;
  const g = big.getContext("2d"), S = N / 440, cx = N / 2;
  g.fillStyle = "#0e0c0a"; g.fillRect(0, 0, N, N);
  const m = sigilModel("Per Annum Sound");
  m.rings = m.rings.filter(r => r.ring >= 2);   // clear the middle for the letters
  m.code = ""; m.city = "";
  drawSigilOn(g, N, m, null);
  g.textAlign = "center"; g.textBaseline = "middle";
  g.font = `${Math.round(112 * S)}px "VT323", monospace`;
  g.shadowColor = "#ffb02e"; g.shadowBlur = 14 * S; g.fillStyle = "#ffb02e";
  g.fillText("PAS", cx, cx + 4 * S);
  g.shadowBlur = 0; g.fillText("PAS", cx, cx + 4 * S);
  const out = {};
  for (const size of [512, 180]) {
    const c = document.createElement("canvas"); c.width = c.height = size;
    const k = c.getContext("2d"); k.imageSmoothingQuality = "high"; k.drawImage(big, 0, 0, size, size);
    const blob = await new Promise(r => c.toBlob(r, "image/png"));
    if (window.ICON_POST) await fetch(`icon-${size}.png`, { method: "POST", body: blob });
    out[size] = c.toDataURL();
  }
  return out;
})();
