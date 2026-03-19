// app.js - Mapzimus board logic v6 - inline editing + localStorage overrides

const VAR_LABELS = {
  rep_pct:"Republican vote % by state", median_household_income:"Median household income by state",
  pct_under_25k:"% households under $25K by state", pct_over_200k:"% households over $200K by state",
  state_gdp_per_capita:"State GDP per capita", violent_crime_rate:"Violent crime rate by state",
  murder_rate:"Murder rate by state", pct_bachelors:"% with bachelor's degree by state",
  pct_hs_grad:"% HS graduates by state", expenditure_per_pupil:"Per-pupil school spending",
  avg_teacher_salary:"Avg teacher salary by state", state_unemployment_rate:"Unemployment rate by state",
  female_lfp_rate:"Female labor force participation by state",
  total_transfers_per_capita:"Govt transfers per capita by state",
  pct_on_snap:"% households on SNAP", pct_on_medicaid:"% households on Medicaid",
  birth_rate_state:"Birth rate by state", teen_birth_rate:"Teen birth rate by state",
  pct_births_unmarried:"% births to unmarried mothers by state",
  total_medicare:"Medicare enrollment by state", per_capita_health_spending:"Health expenditure per capita",
  all_items_cpi:"All-items CPI", gasoline_cpi:"Gasoline CPI", housing_cpi:"Housing CPI",
  home_price_index_2024:"Home price index 2024 by state",
  home_price_pct_change_2005_2024:"Home price % change 2005-2024",
  student_loans_outstanding:"Student loan debt outstanding", mortgage_delinquency_rate:"Mortgage delinquency rate",
  housing_permits_total:"New housing permits by state", population_pct_change:"Population % change by state",
  net_migration_rate:"Net migration rate by country", birth_rate:"Birth rate by country",
  trade_balance_goods:"Trade balance on goods by country", rd_pct_gdp:"R&D spending as % of GDP",
  pct_forest:"% land that is forest by state", national_forest_acres:"National Forest acres by state",
  energy_consumption_per_capita:"Energy consumption per capita by state",
  renewable_energy_share:"Renewable energy share by state", coal_consumption:"Coal consumption by state",
  coal_production_index:"Coal production index", oil_gas_extraction_index:"Oil/gas extraction index",
  avg_farm_size:"Average farm size by state", farm_net_income_state:"Net farm income by state",
  manufacturing_employment_trend:"Manufacturing employment 2000-2024",
  manufacturing_hourly_wages_state:"Manufacturing hourly wages by state",
  manufacturing_value_added_state:"Manufacturing value added by state",
  us_troops_overseas:"US troops stationed overseas", defense_budget_total:"Total US defense budget",
  lottery_revenue_per_capita:"State lottery revenue per capita",
  state_local_revenue_per_capita:"State/local govt revenue per capita",
  state_local_debt_per_capita:"State/local govt debt per capita",
  federal_outlays_by_function:"Federal budget outlays by function",
  mean_elevation:"Mean elevation by state", coastline_miles:"Coastline miles by state",
  pct_bridges_poor:"% bridges in poor condition", waterway_freight_tons:"Waterway freight tonnage",
  passengers_enplaned:"Passengers enplaned by airport",
  incarceration_rate:"Incarceration rate by state/county",
  avg_commute_time:"Average commute time by county", broadband_access_pct:"Broadband access rate",
  language_diversity_index:"Language diversity index", rural_population_pct:"Rural population %",
  dollar_general_density:"Dollar General stores per 10K", grocery_distance:"Drive time to nearest grocery",
  church_count:"Churches per 10K residents", irs_net_migration_households:"IRS net migration households",
  uninsured_rate:"Uninsured rate by state", mean_age_first_birth:"Mean age at first birth",
  flood_zone_uninsured_pct:"FEMA flood zone uninsured %",
  population_pct_change_2020_2025:"Population % change by country 2020-2025",
  population_per_sq_km:"Population density per km2", current_account_balance:"Current account balance",
  foreign_exchange_reserves:"Foreign exchange reserves by country",
};

//  OVERRIDES: localStorage persistence 
// Structure: { [ideaId]: { status: '...', notes: '...' } }
const LS_KEY = 'mapzimus_overrides';

function loadOverrides() {
  try { return JSON.parse(localStorage.getItem(LS_KEY) || '{}'); } catch { return {}; }
}

function saveOverride(id, field, value) {
  const ov = loadOverrides();
  if (!ov[id]) ov[id] = {};
  ov[id][field] = value;
  localStorage.setItem(LS_KEY, JSON.stringify(ov));
  // Also update live D array so filters/sorts reflect changes instantly
  const idea = D.find(d => d.id === id);
  if (idea) idea[field] = value;
}

// Merge overrides into D on startup
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
  const all = [...(d.vars || []), ...(d.join || [])];
  all.forEach(v => {
    if (!VAR_INDEX[v]) VAR_INDEX[v] = [];
    if (!VAR_INDEX[v].find(x => x.id === d.id))
      VAR_INDEX[v].push({ id: d.id, primary: !!(d.vars && d.vars.includes(v)) });
  });
});

const FMT_MAP = {};
D.forEach(d => {
  if (!FMT_MAP[d.fmt]) FMT_MAP[d.fmt] = [];
  FMT_MAP[d.fmt].push(d);
});

//  STATE 
const activeFilters = { type: null, geo: null, fmt: null, status: null, notes: null };
let activeTopics = new Set(); // multi-select, OR logic
let sortK = 'vscore', selFmt = null;
const PAGE = 100;
let filteredIdeas = [], renderedCount = 0;

//  CONSTANTS 
const FC = {
  emotional:'#ef4444', relatability:'#3b82f6', clarity:'#f97316',
  surprise:'#f59e0b', tension:'#dc2626', visual:'#22c55e',
  data_ready:'#a855f7', originality:'#14b8a6'
};
const FL = { emotional:'Emo', relatability:'Rel', clarity:'Cla', surprise:'Sur', tension:'Ten', visual:'Vis', data_ready:'Dat', originality:'Ori' };
const scColor = s => s >= 90 ? '#ef4444' : s >= 83 ? '#f59e0b' : s >= 76 ? '#22c55e' : '#6b7280';

const STATUSES = [
  { val: 'idea',        color: '#6b7280', emoji: '', label: 'Idea' },
  { val: 'in-progress', color: '#f59e0b', emoji: '', label: 'In Progress' },
  { val: 'built',       color: '#22c55e', emoji: '', label: 'Built' },
  { val: 'published',   color: '#3b82f6', emoji: '', label: 'Published' },
];

const SECTION_COLORS = {
  'Health':'#ef4444','Elections':'#3b82f6','Income':'#22c55e','Housing':'#f59e0b',
  'Labor Force':'#a855f7','Law Enforcement':'#dc2626','Education':'#14b8a6',
  'Energy':'#f97316','Agriculture':'#84cc16','Transportation':'#06b6d4',
  'Population':'#ec4899','National Security':'#6366f1','International Statistics':'#8b5cf6',
  'Geography':'#10b981','Banking':'#f59e0b','Information':'#0ea5e9',
  'State Government':'#64748b','Federal Government':'#475569',
};

//  CARD HTML 
function cardHTML(d, highlight = false) {
  const bars = Object.entries(FL).map(([k, l]) =>
    `<div class="br"><span class="bl">${l}</span><div class="bt"><div class="bf" style="width:${(d.sc[k]||0)*10}%;background:${FC[k]}"></div></div></div>`
  ).join('');

  const st = STATUSES.find(s => s.val === (d.status || 'idea')) || STATUSES[0];
  const secColor = SECTION_COLORS[d.section] || '#6b7280';

  // Status dropdown options
  const statusOptions = STATUSES.map(s =>
    `<div class="st-opt${s.val === d.status ? ' active' : ''}" data-id="${d.id}" data-val="${s.val}">
      <span style="color:${s.color}">${s.emoji}</span> ${s.label}
    </div>`
  ).join('');

  // Ext list
  const extList = (d.ext && d.ext.length) ? d.ext.map(e => `<li>${e}</li>`).join('') : '';

  // Notes display
  const notesHtml = d.notes
    ? `<div class="notes-edit" data-id="${d.id}" title="Click to edit note"> ${d.notes}</div>`
    : `<button class="add-note-btn" data-id="${d.id}"> Add note</button>`;

  return `<div class="card${highlight ? ' hi' : ''}" data-id="${d.id}">
    <div class="card-main">
      <div class="card-header">
        <div class="status-wrap">
          <span class="status-dot" style="background:${st.color}" data-id="${d.id}" title="Click to change status - ${st.label}"></span>
          <div class="status-menu" id="sm-${d.id}">
            ${statusOptions}
          </div>
        </div>
        <span class="sect-badge" style="background:${secColor}22;color:${secColor};border:1px solid ${secColor}44">${d.section}</span>
      </div>
      <div class="ct">${d.title}</div>
      <div class="cs">${d.sub}</div>
      <div class="pills">
        <span class="pl ${d.type}">${d.type}</span>
        <span class="pl geo">${d.geo.replace(/_/g,' ')}</span>
        <span class="pl fmt">${d.fmt}</span>
      </div>
      <div class="data-block">
        <div class="data-label"> DATA NEEDED</div>
        <div class="data-primary">${d.tbl}</div>
        ${extList ? `<ul class="data-ext">${extList}</ul>` : ''}
      </div>
      <div class="notes-area">${notesHtml}</div>
    </div>
    <div class="right">
      <div><div class="vs" style="color:${scColor(d.vs)}">${d.vs}</div><div class="vl">V-Score</div></div>
      <div class="brs">${bars}</div>
    </div>
  </div>`;
}

//  EVENT DELEGATION for inline editing 
document.addEventListener('click', function(e) {
  // Close any open status menus if clicking outside
  if (!e.target.closest('.status-wrap')) {
    document.querySelectorAll('.status-menu.open').forEach(m => m.classList.remove('open'));
  }

  // Status dot clicked -> toggle menu
  if (e.target.classList.contains('status-dot')) {
    const id = e.target.dataset.id;
    const menu = document.getElementById('sm-' + id);
    if (!menu) return;
    const wasOpen = menu.classList.contains('open');
    document.querySelectorAll('.status-menu.open').forEach(m => m.classList.remove('open'));
    if (!wasOpen) menu.classList.add('open');
    return;
  }

  // Status option selected
  if (e.target.classList.contains('st-opt') || e.target.closest('.st-opt')) {
    const opt = e.target.closest('.st-opt');
    const id  = opt.dataset.id;
    const val = opt.dataset.val;
    saveOverride(id, 'status', val);
    // Close menu
    const menu = document.getElementById('sm-' + id);
    if (menu) menu.classList.remove('open');
    // Update dot color in place
    const card = document.querySelector(`.card[data-id="${id}"]`);
    if (card) {
      const st = STATUSES.find(s => s.val === val) || STATUSES[0];
      const dot = card.querySelector('.status-dot');
      if (dot) { dot.style.background = st.color; dot.title = 'Click to change status - ' + st.label; }
      // Update active state in menu options
      card.querySelectorAll('.st-opt').forEach(o => o.classList.toggle('active', o.dataset.val === val));
    }
    updateOverrideCount();
    return;
  }

  // "Add note" button clicked
  if (e.target.classList.contains('add-note-btn') || e.target.closest('.add-note-btn')) {
    const btn = e.target.closest('.add-note-btn');
    const id  = btn.dataset.id;
    openNotesEditor(id, btn.closest('.notes-area'), '');
    return;
  }

  // Existing note clicked to edit
  if (e.target.classList.contains('notes-edit') || e.target.closest('.notes-edit')) {
    const el  = e.target.closest('.notes-edit');
    const id  = el.dataset.id;
    const cur = el.textContent.replace(' ', '').trim();
    openNotesEditor(id, el.closest('.notes-area'), cur);
    return;
  }
});

function openNotesEditor(id, container, current) {
  container.innerHTML = `
    <div class="notes-editor">
      <textarea class="notes-ta" placeholder="Add a note about this idea..." autofocus>${current}</textarea>
      <div class="notes-btns">
        <button class="nb-save" data-id="${id}">Save</button>
        <button class="nb-cancel" data-id="${id}">Cancel</button>
        ${current ? `<button class="nb-clear" data-id="${id}">Clear</button>` : ''}
      </div>
    </div>`;
  const ta = container.querySelector('.notes-ta');
  ta.focus();
  ta.setSelectionRange(ta.value.length, ta.value.length);

  container.querySelector('.nb-save').onclick = () => {
    const val = ta.value.trim();
    saveOverride(id, 'notes', val);
    container.innerHTML = val
      ? `<div class="notes-edit" data-id="${id}" title="Click to edit note"> ${val}</div>`
      : `<button class="add-note-btn" data-id="${id}"> Add note</button>`;
    updateOverrideCount();
  };
  container.querySelector('.nb-cancel').onclick = () => {
    const idea = D.find(d => d.id === id);
    const notes = idea ? idea.notes : '';
    container.innerHTML = notes
      ? `<div class="notes-edit" data-id="${id}" title="Click to edit note"> ${notes}</div>`
      : `<button class="add-note-btn" data-id="${id}"> Add note</button>`;
  };
  const clrBtn = container.querySelector('.nb-clear');
  if (clrBtn) clrBtn.onclick = () => {
    saveOverride(id, 'notes', '');
    container.innerHTML = `<button class="add-note-btn" data-id="${id}"> Add note</button>`;
    updateOverrideCount();
  };
}

//  EXPORT OVERRIDES 
function updateOverrideCount() {
  const ov = loadOverrides();
  const n  = Object.keys(ov).length;
  const el = document.getElementById('override-count');
  if (el) el.textContent = n > 0 ? `${n} edited` : '';
}

function exportOverrides() {
  const ov = loadOverrides();
  const n  = Object.keys(ov).length;
  if (!n) { alert('No edits to export yet.'); return; }

  // Build Python patch script
  let script = '"""patch_overrides.py - Apply browser edits to data.js"""\n';
  script += 'import re\n\n';
  script += 'overrides = {\n';
  for (const [id, fields] of Object.entries(ov)) {
    script += `  "${id}": ${JSON.stringify(fields)},\n`;
  }
  script += '}\n\n';
  script += 'with open("data.js","r",encoding="utf-8") as f: content=f.read()\n';
  script += 'lines=content.split("\\n"); new_lines=[]; changed=0\n';
  script += 'for line in lines:\n';
  script += '    if not (line.startswith(",{id:") or line.startswith("{id:")): new_lines.append(line); continue\n';
  script += '    id_m=re.search(\'id:"([^"]+)"\',line)\n';
  script += '    if not id_m: new_lines.append(line); continue\n';
  script += '    id_=id_m.group(1)\n';
  script += '    if id_ in overrides:\n';
  script += '        ov=overrides[id_]\n';
  script += '        if "status" in ov: line=re.sub(r\',status:"[^"]*"\',\',status:"\'+ov["status"]+\'"\',line)\n';
  script += '        if "notes"  in ov: line=re.sub(r\',notes:"[^"]*"\', \',notes:"\' +ov["notes"] +\'"\',line)\n';
  script += '        changed+=1\n';
  script += '    new_lines.append(line)\n';
  script += 'with open("data.js","w",encoding="utf-8") as f: f.write("\\n".join(new_lines))\n';
  script += 'print("Patched",changed,"ideas")\n';

  // Download as file directly - no clipboard needed
  const blob = new Blob([script], {type:'text/plain'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'patch_overrides.py';
  a.click();
  setTimeout(() => {
    alert(` patch_overrides.py downloaded!\n\nIn PowerShell:\n\n  cd D:\\projects\\mapzimus-board\n  Move-Item $env:USERPROFILE\\Downloads\\patch_overrides.py .\n  python patch_overrides.py\n  python maintain.py\n  git add .\n  git commit -m "Apply status updates"\n  git push`);
  }, 500);
  // unused then block below for compat
  Promise.resolve().then(() => {
    alert(` ${n} overrides copied!\n\nIn PowerShell:\n\n  cd D:\\projects\\mapzimus-board\n  # paste into patch_overrides.py, then:\n  python patch_overrides.py\n  python maintain.py\n  git add .\n  git commit -m "Apply status updates"\n  git push\n\n(PowerShell uses separate lines, not &&)`);
  }).catch(() => {
    const win = window.open('', '_blank', 'width=700,height=560');
    win.document.write('<pre style="background:#111;color:#eee;padding:16px;font-size:12px;white-space:pre-wrap">SAVE AS: D:\\projects\\mapzimus-board\\patch_overrides.py\n\nTHEN RUN IN POWERSHELL:\n  cd D:\\projects\\mapzimus-board\n  python patch_overrides.py\n  python maintain.py\n  git add .\n  git commit -m \"Apply status updates\"\n  git push\n\n---\n\n' + script.replace(/</g,'&lt;') + '</pre>');
  });
}

//  FILTER + SORT 
function buildFiltered() {
  const q = (document.getElementById('q').value || '').toLowerCase();
  filteredIdeas = D.filter(d => {
    if (activeFilters.type   && d.type   !== activeFilters.type)   return false;
    if (activeFilters.geo    && d.geo    !== activeFilters.geo)     return false;
    if (activeFilters.fmt    && d.fmt    !== activeFilters.fmt)     return false;
    if (activeFilters.status && d.status !== activeFilters.status)  return false;
    if (activeFilters.notes === 'has'  && !d.notes) return false;
    if (activeFilters.notes === 'none' && d.notes)  return false;
    if (activeTopics.size > 0) {
      const dTopics = d.topics || [];
      if (!dTopics.some(t => activeTopics.has(t))) return false;
    }
    if (q) {
      const h = (d.title+' '+d.sub+' '+d.tags+' '+d.section).toLowerCase();
      if (!h.includes(q)) return false;
    }
    return true;
  });
  if (sortK === 'newest') {
    filteredIdeas.sort((a, b) => D.indexOf(b) - D.indexOf(a));
  } else if (sortK === 'oldest') {
    filteredIdeas.sort((a, b) => D.indexOf(a) - D.indexOf(b));
  } else {
    filteredIdeas.sort((a, b) => {
      const av = sortK === 'vscore' ? a.vs : (a.sc[sortK] || 0);
      const bv = sortK === 'vscore' ? b.vs : (b.sc[sortK] || 0);
      return bv - av;
    });
  }
}

//  VIRTUAL SCROLL 
function renderBrowse() {
  buildFiltered();
  renderedCount = 0;
  document.getElementById('bgrid').innerHTML = '';
  renderMore();
  updateCount();
}

function renderMore() {
  if (renderedCount >= filteredIdeas.length) return;
  const batch = filteredIdeas.slice(renderedCount, renderedCount + PAGE);
  const frag  = document.createDocumentFragment();
  batch.forEach(d => {
    const div = document.createElement('div');
    div.innerHTML = cardHTML(d);
    frag.appendChild(div.firstChild);
  });
  document.getElementById('bgrid').appendChild(frag);
  renderedCount += batch.length;
  updateCount();
}

function updateCount() {
  const total = filteredIdeas.length;
  const shown = Math.min(renderedCount, total);
  document.getElementById('bcnt').textContent =
    shown < total ? `Showing ${shown} of ${total} ideas - scroll for more` : `Showing ${total} of ${D.length} ideas`;
  if (!total) document.getElementById('bgrid').innerHTML = '<div class="empty">No match - try a different keyword or clear a filter.</div>';
}

const sentinel = document.createElement('div');
sentinel.id = 'sentinel';
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('bgrid').after(sentinel);
  new IntersectionObserver(entries => { if (entries[0].isIntersecting) renderMore(); }, { rootMargin: '200px' }).observe(sentinel);
  updateOverrideCount();
});

//  PILL + SORT 
function togglePill(btn) {
  const field = btn.dataset.f, val = btn.dataset.v;
  if (activeFilters[field] === val) { activeFilters[field] = null; btn.classList.remove('on'); }
  else { document.querySelectorAll(`.fp[data-f="${field}"]`).forEach(b=>b.classList.remove('on')); activeFilters[field]=val; btn.classList.add('on'); }
  renderBrowse();
}

function toggleTopic(btn) {
  const val = btn.dataset.v;
  if (activeTopics.has(val)) {
    activeTopics.delete(val);
    btn.classList.remove('on');
  } else {
    activeTopics.add(val);
    btn.classList.add('on');
  }
  renderBrowse();
}
function setSort(btn) {
  sortK = btn.dataset.k;
  document.querySelectorAll('.sb').forEach(b=>b.classList.remove('on'));
  btn.classList.add('on');
  renderBrowse();
}
function setMode(m,btn) {
  document.querySelectorAll('.mode-btn').forEach(b=>b.classList.remove('on')); btn.classList.add('on');
  document.querySelectorAll('.pane').forEach(p=>p.classList.remove('on'));
  document.getElementById('pane-'+m).classList.add('on');
  if(m==='correlate') buildVarSelect();
  if(m==='format') buildFormatGrid();
}

//  CORRELATE 
function buildVarSelect() {
  const sel=document.getElementById('varsel');
  if(sel.options.length>1) return;
  Object.keys(VAR_LABELS).sort((a,b)=>VAR_LABELS[a].localeCompare(VAR_LABELS[b])).forEach(v=>{
    const o=document.createElement('option'); o.value=v; o.textContent=VAR_LABELS[v]; sel.appendChild(o);
  });
}
function renderCorr() {
  const v=document.getElementById('varsel').value;
  if(!v){document.getElementById('cgrid').innerHTML='';document.getElementById('ccnt').textContent='';return;}
  const pIds=new Set((VAR_INDEX[v]||[]).filter(x=>x.primary).map(x=>x.id));
  const jIds=new Set((VAR_INDEX[v]||[]).filter(x=>!x.primary).map(x=>x.id));
  const all=new Set([...pIds,...jIds]);
  document.getElementById('corr-hint').textContent=`${all.size} ideas connect to "${VAR_LABELS[v]}". Blue border = uses this variable directly.`;
  const sorted=D.filter(d=>all.has(d.id)).sort((a,b)=>{const ap=pIds.has(a.id)?1:0,bp=pIds.has(b.id)?1:0;if(ap!==bp)return bp-ap;return b.vs-a.vs;});
  document.getElementById('ccnt').textContent=`${sorted.length} idea${sorted.length!==1?'s':''} relate to this variable`;
  document.getElementById('cgrid').innerHTML=sorted.length?sorted.map(d=>cardHTML(d,pIds.has(d.id))).join(''):'<div class="empty">No ideas indexed for this variable yet.</div>';
}

//  FORMAT 
function buildFormatGrid() {
  const fg=document.getElementById('fgrid');
  if(fg.children.length) return;
  Object.entries(FMT_MAP).sort((a,b)=>b[1].length-a[1].length).forEach(([k,items])=>{
    const btn=document.createElement('button'); btn.className='fb';
    btn.innerHTML=`<div>${k}</div><div class="fct">${items.length} idea${items.length!==1?'s':''}</div>`;
    btn.onclick=()=>toggleFmt(k,btn); fg.appendChild(btn);
  });
}
function toggleFmt(k,btn) {
  if(selFmt===k){selFmt=null;document.querySelectorAll('.fb').forEach(b=>b.classList.remove('on'));document.getElementById('fgridout').innerHTML='';document.getElementById('fcnt').textContent='';}
  else{selFmt=k;document.querySelectorAll('.fb').forEach(b=>b.classList.remove('on'));btn.classList.add('on');const items=(FMT_MAP[k]||[]).sort((a,b)=>b.vs-a.vs);document.getElementById('fcnt').textContent=`${items.length} idea${items.length!==1?'s':''} in this format`;document.getElementById('fgridout').innerHTML=items.map(d=>cardHTML(d)).join('');}
}

//  INIT 
renderBrowse();
