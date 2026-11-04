/* In-page self test for the no-server build. Serve app/web (python3 -m http.server 8091
   --directory web), open it in a browser, then run this file's text in the page (the browser
   tool's javascript call, or the dev console). It defines window.selfTest:

     await selfTest.core()          displays, per-station panels and controls; about 10 s
     await selfTest.play(0, 11)     plays stations 0 to 10 and checks sound starts; run in
                                    slices of about 11 (each slice takes up to 40 s)
     selfTest.layout()              overflow check at the current window width; resize and
                                    repeat (320, 375, 458, 768, 960, 1440 cover the breakpoints)

   Each returns a report; anything other than empty lists or true is worth a look. Draws are
   called directly rather than waiting for animation frames, because a hidden browser pane runs
   none. Presets and the playing station are put back afterwards. */
window.selfTest = {
  async core() {
    const errs = [], wait = ms => new Promise(r => setTimeout(r, ms));
    const tryit = (name, fn) => { try { fn(); } catch (e) { errs.push(`${name}: ${e.message}`); } };
    const savedPresets = presets.slice(), savedLevel = lvlMode, savedVis = visMode.slice();
    act.play(order[0]);
    await wait(2500);
    S.playing = true;
    let t = performance.now();
    const frames = (fn, n = 20) => { for (let i = 0; i < n; i++) { t += 16.7; visLevels = simLevels(t); fn(); } };
    for (const m of VIS_MODES) for (const slot of [0, 1]) {
      visMode[slot] = VIS_MODES.indexOf(m);
      tryit(`spectrum display ${m}`, () => frames(() => drawVisScreen($(slot ? "fall" : "vis"), slot, t)));
    }
    LEVEL_MODES.forEach((m, k) => { lvlMode = k; tryit(`level display ${m}`, () => frames(() => drawLevel(t))); });
    const savedRange = mapRange;
  for (const r of MAP_ORDER) tryit(`map ${r}`, () => { setMapRange(r); drawMap(t); drawMap(t + 5000); });
  setMapRange(savedRange);
    tryit("ripple", () => { if (startDotRipple(true)) { drawArtDots(performance.now()); endDotRipple(); } });
    const aboutFails = [];
    for (const id of order) {
      local.id = id;
      local.desc = { ...(local.desc || {}), station: { id, name: NAMES[id], group: "" }, now: { title: "", subtitle: "" }, signal: {} };
      tryit(`up next ${id}`, () => drawNext());
      tryit(`about ${id}`, () => { openAbout(); if ($("about").hidden) aboutFails.push(id); closeAbout(); });
      tryit(`signal ${id}`, () => drawSignal({}, true));
      tryit(`sigil ${id}`, () => { useSigil(id); drawSigil(t); });
    }
    // Controls, through the same keys a person would press
    const key = (k, code = "", extra = {}) => document.dispatchEvent(new KeyboardEvent("keydown", { key: k, code, bubbles: true, ...extra }));
    const controls = {};
    act.play(order[5]); await wait(600);
    key("ArrowRight"); await wait(400); controls.next = local.id === order[6];
    key("ArrowLeft"); await wait(400); controls.previous = local.id === order[5];
    const before = local.id; key("r"); await wait(400); controls.random = local.id !== before;
    key(" "); await wait(300); controls.spaceStops = !local.playing;
    key(" "); await wait(300); controls.spaceStarts = local.playing;
    const cur = local.id; key("#", "Digit3", { shiftKey: true }); await wait(200);
    act.play(order[0]); await wait(300); key("3", "Digit3"); await wait(400); controls.preset = local.id === cur;
    key("s"); controls.sleepOn = $("sleepBtn").textContent !== "ZZ"; for (let i = 0; i < 4; i++) key("s"); controls.sleepOff = $("sleepBtn").textContent === "ZZ";
    const r0 = mapRange; key("m"); controls.mapKey = mapRange === MAP_ORDER[(MAP_ORDER.indexOf(r0) + 1) % 4]; setMapRange(r0);
    key("?"); controls.helpOpens = !$("help").hidden; key("Escape"); controls.helpCloses = $("help").hidden;
    holdTitle(true); controls.titleHold = $("line1").classList.contains("held"); holdTitle(false);
    holdArt(true); controls.artHold = artHeld; holdArt(false);
    phoneStop();
    presets.splice(0, presets.length, ...savedPresets); store.set("piRadioPresets", presets); drawPresets(local.id, local.playing);
    lvlMode = savedLevel; visMode.splice(0, visMode.length, ...savedVis); drawLevelLabel();
    const failedControls = Object.entries(controls).filter(([, ok]) => !ok).map(([k]) => k);
    return { errors: errs, aboutFails, failedControls, displays: VIS_MODES.length + LEVEL_MODES.length, stations: order.length };
  },

  async play(from = 0, to = order.length) {
    const out = {};
    for (const id of order.slice(from, to)) {
      act.play(id);
      const t0 = performance.now();
      while (performance.now() - t0 < 7000 && audio.currentTime < .3 && !(tuning && tuning.off)) await new Promise(r => setTimeout(r, 300));
      const ms = Math.round(performance.now() - t0);
      if (audio.currentTime < .3) out[id] = tuning && tuning.off ? "no signal (off air?)" : "silent after 7 s";
      else if (ms > 3500) out[id] = `slow: ${ms} ms`;
    }
    phoneStop();
    return { checked: `${from}-${Math.min(to, order.length) - 1}`, problems: out };
  },

  layout() {
    const vw = document.documentElement.clientWidth, head = document.querySelector(".head"), strip = $("strip");
    const over = [...document.querySelectorAll(".unit *, .list *, .deck *")].filter(e => {
      if (e.closest(".tape, .line, .sig, .vis-head, canvas, #recent, .swipe, .presets")) return false;  // these scroll or clip on purpose
      const r = e.getBoundingClientRect();
      return r.width && (r.right > vw + 1 || r.left < -1);
    }).slice(0, 5).map(e => e.id || e.className || e.tagName);
    return { width: vw, pageOverflow: document.documentElement.scrollWidth - vw, headerOverflow: head.scrollWidth - head.clientWidth,
             infoPaneOverflow: strip.scrollHeight - strip.clientHeight, outside: over };
  },
};
"selfTest ready: core(), play(from, to), layout()";
