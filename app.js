// app.js - Mapzimus board logic v3

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
  disability_lfp_rate:"LFP rate with disability (T626)",
  disability_unemployment:"Unemployment rate with disability (T626)",
  metro_unemployment_rate:"Metro area unemployment rate (T630)",
  total_transfers_per_capita:"Govt transfers per capita by state (T573)",
  veterans_benefits:"Veterans benefits by state (T573)", pct_on_snap:"% households on SNAP (T576)",
  pct_on_medicaid:"% households on Medicaid (T576)", snap_households:"SNAP households total (T577)",
  birth_rate_state:"Birth rate by state (T81)", fertility_rate_state:"Fertility rate by state (T81)",
  teen_birth_rate:"Teen birth rate by state (T86)",
  pct_births_unmarried:"% births to unmarried mothers by state (T87)",
  total_fertility_rate_by_race:"Total fertility rate by race (T85)",
  total_medicare:"Medicare enrollment by state (T150)",
  per_capita_health_spending:"Health expenditure per capita (T141)",
  hospital_services_cpi:"Hospital services CPI (T770)",
  health_insurance_cpi:"Health insurance CPI (T770)",
  physicians_services_cpi:"Physicians services CPI (T770)",
  prescription_drugs_cpi:"Prescription drugs CPI (T770)",
  nursing_homes_cpi:"Nursing homes and adult day services CPI (T770)",
  all_items_cpi:"All-items CPI 2000-2024 (T770)",
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
  home_price_pct_change_2005_2024:"Home price % change 2005-2024 by state (T771)",
  credit_card_rate_all_accounts:"Credit card rate - all accounts (T1223)",
  credit_card_rate_assessed:"Credit card rate - accounts assessed interest (T1223)",
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
  pct_ontime_arrivals:"On-time arrival % by airport (T1110)",
  pct_ontime_departures:"On-time departure % by airport (T1110)",
  passengers_enplaned:"Passengers enplaned by airport (T1112)",
  port_total_tons:"Port tonnage - total (T1122)", port_domestic_tons:"Port tonnage - domestic (T1122)",
  port_foreign_tons:"Port tonnage - foreign (T1122)",
  port_total_teus:"Port container traffic - TEUs (T1123)",
  port_inbound_teus:"Port inbound TEUs (T1123)",
  waterway_freight_tons:"Waterway freight tonnage (T1120)",
  pct_bridges_poor:"% bridges in poor condition by state (T1126)",
  total_bridges:"Total bridges by state (T1126)",
  energy_consumption_per_capita:"Energy consumption per capita by state (T975)",
  renewable_energy_share:"Renewable energy share by state (T976)",
  hydroelectric_consumption:"Hydroelectric consumption by state (T976)",
  coal_consumption:"Coal consumption by state (T976)",
  coal_production_index:"Coal production index 1990-2024 (T950)",
  oil_gas_extraction_index:"Oil/gas extraction index (T950)",
  farms_count_2022:"Number of farms by state 2022 (T869)",
  land_in_farms_2022:"Land in farms (acres) by state 2022 (T869)",
  farm_value_land:"Total farmland value by state (T869)",
  pct_cropland:"% land that is cropland by state (T413)",
  pct_forest:"% land that is forest by state (T413)",
  farm_sales_by_size:"Farm sales by farm size class (T871)",
  farmer_avg_age:"Average age of farm operators (T872)",
  farmer_pct_white:"% farm operators who are white (T872)",
  farmer_pct_male:"% farm operators who are male (T872)",
  port_catch_lbs:"Commercial fish landings by port - lbs (T945)",
  port_catch_value:"Commercial fish landings by port - value (T945)",
  species_landed_value:"Landed value by fish species (T944)",
  species_landed_lbs:"Landed pounds by fish species (T944)",
  us_troops_overseas:"US troops stationed overseas by country (T549)",
  defense_budget_total:"Total US defense budget (T543)",
  total_deaths:"Military deaths by conflict (T548)",
  hostile_deaths:"Hostile military deaths by conflict (T548)",
  wounded_in_action:"Wounded in action by conflict (T548)",
  retired_military_count:"Retired military by state (T547)",
  military_pension_monthly:"Military pension payments by state (T547)",
  active_duty_total:"Active duty total by year/branch (T545)",
  active_duty_female_pct:"Active duty female % by year/branch (T545)",
  net_migration_rate:"Net migration rate by country (T1360)",
  population_pct_change_2020_2025:"Population % change by country 2020-2025 (Intl. Statistics)",
  population_pct_change_1950_2020:"Population % change US county 1950-2020 (Population PDF)",
  population_per_sq_km:"Population density per km2 by country (Intl. Statistics)",
  birth_rate:"Birth rate by country (Intl. Statistics)",
  trade_balance_goods:"Trade balance on goods by country (T1310)",
  trade_balance_services:"Trade balance on services by country (T1309)",
  current_account_balance:"Current account balance total (T1306)",
  balance_on_goods:"Balance on goods - US total (T1306)",
  balance_on_services:"Balance on services - US total (T1306)",
  foreign_affiliate_employment:"Employment at foreign-owned US firms by state (T1311)",
  housing_permits_total:"New housing permits by state (T1011)",
  population_pct_change:"Population % change by state (Population PDF)",
  rd_pct_gdp:"R&D spending as % of GDP by country (T842)",
  national_forest_acres:"National Forest acres by state (T932)",
  newspaper_print_revenue:"Newspaper print revenue (T1174)",
  newspaper_digital_revenue:"Newspaper digital revenue (T1174)",
  newspaper_total_revenue:"Newspaper total revenue (T1174)",
  annual_attendance:"Theme park annual attendance (T1271)",
  sports_attendance_12mo:"Sports event attendance last 12 months (T1273)",
  broadway_attendance:"Broadway attendance by season (T1259)",
  gross_ticket_income:"Broadway gross ticket income (T1259)",
  mean_elevation:"Mean elevation by state (T410)",
  border_miles:"US border length by state (T407)",
  coastline_miles:"Coastline miles by state (T408)",
  river_length:"River length - major US rivers (T409)",
  irrigation_water_use:"Irrigation water withdrawal per day (T415)",
  data_center_construction:"Data center construction spending (T1013)",
  total_manufacturing_construction:"Manufacturing construction spending (T1013)",
  healthcare_construction:"Healthcare facility construction (T1013)",
  state_arts_appropriation:"State arts agency appropriations (T1261)",
  gross_arts_output:"Arts and cultural production gross output (T1257)",
  gig_transport_establishments:"Gig/nonemployer transport establishments (T1103)",
  gig_transport_receipts:"Gig/nonemployer transport receipts (T1103)",
  state_gdp:"State GDP total (T715)",
  manufacturing_gdp:"Manufacturing share of state GDP (T712)",
  metro_per_capita_income:"Metro area per capita income (T726)",
  retirement_disability_benefits:"Retirement and disability benefits by state (T573)",
  medical_payments_state:"Medical payments by state (T573)",
  mean_age_first_birth:"Mean age at first birth by race (T80)",
  home_price_change_2019_2024:"Home price % change 2019-2024 by state (T771)",
  federal_debt_pct_gdp:"Federal debt as % of GDP 1960-2024 (T509)",
  federal_outlays_by_function:"Federal budget outlays by function (T512)",
  federal_tax_revenue_type:"Federal budget receipts by source (T514)",
  federal_civilian_employment_state:"Federal civilian employees by state (T537)",
  federal_agi_by_state:"Avg adjusted gross income per return by state (T532)",
  federal_tax_refunds_state:"Federal tax refunds by state 2024 (T533)",
  unclaimed_refunds_state:"Individuals due unclaimed refunds by state (T534)",
  lottery_revenue_per_capita:"State lottery revenue per capita (T493)",
  sports_betting_revenue:"Sports betting tax revenue by state (T493)",
  state_local_revenue_per_capita:"State and local govt revenue per capita (T488)",
  state_local_expenditure_per_capita:"State and local govt expenditures per capita (T488)",
  state_local_debt_per_capita:"State and local govt debt per capita (T486)",
  state_local_avg_earnings:"State/local govt avg monthly earnings by state (T505)",
  state_general_fund_balance:"State general fund surplus/deficit (T495)",
  state_income_tax_revenue:"State individual income tax revenue (T497)",
  manufacturing_employment_trend:"Manufacturing employment 2000-2024 (T1064)",
  manufacturing_hourly_wages_state:"Manufacturing hourly wages by state (T1067)",
  manufacturing_value_added_state:"Manufacturing value added by state (T1062)",
  manufacturing_payroll_state:"Manufacturing payroll by state (T1062)",
  manufacturing_shipments_state:"Manufacturing shipments by state (T1063)",
  retail_sales_per_capita:"Per capita retail sales (T1090)",
  ecommerce_sales:"E-commerce sales by category (T1093)",
  wholesale_employees_state:"Wholesale and retail employees by state (T1084)",
  wholesale_sales_total:"Merchant wholesaler sales total (T1083)",
  holc_grade:"HOLC redlining grade by neighborhood (Mapping Inequality - ext.)",
  abortion_provider_distance:"Drive time to nearest abortion provider (Guttmacher - ext.)",
  trauma_center_distance:"Drive time to nearest trauma center (HRSA - ext.)",
  nicu_distance:"Drive time to nearest NICU (CMS - ext.)",
  grocery_distance:"Drive time to nearest full grocery store (USDA FARA - ext.)",
  gofundme_medical_per_capita:"GoFundMe medical campaigns per capita (GoFundMe - ext.)",
  irs_net_migration_households:"IRS net migration households by state (IRS SOI - ext.)",
  dollar_general_density:"Dollar General stores per 10K residents (OSM - ext.)",
  church_count:"Churches per 10K residents (IRS 501c3 - ext.)",
  brewery_count:"Breweries per 10K residents (USDA/OSM - ext.)",
  lightning_strikes_per_sqmi:"Lightning strikes per sq mile (VAISALA - ext.)",
  airbnb_listings_per_sqmi:"Airbnb listings density (Inside Airbnb - ext.)",
  county_vote_swing_2016_2024:"County vote swing 2016-2024 (MIT Election Lab - ext.)",
  foreign_born_physician_pct:"Foreign-born physicians % by state (ACS - ext.)",
  sex_ratio_county:"Sex ratio (men per 100 women) by county (ACS - ext.)",
  avg_commute_time:"Average commute time in minutes by county (ACS - ext.)",
  broadband_access_pct:"Broadband access rate by county (FCC - ext.)",
  language_diversity_index:"Language diversity index by county (ACS - ext.)",
  rural_population_pct:"Rural population % by county (ACS - ext.)",
  superfund_sites_per_sqmi:"Superfund sites per sq mile by county (EPA - ext.)",
  flood_zone_uninsured_pct:"FEMA flood zone properties uninsured % (FEMA NFIP - ext.)",
  mental_health_providers_per_100k:"Mental health providers per 100K (SAMHSA/HRSA - ext.)",
};

//  Build variable index 
const VAR_INDEX = {};
D.forEach(d => {
  const all = [...(d.vars || []), ...(d.join || [])];
  all.forEach(v => {
    if (!VAR_INDEX[v]) VAR_INDEX[v] = [];
    if (!VAR_INDEX[v].find(x => x.id === d.id))
      VAR_INDEX[v].push({ id: d.id, primary: !!(d.vars && d.vars.includes(v)) });
  });
});

//  Format index 
const FMT_MAP = {};
D.forEach(d => {
  if (!FMT_MAP[d.fmt]) FMT_MAP[d.fmt] = [];
  FMT_MAP[d.fmt].push(d);
});

//  Active filters state 
const activeFilters = { type: null, geo: null, fmt: null };

//  Color helpers 
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

//  Mode switching 
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

//  Pill toggle 
function togglePill(btn) {
  const field = btn.dataset.f;
  const val   = btn.dataset.v;
  if (activeFilters[field] === val) {
    // deselect
    activeFilters[field] = null;
    btn.classList.remove('on');
  } else {
    // deselect previous in same group
    document.querySelectorAll(`.fp[data-f="${field}"]`).forEach(b => b.classList.remove('on'));
    activeFilters[field] = val;
    btn.classList.add('on');
  }
  renderBrowse();
}

//  Card HTML 
function cardHTML(d, highlight = false) {
  const bars = Object.entries(FL).map(([k, l]) =>
    `<div class="br"><span class="bl">${l}</span><div class="bt"><div class="bf" style="width:${(d.sc[k]||0)*10}%;background:${FC[k]}"></div></div></div>`
  ).join('');
  const extBadge = (d.ext && d.ext.length)
    ? `<div class="ext-badge">+ ext: ${d.ext.join('  |  ')}</div>` : '';
  return `<div class="card${highlight ? ' hi' : ''}">
    <div>
      <div class="ct">${d.title}</div>
      <div class="cs">${d.sub}</div>
      <div class="pills">
        <span class="pl ${d.type}">${d.type}</span>
        <span class="pl geo">${d.geo.replace(/_/g,' ')}</span>
        <span class="pl fmt">${d.fmt}</span>
      </div>
      <div class="src">${d.tbl}  |  ${d.section}</div>
      ${extBadge}
    </div>
    <div class="right">
      <div><div class="vs" style="color:${scColor(d.vs)}">${d.vs}</div><div class="vl">V-Score</div></div>
      <div class="brs">${bars}</div>
    </div>
  </div>`;
}

//  Browse 
function renderBrowse() {
  const q = (document.getElementById('q').value || '').toLowerCase();
  const r = D.filter(d => {
    if (activeFilters.type && d.type !== activeFilters.type) return false;
    if (activeFilters.geo  && d.geo  !== activeFilters.geo)  return false;
    if (activeFilters.fmt  && d.fmt  !== activeFilters.fmt)  return false;
    if (q) {
      const h = d.title.toLowerCase()+' '+d.sub.toLowerCase()+' '+d.tags.toLowerCase()+' '+d.section.toLowerCase();
      if (!h.includes(q)) return false;
    }
    return true;
  });
  // Sort
  if (sortK === 'newest') {
    r.sort((a, b) => D.indexOf(b) - D.indexOf(a));
  } else if (sortK === 'oldest') {
    r.sort((a, b) => D.indexOf(a) - D.indexOf(b));
  } else {
    r.sort((a, b) => {
      const av = sortK === 'vscore' ? a.vs : (a.sc[sortK] || 0);
      const bv = sortK === 'vscore' ? b.vs : (b.sc[sortK] || 0);
      return bv - av;
    });
  }
  document.getElementById('bcnt').textContent = `Showing ${r.length} of ${D.length} ideas`;
  document.getElementById('bgrid').innerHTML = r.length
    ? r.map(d => cardHTML(d)).join('')
    : '<div class="empty">No match - try a different keyword or clear a filter.</div>';
}

//  Correlate 
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

//  Format 
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

//  Init 
renderBrowse();
