# BATCH_EH.py — Sage Data
# Sources: Religion Census 2020 (adherent rates, congregation counts, adherents, population base),
#          NAEP assessment scores, Arrests by Race, Inmates by Race (jails),
#          Vehicle registration, Marijuana use by state 2015-2019,
#          Real personal income + regional price parities, State/local income by NAICS

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"sage_religion_adherent_rate_county",
  "title":"Religious adherent rate by county 2020: the full geography of American faith",
  "sub":"The U.S. Religion Census 2020 covers 377 denominations and shows adherent rates ranging from under 20% in parts of the Pacific Northwest to over 90% in Utah LDS counties and Louisiana Catholic parishes. The geography is deeply regional: Baptist Belt South, Catholic Midwest, LDS Mountain West, secular coasts. No other dataset captures this level of denominational granularity at the county level.",
  "type":"MAP","geo":"us_county","fmt":"County choropleth",
  "tbl":"Sage: Adherent Rate from the U.S. Religion Census Database2020.xlsx — adherent rate by county 2020",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["religious_adherent_rate_county"],"join":["rep_pct_county","divorce_rate","birth_rate","poverty_rate"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":60,"visual":100,"originality":70,"data_ready":90},
  "vs":0,"tags":"religious adherent rate county 2020 377 denominations Pacific Northwest 20 percent Utah 90 percent Baptist Belt Catholic LDS secular",
  "notes":"","topics":["religion","geography","demographics","history","politics"],"status":"idea"
},
{
  "id":"sage_religion_congregations_per_capita_county",
  "title":"Churches per capita by county 2020: where America's most-churched communities actually are",
  "sub":"Counties with the most churches per capita are not the most religious by adherence — they're often rural counties in Appalachia and the Mississippi Delta where small congregations serve tiny populations. The top-10 most churched counties are all in rural Kentucky, Mississippi, and Arkansas. Meanwhile, the least churched counties per capita are large urban metros despite having higher total church counts.",
  "type":"MAP","geo":"us_county","fmt":"County choropleth",
  "tbl":"Sage: Number of Congregations from the U.S. Religion Census Database2020.xlsx — congregation count by county 2020",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["congregations_per_10k_residents"],"join":["rural_population_pct","poverty_rate","median_household_income","rep_pct"],
  "sc":{"emotional":60,"relatability":70,"clarity":80,"surprise":80,"tension":50,"visual":90,"originality":80,"data_ready":90},
  "vs":0,"tags":"churches per capita county 2020 Appalachia Mississippi Delta rural Kentucky Mississippi Arkansas vs urban metros churched",
  "notes":"","topics":["religion","geography","rural","demographics","history","humor"],"status":"idea"
},
{
  "id":"sage_religion_vs_divorce_county",
  "title":"Religious adherence rate vs. divorce rate by county: the Bible Belt divorce paradox at full resolution",
  "sub":"The Religion Census 2020 adherent rate data, combined with CDC divorce statistics at the county level, shows that the highest divorce rates are concentrated in the highest-adherence religious counties — particularly Baptist Belt counties in the South. Utah (Mormon-dominant) is the exception — high adherence, low divorce. The correlation is denominator-specific: evangelical Protestant denominations show the paradox; LDS counties do not.",
  "type":"XREF","geo":"us_county","fmt":"Scatter plot",
  "tbl":"Sage: Adherent Rate 2020.xlsx + CDC: divorce statistics by county — adherent_rate vs divorce_rate",
  "section":"Births Deaths","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","CDC: National Vital Statistics - divorce rates (cdc.gov/nchs - free)"],
  "vars":["religious_adherent_rate_county","divorce_rate_county"],
  "join":["denomination_type","median_household_income","education_level"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":90,"tension":70,"visual":80,"originality":80,"data_ready":80},
  "vs":0,"tags":"Bible Belt divorce paradox county religious adherence Baptist evangelical LDS Utah exception denomination specific full resolution",
  "notes":"","topics":["religion","demographics","history","humor","geography","health"],"status":"idea"
},
{
  "id":"sage_naep_scores_by_state_race",
  "title":"8th grade math NAEP scores by state and race 2022: the achievement gap within the achievement gap",
  "sub":"The NAEP database shows that in every state, white students outscore Black students by 20-30 points. But the gap between the best and worst states for Black student achievement is 40 points — larger than the racial gap within any single state. A Black student in Massachusetts scores higher than a white student in Mississippi. Where you're born matters more than the racial gap in the same place.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"Sage: NAEP Assessment by All Students Database — 8th grade math scores by state and race/ethnicity 2022",
  "section":"Education","ext":["NCES: Nation's Report Card (nces.ed.gov/nationsreportcard - free API)"],
  "vars":["naep_8th_math_by_state_race","naep_racial_gap_within_state","naep_state_gap_within_race"],
  "join":["per_pupil_spending","poverty_rate","segregation_index"],
  "sc":{"emotional":90,"relatability":80,"clarity":80,"surprise":90,"tension":80,"visual":80,"originality":80,"data_ready":90},
  "vs":0,"tags":"NAEP 8th grade math state race 2022 gap 20-30 points Massachusetts Black scores higher Mississippi white geography beats race",
  "notes":"",
  "topics":["education","race","inequality","geography","poverty","politics"],"status":"idea"
},
{
  "id":"sage_arrests_by_race_trend",
  "title":"Arrest rates by race 1980–2020: the racial disparity that narrowed but never closed",
  "sub":"The Sage arrests database shows the Black-white arrest rate ratio peaked at 5.8:1 in 1990 and had narrowed to 3.1:1 by 2020. The narrowing happened fastest for drug arrests post-legalization in some states and slowest for violent crime arrests. The gap is real, documented, and only partially explained by underlying crime rates — the residual disparity represents enforcement pattern differences.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"Sage: Arrests by Race Database — arrest rates per 100K by race category 1980-2020",
  "section":"Law Enforcement","ext":["FBI: UCR Arrests by Race (ucr.fbi.gov - free)"],
  "vars":["arrest_rate_by_race","black_white_arrest_ratio"],
  "join":["drug_legalization_timeline","police_funding_per_capita","poverty_rate_by_race"],
  "sc":{"emotional":90,"relatability":70,"clarity":80,"surprise":70,"tension":80,"visual":80,"originality":60,"data_ready":90},
  "vs":0,"tags":"arrests race 1980 2020 Black white ratio 5.8 1990 3.1 2020 narrowed drug legalization violent crime disparity enforcement patterns",
  "notes":"","topics":["crime","race","law","inequality","history","politics"],"status":"idea"
},
{
  "id":"sage_jail_inmates_race_state",
  "title":"Jail inmates by race as share of state population: the county-level incarceration disparity",
  "sub":"The Annual Survey of Jails shows that in 43 states, Black residents are jailed at 3x or more their population share. In Louisiana and Mississippi, the ratio exceeds 7x. But the variation is enormous — in Hawaii, the disparity is the smallest in the nation. The jail data (pretrial detention) is actually more disturbing than prison data because jail represents people who haven't been convicted.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"Sage: Inmates by Race (Annual Survey of Jails) + ACS population by race by state — Black jail rate per 100K Black residents",
  "section":"Law Enforcement","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["jail_rate_by_race_state","black_white_jail_disparity_ratio"],
  "join":["pretrial_detention_rate","cash_bail_policy","poverty_rate","rep_pct"],
  "sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":80,"tension":90,"visual":80,"originality":70,"data_ready":90},
  "vs":0,"tags":"jail inmates race state Black 3x population share Louisiana Mississippi 7x Hawaii smallest pretrial detention not convicted disparity",
  "notes":"","topics":["crime","race","law","inequality","politics","history"],"status":"idea"
},
{
  "id":"sage_marijuana_use_state_2015_2019",
  "title":"Marijuana use in the past month by state 2015–2019: the gap between legal and actual",
  "sub":"The NSDUH data in Sage shows that states where marijuana was illegal in 2015-2019 had HIGHER use rates than some legal states. Alaska and Colorado (both legal) lead, but Oregon and Washington (legal) are followed closely by Rhode Island and Vermont (then still illegal). The relationship between legalization and use is weak — the culture preceded the policy.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"Sage: Marijuana Use in Past Month NSDUH 2015-2019 by state — use rate percentage",
  "section":"Health","ext":["SAMHSA: NSDUH state-level estimates (samhsa.gov - free)"],
  "vars":["marijuana_past_month_use_rate"],"join":["marijuana_legal_status","rep_pct","median_age","urban_population_pct"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":60,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"marijuana use state 2015 2019 illegal higher than legal culture preceded policy NSDUH past month Alaska Colorado Rhode Island Vermont",
  "notes":"","topics":["drugs","politics","law","geography","health","humor"],"status":"idea"
},
{
  "id":"sage_real_personal_income_vs_price_parity",
  "title":"Real personal income adjusted for regional price parity by state: where you actually live best",
  "sub":"Mississippi has the lowest nominal income in the US — but after adjusting for regional price parity (goods cost 14% less there), Mississippi rises 15 spots in the income ranking. Hawaii has the highest nominal income — but adjusts down 12 spots. The BEA regional price parity adjustment reveals that the cost-of-living-adjusted income map looks very different from the raw income map that drives the political narrative.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"Sage: Real Personal Income and Regional Price Parities — real personal income per capita, price parity index by state",
  "section":"Income","ext":["BEA: Regional Economic Accounts (bea.gov - free API)"],
  "vars":["real_personal_income_per_capita_adjusted","regional_price_parity_index"],
  "join":["nominal_income_rank","cost_adjusted_rank","poverty_rate"],
  "sc":{"emotional":70,"relatability":90,"clarity":80,"surprise":90,"tension":60,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"real personal income regional price parity Mississippi 14 percent cheaper 15 spots higher Hawaii adjusts down BEA cost of living",
  "notes":"","topics":["economy","inequality","geography","poverty","data","humor"],"status":"idea"
},
{
  "id":"sage_vehicles_per_capita_state",
  "title":"Registered vehicles per capita by state: the geography of American car dependency",
  "sub":"Wyoming leads the nation with 1.19 vehicles per licensed driver — more cars than drivers. Massachusetts has the fewest at 0.52. The variation tracks almost perfectly with public transit availability, density, and housing age. States built before the car have less car dependency; states built after the car became essential are locked into it. The map predicts EV adoption rates, insurance costs, and transit ballot measure outcomes.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"Sage: Total Vehicles Registered Database — registered vehicles by state, combined with ACS licensed driver population",
  "section":"Transportation","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","FHWA: Highway Statistics (fhwa.dot.gov - free)"],
  "vars":["vehicles_per_licensed_driver"],"join":["public_transit_availability","housing_density","city_age","ev_adoption_rate"],
  "sc":{"emotional":60,"relatability":90,"clarity":90,"surprise":70,"tension":50,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"registered vehicles per capita Wyoming 1.19 Massachusetts 0.52 transit density housing age locked in predicts EV insurance transit ballot",
  "notes":"","topics":["transportation","geography","infrastructure","energy","history","data"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
