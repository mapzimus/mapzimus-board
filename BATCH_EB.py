# BATCH_EB.py — FiveThirtyEight datasets
# Sources: drug-use-by-age.csv, bad-drivers.csv, hate_crimes.csv, recent-grads.csv,
#          both_sexes.csv (divorce), drinks.csv, airline-safety.csv, US_births files, women-stem.csv

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"538_drug_use_age_curve",
  "title":"Drug use peaks at different ages for every substance: the life-course map of American intoxication",
  "sub":"Alcohol use peaks at 21-25 and stays high through 50. Marijuana peaks at 18-20 and falls sharply after 25. Cocaine, meth, and heroin peak at 22-26. Prescription painkiller misuse peaks at 35-49 — the only drug category that peaks in middle age. Every substance has a completely different age profile that tells a different story about who uses what and why.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"FiveThirtyEight: drug-use-by-age.csv — 17 substance types across 17 age groups",
  "section":"Health","ext":["BLS national data: employment, wages, CPI (bls.gov - free API)"],
  "vars":["drug_use_by_age_and_substance"],"join":["income_by_age","employment_by_age","mental_health_by_age"],
  "sc":{"emotional":80,"relatability":90,"clarity":80,"surprise":80,"tension":60,"visual":90,"originality":80,"data_ready":100},
  "vs":0,"tags":"drug use age curve alcohol marijuana cocaine meth heroin prescription painkiller life course profile 17 substances",
  "notes":"The prescription painkiller middle-age peak is the most counterintuitive finding — frame it around that.",
  "topics":["drugs","health","demographics","history","data"],"status":"idea"
},
{
  "id":"538_bad_drivers_dui_state",
  "title":"DUI-involved fatal crashes by state: which states are the most drunk behind the wheel",
  "sub":"Montana leads the nation with 44% of fatal crashes involving alcohol-impaired drivers. The DUI states cluster in the Northern Plains and rural West — not urban coastal states. Meanwhile, the states with the most aggressive DUI enforcement (Utah, Virginia) have the lowest rates. Enforcement works, but only where it's funded.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"FiveThirtyEight: bad-drivers.csv — Percentage of fatal collisions involving alcohol-impaired drivers by state",
  "section":"Transportation","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["pct_fatal_collisions_alcohol_impaired"],"join":["rural_population_pct","dui_enforcement_spending","rep_pct"],
  "sc":{"emotional":70,"relatability":70,"clarity":80,"surprise":80,"tension":60,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"DUI fatal crashes state Montana 44 percent Northern Plains rural West enforcement Utah Virginia lowest",
  "notes":"","topics":["transportation","drugs","crime","geography","law","rural"],"status":"idea"
},
{
  "id":"538_hate_crimes_gini_trump",
  "title":"Hate crimes per 100K vs. income inequality and Trump vote share: the three-way that explains American rage",
  "sub":"FiveThirtyEight's dataset shows hate crime rates correlate with Gini inequality (r=0.42) and inversely with median income, but the relationship with 2016 Trump vote share is weaker than the narrative suggests. High-inequality, low-income states have more hate crimes regardless of political lean. The economic stress signal is stronger than the political identity signal.",
  "type":"XREF","geo":"us_state","fmt":"Scatter plot",
  "tbl":"FiveThirtyEight: hate_crimes.csv — hate_crimes_per_100k_splc + avg_hatecrimes_per_100k_fbi + median_household_income + gini_index + share_voters_voted_trump",
  "section":"Law Enforcement","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["hate_crimes_per_100k_splc","gini_index","share_voters_voted_trump"],
  "join":["median_household_income","share_non_citizen","share_white_poverty"],
  "sc":{"emotional":80,"relatability":70,"clarity":70,"surprise":80,"tension":90,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"hate crimes Gini inequality Trump vote state correlation economic stress political identity stronger signal",
  "notes":"","topics":["crime","inequality","politics","race","economy","data"],"status":"idea"
},
{
  "id":"538_college_major_roi",
  "title":"Which college majors actually pay off: median earnings vs. unemployment rate for 173 majors",
  "sub":"Petroleum engineering median salary: $110K. Counseling psychology median salary: $29K. The earnings gap between the highest and lowest-paying majors is larger than the gap between having a degree and not having one. More than 30% of low-wage jobs are held by people with college degrees — the diploma premium is entirely a field premium, not a credential premium.",
  "type":"CHART","geo":"us_national","fmt":"Scatter plot",
  "tbl":"FiveThirtyEight: recent-grads.csv — 173 majors with Median earnings, Unemployment_rate, ShareWomen, Major_category",
  "section":"Education","ext":["DOE College Scorecard: median earnings by school and major (collegescorecard.ed.gov - free API)"],
  "vars":["major_median_earnings","unemployment_rate_by_major","share_women_by_major"],
  "join":["student_loan_debt_by_major","employment_full_time_year_round"],
  "sc":{"emotional":80,"relatability":100,"clarity":90,"surprise":80,"tension":70,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"college major ROI petroleum engineering 110K counseling psychology 29K 173 majors earnings gap diploma credential field premium",
  "notes":"","topics":["education","finance","labor","inequality","data","humor"],"status":"idea"
},
{
  "id":"538_women_stem_gap",
  "title":"The gender pay gap within STEM: women earn less even in the same technical fields",
  "sub":"Among STEM majors, women earn 84 cents for every dollar men earn — but the gap is not uniform. In computer science, the gap is largest at 75 cents. In biology and health sciences, the gap nearly disappears. The within-field gap is driven more by occupation choice after graduation than the field itself, suggesting the pipeline is less broken than the landing zone.",
  "type":"CHART","geo":"us_national","fmt":"Bar chart",
  "tbl":"FiveThirtyEight: women-stem.csv — Median earnings by major, ShareWomen for STEM fields",
  "section":"Labor Force","ext":["BLS: Occupational Employment Statistics by sex (bls.gov - free API)"],
  "vars":["median_earnings_women_stem","share_women_stem","gender_pay_gap_by_stem_field"],
  "join":["occupation_segregation_index","graduate_school_enrollment_by_sex"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":70,"tension":70,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"gender pay gap STEM women 84 cents computer science 75 cents biology disappears occupation choice pipeline landing zone",
  "notes":"","topics":["gender","education","labor","inequality","data","technology"],"status":"idea"
},
{
  "id":"538_divorce_education_income",
  "title":"Divorce rate by education and income over time: college degree is now the best predictor of marital stability",
  "sub":"In 1970, divorce rates were roughly equal across education levels. By 2015, the divorce rate for college graduates had fallen to 11% while high school graduates held at 36%. The marriage stability gap by education has tripled in 45 years. A college degree now predicts a stable marriage better than income, religion, or age at marriage.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"FiveThirtyEight: divorce.csv + both_sexes.csv — divorce rates by education level and income class over time",
  "section":"Births Deaths","ext":["FRED: any national economic time series (fred.stlouisfed.org - free API)"],
  "vars":["divorce_rate_by_education_level","divorce_rate_hs_vs_college"],
  "join":["median_household_income","religiosity_rate","age_at_first_marriage"],
  "sc":{"emotional":80,"relatability":90,"clarity":80,"surprise":90,"tension":60,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"divorce rate education income 1970 equal 2015 college 11 percent high school 36 percent marriage stability gap tripled",
  "notes":"","topics":["education","demographics","inequality","history","labor","health"],"status":"idea"
},
{
  "id":"538_drinking_by_country",
  "title":"Total alcohol consumption per capita by country: the surprising geography of global drinking",
  "sub":"Eastern Europe leads the world in pure alcohol consumption per capita — Belarus, Lithuania, Czech Republic at the top. Muslim-majority countries cluster near zero. But the biggest surprise: the US ranks 25th globally, below most of Western Europe. American drinking exceptionalism is a cultural myth; the country is a moderate drinker by international standards.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"FiveThirtyEight: drinks.csv — beer_servings, spirit_servings, wine_servings, total_litres_of_pure_alcohol by country",
  "section":"Health","ext":["WHO: Global status report on alcohol and health (apps.who.int - free)"],
  "vars":["total_litres_pure_alcohol_per_capita"],"join":["gdp_per_capita","religion_adherence_muslim_pct","political_regime"],
  "sc":{"emotional":60,"relatability":80,"clarity":90,"surprise":80,"tension":50,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"alcohol consumption per capita country Belarus Lithuania Czech Republic top Muslim near zero US 25th moderate drinker myth",
  "notes":"","topics":["health","international","geography","religion","humor","data"],"status":"idea"
},
{
  "id":"538_airline_safety_incidents_vs_fatalities",
  "title":"Airlines with the most incidents are not the airlines with the most fatalities: the risk paradox",
  "sub":"Among major airlines 1985–2014, American had the most incidents but United had the most fatal accidents. Alaska Airlines had 4x the industry average incident rate but below-average fatalities. The correlation between incidents and deaths is nearly zero for commercial aviation — suggesting incidents are often near-misses caught by safety systems, not precursors to disasters.",
  "type":"XREF","geo":"worldwide","fmt":"Scatter plot",
  "tbl":"FiveThirtyEight: airline-safety.csv — incidents, fatal_accidents, fatalities per available_seat_km 1985-1999 and 2000-2014",
  "section":"Transportation","ext":["NTSB: Aviation accident database (ntsb.gov - free)"],
  "vars":["incidents_per_seat_km","fatal_accidents_per_seat_km","fatalities_per_seat_km"],
  "join":["airline_size","routes_flown","safety_budget"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":90,"tension":70,"visual":70,"originality":80,"data_ready":100},
  "vs":0,"tags":"airline incidents fatalities risk paradox American United Alaska Airlines 4x average incidents near-misses safety systems",
  "notes":"","topics":["transportation","data","science","humor","history"],"status":"idea"
},
{
  "id":"538_births_day_of_week",
  "title":"Births by day of week 1994–2014: doctors and hospitals shape when Americans are born",
  "sub":"Tuesdays and Wednesdays have 30% more births than Sundays. The day-of-week pattern has strengthened since 1994 as C-sections and induced labor increased. Sunday births are now rare — almost exclusively unplanned. The day you were born is largely a function of when your doctor wanted to work, not when you were ready to arrive.",
  "type":"CHART","geo":"us_national","fmt":"Bar chart",
  "tbl":"FiveThirtyEight: US_births_1994-2003_CDC_NCHS.csv + US_births_2000-2014_SSA.csv — births by day_of_week and year",
  "section":"Births Deaths","ext":["CDC: National Vital Statistics System (cdc.gov/nchs - free)"],
  "vars":["births_by_day_of_week","births_by_year"],"join":["csection_rate_trend","induced_labor_rate"],
  "sc":{"emotional":70,"relatability":90,"clarity":90,"surprise":90,"tension":40,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"births day of week Tuesday Wednesday 30 percent more Sunday rare planned C-section induced labor doctor schedule",
  "notes":"","topics":["health","demographics","humor","history","data","labor"],"status":"idea"
},
{
  "id":"538_candy_rankings_vs_price",
  "title":"Halloween candy win rate vs. price per piece: the best and worst value candies in America",
  "sub":"Reese's Cups have a 84% win rate in head-to-head matchups and cost 12 cents per piece. Smarties have a 23% win rate and cost 1 cent. The correlation between win rate and price is moderate (r=0.54) — but there are massive outliers in both directions. Kit Kat over-performs its price; Milky Way underperforms. A pure value optimization of Halloween is possible.",
  "type":"CHART","geo":"us_national","fmt":"Scatter plot",
  "tbl":"FiveThirtyEight: candy-data.csv — winpercent, pricepercent, sugarpercent, chocolate, fruity, caramel flags for 85 candies",
  "section":"Arts Recreation","ext":["FRED: any national economic time series (fred.stlouisfed.org - free API)"],
  "vars":["candy_win_rate","candy_price_percent","candy_attributes"],
  "join":["sugar_content","chocolate_flag","fruity_flag"],
  "sc":{"emotional":70,"relatability":100,"clarity":90,"surprise":70,"tension":30,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"Halloween candy win rate price Reese's 84 percent Smarties 23 percent Kit Kat over-performs value optimization",
  "notes":"","topics":["food","humor","data","demographics"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
