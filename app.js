// app.js — Mapzimus board logic v2

const VAR_LABELS = {
  // Elections
  rep_pct:"Republican vote % by state (T454)", dem_pct:"Democratic vote % by state (T454)",
  margin:"Vote margin by state (T454)", pct_voted_state:"Voter turnout % by state (T449)",
  pct_registered_state:"Voter registration % by state (T449)",
  // Income & Poverty
  median_household_income:"Median household income by state (T727)",
  pct_under_25k:"% households under $25K by state (T727)",
  pct_over_200k:"% households over $200K by state (T727)",
  real_per_capita_income:"Real per capita income by state (T723)",
  disposable_income_per_capita:"Disposable income per capita by state (T725)",
  state_gdp_per_capita:"State GDP per capita (T715)",
  // Crime
  violent_crime_rate:"Violent crime rate by state (T340)", murder_rate:"Murder rate by state (T340)",
  property_crime_rate:"Property crime rate by state (T340)",
  // Education
  pct_bachelors:"% with bachelor's degree by state (T254)", pct_hs_grad:"% HS graduates by state (T254)",
  expenditure_per_pupil:"Per-pupil school spending (T258)", avg_teacher_salary:"Avg teacher salary by state (T268)",
  teacher_count:"Teacher count by state (T268)", revenue_federal_pct:"% school revenue from federal (T258)",
  revenue_local_pct:"% school revenue from local taxes (T258)",
  district_enrollment:"District enrollment — top 50 (T261)",
  // Labor
  state_unemployment_rate:"Unemployment rate by state (T629)",
  female_lfp_rate:"Female labor force participation by state (T629)",
  disability_lfp_rate:"LFP rate with disability (T626)",
  disability_unemployment:"Unemployment rate with disability (T626)",
  metro_unemployment_rate:"Metro area unemployment rate (T630)",
  // Social Insurance
  total_transfers_per_capita:"Govt transfers per capita by state (T573)",
  veterans_benefits:"Veterans benefits by state (T573)", pct_on_snap:"% households on SNAP (T576)",
  pct_on_medicaid:"% households on Medicaid (T576)", snap_households:"SNAP households total (T577)",
  // Births & Fertility
  birth_rate_state:"Birth rate by state (T81)", fertility_rate_state:"Fertility rate by state (T81)",
  teen_birth_rate:"Teen birth rate by state (T86)",
  pct_births_unmarried:"% births to unmarried mothers by state (T87)",
  total_fertility_rate_by_race:"Total fertility rate by race (T85)",
  // Health
  total_medicare:"Medicare enrollment by state (T150)",
  per_capita_health_spending:"Health expenditure per capita (T141)",
  hospital_services_cpi:"Hospital services CPI (T770)",
  health_insurance_cpi:"Health insurance CPI (T770)",
  physicians_services_cpi:"Physicians services CPI (T770)",
  prescription_drugs_cpi:"Prescription drugs CPI (T770)",
  nursing_homes_cpi:"Nursing homes and adult day services CPI (T770)",
  // CPI & Prices
  all_items_cpi:"All-items CPI 2000–2024 (T770)",
  food_at_home_cpi:"Food at home CPI (T770)", eggs_cpi:"Eggs CPI (T770)",
  beef_and_veal_cpi:"Beef and veal CPI (T770)", poultry_cpi:"Poultry CPI (T770)",
  dairy_cpi:"Dairy products CPI (T770)", cereals_bakery_cpi:"Cereals and bakery CPI (T770)",
  motor_vehicle_insurance_cpi:"Motor vehicle insurance CPI (T770)",
  gasoline_cpi:"Gasoline CPI (T770)", housing_cpi:"Housing CPI (T770)",
  housing_cpi_city:"Housing CPI by major city (T769)",
  rent_primary_residence_cpi:"Rent of primary residence CPI (T769)",
  college_tuition_cpi:"College tuition and fees CPI (T770)",
  daycare_preschool_cpi:"Daycare and preschool CPI (T770)",
  tobacco_cpi:"Tobacco and smoking products CPI (T770)",
  cigarette_cpi:"Cigarette CPI (T770)",
  gasoline_price_regular:"Regular gasoline price by city (T773)",
  home_price_index_2024:"Home price index 2024 by state (T771)",
  home_price_pct_change_2005_2024:"Home price % change 2005–2024 by state (T771)",
  // Banking & Finance
  credit_card_rate_all_accounts:"Credit card rate — all accounts (T1223)",
  credit_card_rate_assessed:"Credit card rate — accounts assessed interest (T1223)",
  total_consumer_credit:"Total consumer credit outstanding (T1222)",
  student_loans_outstanding:"Student loan debt outstanding (T1222)",
  auto_loan_rate:"Auto loan interest rate (T1223)",
  mortgage_delinquency_rate:"Mortgage delinquency rate (T1225)",
  foreclosure_rate_total:"Foreclosure rate (T1225)",
  home_equity_loans:"Home equity loans outstanding (T1224)",
  total_mortgage_debt:"Total mortgage debt outstanding (T1224)",
  corporate_profits:"Corporate profits before tax (T793)",
  income_tax_after_credits:"Corporate income tax after credits (T793)",
  corp_audit_rate:"IRS corporate audit rate (T794)",
  recommended_additional_tax:"IRS recommended additional taxes (T794)",
  pct_families_own_stocks:"% families owning stocks directly (T1207)",
  pct_families_own_retirement:"% families owning retirement accounts (T1207)",
  pct_families_own_any_asset:"% families owning any financial asset (T1207)",
  median_stock_value:"Median value of stocks held (T1207)",
  // Transportation
  pct_ontime_arrivals:"On-time arrival % by airport (T1110)",
  pct_ontime_departures:"On-time departure % by airport (T1110)",
  passengers_enplaned:"Passengers enplaned by airport (T1112)",
  port_total_tons:"Port tonnage — total (T1122)", port_domestic_tons:"Port tonnage — domestic (T1122)",
  port_foreign_tons:"Port tonnage — foreign (T1122)",
  port_total_teus:"Port container traffic — TEUs (T1123)",
  port_inbound_teus:"Port inbound TEUs (T1123)",
  waterway_freight_tons:"Waterway freight tonnage (T1120)",
  pct_bridges_poor:"% bridges in poor condition by state (T1126)",
  total_bridges:"Total bridges by state (T1126)",
  // Energy
  energy_consumption_per_capita:"Energy consumption per capita by state (T975)",
  renewable_energy_share:"Renewable energy share by state (T976)",
  hydroelectric_consumption:"Hydroelectric consumption by state (T976)",
  coal_consumption:"Coal consumption by state (T976)",
  coal_production_index:"Coal production index 1990–2024 (T950)",
  oil_gas_extraction_index:"Oil/gas extraction index (T950)",
  // Agriculture
  farms_count_2022:"Number of farms by state 2022 (T869)",
  land_in_farms_2022:"Land in farms (acres) by state 2022 (T869)",
  farm_value_land:"Total farmland value by state (T869)",
  pct_cropland:"% land that is cropland by state (T413)",
  pct_forest:"% land that is forest by state (T413)",
  farm_sales_by_size:"Farm sales by farm size class (T871)",
  farmer_avg_age:"Average age of farm operators (T872)",
  farmer_pct_white:"% farm operators who are white (T872)",
  farmer_pct_male:"% farm operators who are male (T872)",
  // Fishing
  port_catch_lbs:"Commercial fish landings by port — lbs (T945)",
  port_catch_value:"Commercial fish landings by port — value (T945)",
  species_landed_value:"Landed value by fish species (T944)",
  species_landed_lbs:"Landed pounds by fish species (T944)",
  // Military
  us_troops_overseas:"US troops stationed overseas by country (T549)",
  defense_budget_total:"Total US defense budget (T543)",
  total_deaths:"Military deaths by conflict (T548)",
  hostile_deaths:"Hostile military deaths by conflict (T548)",
  wounded_in_action:"Wounded in action by conflict (T548)",
  retired_military_count:"Retired military by state (T547)",
  military_pension_monthly:"Military pension payments by state (T547)",
  active_duty_total:"Active duty total by year/branch (T545)",
  active_duty_female_pct:"Active duty female % by year/branch (T545)",
  // International
  net_migration_rate:"Net migration rate by country (T1360)",
  population_pct_change_2020_2025:"Population % change by country 2020–2025 (Intl. Statistics)",
  population_pct_change_1950_2020:"Population % change US county 1950–2020 (Population PDF)",
  population_per_sq_km:"Population density per km² by country (Intl. Statistics)",
  birth_rate:"Birth rate by country (Intl. Statistics)",
  // Trade
  trade_balance_goods:"Trade balance on goods by country (T1310)",
  trade_balance_services:"Trade balance on services by country (T1309)",
  current_account_balance:"Current account balance total (T1306)",
  balance_on_goods:"Balance on goods — US total (T1306)",
  balance_on_services:"Balance on services — US total (T1306)",
  foreign_affiliate_employment:"Employment at foreign-owned US firms by state (T1311)",
  // Construction & Housing
  housing_permits_total:"New housing permits by state (T1011)",
  population_pct_change:"Population % change by state (Population PDF)",
  // Science
  rd_pct_gdp:"R&D spending as % of GDP by country (T842)",
  // Forestry
  national_forest_acres:"National Forest acres by state (T932)",
  // Media & Arts
  newspaper_print_revenue:"Newspaper print revenue (T1174)",
  newspaper_digital_revenue:"Newspaper digital revenue (T1174)",
  newspaper_total_revenue:"Newspaper total revenue (T1174)",
  annual_attendance:"Theme park annual attendance (T1271)",
  sports_attendance_12mo:"Sports event attendance last 12 months (T1273)",
  broadway_attendance:"Broadway attendance by season (T1259)",
  gross_ticket_income:"Broadway gross ticket income (T1259)",
  // Geography
  mean_elevation:"Mean elevation by state (T410)",
  border_miles:"US border length by state (T407)",
  coastline_miles:"Coastline miles by state (T408)",
};

// ── Build variable → ideas index ─────────────────────────────────────────────
const VAR_INDEX = {};
D.forEach(d => {
  const all = [...(d.vars || []), ...(d.join || [])];
  all.forEach(v => {
    if (!VAR_INDEX[v]) VAR_INDEX[v] = [];
    if (!VAR_INDEX[v].find(x => x.id === d.id))
      VAR_INDEX[v].push({ id: d.id, primary: !!(d.vars && d.vars.includes(v)) });
  });
});

// ── Format index ─────────────────────────────────────────────────────────────
const FMT_MAP = {};
D.forEach(d => {
  const fk = d.fmt.split('—')[0].split('(')[0].trim();
  if (!FMT_MAP[fk]) FMT_MAP[fk] = [];
  FMT_MAP[fk].push(d);
});

// ── Color helpers ─────────────────────────────────────────────────────────────
const FC = {
  emotional:'#ef4444', relatability:'#3b82f6', surprise:'#f59e0b',
  tension:'#dc2626', visual:'#22c55e', data_ready:'#a855f7', originality:'#14b8a6'
};
const FL = {
  emotional:'Emo', relatability:'Rel', surprise:'Sur', tension:'Ten',
  visual:'Vis', data_ready:'Dat', originality:'Ori'
};
const scColor = s => s >= 93 ? '#ef4444' : s >= 87 ? '#f59e0b' : s >= 80 ? '#22c55e' : '#6b7280';

let sortK = 'vscore', selFmt = null;

// ── Mode switching ────────────────────────────────────────────────────────────
function setMode(m, btn) {
  document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('on'));
  btn.classList.add('on');
  document.querySelectorAll('.pane').forEach(p => p.classList.remove('on'));
  document.getElementById('pane-' + m).classList.add('on');
  if (m === 'correlate') buildVarSelect();
  if (m === 'format') buildFormatGrid();
}

function setSort(btn) {
  sortK = btn.dataset.k;
  document.querySelectorAll('.sb').forEach(b => b.classList.remove('on'));
  btn.classList.add('on');
  renderBrowse();
}

// ── Card HTML ─────────────────────────────────────────────────────────────────
function cardHTML(d, highlight = false) {
  const bars = Object.entries(FL).map(([k, l]) =>
    `<div class="br"><span class="bl">${l}</span><div class="bt"><div class="bf" style="width:${(d.sc[k]||0)*10}%;background:${FC[k]}"></div></div></div>`
  ).join('');
  const fmtShort = d.fmt.split('—')[0].split('(')[0].trim();
  const proxyWarn = d.proxy
    ? `<div class="proxy-warn">⚠ Proxy: ${d.proxyNote || 'indirect data source'}</div>` : '';
  return `<div class="card${highlight ? ' hi' : ''}">
    <div>
      <div class="ct">${d.title}</div>
      <div class="cs">${d.sub}</div>
      <div class="pills">
        <span class="pl ${d.type}">${d.type}</span>
        <span class="pl geo">${d.geo.replace(/_/g,' ')}</span>
        <span class="pl fmt">${fmtShort}</span>
      </div>
      <div class="src">${d.tbl} · ${d.section}</div>
      ${proxyWarn}
    </div>
    <div class="right">
      <div><div class="vs" style="color:${scColor(d.vs)}">${d.vs}</div><div class="vl">V-Score</div></div>
      <div class="brs">${bars}</div>
    </div>
  </div>`;
}

// ── Browse ────────────────────────────────────────────────────────────────────
function renderBrowse() {
  const q = (document.getElementById('q').value || '').toLowerCase();
  const tf = document.getElementById('tf').value;
  const gf = document.getElementById('gf').value;
  const r = D.filter(d => {
    if (tf && d.type !== tf) return false;
    if (gf && d.geo !== gf) return false;
    if (q) {
      const h = d.title.toLowerCase()+' '+d.sub.toLowerCase()+' '+d.tags.toLowerCase()+' '+d.section.toLowerCase();
      if (!h.includes(q)) return false;
    }
    return true;
  }).sort((a, b) => {
    const av = sortK === 'vscore' ? a.vs : (a.sc[sortK] || 0);
    const bv = sortK === 'vscore' ? b.vs : (b.sc[sortK] || 0);
    return bv - av;
  });
  document.getElementById('bcnt').textContent = `Showing ${r.length} of ${D.length} ideas`;
  document.getElementById('bgrid').innerHTML = r.length
    ? r.map(d => cardHTML(d)).join('')
    : '<div class="empty">No match — try a different keyword.</div>';
}

// ── Correlate ─────────────────────────────────────────────────────────────────
function buildVarSelect() {
  const sel = document.getElementById('varsel');
  if (sel.options.length > 1) return;
  Object.keys(VAR_LABELS).sort((a,b) => VAR_LABELS[a].localeCompare(VAR_LABELS[b])).forEach(v => {
    const o = document.createElement('option');
    o.value = v;
    o.textContent = VAR_LABELS[v];
    sel.appendChild(o);
  });
}

function renderCorr() {
  const v = document.getElementById('varsel').value;
  if (!v) {
    document.getElementById('cgrid').innerHTML = '';
    document.getElementById('ccnt').textContent = '';
    return;
  }
  const primaryIds = new Set((VAR_INDEX[v]||[]).filter(x=>x.primary).map(x=>x.id));
  const joinIds    = new Set((VAR_INDEX[v]||[]).filter(x=>!x.primary).map(x=>x.id));
  const allIds     = new Set([...primaryIds,...joinIds]);
  document.getElementById('corr-hint').textContent =
    `${allIds.size} ideas connect to "${VAR_LABELS[v]}". Blue border = uses this variable directly.`;
  const sorted = D.filter(d=>allIds.has(d.id)).sort((a,b)=>{
    const ap = primaryIds.has(a.id)?1:0, bp = primaryIds.has(b.id)?1:0;
    if (ap!==bp) return bp-ap;
    return b.vs-a.vs;
  });
  document.getElementById('ccnt').textContent = `${sorted.length} idea${sorted.length!==1?'s':''} relate to this variable`;
  document.getElementById('cgrid').innerHTML = sorted.length
    ? sorted.map(d=>cardHTML(d, primaryIds.has(d.id))).join('')
    : '<div class="empty">No ideas indexed for this variable yet.</div>';
}

// ── Format ────────────────────────────────────────────────────────────────────
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

// ── Init ──────────────────────────────────────────────────────────────────────
document.getElementById('subl').textContent =
  `${D.length} ideas · ProQuest Statistical Abstract of the U.S. 2026 · all 36 PDFs · @mapzimus`;
renderBrowse();
