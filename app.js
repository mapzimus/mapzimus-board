// app.js - Mapzimus board logic v4 - virtual scroll + status + clarity

const VAR_LABELS = {
  rep_pct:"Republican vote % by state (T454)", dem_pct:"Democratic vote % by state (T454)",
  margin:"Vote margin by state (T454)", pct_voted_state:"Voter turnout % by state (T449)",
  pct_registered_state:"Voter registration % by state (T449)",
  median_household_income:"Median household income by state (T727)",
  pct_under_25k:"% households under $25K by state (T727)",
  pct_over_200k:"% households over $200K by state (T727)",
  real_per_capita_income:"Real per capita income by state (T723)",
  disposable_income_per_capita:"Disposable income per capita by state (T725)",
  state_gdp_per_capita:"State GDP per capita (T715)",
  violent_crime_rate:"Violent crime rate by state (T340)", murder_rate:"Murder rate by state (T340)",
  property_crime_rate:"Property crime rate by state (T340)",
  pct_bachelors:"% with bachelor's degree by state (T254)", pct_hs_grad:"% HS graduates by state (T254)",
  expenditure_per_pupil:"Per-pupil school spending (T258)", avg_teacher_salary:"Avg teacher salary by state (T268)",
  teacher_count:"Teacher count by state (T268)", revenue_federal_pct:"% school revenue from federal (T258)",
  revenue_local_pct:"% school revenue from local taxes (T258)",
  district_enrollment:"District enrollment - top 50 (T261)",
  state_unemployment_rate:"Unemployment rate by state (T629)",
  female_lfp_rate:"Female labor force participation by state (T629)",
  total_transfers_per_capita:"Govt transfers per capita by state (T573)",
  veterans_benefits:"Veterans benefits by state (T573)", pct_on_snap:"% households on SNAP (T576)",
  pct_on_medicaid:"% households on Medicaid (T576)",
  birth_rate_state:"Birth rate by state (T81)", teen_birth_rate:"Teen birth rate by state (T86)",
  pct_births_unmarried:"% births to unmarried mothers by state (T87)",
  total_medicare:"Medicare enrollment by state (T150)",
  per_capita_health_spending:"Health expenditure per capita (T141)",
  all_items_cpi:"All-items CPI 2000-2024 (T770)",
  gasoline_cpi:"Gasoline CPI (T770)", housing_cpi:"Housing CPI (T770)",
  gasoline_price_regular:"Regular gasoline price by city (T773)",
  home_price_index_2024:"Home price index 2024 by state (T771)",
  home_price_pct_change_2005_2024:"Home price % change 2005-2024 by state (T771)",
  student_loans_outstanding:"Student loan debt outstanding (T1222)",
  mortgage_delinquency_rate:"Mortgage delinquency rate (T1225)",
  housing_permits_total:"New housing permits by state (T1011)",
  population_pct_change:"Population % change by state (Population PDF)",
  net_migration_rate:"Net migration rate by country (T1360)",
  population_pct_change_2020_2025:"Population % change by country 2020-2025",
  population_per_sq_km:"Population density per km2 by country",
  birth_rate:"Birth rate by country", trade_balance_goods:"Trade balance on goods by country (T1310)",
  current_account_balance:"Current account balance total (T1306)",
  rd_pct_gdp:"R&D spending as % of GDP by country (T842)",
  pct_forest:"% land that is forest by state (T413)",
  national_forest_acres:"National Forest acres by state (T932)",
  energy_consumption_per_capita:"Energy consumption per capita by state (T975)",
  renewable_energy_share:"Renewable energy share by state (T976)",
  coal_consumption:"Coal consumption by state (T976)",
  coal_production_index:"Coal production index 1990-2024 (T950)",
  oil_gas_extraction_index:"Oil/gas extraction index (T950)",
  avg_farm_size:"Average farm size by state (T869)",
  farm_net_income_state:"Net farm income by state (T869)",
  farmland_value_state:"Farmland value by state (T869)",
  manufacturing_employment_trend:"Manufacturing employment 2000-2024 (T1064)",
  manufacturing_hourly_wages_state:"Manufacturing hourly wages by state (T1067)",
  manufacturing_value_added_state:"Manufacturing value added by state (T1062)",
  us_troops_overseas:"US troops stationed overseas by country (T549)",
  defense_budget_total:"Total US defense budget (T543)",
  lottery_revenue_per_capita:"State lottery revenue per capita (T493)",
  sports_betting_revenue:"Sports betting tax revenue by state (T493)",
  state_local_revenue_per_capita:"State and local govt revenue per capita (T488)",
  state_local_expenditure_per_capita:"State and local govt expenditures per capita (T488)",
  state_local_debt_per_capita:"State and local govt debt per capita (T486)",
  state_income_tax_revenue:"State individual income tax revenue (T497)",
  federal_outlays_by_function:"Federal budget outlays by function (T512)",
  total_transfers_per_capita:"Govt transfers per capita by state (T573)",
  mean_elevation:"Mean elevation by state (T410)",
  coastline_miles:"Coastline miles by state (T408)",
  pct_bridges_poor:"% bridges in poor condition by state (T1126)",
  total_bridges:"Total bridges by state (T1126)",
  port_total_tons:"Port tonnage - total (T1122)",
  waterway_freight_tons:"Waterway freight tonnage (T1120)",
  passengers_enplaned:"Passengers enplaned by airport (T1112)",
  sports_attendance_12mo:"Sports event attendance last 12 months (T1273)",
  annual_attendance:"Theme park annual attendance (T1271)",
  newspaper_total_revenue:"Newspaper total revenue (T1174)",
  gross_arts_output:"Arts and cultural production gross output (T1257)",
  gig_transport_receipts:"Gig/nonemployer transport receipts (T1103)",
  incarceration_rate:"Incarceration rate by state/county",
  avg_commute_time:"Average commute time in minutes by county (ACS)",
  broadband_access_pct:"Broadband access rate by county (FCC)",
  language_diversity_index:"Language diversity index by county (ACS)",
  rural_population_pct:"Rural population % by county (ACS)",
  dollar_general_density:"Dollar General stores per 10K residents (OSM)",
  grocery_distance:"Drive time to nearest full grocery store (USDA)",
  church_count:"Churches per 10K residents (IRS 501c3)",
  irs_net_migration_households:"IRS net migration households by state (IRS SOI)",
  foreign_exchange_reserves:"Foreign exchange reserves by country",
  per_capita_health_spending:"Health expenditure per capita",
  uninsured_rate:"Uninsured rate by state (ACS)",
  mean_age_first_birth:"Mean age at first birth (T80)",
  irrigated_acres:"Irrigated acres by county (USDA)",
  flood_zone_uninsured_pct:"FEMA flood zone uninsured %",
};

// Build variable index
const VAR_INDEX = {};
D.forEach(d => {
  const all = [...(d.vars || []), ...(d.join || [])];
  all.forEach(v => {
    if (!VAR_INDEX[v]) VAR_INDEX[v] = [];
    if (!VAR_INDEX[v].find(x => x.id === d.id))
      VAR_INDEX[v].push({ id: d.id, primary: !!(d.vars && d.vars.includes(v)) });
  });
});

// Format index
const FMT_MAP = {};
D.forEach(d => {
  if (!FMT_MAP[d.fmt]) FMT_MAP[d.fmt] = [];
  FMT_MAP[d.fmt].push(d);
});

//  STATE 
const activeFilters = { type: null, geo: null, fmt: null, status: null, notes: null };
let sortK = 'vscore', selFmt = null;

// Virtual scroll state
const PAGE = 100;
let filteredIdeas = [], renderedCount = 0;

//  COLORS 
const FC = {
  emotional:'#ef4444', relatability:'#3b82f6', clarity:'#f97316',
  surprise:'#f59e0b', tension:'#dc2626', visual:'#22c55e',
  data_ready:'#a855f7', originality:'#14b8a6'
};
const FL = {
  emotional:'Emo', relatability:'Rel', clarity:'Cla',
  surprise:'Sur', tension:'Ten', visual:'Vis',
  data_ready:'Dat', originality:'Ori'
};
const scColor = s => s >= 90 ? '#ef4444' : s >= 83 ? '#f59e0b' : s >= 76 ? '#22c55e' : '#6b7280';

const STATUS_DOT = {
  'idea':        { color: '#6b7280', label: 'Idea' },
  'in-progress': { color: '#f59e0b', label: 'In Progress' },
  'built':       { color: '#22c55e', label: 'Built' },
  'published':   { color: '#3b82f6', label: 'Published' },
};

const SECTION_COLORS = {
  'Health':'#ef4444','Elections':'#3b82f6','Income':'#22c55e',
  'Housing':'#f59e0b','Labor Force':'#a855f7','Law Enforcement':'#dc2626',
  'Education':'#14b8a6','Energy':'#f97316','Agriculture':'#84cc16',
  'Transportation':'#06b6d4','Population':'#ec4899','National Security':'#6366f1',
  'International Statistics':'#8b5cf6','Geography':'#10b981','Banking':'#f59e0b',
  'Information':'#0ea5e9','State Government':'#64748b','Federal Government':'#475569',
};

//  CARD HTML 
function cardHTML(d, highlight = false) {
  const bars = Object.entries(FL).map(([k, l]) =>
    `<div class="br"><span class="bl">${l}</span><div class="bt"><div class="bf" style="width:${(d.sc[k]||0)*10}%;background:${FC[k]}"></div></div></div>`
  ).join('');

  const st = STATUS_DOT[d.status] || STATUS_DOT['idea'];
  const secColor = SECTION_COLORS[d.section] || '#6b7280';

  // Primary data source (tbl) + ext sources
  const extList = (d.ext && d.ext.length)
    ? d.ext.map(e => `<li>${e}</li>`).join('')
    : '';
  const dataSection = `
    <div class="data-block">
      <div class="data-label"> DATA NEEDED</div>
      <div class="data-primary">${d.tbl}</div>
      ${extList ? `<ul class="data-ext">${extList}</ul>` : ''}
    </div>`;

  const notesSection = d.notes
    ? `<div class="notes-block"><span class="notes-icon"></span> ${d.notes}</div>`
    : '';

  return `<div class="card${highlight ? ' hi' : ''}">
    <div class="card-main">
      <div class="card-header">
        <span class="status-dot" style="background:${st.color}" title="${st.label}"></span>
        <span class="sect-badge" style="background:${secColor}22;color:${secColor};border:1px solid ${secColor}44">${d.section}</span>
      </div>
      <div class="ct">${d.title}</div>
      <div class="cs">${d.sub}</div>
      <div class="pills">
        <span class="pl ${d.type}">${d.type}</span>
        <span class="pl geo">${d.geo.replace(/_/g,' ')}</span>
        <span class="pl fmt">${d.fmt}</span>
      </div>
      ${dataSection}
      ${notesSection}
    </div>
    <div class="right">
      <div><div class="vs" style="color:${scColor(d.vs)}">${d.vs}</div><div class="vl">V-Score</div></div>
      <div class="brs">${bars}</div>
    </div>
  </div>`;
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
    if (q) {
      const h = (d.title+' '+d.sub+' '+d.tags+' '+d.section).toLowerCase();
      if (!h.includes(q)) return false;
    }
    return true;
  });

  // Sort
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

//  VIRTUAL SCROLL RENDER 
function renderBrowse() {
  buildFiltered();
  renderedCount = 0;
  const grid = document.getElementById('bgrid');
  grid.innerHTML = '';
  renderMore();
  updateCount();
}

function renderMore() {
  if (renderedCount >= filteredIdeas.length) return;
  const batch = filteredIdeas.slice(renderedCount, renderedCount + PAGE);
  const frag = document.createDocumentFragment();
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
    shown < total
      ? `Showing ${shown} of ${total} ideas - scroll for more`
      : `Showing ${total} of ${D.length} ideas`;
  if (!total) {
    document.getElementById('bgrid').innerHTML =
      '<div class="empty">No match - try a different keyword or clear a filter.</div>';
  }
}

// Intersection Observer for infinite scroll
const sentinel = document.createElement('div');
sentinel.id = 'sentinel';
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('bgrid').after(sentinel);
  const obs = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) renderMore();
  }, { rootMargin: '200px' });
  obs.observe(sentinel);
});

//  PILL TOGGLES 
function togglePill(btn) {
  const field = btn.dataset.f;
  const val   = btn.dataset.v;
  if (activeFilters[field] === val) {
    activeFilters[field] = null;
    btn.classList.remove('on');
  } else {
    document.querySelectorAll(`.fp[data-f="${field}"]`).forEach(b => b.classList.remove('on'));
    activeFilters[field] = val;
    btn.classList.add('on');
  }
  renderBrowse();
}

function setSort(btn) {
  sortK = btn.dataset.k;
  document.querySelectorAll('.sb').forEach(b => b.classList.remove('on'));
  btn.classList.add('on');
  renderBrowse();
}

//  MODE SWITCHING 
function setMode(m, btn) {
  document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('on'));
  btn.classList.add('on');
  document.querySelectorAll('.pane').forEach(p => p.classList.remove('on'));
  document.getElementById('pane-' + m).classList.add('on');
  if (m === 'correlate') buildVarSelect();
  if (m === 'format') buildFormatGrid();
}

//  CORRELATE 
function buildVarSelect() {
  const sel = document.getElementById('varsel');
  if (sel.options.length > 1) return;
  Object.keys(VAR_LABELS).sort((a,b) => VAR_LABELS[a].localeCompare(VAR_LABELS[b])).forEach(v => {
    const o = document.createElement('option');
    o.value = v; o.textContent = VAR_LABELS[v];
    sel.appendChild(o);
  });
}

function renderCorr() {
  const v = document.getElementById('varsel').value;
  if (!v) { document.getElementById('cgrid').innerHTML = ''; document.getElementById('ccnt').textContent = ''; return; }
  const primaryIds = new Set((VAR_INDEX[v]||[]).filter(x=>x.primary).map(x=>x.id));
  const joinIds    = new Set((VAR_INDEX[v]||[]).filter(x=>!x.primary).map(x=>x.id));
  const allIds     = new Set([...primaryIds,...joinIds]);
  document.getElementById('corr-hint').textContent =
    `${allIds.size} ideas connect to "${VAR_LABELS[v]}". Blue border = uses this variable directly.`;
  const sorted = D.filter(d=>allIds.has(d.id)).sort((a,b)=>{
    const ap=primaryIds.has(a.id)?1:0, bp=primaryIds.has(b.id)?1:0;
    if(ap!==bp) return bp-ap; return b.vs-a.vs;
  });
  document.getElementById('ccnt').textContent = `${sorted.length} idea${sorted.length!==1?'s':''} relate to this variable`;
  document.getElementById('cgrid').innerHTML = sorted.length
    ? sorted.map(d=>cardHTML(d, primaryIds.has(d.id))).join('')
    : '<div class="empty">No ideas indexed for this variable yet.</div>';
}

//  FORMAT 
function buildFormatGrid() {
  const fg = document.getElementById('fgrid');
  if (fg.children.length) return;
  Object.entries(FMT_MAP).sort((a,b)=>b[1].length-a[1].length).forEach(([k,items])=>{
    const btn = document.createElement('button');
    btn.className = 'fb';
    btn.innerHTML = `<div>${k}</div><div class="fct">${items.length} idea${items.length!==1?'s':''}</div>`;
    btn.onclick = () => toggleFmt(k, btn);
    fg.appendChild(btn);
  });
}

function toggleFmt(k, btn) {
  if (selFmt === k) {
    selFmt = null;
    document.querySelectorAll('.fb').forEach(b=>b.classList.remove('on'));
    document.getElementById('fgridout').innerHTML = '';
    document.getElementById('fcnt').textContent = '';
  } else {
    selFmt = k;
    document.querySelectorAll('.fb').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    const items = (FMT_MAP[k]||[]).sort((a,b)=>b.vs-a.vs);
    document.getElementById('fcnt').textContent = `${items.length} idea${items.length!==1?'s':''} in this format`;
    document.getElementById('fgridout').innerHTML = items.map(d=>cardHTML(d)).join('');
  }
}

//  INIT 
renderBrowse();
