// The home-screen icon: the desktop dial's rotating window (an arc of katakana fading out either
// side of the lit one, needle above) on a dark dot-matrix plate, with the lit glyph shown large
// in LED dots below. Option D in mockups/app-icon-dial.html. Run in the app page while
// make_icons.py serves it; with window.ICON_POST set it posts both sizes back and make_icons.py
// writes them to static/. Returns the 512 and 180 px data URLs for a look.
(async () => {
  const N = 1024, GLYPHS = [..."ｦｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃ"];
  const FONT = '"Hiragino Sans", "Hiragino Kaku Gothic ProN", "Apple Symbols", sans-serif';
  const big = document.createElement("canvas");
  big.width = big.height = N;
  const g = big.getContext("2d"), c = N / 2;

  // Plate: the page's --bg, a faint dot matrix brighter toward the middle, a darker rim
  g.fillStyle = "#0e0c0a"; g.fillRect(0, 0, N, N);
  for (let y = 16; y < N; y += 32) for (let x = 16; x < N; x += 32) {
    const f = 1 - Math.min(1, Math.hypot(x - c, y - c) / (N * .7));
    g.fillStyle = `rgba(255,176,46,${(.03 + f * .06).toFixed(3)})`;
    g.beginPath(); g.arc(x, y, 5, 0, Math.PI * 2); g.fill();
  }
  const v = g.createRadialGradient(c, c, N * .32, c, c, N * .75);
  v.addColorStop(0, "rgba(0,0,0,0)"); v.addColorStop(1, "rgba(0,0,0,.5)");
  g.fillStyle = v; g.fillRect(0, 0, N, N);

  // The rotating window: 20 slots round a circle centred low, only five either side of the top shown
  const cy = N * .78, r = 540, count = 20, span = 5;
  g.textAlign = "center"; g.textBaseline = "middle";
  for (let i = -span; i <= span; i++) {
    const a = -Math.PI / 2 + i / count * Math.PI * 2, x = c + Math.cos(a) * r, y = cy + Math.sin(a) * r;
    g.save();
    if (i === 0) { g.fillStyle = "#ffb02e"; g.shadowColor = "#ffb02e"; g.shadowBlur = 30; g.font = `700 112px ${FONT}`; }
    else { g.fillStyle = `rgba(208,140,38,${Math.max(.12, 1 - Math.abs(i) / (span + 1)).toFixed(2)})`; g.font = `600 84px ${FONT}`; }
    g.fillText(GLYPHS[(i + count) % count], x, y); g.restore();
  }
  g.save(); g.shadowColor = "#ffb02e"; g.shadowBlur = 20; g.fillStyle = "#ffb02e";   // needle
  const ny = cy - r - 136; g.beginPath(); g.moveTo(c - 22, ny); g.lineTo(c + 22, ny); g.lineTo(c, ny + 30); g.closePath(); g.fill();
  g.restore();

  // The lit glyph again, large, sampled onto a 13x13 LED grid
  const grid = 13, size = 400, ox = c - size / 2, oy = N * .62 - size / 2, pitch = size / grid, lr = pitch * .38;
  const t = document.createElement("canvas"); t.width = t.height = grid;
  const k = t.getContext("2d"); k.fillStyle = "#fff"; k.textAlign = "center"; k.textBaseline = "middle";
  k.font = `600 ${grid * .95}px ${FONT}`; k.fillText(GLYPHS[0], grid / 2, grid / 2 + grid * .04);
  const px = k.getImageData(0, 0, grid, grid).data;
  for (let yy = 0; yy < grid; yy++) for (let xx = 0; xx < grid; xx++) {
    const on = px[(yy * grid + xx) * 4 + 3] > 110, x = ox + (xx + .5) * pitch, y = oy + (yy + .5) * pitch;
    g.save();
    if (on) { g.shadowColor = "rgba(255,176,46,.9)"; g.shadowBlur = lr * 1.6; g.fillStyle = "#ffb02e"; }
    else g.fillStyle = "#2c200c";
    g.beginPath(); g.arc(x, y, on ? lr : lr * .6, 0, Math.PI * 2); g.fill(); g.restore();
    if (on) { g.fillStyle = "rgba(255,245,220,.5)"; g.beginPath(); g.arc(x - lr * .3, y - lr * .3, lr * .3, 0, Math.PI * 2); g.fill(); }
  }

  // Glass: a soft highlight across the top
  const s = g.createLinearGradient(0, 0, 0, N * .5);
  s.addColorStop(0, "rgba(255,240,215,.10)"); s.addColorStop(1, "rgba(255,240,215,0)");
  g.fillStyle = s; g.fillRect(0, 0, N, N * .5);

  const out = {};
  for (const size of [512, 180]) {
    const cv = document.createElement("canvas"); cv.width = cv.height = size;
    const kx = cv.getContext("2d"); kx.imageSmoothingQuality = "high"; kx.drawImage(big, 0, 0, size, size);
    const blob = await new Promise(res => cv.toBlob(res, "image/png"));
    if (window.ICON_POST) await fetch(`icon-${size}.png`, { method: "POST", body: blob });
    out[size] = cv.toDataURL();
  }
  return out;
})();
