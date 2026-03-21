"""
BATCH_GI.py — Cross-reference mega-batch: novel dataset combos, multi-source XREFs
Target: ~65 high-originality ideas that combine 2+ sources
"""
import re, sys

DATA_JS = r"D:\projects\mapzimus-board\data.js"

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

ideas = []

# ============================================================
# HEALTH x ECONOMY cross-refs
# ============================================================
ideas.append(mk("xr_life_exp_vs_healthcare_spend","Does Spending More on Healthcare Buy More Years","US spends 2x per capita but ranks 46th in life expectancy","XREF","worldwide","Scatter plot","Health","WHO GHE + World Bank HE https://apps.who.int/gho + https://data.worldbank.org",75,70,80,75,65,65,70,95))
ideas.append(mk("xr_mental_health_vs_gdp","Wealth Doesnt Protect Against Depression","Depression rates vs GDP per capita worldwide","XREF","worldwide","Scatter plot","Health","IHME GBD + World Bank GDP https://www.healthdata.org + https://data.worldbank.org",70,75,80,70,55,60,65,90))
ideas.append(mk("xr_infant_mortality_vs_inequality","Infant Mortality Tracks Inequality Not Wealth","Gini coefficient vs infant mortality by country","XREF","worldwide","Scatter plot","Health","World Bank + UNICEF https://data.worldbank.org + https://data.unicef.org",80,60,80,70,75,60,70,90))
ideas.append(mk("xr_obesity_vs_food_desert_county","Food Deserts Predict Obesity at County Level","USDA food desert designation vs obesity prevalence","XREF","us_county","Bivariate choropleth","Health","USDA Food Access + CDC PLACES https://www.ers.usda.gov/data-products/food-access-research-atlas/ + https://www.cdc.gov/places/",75,80,80,55,55,85,60,90))
ideas.append(mk("xr_suicide_vs_gun_ownership","Suicide Rate Tracks Gun Ownership by State","States with more guns have more suicides even after controlling for poverty","XREF","us_state","Bivariate choropleth","Health","CDC WONDER + RAND Gun Policy https://wonder.cdc.gov + https://www.rand.org/pubs/tools/TLA243-2-v2.html",80,65,80,60,85,85,60,85))

# ============================================================
# CRIME x SOCIAL cross-refs
# ============================================================
ideas.append(mk("xr_incarceration_vs_education_spend","States That Spend More on Prisons Spend Less on Schools","Per capita prison spending vs education spending by state","XREF","us_state","Bivariate choropleth","Crime and Law Enforcement","Vera Institute + Census Gov Finance https://www.vera.org + https://www.census.gov/programs-surveys/gov-finances.html",80,75,80,70,80,85,65,90))
ideas.append(mk("xr_police_shootings_vs_body_cams","Do Body Cameras Reduce Police Shootings","Police shooting rate vs body cam adoption by department","XREF","us_national","Scatter plot","Crime and Law Enforcement","WaPo Fatal Force + LEMAS Survey https://www.washingtonpost.com/graphics/investigations/police-shootings-database/ + https://bjs.ojp.gov/data-collection/law-enforcement-management-and-administrative-statistics-lemas",75,65,80,70,75,60,75,70))
ideas.append(mk("xr_drug_overdose_vs_unemployment","Overdose Deaths Track Unemployment by County","Opioid death rates vs jobless rates by county 2015-2023","XREF","us_county","Bivariate choropleth","Health","CDC WONDER + BLS LAUS https://wonder.cdc.gov + https://www.bls.gov/lau/",80,75,80,60,75,85,60,85))
ideas.append(mk("xr_homicide_vs_heat","Murder Rate Rises with Temperature","Monthly homicide rate correlates with average temperature by city","XREF","us_national","Scatter plot","Crime and Law Enforcement","FBI UCR + NOAA Climate https://cde.ucr.cjis.gov + https://www.ncei.noaa.gov",60,55,75,70,55,60,70,85))
ideas.append(mk("xr_recidivism_vs_min_wage","Does Minimum Wage Reduce Repeat Offenders","State recidivism rates vs minimum wage levels","XREF","us_state","Scatter plot","Crime and Law Enforcement","BJS Recidivism + DOL Wage Data https://bjs.ojp.gov + https://www.dol.gov/agencies/whd/minimum-wage/state",55,55,75,70,55,60,75,65))

# ============================================================
# ENVIRONMENT x ECONOMY cross-refs
# ============================================================
ideas.append(mk("xr_co2_vs_gdp_trajectory","Countries That Got Rich by Polluting","Historical CO2 emissions vs GDP trajectory 1900-2024","XREF","worldwide","Scatter plot","Environment","OWID CO2 + World Bank GDP https://github.com/owid/co2-data + https://data.worldbank.org",70,55,80,65,65,60,65,95))
ideas.append(mk("xr_renewable_jobs_vs_fossil","Green Energy Jobs Are Overtaking Fossil Fuel Jobs","Renewable energy employment vs fossil fuel employment by state","XREF","us_state","State choropleth","Economy","DOE USEER + BLS QCEW https://www.energy.gov/us-energy-employment-report + https://www.bls.gov/cew/",65,65,80,70,55,75,65,80))
ideas.append(mk("xr_ev_adoption_vs_charging","EV Adoption Outpaces Charging Infrastructure","EV registrations per charging port by state","XREF","us_state","State choropleth","Transportation","DOE AFDC + IHS Markit https://afdc.energy.gov + https://www.spglobal.com/mobility/",60,70,80,60,50,75,60,80))
ideas.append(mk("xr_wildfire_cost_vs_housing_dev","Building in Fire Zones Costs Billions","Wildfire damage costs vs new housing permits in WUI areas","XREF","us_state","Bar chart","Climate","NIFC + Census Building Permits https://www.nifc.gov + https://www.census.gov/construction/bps/",70,65,80,60,65,60,65,75))
ideas.append(mk("xr_air_quality_vs_property_value","Clean Air Is Worth Money","PM2.5 levels vs median home values by metro area","XREF","us_national","Scatter plot","Environment","EPA AQS + Zillow ZHVI https://www.epa.gov/aqs + https://www.zillow.com/research/",55,65,75,55,45,60,60,85))

# ============================================================
# EDUCATION x DEMOGRAPHICS cross-refs
# ============================================================
ideas.append(mk("xr_student_debt_vs_home_ownership","Student Debt Is Killing Home Ownership","Average student debt vs home ownership rate by age group and state","XREF","us_state","Bivariate choropleth","Education","Fed Reserve SCF + Census ACS https://www.federalreserve.gov/econres/scfindex.htm + https://data.census.gov",80,85,80,60,65,85,60,80))
ideas.append(mk("xr_teacher_pay_vs_outcomes","Does Paying Teachers More Produce Better Students","Average teacher salary vs standardized test scores by state","XREF","us_state","Scatter plot","Education","NEA + NAEP https://www.nea.org/resource-library/educator-pay-and-student-spending + https://nces.ed.gov/nationsreportcard/",65,70,80,65,55,60,65,90))
ideas.append(mk("xr_school_segregation_2024","Americas Schools Are Resegregating","School racial composition vs district demographics 1990 vs 2024","XREF","us_national","Scatter plot","Education","NCES CCD + Census Decennial https://nces.ed.gov/ccd/ + https://data.census.gov",80,70,80,65,80,60,65,90))
ideas.append(mk("xr_college_degree_vs_voting","The College Degree Political Realignment","County college degree rate vs 2024 presidential vote margin","XREF","us_county","Bivariate choropleth","Elections","Census ACS + MIT Election Lab https://data.census.gov + https://electionlab.mit.edu",70,70,80,65,70,85,55,95))
ideas.append(mk("xr_library_closures_vs_poverty","Libraries Are Disappearing Where They Are Needed Most","Public library closures 2010-2024 overlaid with poverty rate","XREF","us_county","Bivariate choropleth","Education","IMLS PLS + Census ACS https://www.imls.gov/research-evaluation/data-collection/public-libraries-survey + https://data.census.gov",75,70,80,65,65,85,70,75))

# ============================================================
# TRANSPORTATION x URBAN cross-refs
# ============================================================
ideas.append(mk("xr_commute_time_vs_happiness","Long Commutes Destroy Happiness","Average commute time vs life satisfaction index by metro area","XREF","us_national","Scatter plot","Transportation","Census ACS + Gallup Wellbeing Index https://data.census.gov + https://www.gallup.com",75,85,80,55,45,60,65,80))
ideas.append(mk("xr_transit_access_vs_car_ownership","Car Dependency Mapped by County","Transit access score vs vehicles per household","XREF","us_county","Bivariate choropleth","Transportation","EPA SLD + Census ACS https://www.epa.gov/smartgrowth/smart-location-mapping + https://data.census.gov",55,70,80,55,40,85,55,90))
ideas.append(mk("xr_walkability_vs_obesity_county","Walkable Neighborhoods Have Less Obesity","Walk score vs obesity prevalence by county","XREF","us_county","Bivariate choropleth","Health","EPA Walkability Index + CDC PLACES https://www.epa.gov/smartgrowth/national-walkability-index + https://www.cdc.gov/places/",70,75,80,55,50,85,55,85))
ideas.append(mk("xr_traffic_deaths_vs_speed_limit","Higher Speed Limits Kill More People","Traffic fatality rate vs maximum speed limit by state","XREF","us_state","Scatter plot","Transportation","NHTSA FARS + IIHS https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars + https://www.iihs.org",70,70,80,55,65,60,55,90))
ideas.append(mk("xr_bike_infra_vs_bike_commute","If You Build It They Will Ride","Bike lane miles per capita vs bicycle commute share by city","XREF","us_national","Scatter plot","Transportation","PeopleForBikes + Census ACS https://www.peopleforbikes.org + https://data.census.gov",50,60,80,60,35,60,60,75))

# ============================================================
# HOUSING x DEMOGRAPHICS cross-refs
# ============================================================
ideas.append(mk("xr_housing_cost_vs_birth_rate","Expensive Housing Is Killing the Birth Rate","Housing cost burden vs fertility rate by state","XREF","us_state","Bivariate choropleth","Housing","Census ACS + CDC NVSS https://data.census.gov + https://www.cdc.gov/nchs/nvss/births.htm",80,80,80,65,65,85,65,85))
ideas.append(mk("xr_rent_burden_vs_eviction","Rent Burden Predicts Eviction Rates","Rent-burdened household share vs eviction filing rate by county","XREF","us_county","Bivariate choropleth","Housing","Census ACS + Eviction Lab https://data.census.gov + https://evictionlab.org",80,75,80,55,75,85,65,80))
ideas.append(mk("xr_zoning_vs_homelessness","Strict Zoning Causes Homelessness","Single-family zoning share vs homeless per capita by metro","XREF","us_national","Scatter plot","Housing","HUD PIT Count + Urban Institute https://www.huduser.gov/portal/datasets/ahar.html + https://www.urban.org",70,65,80,65,70,60,70,70))
ideas.append(mk("xr_airbnb_vs_rent_increase","Airbnb Is Raising Your Rent","Airbnb listing density vs rent increase 2015-2024 by zip code","XREF","us_national","Scatter plot","Housing","Inside Airbnb + Zillow ZORI https://insideairbnb.com + https://www.zillow.com/research/",70,80,80,60,65,60,65,80))
ideas.append(mk("xr_remote_work_vs_housing_migration","Remote Work Reshuffled Where Americans Live","Remote work rate change vs net migration by county 2019-2024","XREF","us_county","Bivariate choropleth","Housing","Census ACS + IRS SOI Migration https://data.census.gov + https://www.irs.gov/statistics/soi-tax-stats-migration-data",65,75,80,65,50,85,65,80))

# ============================================================
# WORLD COMPARISONS cross-refs
# ============================================================
ideas.append(mk("xr_democracy_vs_happiness","Democracy Doesnt Guarantee Happiness","Democracy index vs World Happiness Report score","XREF","worldwide","Scatter plot","International Statistics","EIU Democracy Index + WHR https://www.eiu.com/n/campaigns/democracy-index/ + https://worldhappiness.report",55,55,80,70,55,60,70,90))
ideas.append(mk("xr_military_spend_vs_education","Countries That Choose Guns Over Books","Military spending share vs education spending share of GDP","XREF","worldwide","Scatter plot","International Statistics","SIPRI + World Bank https://www.sipri.org/databases/milex + https://data.worldbank.org",65,55,80,70,70,60,65,90))
ideas.append(mk("xr_internet_freedom_vs_gdp","Internet Censorship Doesnt Help Economies","Freedom on the Net score vs GDP growth","XREF","worldwide","Scatter plot","Science & Technology","Freedom House + World Bank https://freedomhouse.org/report/freedom-net + https://data.worldbank.org",55,50,80,65,60,60,70,85))
ideas.append(mk("xr_gender_equality_vs_fertility","Gender Equality Paradox in Fertility","Gender Inequality Index vs total fertility rate by country","XREF","worldwide","Scatter plot","Demographics","UNDP HDR + World Bank https://hdr.undp.org + https://data.worldbank.org",55,55,80,75,50,60,75,90))
ideas.append(mk("xr_corruption_vs_co2","Corrupt Countries Pollute More","Corruption Perceptions Index vs CO2 per capita","XREF","worldwide","Scatter plot","Environment","Transparency International + OWID CO2 https://www.transparency.org + https://github.com/owid/co2-data",55,45,75,70,55,60,70,90))
ideas.append(mk("xr_press_freedom_vs_trust","Countries With Free Press Have Higher Trust","Press Freedom Index vs generalized trust survey","XREF","worldwide","Scatter plot","International Statistics","RSF + World Values Survey https://rsf.org/en/index + https://www.worldvaluessurvey.org",50,50,75,65,55,60,70,80))

# ============================================================
# FOOD x GEOGRAPHY cross-refs
# ============================================================
ideas.append(mk("xr_fast_food_density_vs_diabetes","Fast Food Density Predicts Diabetes by County","Fast food restaurants per capita vs diabetes prevalence","XREF","us_county","Bivariate choropleth","Food & Nutrition","Census CBP + CDC PLACES https://www.census.gov/programs-surveys/cbp.html + https://www.cdc.gov/places/",75,80,80,55,55,85,55,90))
ideas.append(mk("xr_farm_subsidy_vs_crop_diversity","Subsidies Kill Crop Diversity","USDA subsidy amount vs crop diversity index by county","XREF","us_county","Bivariate choropleth","Food & Nutrition","EWG Farm Subsidies + USDA NASS https://farm.ewg.org + https://www.nass.usda.gov/",55,50,75,65,50,85,70,80))
ideas.append(mk("xr_food_waste_vs_hunger","America Wastes 30% of Its Food While 13% Go Hungry","Food waste tonnage vs food insecurity rate by state","XREF","us_state","Bivariate choropleth","Food & Nutrition","USDA ERS + ReFED https://www.ers.usda.gov + https://refed.org",80,75,80,60,75,85,60,75))
ideas.append(mk("xr_organic_farm_vs_income","Organic Farms Cluster in Wealthy Counties","Organic farm share vs median household income","XREF","us_county","Bivariate choropleth","Food & Nutrition","USDA Census of Agriculture + Census ACS https://www.nass.usda.gov/ + https://data.census.gov",45,55,75,55,35,85,55,85))

# ============================================================
# TECHNOLOGY x SOCIAL cross-refs
# ============================================================
ideas.append(mk("xr_broadband_vs_telehealth","No Internet No Doctor","Broadband access vs telehealth utilization by county","XREF","us_county","Bivariate choropleth","Science & Technology","FCC Broadband Map + CDC PLACES https://broadbandmap.fcc.gov + https://www.cdc.gov/places/",70,70,80,55,55,85,60,80))
ideas.append(mk("xr_social_media_vs_teen_depression","Teen Depression Tracks Social Media Adoption","Social media usage rate vs teen depression diagnoses 2010-2024","XREF","us_national","Scatter plot","Health","Pew Research + SAMHSA NSDUH https://www.pewresearch.org + https://www.samhsa.gov/data/",80,80,80,55,70,60,55,85))
ideas.append(mk("xr_ai_jobs_vs_displacement","AI Job Creation vs Displacement by Industry","New AI-related job postings vs automation-displaced positions","XREF","us_national","Bar chart","Science & Technology","BLS OES + Indeed Hiring Lab https://www.bls.gov/oes/ + https://www.hiringlab.org",60,65,75,70,65,55,70,65))
ideas.append(mk("xr_stem_graduates_vs_innovation","STEM Grads Dont Guarantee Innovation","STEM degree share vs patent applications per capita by country","XREF","worldwide","Scatter plot","Science & Technology","UNESCO UIS + WIPO https://data.uis.unesco.org + https://www.wipo.int/ipstats/",50,50,75,70,45,60,70,85))

# ============================================================
# SPORTS x DEMOGRAPHICS cross-refs
# ============================================================
ideas.append(mk("xr_stadium_subsidy_vs_poverty","Billion Dollar Stadiums in Americas Poorest Cities","Public stadium subsidy amount vs city poverty rate","XREF","us_national","Scatter plot","Sports & Recreation","Brookings + Census ACS https://www.brookings.edu + https://data.census.gov",70,65,80,70,75,60,70,75))
ideas.append(mk("xr_youth_sports_cost_vs_income","Youth Sports Have Become a Rich Kids Game","Average youth sports spending vs household income by metro","XREF","us_national","Scatter plot","Sports & Recreation","Aspen Institute + BLS CE https://www.aspenprojectplay.org + https://www.bls.gov/cex/",75,80,80,60,60,60,65,70))
ideas.append(mk("xr_nfl_injuries_vs_rule_changes","NFL Concussions vs Rule Changes Timeline","Reported concussions per season overlaid with major rule changes","XREF","us_national","Bar chart","Sports & Recreation","NFL Injury Reports + Football Operations https://www.nfl.com/playerhealthandsafety/",65,70,80,55,55,55,60,80))

# ============================================================
# ELECTIONS x ECONOMY cross-refs
# ============================================================
ideas.append(mk("xr_gas_price_vs_incumbent","Gas Prices Predict Presidential Elections","Average gas price trend vs incumbent party vote share 1976-2024","XREF","us_national","Scatter plot","Elections","EIA Gas Prices + MIT Election Lab https://www.eia.gov + https://electionlab.mit.edu",65,75,80,65,55,60,65,90))
ideas.append(mk("xr_county_flip_vs_job_loss","Counties That Flipped Red Lost Manufacturing Jobs","County partisan flip 2012-2024 vs manufacturing job change","XREF","us_county","Bivariate choropleth","Elections","MIT Election Lab + BLS QCEW https://electionlab.mit.edu + https://www.bls.gov/cew/",75,70,80,65,70,85,65,85))
ideas.append(mk("xr_voter_turnout_vs_income","Rich People Vote Poor People Dont","Voter turnout vs median household income by county","XREF","us_county","Bivariate choropleth","Elections","EAC EAVS + Census ACS https://www.eac.gov/research-and-data/datasets-codebooks-and-surveys + https://data.census.gov",70,70,80,55,65,85,55,90))
ideas.append(mk("xr_gerrymandering_vs_competitiveness","Gerrymandering Has Killed Competitive Elections","Compactness score vs margin of victory by congressional district","XREF","us_national","Scatter plot","Elections","DRA + Cook PVI https://davesredistricting.org + https://www.cookpolitical.com",65,60,80,65,70,60,70,80))

# ============================================================
# HISTORY x MODERN cross-refs
# ============================================================
ideas.append(mk("xr_redlining_vs_tree_cover","1930s Redlining Still Visible in Tree Cover Today","HOLC grade vs tree canopy percentage by census tract","XREF","us_national","Scatter plot","History","Mapping Inequality + NLCD https://dsl.richmond.edu/panorama/redlining/ + https://www.mrlc.gov",80,65,80,80,65,60,80,80))
ideas.append(mk("xr_slavery_1860_vs_poverty_today","The Shadow of Slavery in County Poverty Rates","1860 enslaved population share vs 2024 poverty rate by county","XREF","us_county","Bivariate choropleth","History","Census 1860 + Census ACS 2024 https://www.nhgis.org + https://data.census.gov",85,65,80,75,85,85,75,85))
ideas.append(mk("xr_sundown_towns_vs_demographics","Former Sundown Towns Are Still Mostly White","Historical sundown town designation vs non-white population share","XREF","us_national","Scatter plot","History","Sundown Towns Database + Census ACS https://sundown.tougaloo.edu + https://data.census.gov",80,60,80,70,80,60,80,70))
ideas.append(mk("xr_interstate_highways_vs_black_neighborhoods","Highways Were Built Through Black Neighborhoods","Interstate routing vs historical Black population density","XREF","us_national","Special map","History","FHWA + Census 1950 https://www.fhwa.dot.gov + https://www.nhgis.org",80,60,80,75,80,75,80,70))
ideas.append(mk("xr_dust_bowl_migration_vs_california_today","Dust Bowl Migration Routes Echo in Californias Culture","1930s migration patterns vs modern cultural and economic geography","XREF","us_state","Special map","History","Census Historical + HSUS https://www.nhgis.org + Historical Statistics of the US",55,55,75,65,40,70,75,65))

# ============================================================
# LABOR x ECONOMY cross-refs
# ============================================================
ideas.append(mk("xr_union_density_vs_wages","Unions Disappear and Wages Stagnate","Union membership rate vs real median wage 1950-2024","XREF","us_national","Scatter plot","Labor","BLS Union Membership + BLS CES https://www.bls.gov/news.release/union2.toc.htm + https://www.bls.gov/ces/",75,70,80,60,60,60,55,95))
ideas.append(mk("xr_gig_economy_vs_benefits","Gig Workers Dont Get Benefits","Gig economy share vs employer-provided insurance rate by state","XREF","us_state","Bivariate choropleth","Labor","BLS Contingent Worker Survey + Census ACS https://www.bls.gov/cps/lfcharacteristics.htm + https://data.census.gov",70,75,80,55,60,85,60,70))
ideas.append(mk("xr_automation_risk_vs_education","Jobs Most at Risk of Automation Are in Low-Education Counties","Automation risk score vs college degree rate by county","XREF","us_county","Bivariate choropleth","Labor","Brookings Automation + Census ACS https://www.brookings.edu + https://data.census.gov",70,70,80,65,65,85,65,80))
ideas.append(mk("xr_childcare_cost_vs_female_labor","Expensive Childcare Keeps Mothers Out of Work","Childcare cost as percent of income vs female labor force participation by state","XREF","us_state","Bivariate choropleth","Labor","DOL Childcare + BLS LFPS https://www.dol.gov/agencies/wb/topics/childcare + https://www.bls.gov/lau/",75,80,80,55,60,85,60,80))

# ============================================================
# INJECTION LOGIC
# ============================================================
print(f"[BATCH_GI] {len(ideas)} ideas ready")

with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()

existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
new_ideas = []
skipped = 0
for idea in ideas:
    m = re.search(r'id:"([^"]+)"', idea)
    if m and m.group(1) not in existing_ids:
        new_ideas.append(idea)
    else:
        skipped += 1

tail = "]; // end D"
if tail not in raw:
    print("[BATCH_GI] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GI] Injected {len(new_ideas)} new ideas ({skipped} dupes skipped)")
