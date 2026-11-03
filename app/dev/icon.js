// The home-screen icon: a display window like the site's panels (chamfered, thin amber edge, code
// tab) on the site's dark dotted background, with PAS glowing in VT323. Run in the app page while
// make_icons.py serves it; with window.ICON_POST set it posts both sizes back and make_icons.py
// writes them to static/. Returns the 512 and 180 px data URLs for a look.
(async () => {
  await Promise.all([document.fonts.load('330px "VT323"'), document.fonts.load('600 60px "Saira Condensed"')]);
  const N = 1024, big = document.createElement("canvas");
  big.width = big.height = N;
  const g = big.getContext("2d");

  // Background: the page's --bg with its faint amber dot texture and a darker rim
  g.fillStyle = "#0e0c0a"; g.fillRect(0, 0, N, N);
  for (let y = 11; y < N; y += 22) for (let x = 11; x < N; x += 22) {
    g.fillStyle = "rgba(255,176,46,.07)"; g.beginPath(); g.arc(x, y, 3, 0, Math.PI * 2); g.fill();
  }
  const v = g.createRadialGradient(N / 2, N / 2, N * .3, N / 2, N / 2, N * .75);
  v.addColorStop(0, "rgba(0,0,0,0)"); v.addColorStop(1, "rgba(0,0,0,.55)");
  g.fillStyle = v; g.fillRect(0, 0, N, N);

  // The display window, chamfered on two corners like the page's .cham panels
  const x = 140, y = 290, w = N - 280, h = 444, k = 60;
  const path = () => { g.beginPath(); g.moveTo(x + k, y); g.lineTo(x + w, y); g.lineTo(x + w, y + h - k);
    g.lineTo(x + w - k, y + h); g.lineTo(x, y + h); g.lineTo(x, y + k); g.closePath(); };
  g.save(); g.shadowColor = "rgba(255,150,30,.22)"; g.shadowBlur = 70;
  path(); g.fillStyle = "#070503"; g.fill(); g.restore();
  g.save(); path(); g.clip();
  for (let yy = y + 14; yy < y + h; yy += 22) for (let xx = x + 14; xx < x + w; xx += 22) {
    g.fillStyle = "rgba(255,176,46,.08)"; g.fillRect(xx - 3, yy - 3, 6, 6);   // unlit dot matrix
  }
  g.textAlign = "center"; g.textBaseline = "middle"; g.font = '400 330px "VT323"';
  g.shadowColor = "#ffb02e"; g.shadowBlur = 44; g.fillStyle = "#ffb02e";
  g.fillText("PAS", N / 2, y + h / 2 + 14);
  g.shadowBlur = 0; g.fillText("PAS", N / 2, y + h / 2 + 14);
  g.restore();
  g.lineWidth = 7; g.strokeStyle = "#6b4c1c"; path(); g.stroke();   // the panel edge, a step brighter than --line

  // Code tab on the top-right corner, inverse like 01 ART
  const tw = 128, th = 50;
  g.fillStyle = "#9c6c22"; g.fillRect(x + w - tw, y, tw, th);
  g.fillStyle = "#0e0c0a"; g.font = '600 40px "Saira Condensed"'; g.textAlign = "center"; g.textBaseline = "middle";
  g.fillText("01", x + w - tw / 2, y + th / 2 + 2);

  // Registration brackets outside the window's square corners
  g.strokeStyle = "#9c6c22"; g.lineWidth = 7; g.lineCap = "square";
  const L = 44, o = 30;
  g.beginPath(); g.moveTo(x + w + o - L, y - o); g.lineTo(x + w + o, y - o); g.lineTo(x + w + o, y - o + L); g.stroke();
  g.beginPath(); g.moveTo(x - o, y + h + o - L); g.lineTo(x - o, y + h + o); g.lineTo(x - o + L, y + h + o); g.stroke();

  // Glass: a soft highlight across the top, as iOS icons have
  const s = g.createLinearGradient(0, 0, 0, N * .5);
  s.addColorStop(0, "rgba(255,240,215,.10)"); s.addColorStop(1, "rgba(255,240,215,0)");
  g.fillStyle = s; g.fillRect(0, 0, N, N * .5);

  const out = {};
  for (const size of [512, 180]) {
    const c = document.createElement("canvas"); c.width = c.height = size;
    const kx = c.getContext("2d"); kx.imageSmoothingQuality = "high"; kx.drawImage(big, 0, 0, size, size);
    const blob = await new Promise(r => c.toBlob(r, "image/png"));
    if (window.ICON_POST) await fetch(`icon-${size}.png`, { method: "POST", body: blob });
    out[size] = c.toDataURL();
  }
  return out;
})();
