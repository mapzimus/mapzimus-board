// app.js - Mapzimus board v16
// sc fields: 0-100 | vs: 0-100 | pastel palette | sub-score range filters | sort direction toggle

const VAR_LABELS = {
  rep_pct:"Republican vote % by state", median_household_income:"Median household income by state",
  pct_under_25k:"% households under $25K", pct_over_200k:"% households over $200K",
  state_gdp_per_capita:"State GDP per capita", violent_crime_rate:"Violent crime rate by state",
  murder_rate:"Murder rate by state", pct_bachelors:"% with bachelor's degree",
  pct_hs_grad:"% HS graduates", expenditure_per_pupil:"Per-pupil school spending",
  avg_teacher_salary:"Avg teacher salary", state_unemployment_rate:"Unemployment rate by state",
  female_lfp_rate:"Female labor force participation", total_transfers_per_capita:"Govt transfers per capita",
  pct_on_snap:"% households on SNAP", pct_on_medicaid:"% on Medicaid",
  birth_rate_state:"Birth rate by state", teen_birth_rate:"Teen birth rate",
  pct_births_unmarried:"% births to unmarried mothers", total_medicare:"Medicare enrollment",
  per_capita_health_spending:"Health spending per capita", all_items_cpi:"All-items CPI",
  gasoline_cpi:"Gasoline CPI", housing_cpi:"Housing CPI",
  home_price_index_2024:"Home price index 2024", home_price_pct_change_2005_2024:"Home price % change 2005-2024",
  student_loans_outstanding:"Student loan debt outstanding", mortgage_delinquency_rate:"Mortgage delinquency rate",
  housing_permits_total:"New housing permits", population_pct_change:"Population % change",
  net_migration_rate:"Net migration rate", birth_rate:"Birth rate by country",
  trade_balance_goods:"Trade balance on goods", rd_pct_gdp:"R&D spending % of GDP",
  pct_forest:"% land that is forest", energy_consumption_per_capita:"Energy per capita",
  renewable_energy_share:"Renewable energy share", coal_production_index:"Coal production index",
  us_troops_overseas:"US troops stationed overseas", defense_budget_total:"Total defense budget",
  pct_bridges_poor:"% bridges in poor condition", waterway_freight_tons:"Waterway freight tonnage",
  passengers_enplaned:"Passengers enplaned", incarceration_rate:"Incarceration rate",
  avg_commute_time:"Average commute time", broadband_access_pct:"Broadband access rate",
  dollar_general_density:"Dollar General stores per 10K", grocery_distance:"Drive time to nearest grocery",
  population_pct_change_2020_2025:"Population % change 2020-2025",
  population_per_sq_km:"Population density per km2", current_account_balance:"Current account balance",
  water_access_pct:"Drinking water access %", political_regime:"Political regime type",
  median_age:"Median age", natural_growth_rate:"Natural population growth rate",
  old_age_dependency_ratio:"Old-age dependency ratio", youth_dependency_ratio:"Youth dependency ratio",
  migration_contribution_pct:"Migration contribution to growth",
  population_pct_change_2023_2100:"Population % change 2023-2100",
};

//  OVERRIDES 
const LS_KEY = 'mapzimus_overrides_v2';
function loadOverrides() { try { return JSON.parse(localStorage.getItem(LS_KEY)||'{}'); } catch { return {}; } }
function saveOverride(id, field, value) {
  const ov = loadOverrides();
  if (!ov[id]) ov[id] = {};
  ov[id][field] = value;
  localStorage.setItem(LS_KEY, JSON.stringify(ov));
  const idea = D.find(d => d.id === id);
  if (idea) idea[field] = value;
}
(function applyOverrides() {
  const ov = loadOverrides();
  D.forEach(d => {
    if (ov[d.id]) {
      if (ov[d.id].status !== undefined) d.status = ov[d.id].status;
      if (ov[d.id].notes  !== undefined) d.notes  = ov[d.id].notes;
    }
  });
})();

//  INDEXES 
const VAR_INDEX = {};
D.forEach(d => {
  [...(d.vars || []), ...(d.join || [])].forEach(v => {
    if (!VAR_INDEX[v]) VAR_INDEX[v] = [];
    if (!VAR_INDEX[v].find(x => x.id === d.id))
      VAR_INDEX[v].push({ id: d.id, primary: !!(d.vars && d.vars.includes(v)) });
  });
});
const FMT_MAP = {};
D.forEach(d => { if (!FMT_MAP[d.fmt]) FMT_MAP[d.fmt] = []; FMT_MAP[d.fmt].push(d); });

//  PASTEL COLOR PALETTE 
const P = {
  red:'#ff9eae', orange:'#ffb87a', yellow:'#ffe083', green:'#8eedc7',
  teal:'#7de8e8', blue:'#87c3ff', purple:'#c4a3ff', pink:'#f9a8d4',
  lime:'#bef264', sky:'#7dd3fc', amber:'#fcd34d', rose:'#fda4af',
  indigo:'#a5b4fc', mint:'#6ee7b7', peach:'#fdba74', violet:'#e879f9',
};

//  TOPIC COLORS 
const TOPIC_COLORS = {
  health:P.red, economy:P.green, politics:P.blue, crime:P.rose,
  poverty:P.amber, housing:P.orange, education:P.teal, labor:P.purple,
  race:P.pink, gender:P.violet, immigration:P.sky, war:P.red,
  military:P.indigo, energy:P.yellow, climate:P.mint, environment:P.lime,
  food:P.peach, agriculture:P.lime, drugs:P.purple, guns:P.rose,
  finance:P.amber, trade:P.sky, inequality:P.pink, transportation:P.teal,
  infrastructure:P.indigo, technology:P.blue, media:P.sky, population:P.violet,
  international:P.purple, democracy:P.blue, religion:P.amber,
  history:P.peach, space:P.indigo, data:P.mint,
  humor:'#f9a8d4', science:'#7dd3fc', geography:'#86efac', demographics:'#fde68a',
  children:P.pink, rural:P.lime, manufacturing:P.teal, law:P.rose,
};

//  SECTION COLORS 
const SECTION_COLORS = {
  'Health':P.red, 'Elections':P.blue, 'Income':P.green, 'Housing':P.orange,
  'Labor Force':P.purple, 'Law Enforcement':P.rose, 'Education':P.teal,
  'Energy':P.yellow, 'Agriculture':P.lime, 'Transportation':P.teal,
  'Population':P.violet, 'National Security':P.indigo,
  'International Statistics':P.purple, 'Geography':P.mint,
  'Banking':P.amber, 'Finance':P.amber, 'Prices':P.peach,
  'Births Deaths':P.pink, 'Arts Recreation':P.sky,
  'Business Enterprise':P.indigo, 'Foreign Commerce':P.sky,
  'Social Insurance':P.green, 'Wholesale':P.orange, 'Retail Trade':P.orange,
  'Accommodation':P.peach, 'Food Services':P.peach,
  'Forestry':P.lime, 'Fishing':P.sky, 'Mining':P.amber,
};

function getSectionColor(section) {
  if (!section) return '#888';
  const entries = Object.entries(SECTION_COLORS).sort((a,b) => b[0].length - a[0].length);
  for (const [key, color] of entries) {
    if (section.includes(key)) return color;
  }
  return '#888';
}

// Sections that show as clickable badges on cards (excludes catch-all sections)
const BADGE_SECTIONS = new Set([
  'Health','Elections','Income','Housing','Labor Force','Law Enforcement',
  'Education','Energy','Agriculture','Transportation','Population',
  'National Security','Banking','Finance','Prices','Births Deaths',
  'Business Enterprise','Foreign Commerce','Social Insurance',
  'Geography','Arts Recreation','Information',
]);

//  SCORE FIELDS 
// Virality algorithm v3:
// - identity_signal removed (curatorial identity lives in selection, not scoring)
// - tension back to 1.0 (no longer carrying identity's weight)
// - visual bumped to 1.25 (Instagram-specific)
// - originality kept at 1.0 (genuinely distinct from surprise)
// - data_ready is soft penalty: vs *= (1 - 0.3*(1 - data_ready/100))
// - denominator 10.75
const SC_FIELDS = [
  { key:'emotional',    label:'Emotional',    short:'Emo', color:'#ff6b8a', weight:2    },
  { key:'relatability', label:'Relatability', short:'Rel', color:'#38bdf8', weight:2    },
  { key:'clarity',      label:'Clarity',      short:'Cla', color:'#fb923c', weight:2    },
  { key:'surprise',     label:'Surprise',     short:'Sur', color:'#facc15', weight:1.5  },
  { key:'tension',      label:'Tension',      short:'Ten', color:'#c084fc', weight:1.0  },
  { key:'visual',       label:'Visual',       short:'Vis', color:'#34d399', weight:1.25 },
  { key:'originality',  label:'Originality',  short:'Ori', color:'#f472b6', weight:1.0  },
  { key:'data_ready',   label:'Data Ready',   short:'Dat', color:'#818cf8', weight:0    },
];

const scColor = s => s >= 85 ? '#ff6b8a' : s >= 72 ? '#facc15' : s >= 58 ? '#34d399' : '#444';

//  STATUSES 
const STATUSES = [
  { val:'idea',        color:P.indigo, label:'Idea'        },
  { val:'in-progress', color:P.amber,  label:'In Progress' },
  { val:'built',       color:P.green,  label:'Built'       },
  { val:'published',   color:P.blue,   label:'Published'   },
];

//  STATE 
const activeFilters = { type:null, geo:null, fmt:null, status:null, notes:null, section:null };
let activeTopics = new Set();
let sortK = 'vscore', sortDir = 'desc';
let scFilters = {};
const PAGE = 60;
let filteredIdeas = [], renderedCount = 0, _renderPending = false;

//  CARD HTML 
function cardHTML(d, highlight=false) {
  const bars = SC_FIELDS.map(f => {
    const v = d.sc[f.key] || 0;
    return `<div class="br"><span class="bl">${f.short}</span><div class="bt"><div class="bf" style="width:${v}%;background:${f.color}"></div></div><span class="bv">${v}</span></div>`;
  }).join('');

  const st = STATUSES.find(s => s.val === (d.status||'idea')) || STATUSES[0];
  // Use first segment of compound sections (e.g. "Health - Foreign Commerce" -> "Health")
  const secDisplay = d.section ? d.section.split(/\s*[--]\s*/)[0].trim() : '';
  const secColor = getSectionColor(secDisplay);
  // Only show badge for canonical sections - hides catch-alls like "International Statistics"
  const showSecBadge = secDisplay && BADGE_SECTIONS.has(secDisplay);

  const statusOptions = STATUSES.map(s =>
    `<div class="st-opt${s.val===d.status?' active':''}" data-id="${d.id}" data-val="${s.val}">
      <span class="sdot" style="background:${s.color}"></span>${s.label}
    </div>`
  ).join('');

  const topicBadges = (d.topics||[]).map(t => {
    const c = TOPIC_COLORS[t] || '#888';
    return `<span class="topic-badge" style="background:${c}1a;color:${c};border:1px solid ${c}55">${t}</span>`;
  }).join('');

  const extList = (d.ext&&d.ext.length) ? d.ext.map(e => `<li>${e}</li>`).join('') : '';
  const notesHtml = d.notes
    ? `<div class="notes-edit" data-id="${d.id}" title="Click to edit"> ${d.notes}</div>`
    : `<button class="add-note-btn" data-id="${d.id}">+ Add note</button>`;

  return `<div class="card${highlight?' hi':''}" data-id="${d.id}" style="border-left-color:${showSecBadge ? secColor : 'var(--border)'};">
    <div class="card-main">
      <div class="card-header">
        <div class="status-wrap">
          <span class="status-dot" style="background:${st.color}" data-id="${d.id}" title="${st.label}"></span>
          <div class="status-menu" id="sm-${d.id}">${statusOptions}</div>
        </div>
        <div class="badge-row">
          ${showSecBadge ? `<span class="sect-badge" style="background:${secColor}1a;color:${secColor};border:1px solid ${secColor}55;cursor:pointer" onclick="filterBySection('${secDisplay.replace(/'/g,"\\'")}',this)">${secDisplay}</span>` : ''}
          ${topicBadges}
        </div>
      </div>
      <div class="ct">${d.title}</div>
      <div class="cs">${d.sub}</div>
      <div class="pills">
        <span class="pl ${d.type}">${d.type}</span>
        <span class="pl geo">${d.geo.replace(/_/g,' ')}</span>
        <span class="pl fmt">${d.fmt}</span>
      </div>
      <div class="data-block">
        <div class="data-label">DATA NEEDED</div>
        <div class="data-primary">${d.tbl}</div>
        ${extList?`<ul class="data-ext">${extList}</ul>`:''}
      </div>
      <div class="notes-area">${notesHtml}</div>
    </div>
    <div class="right">
      <div><div class="vs" style="color:${scColor(d.vs)}">${d.vs}</div><div class="vl">V-Score</div></div>
      <div class="brs">${bars}</div>
    </div>
  </div>`;
}

//  EVENT DELEGATION 
document.addEventListener('click', function(e) {
  if (!e.target.closest('.status-wrap'))
    document.querySelectorAll('.status-menu.open').forEach(m => m.classList.remove('open'));

  if (e.target.classList.contains('status-dot')) {
    const id = e.target.dataset.id;
    const menu = document.getElementById('sm-' + id);
    if (!menu) return;
    const was = menu.classList.contains('open');
    document.querySelectorAll('.status-menu.open').forEach(m => m.classList.remove('open'));
    if (!was) menu.classList.add('open');
    return;
  }
  if (e.target.classList.contains('st-opt') || e.target.closest('.st-opt')) {
    const opt = e.target.closest('.st-opt');
    const id = opt.dataset.id, val = opt.dataset.val;
    saveOverride(id, 'status', val);
    document.getElementById('sm-' + id)?.classList.remove('open');
    const card = document.querySelector(`.card[data-id="${id}"]`);
    if (card) {
      const st = STATUSES.find(s => s.val === val) || STATUSES[0];
      const dot = card.querySelector('.status-dot');
      if (dot) { dot.style.background = st.color; dot.title = st.label; }
      card.querySelectorAll('.st-opt').forEach(o => o.classList.toggle('active', o.dataset.val === val));
    }
    updateOverrideCount(); return;
  }
  if (e.target.classList.contains('add-note-btn') || e.target.closest('.add-note-btn')) {
    const btn = e.target.closest('.add-note-btn');
    openNotesEditor(btn.dataset.id, btn.closest('.notes-area'), ''); return;
  }
  if (e.target.classList.contains('notes-edit') || e.target.closest('.notes-edit')) {
    const el = e.target.closest('.notes-edit');
    openNotesEditor(el.dataset.id, el.closest('.notes-area'), el.textContent.replace(/^\s+/,'').trim()); return;
  }
});

function openNotesEditor(id, container, current) {
  container.innerHTML = `<div class="notes-editor">
    <textarea class="notes-ta" autofocus>${current}</textarea>
    <div class="notes-btns">
      <button class="nb-save" data-id="${id}">Save</button>
      <button class="nb-cancel" data-id="${id}">Cancel</button>
      ${current ? `<button class="nb-clear" data-id="${id}">Clear</button>` : ''}
    </div></div>`;
  const ta = container.querySelector('.notes-ta'); ta.focus();
  container.querySelector('.nb-save').onclick = () => {
    const val = ta.value.trim(); saveOverride(id, 'notes', val);
    container.innerHTML = val
      ? `<div class="notes-edit" data-id="${id}" title="Click to edit"> ${val}</div>`
      : `<button class="add-note-btn" data-id="${id}">+ Add note</button>`;
    updateOverrideCount();
  };
  container.querySelector('.nb-cancel').onclick = () => {
    const idea = D.find(d => d.id === id), notes = idea ? idea.notes : '';
    container.innerHTML = notes
      ? `<div class="notes-edit" data-id="${id}" title="Click to edit"> ${notes}</div>`
      : `<button class="add-note-btn" data-id="${id}">+ Add note</button>`;
  };
  const clr = container.querySelector('.nb-clear');
  if (clr) clr.onclick = () => {
    saveOverride(id, 'notes', '');
    container.innerHTML = `<button class="add-note-btn" data-id="${id}">+ Add note</button>`;
    updateOverrideCount();
  };
}

//  EXPORT 
function updateOverrideCount() {
  const n = Object.keys(loadOverrides()).length;
  const el = document.getElementById('override-count');
  if (el) el.textContent = n > 0 ? `${n} edited` : '';
}
function exportOverrides() {
  const ov = loadOverrides(), n = Object.keys(ov).length;
  if (!n) { alert('No edits yet.'); return; }
  let s = '# patch_overrides.py\nimport re\noverrides={\n';
  for (const [id, fields] of Object.entries(ov))
    s += `  "${id}":${JSON.stringify(fields)},\n`;
  s += '}\nwith open("data.js","r",encoding="utf-8") as f: content=f.read()\n';
  s += 'lines=content.split("\\n"); new_lines=[]; changed=0\n';
  s += 'for line in lines:\n';
  s += '    if not (line.startswith(",{id:") or line.startswith("{id:")): new_lines.append(line); continue\n';
  s += '    id_m=__import__("re").search(\'id:"([^"]+)"\',line)\n';
  s += '    if not id_m: new_lines.append(line); continue\n';
  s += '    id_=id_m.group(1)\n';
  s += '    if id_ in overrides:\n';
  s += '        ov=overrides[id_]\n';
  s += '        if "status" in ov: line=re.sub(r\',status:"[^"]*"\',\',status:"\'+ov["status"]+\'"\',line)\n';
  s += '        if "notes" in ov: line=re.sub(r\',notes:"[^"]*"\',\',notes:"\'+ov["notes"]+\'"\',line)\n';
  s += '        changed+=1\n    new_lines.append(line)\n';
  s += 'with open("data.js","w",encoding="utf-8") as f: f.write("\\n".join(new_lines))\n';
  s += 'print("Patched",changed,"ideas")\n';
  const blob = new Blob([s], {type:'text/plain'});
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'patch_overrides.py'; a.click();
}

//  FILTER + SORT 
function buildFiltered() {
  const q = (document.getElementById('q').value || '').toLowerCase();
  filteredIdeas = D.filter(d => {
    if (activeFilters.type   && d.type   !== activeFilters.type)   return false;
    if (activeFilters.geo    && d.geo    !== activeFilters.geo)     return false;
    if (activeFilters.fmt    && d.fmt    !== activeFilters.fmt)     return false;
    if (activeFilters.status && d.status !== activeFilters.status)  return false;
    if (activeFilters.section && !d.section?.includes(activeFilters.section)) return false;
    if (activeFilters.notes === 'has'  && !d.notes)  return false;
    if (activeFilters.notes === 'none' && d.notes)   return false;
    if (activeTopics.size > 0) {
      if (!(d.topics||[]).some(t => activeTopics.has(t))) return false;
    }
    for (const [key, range] of Object.entries(scFilters)) {
      const v = d.sc[key] || 0;
      if (v < range.min || v > range.max) return false;
    }
    if (q) {
      const h = (d.title+' '+d.sub+' '+d.tags+' '+d.section).toLowerCase();
      if (!h.includes(q)) return false;
    }
    return true;
  });

  filteredIdeas.sort((a, b) => {
    let av, bv;
    if (sortK === 'vscore')  { av = a.vs;           bv = b.vs; }
    else if (sortK === 'newest') { av = D.indexOf(a); bv = D.indexOf(b); }
    else if (sortK === 'oldest') { av = D.indexOf(a); bv = D.indexOf(b); }
    else { av = a.sc[sortK]||0; bv = b.sc[sortK]||0; }
    // newest = desc by index = larger index first
    if (sortK === 'newest') return bv - av;
    if (sortK === 'oldest') return av - bv;
    return sortDir === 'desc' ? bv - av : av - bv;
  });
}

//  VIRTUAL SCROLL 
function renderBrowse() {
  buildFiltered(); renderedCount = 0; _renderPending = false;
  document.getElementById('bgrid').innerHTML = '';
  renderMore(); updateCount();
}
function renderMore() {
  if (_renderPending || renderedCount >= filteredIdeas.length) return;
  _renderPending = true;
  requestAnimationFrame(() => {
    const batch = filteredIdeas.slice(renderedCount, renderedCount + PAGE);
    const frag = document.createDocumentFragment();
    batch.forEach(d => {
      const div = document.createElement('div');
      div.innerHTML = cardHTML(d);
      frag.appendChild(div.firstChild);
    });
    document.getElementById('bgrid').appendChild(frag);
    renderedCount += batch.length;
    _renderPending = false;
    updateCount();
  });
}
function updateCount() {
  const total = filteredIdeas.length, shown = Math.min(renderedCount, total);
  document.getElementById('bcnt').textContent =
    shown < total ? `Showing ${shown} of ${total} ideas - scroll for more` : `Showing ${total} of ${D.length} ideas`;
  if (!total) document.getElementById('bgrid').innerHTML = '<div class="empty">No match.</div>';
}

const sentinel = document.createElement('div'); sentinel.id = 'sentinel';
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('bgrid').after(sentinel);
  new IntersectionObserver(entries => { if (entries[0].isIntersecting) renderMore(); }, { rootMargin:'200px' }).observe(sentinel);
  updateOverrideCount();
  buildScFilters();
});

//  PILLS / SORT / TOPIC 
function togglePill(btn) {
  const field = btn.dataset.f, val = btn.dataset.v;
  if (activeFilters[field] === val) {
    activeFilters[field] = null; btn.classList.remove('on');
  } else {
    document.querySelectorAll(`.fp[data-f="${field}"]`).forEach(b => b.classList.remove('on'));
    activeFilters[field] = val; btn.classList.add('on');
  }
  updateResetBtn(); renderBrowse();
}
function updateResetBtn() {
  const hasFilter = Object.values(activeFilters).some(v => v) ||
    activeTopics.size > 0 || (document.getElementById('q')?.value||'').trim();
  const btn = document.getElementById('reset-btn');
  if (btn) btn.style.display = hasFilter ? 'inline-flex' : 'none';
}
function resetAllFilters() {
  Object.keys(activeFilters).forEach(k => activeFilters[k] = null);
  activeTopics.clear();
  document.querySelectorAll('.fp.on').forEach(b => b.classList.remove('on'));
  document.querySelectorAll('.sect-badge.sect-active').forEach(b => b.classList.remove('sect-active'));
  document.querySelectorAll('.fp.topic').forEach(btn => {
    const val = btn.dataset.v, c = TOPIC_COLORS[val];
    if (c) { btn.style.color=c; btn.style.borderColor=c+'55'; btn.style.background=c+'12'; }
  });
  document.getElementById('q').value = '';
  updateResetBtn(); renderBrowse();
}
function toggleTopic(btn) {
  const val = btn.dataset.v;
  const c = TOPIC_COLORS[val] || '#888';
  if (activeTopics.has(val)) {
    activeTopics.delete(val); btn.classList.remove('on');
    btn.style.color = c; btn.style.borderColor = c+'55'; btn.style.background = c+'12';
  } else {
    activeTopics.add(val); btn.classList.add('on');
    btn.style.background = c+'33'; btn.style.color = c; btn.style.borderColor = c;
  }
  updateResetBtn(); renderBrowse();
}
function filterBySection(sec, el) {
  if (activeFilters.section === sec) {
    activeFilters.section = null;
    document.querySelectorAll('.sect-badge.sect-active').forEach(b => b.classList.remove('sect-active'));
  } else {
    activeFilters.section = sec;
    document.querySelectorAll('.sect-badge.sect-active').forEach(b => b.classList.remove('sect-active'));
    if (el) el.classList.add('sect-active');
  }
  updateResetBtn(); renderBrowse();
}
function setSort(btnOrKey) {
  const key = (typeof btnOrKey === 'string') ? btnOrKey : btnOrKey.dataset.k;
  if (sortK === key) {
    sortDir = sortDir === 'desc' ? 'asc' : 'desc';
  } else {
    sortK = key; sortDir = 'desc';
  }
  document.querySelectorAll('.sb').forEach(b => b.classList.remove('on','asc','desc'));
  const active = document.querySelector(`.sb[data-k="${key}"]`);
  if (active) {
    active.classList.add('on');
    active.classList.add(sortDir); // explicit separate add so both land
  }
  renderBrowse();
}
function setMode(m, btn) {
  document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('on')); btn.classList.add('on');
  document.querySelectorAll('.pane').forEach(p => p.classList.remove('on'));
  document.getElementById('pane-' + m).classList.add('on');
  if (m === 'correlate') buildVarSelect();
  if (m === 'format') buildFormatGrid();
  if (m === 'score-filters') buildScFilters();
}

//  SUB-SCORE RANGE FILTERS 
function buildScFilters() {
  const container = document.getElementById('sc-filter-grid');
  if (!container || container.dataset.built) return;
  container.dataset.built = '1';
  SC_FIELDS.forEach(f => {
    const div = document.createElement('div'); div.className = 'scf';
    div.innerHTML = `
      <div class="scf-label" style="color:${f.color}">${f.label} <span style="color:#555;font-weight:400;font-size:9px">(weight ${f.weight}x)</span></div>
      <div class="scf-row">
        <span class="scf-val" id="scf-min-${f.key}">0</span>
        <input type="range" min="0" max="100" value="0"   step="5" class="scf-range" id="scf-rmin-${f.key}" data-key="${f.key}" data-bound="min">
        <input type="range" min="0" max="100" value="100" step="5" class="scf-range" id="scf-rmax-${f.key}" data-key="${f.key}" data-bound="max">
        <span class="scf-val" id="scf-max-${f.key}">100</span>
      </div>
      <div class="scf-hint" id="scf-cnt-${f.key}"></div>`;
    container.appendChild(div);
    div.querySelectorAll('.scf-range').forEach(r => r.addEventListener('input', () => updateScFilter(f.key)));
  });
}
function updateScFilter(key) {
  const minEl = document.getElementById(`scf-rmin-${key}`);
  const maxEl = document.getElementById(`scf-rmax-${key}`);
  let min = parseInt(minEl.value), max = parseInt(maxEl.value);
  if (min > max) { min = max; minEl.value = min; }
  document.getElementById(`scf-min-${key}`).textContent = min;
  document.getElementById(`scf-max-${key}`).textContent = max;
  if (min === 0 && max === 100) delete scFilters[key];
  else scFilters[key] = { min, max };
  const cnt = D.filter(d => (d.sc[key]||0) >= min && (d.sc[key]||0) <= max).length;
  document.getElementById(`scf-cnt-${key}`).textContent = `${cnt.toLocaleString()} ideas match`;
  buildFiltered();
  // Render into score-filter pane's own grid
  const sfGrid = document.getElementById('sf-grid');
  const sfCnt  = document.getElementById('sf-cnt');
  if (sfGrid) {
    sfGrid.innerHTML = filteredIdeas.map(d => cardHTML(d)).join('');
    if (sfCnt) sfCnt.textContent = `${filteredIdeas.length} of ${D.length} ideas`;
  }
}
function clearScFilters() {
  scFilters = {};
  document.querySelectorAll('.scf-range').forEach(r => {
    r.value = r.dataset.bound === 'min' ? 0 : 100;
  });
  SC_FIELDS.forEach(f => {
    document.getElementById(`scf-min-${f.key}`).textContent = '0';
    document.getElementById(`scf-max-${f.key}`).textContent = '100';
    document.getElementById(`scf-cnt-${f.key}`).textContent = '';
  });
  renderBrowse();
}

//  CORRELATE 
function buildVarSelect() {
  const sel = document.getElementById('varsel');
  if (sel.options.length > 1) return;
  Object.keys(VAR_LABELS).sort((a,b) => VAR_LABELS[a].localeCompare(VAR_LABELS[b])).forEach(v => {
    const o = document.createElement('option'); o.value = v; o.textContent = VAR_LABELS[v]; sel.appendChild(o);
  });
}
function renderCorr() {
  const v = document.getElementById('varsel').value;
  if (!v) { document.getElementById('cgrid').innerHTML = ''; document.getElementById('ccnt').textContent = ''; return; }
  const pIds = new Set((VAR_INDEX[v]||[]).filter(x => x.primary).map(x => x.id));
  const jIds = new Set((VAR_INDEX[v]||[]).filter(x => !x.primary).map(x => x.id));
  const all = new Set([...pIds, ...jIds]);
  document.getElementById('corr-hint').textContent = `${all.size} ideas connect to "${VAR_LABELS[v]}". Blue border = uses this variable directly.`;
  const sorted = D.filter(d => all.has(d.id)).sort((a,b) => {
    const ap = pIds.has(a.id)?1:0, bp = pIds.has(b.id)?1:0;
    if (ap !== bp) return bp - ap; return b.vs - a.vs;
  });
  document.getElementById('ccnt').textContent = `${sorted.length} idea${sorted.length!==1?'s':''} relate`;
  document.getElementById('cgrid').innerHTML = sorted.length
    ? sorted.map(d => cardHTML(d, pIds.has(d.id))).join('')
    : '<div class="empty">No ideas indexed for this variable.</div>';
}

//  FORMAT 
let selFmt = null;
function buildFormatGrid() {
  const fg = document.getElementById('fgrid');
  if (fg.children.length) return;
  Object.entries(FMT_MAP).sort((a,b) => b[1].length - a[1].length).forEach(([k, items]) => {
    const btn = document.createElement('button'); btn.className = 'fb';
    btn.innerHTML = `<div>${k}</div><div class="fct">${items.length} ideas</div>`;
    btn.onclick = () => toggleFmt(k, btn); fg.appendChild(btn);
  });
}
function toggleFmt(k, btn) {
  if (selFmt === k) {
    selFmt = null;
    document.querySelectorAll('.fb').forEach(b => b.classList.remove('on'));
    document.getElementById('fgridout').innerHTML = '';
    document.getElementById('fcnt').textContent = '';
  } else {
    selFmt = k;
    document.querySelectorAll('.fb').forEach(b => b.classList.remove('on'));
    btn.classList.add('on');
    const items = (FMT_MAP[k]||[]).sort((a,b) => b.vs - a.vs);
    document.getElementById('fcnt').textContent = `${items.length} ideas`;
    document.getElementById('fgridout').innerHTML = items.map(d => cardHTML(d)).join('');
  }
}

//  INIT 
(function initTopicPills() {
  document.querySelectorAll('.fp.topic').forEach(btn => {
    const val = btn.dataset.v;
    const c = TOPIC_COLORS[val];
    if (c) {
      btn.style.color = c;
      btn.style.borderColor = c + '55';
      btn.style.background = c + '12';
    }
  });
})();

renderBrowse();
