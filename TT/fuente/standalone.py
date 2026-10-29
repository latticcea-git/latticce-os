# Builds a self-contained tt.html: page + d3 + logos + data + a small stand-in for the dashboard runtime.
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
D3 = sys.argv[1]
IG = json.loads(sys.argv[2])
out_dir = os.path.join(here, 'standalone'); os.makedirs(out_dir, exist_ok=True)
page = open(os.path.join(here, 'index.html')).read()
page = page.replace('<script src="logos.js"></script>', '')
for a, b in [
    ('Instagram de Design en 2026, en vivo', 'Instagram de Design en 2026 (corte 28 oct)'),
    ('La única cuenta conectada a Metricool. Se actualiza al abrir el tablero con tu acceso a Metricool.', 'La única cuenta conectada a Metricool. En esta versión independiente es un corte fijo del 28 de octubre.'),
    ('Instagram Design en vivo', 'Instagram Design'),
    ("'Instagram 2026 en vivo (Metricool)'", "'Instagram 2026 (Metricool, corte 28 oct)'"),
]:
    page = page.replace(a, b)
data = {}
for n in ['proyectos', 'hitos', 'etapas', 'capacidad', 'nodos', 'book', 'blog', 'madurez', 'redes', 'rumbo']:
    data[n] = json.load(open(os.path.join(here, n + '.json')))
shim = r"""
<script>
(function () {
  const RAW = %DATA%;
  const IG = %IG%;
  const store = {}, calcs = [], draws = {}, cbs = [], loaders = {};
  let P = {};
  for (const k in RAW) store[k] = {status: 'ok', data: RAW[k], columns: RAW[k].length ? Object.keys(RAW[k][0]) : [], meta: []};
  const under = (el) => !!el.closest('[hidden]');
  const runCalcs = () => {
    for (let pass = 0; pass < 4; pass++) for (const c of calcs) {
      const ins = c.inputs.map((x) => store[x]);
      if (ins.every((x) => x && x.status === 'ok')) {
        try { const d = c.fn(...ins.map((x) => x.data)); store[c.id] = {status: 'ok', data: d, columns: Array.isArray(d) && d.length ? Object.keys(d[0]) : [], meta: []}; }
        catch (e) { console.error('calc', c.id, e); store[c.id] = {status: 'error', data: [], message: String(e)}; }
      }
    }
  };
  const fill = (el) => {
    const d = store[el.dataset.source]; if (!d || d.status !== 'ok' || !Array.isArray(d.data)) return;
    let rows = d.data;
    if (el.dataset.where) { const q = new URLSearchParams(el.dataset.where); rows = rows.filter((r) => [...q].every(([k, v]) => String(r[k]) === v)); }
    const r = el.dataset.row != null ? rows[Number(el.dataset.row)] : rows[0];
    if (r && r[el.dataset.field] != null) el.textContent = r[el.dataset.field];
  };
  const drawAll = (only) => {
    document.querySelectorAll('#dash-root [data-draw]').forEach((el) => {
      const n = el.dataset.draw; if (only && n !== only) return; if (under(el)) return;
      if (draws[n]) { try { draws[n](el); } catch (e) { console.error('draw', n, e); } }
      else if (el.dataset.field) fill(el);
    });
  };
  const render = () => { cbs.forEach((f) => { try { f(); } catch (e) { console.error('onData', e); } }); drawAll(); };
  window.dash = {
    colors: ['#72E7FF', '#FE5C14', '#EAB43F', '#A78BFA', '#7EE0A1', '#FF7A6B', '#DCEAF2', '#C9CDD0'],
    loader: (id, o) => { loaders[id] = o; },
    calc: (id, o) => calcs.push({id, ...o}),
    draw: (n, f) => { if (f) { draws[n] = typeof f === 'function' ? f : (el) => { if (!el.__m) el.__m = f.mount ? f.mount(el) : null; if (f.update) f.update(el, el.__m); }; } else drawAll(n); },
    data: (id) => store[id] || {status: 'missing', data: [], columns: [], meta: []},
    params: () => ({...P}),
    setParams: (o) => { P = {...P, ...o}; for (const k in P) if (P[k] == null) delete P[k]; render(); },
    resetParams: () => { P = {}; render(); },
    onData: (f) => { cbs.push(f); },
    setLink: (name) => { try { history.replaceState(null, '', '#' + name); } catch (e) {} },
    refresh: () => {},
  };
  window.__ttStart = () => {
    const l = loaders.ig_design;
    if (l) { try { const r = l.fn({answer: JSON.stringify(IG), args: {metrics: ['IGEV01', 'IGEV37', 'IGEV38']}}); store.ig_design = {status: 'ok', data: r.rows || r, columns: r.columns || [], meta: []}; } catch (e) { store.ig_design = {status: 'error', data: [], message: String(e)}; } }
    runCalcs(); render();
    new MutationObserver(() => drawAll()).observe(document.getElementById('dash-root'), {attributes: true, subtree: true, attributeFilter: ['hidden']});
    let t = 0; window.addEventListener('resize', () => { clearTimeout(t); t = setTimeout(render, 150); });
    const h = location.hash.slice(1); if (h) { const el = document.getElementById(h); if (el) el.scrollIntoView(); }
  };
})();
</script>
""".replace('%DATA%', json.dumps(data, ensure_ascii=False)).replace('%IG%', json.dumps(IG))
logos = open(os.path.join(here, 'logos.js')).read()
d3 = open(D3).read()
html = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>LATTICCE TT · Trayectoria Trazada</title>
<style>
  :root {{ --font-anthropic-sans: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif; --font-anthropic-serif: Georgia, "Times New Roman", serif;
    --cds-dur-slow: 240ms; --cds-ease-out: cubic-bezier(.2,.8,.2,1); --cds-font-size-body: 14px; color-scheme: dark; }}
  html, body {{ margin: 0; background: #07080B; }}
  #dash-root {{ max-width: 1680px; margin: 0 auto; padding: 16px; }}
  :where(#dash-root) :where(button, select, input) {{ font-family: inherit; font-size: inherit; color: inherit; }}
  :where(#dash-root) :where(button) {{ cursor: pointer; }}
  .tt-standalone {{ font: 12px/1.4 var(--font-anthropic-sans); color: #8C9099; text-align: center; padding: 8px 16px 0; }}
</style>
<script>{d3}</script>
<script>{logos}</script>
{shim}
</head><body>
<p class="tt-standalone">Versión independiente · datos al 29 de octubre de 2026 (Instagram: corte del 28) · uso interno de LATTICCE, no compartir públicamente</p>
<div id="dash-root">
{page}
</div>
<script>__ttStart();</script>
</body></html>"""
open(os.path.join(out_dir, 'tt.html'), 'w').write(html)
print(len(html.encode()))
