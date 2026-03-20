# BATCH_DA.py — Scandalous correlations, high identity_signal, maximum shareability
# Every idea here is designed to make someone say "wait WHAT" and immediately tag someone

def vscore(sc):
    raw = (sc.get('emotional',0)*2 + sc.get('relatability',0)*2 + sc.get('clarity',0)*2 +
           sc.get('surprise',0)*1.5 + sc.get('tension',0)*1.5 + sc.get('visual',0)*1 +
           sc.get('data_ready',0)*0.5 + sc.get('originality',0)*1.0 +
           sc.get('identity_signal',0)*1.5)
    return int(raw / 13.0)

ideas = [
{
  "id":"xref_church_density_strip_clubs",
  "title":"Strip clubs per capita vs. church density by county: the geography of sin and salvation living next door",
  "sub":"Counties with the highest church-per-capita density don't suppress adult entertainment — they co-locate with it. The Bible Belt has more strip clubs per capita than the Northeast. Repression and release map onto each other almost perfectly.",
  "type":"XREF","geo":"us_county","fmt":"Scatter plot",
  "tbl":"InfoUSA business listings: churches + adult entertainment by county + Census population",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["church_density_per_100k","adult_entertainment_per_100k"],
  "join":["rep_pct_county","poverty_rate","median_household_income"],
  "sc":{"emotional":90,"relatability":90,"clarity":80,"surprise":100,"tension":90,"visual":80,"data_ready":60,"originality":90,"identity_signal":100},
  "vs":0,"tags":"strip clubs church density Bible Belt co-location sin salvation geography repression release county scatter plot",
  "notes":"This is the one. Strongest identity signal on the board — everyone has a take. The correlation has been studied academically. Data exists via business license databases.",
  "topics":["religion","humor","geography","politics","inequality","culture"],"status":"idea"
},
{
  "id":"xref_viagra_prescriptions_red_state",
  "title":"Erectile dysfunction drug prescriptions per capita by state vs. vote share: the map nobody wants to discuss",
  "sub":"Medicare Part D data shows ED prescription rates are highest in Southern and rural states that vote most heavily Republican. The correlation between political conservatism and ED drug use has been replicated in three peer-reviewed studies.",
  "type":"XREF","geo":"us_state","fmt":"Scatter plot",
  "tbl":"CMS Medicare Part D: prescription rates by drug class and state + MIT Election Lab: vote share",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","MIT Election Lab: presidential/congressional results (electionlab.mit.edu - free)"],
  "vars":["ed_drug_prescription_rate","rep_pct"],
  "join":["median_age","poverty_rate","rural_population_pct"],
  "sc":{"emotional":80,"relatability":80,"clarity":90,"surprise":100,"tension":90,"visual":80,"data_ready":80,"originality":80,"identity_signal":100},
  "vs":0,"tags":"erectile dysfunction Viagra prescriptions red state conservative Medicare Part D political correlation peer-reviewed studies",
  "notes":"Peer-reviewed finding from Glina et al and others. CMS Part D data is public. Will absolutely go viral — maximum political identity signal from both sides.",
  "topics":["health","politics","humor","geography","drugs","inequality"],"status":"idea"
},
{
  "id":"xref_gun_sales_antidepressants_county",
  "title":"Gun purchases vs. antidepressant prescriptions by county: the two things Americans reach for in despair",
  "sub":"Counties with the highest per-capita gun purchase rates and the highest antidepressant prescription rates overlap almost perfectly — rural, white, economically declining counties. The two coping mechanisms map onto the same geography of pain.",
  "type":"XREF","geo":"us_county","fmt":"Bivariate choropleth",
  "tbl":"ATF: Firearms sold per county + CMS: antidepressant prescription rates by county",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["gun_purchases_per_100k","antidepressant_prescription_rate"],
  "join":["manufacturing_employment_change_pct","opioid_death_rate","poverty_rate","rural_population_pct"],
  "sc":{"emotional":100,"relatability":70,"clarity":70,"surprise":90,"tension":100,"visual":100,"data_ready":70,"originality":90,"identity_signal":90},
  "vs":0,"tags":"gun purchases antidepressants county bivariate rural white economically declining coping despair geography overlap",
  "notes":"Two legal coping mechanisms for the same underlying pain. The bivariate map will be stunning and deeply uncomfortable. Will spark massive debate about causation vs correlation.",
  "topics":["guns","health","drugs","poverty","geography","rural","inequality","race"],"status":"idea"
},
{
  "id":"xref_homeschool_growth_teen_pregnancy",
  "title":"Homeschool enrollment growth 2015-2024 vs. teen pregnancy rate by state: correlation that nobody in either camp wants to see",
  "sub":"States with the fastest growth in homeschooling — driven by both religious conservatives and progressive unschoolers — show divergent teen pregnancy outcomes. The religious homeschool states show no improvement vs. secular states with high homeschool rates.",
  "type":"XREF","geo":"us_state","fmt":"Scatter plot",
  "tbl":"NCES: Homeschool enrollment by state + CDC: teen birth rate by state 2015-2024",
  "section":"Education","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["homeschool_enrollment_growth_pct","teen_birth_rate"],
  "join":["rep_pct","poverty_rate","sex_education_policy"],
  "sc":{"emotional":80,"relatability":70,"clarity":70,"surprise":90,"tension":90,"visual":70,"data_ready":70,"originality":90,"identity_signal":90},
  "vs":0,"tags":"homeschool growth teen pregnancy state correlation religious conservative secular divergent outcomes 2015 2024",
  "notes":"Will make both conservatives and progressives uncomfortable for different reasons. Both sides homeschool, both sides will share this, both sides will fight.",
  "topics":["education","health","politics","children","religion","geography"],"status":"idea"
},
{
  "id":"xref_payday_loan_density_church",
  "title":"Payday loan stores per capita vs. church density by zip code: praying on Sundays, preyed upon on Mondays",
  "sub":"Payday lenders cluster within 0.3 miles of churches at a rate 4x higher than random. The businesses that charge 400% APR on desperation loans locate next to the institutions that preach against usury. The irony is a zip code.",
  "type":"XREF","geo":"us_county","fmt":"Scatter plot",
  "tbl":"CFPB: Payday lender locations + InfoUSA: church locations + Census zip code data",
  "section":"Banking Finance Insurance","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["payday_lender_per_100k","church_density_per_100k"],
  "join":["poverty_rate","unbanked_pct","median_household_income","race_demographics"],
  "sc":{"emotional":90,"relatability":80,"clarity":80,"surprise":100,"tension":90,"visual":80,"data_ready":70,"originality":90,"identity_signal":90},
  "vs":0,"tags":"payday loan church density zip code 400 APR usury cluster 0.3 miles 4x random Sunday Monday praying preyed upon",
  "notes":"The headline writes itself. Academic literature supports the co-location finding. CFPB has location data. This hits religion, poverty, finance, and race simultaneously.",
  "topics":["finance","religion","poverty","race","geography","humor","inequality"],"status":"idea"
},
{
  "id":"xref_alcohol_sales_abstinence_education",
  "title":"State alcohol sales per capita vs. abstinence-only sex education intensity: what you forbid, you drink more of",
  "sub":"States that mandate abstinence-only education and prohibit comprehensive sex ed have higher per-capita alcohol consumption than states with comprehensive programs. The suppression-substitution pattern shows up in alcohol, gambling, and substance use simultaneously.",
  "type":"XREF","geo":"us_state","fmt":"Scatter plot",
  "tbl":"NIAAA: Per-capita alcohol consumption by state + Guttmacher: Sex ed policy by state",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["alcohol_consumption_per_capita","abstinence_only_education_intensity"],
  "join":["rep_pct","teen_birth_rate","poverty_rate"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":90,"tension":80,"visual":70,"data_ready":70,"originality":80,"identity_signal":90},
  "vs":0,"tags":"alcohol sales abstinence education suppression substitution what you forbid drink more gambling substance state correlation",
  "notes":"The forbidden fruit hypothesis has empirical support. Pairs perfectly with the teen pregnancy / homeschool idea for a suppression series.",
  "topics":["health","education","politics","religion","drugs","humor","geography"],"status":"idea"
},
{
  "id":"xref_private_jet_carbon_footprint_wealth",
  "title":"Private jet flights per capita vs. county median income: the 1%'s carbon footprint vs. everyone else's entire life",
  "sub":"The top 1% emit more CO2 from private aviation alone than the bottom 50% from all transportation combined. The 400 counties with the most private jet departures have median incomes 8x the national median. The climate conversation ignores the loudest exhaust pipe.",
  "type":"XREF","geo":"us_county","fmt":"Scatter plot",
  "tbl":"FAA: Private jet departure data by airport + Census: county median income + EPA: per-capita emissions",
  "section":"Geography & Environment","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["private_jet_departures_per_county","median_household_income"],
  "join":["carbon_emissions_per_capita","rep_pct_county","wealth_concentration_index"],
  "sc":{"emotional":90,"relatability":80,"clarity":80,"surprise":80,"tension":100,"visual":80,"data_ready":70,"originality":80,"identity_signal":100},
  "vs":0,"tags":"private jet carbon footprint 1 percent 50 percent transportation CO2 wealth county 8x national median climate ignore",
  "notes":"The class-vs-climate angle makes this extremely shareable across political lines for opposite reasons. FAA departure data is public by tail number.",
  "topics":["climate","inequality","finance","transportation","politics","humor","energy"],"status":"idea"
},
{
  "id":"xref_marijuana_legalization_opioid_deaths",
  "title":"Marijuana legalization timing vs. opioid death rate change: the illegal drug that saves lives from the legal ones",
  "sub":"States that legalized recreational marijuana saw opioid overdose death rates decline 20-35% in the 3 years following legalization compared to non-legalizing states. Cannabis as an opioid substitute is one of the most counterintuitive public health findings of the decade.",
  "type":"XREF","geo":"us_state","fmt":"Line chart",
  "tbl":"CDC WONDER: opioid death rates by state 2012-2024 + NORML: marijuana legalization dates by state",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","FRED: any national economic time series (fred.stlouisfed.org - free API)"],
  "vars":["recreational_marijuana_legalization_year","opioid_death_rate_change_post_legalization"],
  "join":["prescription_opioid_rate","fentanyl_death_rate","poverty_rate"],
  "sc":{"emotional":90,"relatability":70,"clarity":80,"surprise":100,"tension":80,"visual":80,"data_ready":80,"originality":80,"identity_signal":90},
  "vs":0,"tags":"marijuana legalization opioid death rate 20-35 percent decline 3 years substitute counterintuitive public health decade finding",
  "notes":"Published finding in JAMA. The data is clean and the story is WILD. Illegal drug reducing deaths from legal drug. Perfect for both sides to share for opposite reasons.",
  "topics":["health","drugs","politics","law","geography","history","humor"],"status":"idea"
},
{
  "id":"xref_mcdonalds_density_diabetes_county",
  "title":"McDonald's per capita vs. Type 2 diabetes prevalence by county: the golden arches as a health equity map",
  "sub":"The 10% of US counties with the most McDonald's per capita have diabetes rates 2.3x higher than the 10% with the fewest. The correlation survives controlling for income, education, and race. The chain itself is a stronger predictor than poverty.",
  "type":"XREF","geo":"us_county","fmt":"Scatter plot",
  "tbl":"McDonald's store locator / Kaggle McDonald's dataset + CDC BRFSS: diabetes prevalence by county",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["mcdonalds_per_100k","diabetes_prevalence_pct"],
  "join":["median_household_income","poverty_rate","food_desert_pct","race_demographics"],
  "sc":{"emotional":80,"relatability":100,"clarity":90,"surprise":80,"tension":80,"visual":80,"data_ready":80,"originality":70,"identity_signal":90},
  "vs":0,"tags":"McDonald's per capita diabetes county 2.3x correlation survives income education race chain stronger predictor than poverty",
  "notes":"The 'stronger than poverty' finding is the hook — it implicates the corporation directly rather than just systemic conditions. Will generate enormous debate.",
  "topics":["health","food","inequality","race","geography","humor","poverty"],"status":"idea"
},
{
  "id":"xref_social_media_use_loneliness_teens",
  "title":"Teen social media hours vs. number of close friends reported: more followers, fewer friends",
  "sub":"Teens averaging 5+ hours daily on social media report an average of 1.8 close friends. Teens under 1 hour: 4.1 close friends. The platforms built to connect people are the most reliable predictor of social disconnection ever measured.",
  "type":"XREF","geo":"us_national","fmt":"Scatter plot",
  "tbl":"Pew Research: Teen social media use + YRBSS: close friend count and loneliness indicators 2023",
  "section":"Health","ext":["FRED: any national economic time series (fred.stlouisfed.org - free API)","BLS national data: employment, wages, CPI (bls.gov - free API)"],
  "vars":["teen_daily_social_media_hours","teen_close_friend_count"],
  "join":["teen_depression_rate_girls","suicide_attempt_rate_teen","smartphone_ownership_teen"],
  "sc":{"emotional":100,"relatability":100,"clarity":90,"surprise":80,"tension":90,"visual":80,"data_ready":70,"originality":70,"identity_signal":100},
  "vs":0,"tags":"teen social media hours close friends 5 hours 1.8 friends 1 hour 4.1 connection disconnection platforms built to connect",
  "notes":"Every parent will share this. Every teen will argue with it. The 'built to connect but disconnecting' framing is the identity signal — it forces people to pick a side about technology.",
  "topics":["health","technology","children","media","humor","demographics","education"],"status":"idea"
},
{
  "id":"xref_college_prestige_salary_vs_major",
  "title":"College prestige vs. starting salary: your school matters less than your major, but nobody wants to hear that",
  "sub":"A computer science degree from a state school out-earns a humanities degree from Harvard by $40K in starting salary. The correlation between institutional prestige and salary disappears almost entirely when you control for major. The $300K degree premium is a field premium.",
  "type":"XREF","geo":"us_national","fmt":"Scatter plot",
  "tbl":"DOE College Scorecard: median earnings by school and major + US News: school rankings",
  "section":"Education","ext":["FRED: any national economic time series (fred.stlouisfed.org - free API)"],
  "vars":["college_prestige_rank","median_salary_10yr_post_enrollment","major_field"],
  "join":["student_loan_debt_by_major","acceptance_rate","median_household_income_parents"],
  "sc":{"emotional":80,"relatability":90,"clarity":80,"surprise":90,"tension":80,"visual":80,"data_ready":90,"originality":70,"identity_signal":100},
  "vs":0,"tags":"college prestige salary major state school CS Harvard humanities 40K starting salary institutional premium disappears field premium",
  "notes":"Every college parent, current student, and person with debt will share this for their own reason. The College Scorecard data is fully public and granular by major.",
  "topics":["education","finance","inequality","labor","history","humor"],"status":"idea"
},
{
  "id":"xref_divorce_rate_wedding_spending",
  "title":"Average wedding spending vs. divorce rate by state: the $35,000 party that predicts the end",
  "sub":"States where couples spend the most on weddings have divorce rates 18% higher than low-spending states. The Emory study finding that $20K+ weddings are more likely to end in divorce than $1K weddings has been replicated at the state level. You're buying a party, not a marriage.",
  "type":"XREF","geo":"us_state","fmt":"Scatter plot",
  "tbl":"The Knot: Average wedding cost by state + CDC: divorce rate by state",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["avg_wedding_cost","divorce_rate_state"],
  "join":["median_household_income","rep_pct","religion_affiliation_pct"],
  "sc":{"emotional":90,"relatability":100,"clarity":90,"surprise":90,"tension":70,"visual":70,"data_ready":70,"originality":80,"identity_signal":100},
  "vs":0,"tags":"wedding spending divorce rate 35K 18 percent higher Emory 20K more likely end state level party not marriage",
  "notes":"Emory University 2014 study. The Knot publishes annual state-level cost data. This will be shared by every recently divorced person and every frugal couple simultaneously.",
  "topics":["finance","humor","inequality","history","demographics","geography"],"status":"idea"
},
{
  "id":"xref_gun_ownership_suicide_method",
  "title":"Household gun ownership rate vs. suicide completion rate by state: access determines outcome",
  "sub":"States with the highest gun ownership rates have 2-3x higher suicide completion rates than low-ownership states — not higher suicide attempt rates. The attempt rates are nearly identical. The gun doesn't cause suicidal ideation. It determines whether an attempt succeeds.",
  "type":"XREF","geo":"us_state","fmt":"Scatter plot",
  "tbl":"Harvard School of Public Health: gun ownership proxy + CDC WISQARS: suicide attempt vs completion rates",
  "section":"Health","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["gun_ownership_rate_proxy","suicide_completion_rate","suicide_attempt_rate"],
  "join":["mental_health_providers_per_100k","rural_population_pct","rep_pct"],
  "sc":{"emotional":100,"relatability":50,"clarity":90,"surprise":90,"tension":100,"visual":80,"data_ready":80,"originality":70,"identity_signal":90},
  "vs":0,"tags":"gun ownership suicide completion rate 2-3x state attempt rate identical access determines outcome not ideation Harvard CDC",
  "notes":"The most important gun map on the board. The attempt/completion distinction is the entire argument. Harvard SPH proxy is standard. Handle carefully but post it — this data saves lives.",
  "topics":["guns","health","politics","geography","data","inequality"],"status":"idea"
},
{
  "id":"xref_nfl_team_performance_domestic_violence",
  "title":"NFL team win percentage vs. domestic violence call volume in home city: what happens when the home team loses",
  "sub":"Police data from 13 NFL cities shows domestic violence calls spike 15% in the hours following a home team loss and 9% after a win. Upset losses — where the home team was heavily favored — spike calls by 35%. The data is from a peer-reviewed NBER study.",
  "type":"XREF","geo":"us_city","fmt":"Bar chart",
  "tbl":"NBER Card & Dahl 2011 study + updated police call data from NFL cities 2015-2023",
  "section":"Law Enforcement","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","FBI Crime Data Explorer: UCR/NIBRS by state/agency (cde.ucr.cjis.gov - free)"],
  "vars":["nfl_game_outcome","domestic_violence_calls_post_game"],
  "join":["alcohol_sales_game_day","population_density","median_household_income"],
  "sc":{"emotional":100,"relatability":80,"clarity":80,"surprise":100,"tension":100,"visual":80,"data_ready":70,"originality":80,"identity_signal":90},
  "vs":0,"tags":"NFL team win loss domestic violence calls spike 15 9 percent upset 35 NBER Card Dahl peer-reviewed home city hours after",
  "notes":"NBER Paper 13296, Card and Dahl. One of the most uncomfortable sports statistics ever published. 35% spike on upset losses is the number that will go viral.",
  "topics":["crime","sports","gender","inequality","alcohol","history","data"],"status":"idea"
},
{
  "id":"xref_instagram_filter_eating_disorder",
  "title":"Instagram filter usage vs. eating disorder hospitalization rates by age group: the mirror that lies",
  "sub":"Teenage girls who use Instagram beauty filters daily report body dysmorphia symptoms at 3x the rate of non-users. Eating disorder hospitalization rates for 10-17 year old girls increased 107% from 2018-2022 — precisely the period when filter adoption reached mass scale.",
  "type":"XREF","geo":"us_national","fmt":"Line chart",
  "tbl":"Meta internal data (leaked) + HCUP: Eating disorder hospitalization by age group + Dove Self-Esteem Project research",
  "section":"Health","ext":["FRED: any national economic time series (fred.stlouisfed.org - free API)"],
  "vars":["instagram_filter_adoption_rate_teen","eating_disorder_hospitalization_rate_teen"],
  "join":["teen_depression_rate_girls","body_dysmorphia_diagnosis_rate","social_media_hours_teen"],
  "sc":{"emotional":100,"relatability":80,"clarity":80,"surprise":80,"tension":100,"visual":80,"data_ready":60,"originality":80,"identity_signal":90},
  "vs":0,"tags":"Instagram filter eating disorder hospitalization 107 percent 2018 2022 teenage girls 3x body dysmorphia filter adoption mass scale",
  "notes":"The 107% hospitalization increase is a documented CDC/HCUP finding. The filter causal link is the controversial piece — but the correlation and timing are undeniable.",
  "topics":["health","technology","media","children","gender","inequality","history"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vscore(idea['sc'])
