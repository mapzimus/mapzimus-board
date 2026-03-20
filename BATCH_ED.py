# BATCH_ED.py — HSUS Historical Statistics of the United States
# Sources: Cambridge HSUS 202 XLS files covering US population 1790-2000,
#          births, internal migration, immigration, households, slave population, rural/urban

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"hsus_us_population_growth_1790_2020",
  "title":"US population by decade 1790–2020: every immigration wave and baby boom in one chart",
  "sub":"The US grew from 3.9 million in 1790 to 331 million in 2020 — an 85-fold increase. The growth rate peaked in the 1800-1810 decade at 36.4% and has slowed steadily since. The fastest absolute growth came in the post-WWII baby boom. Every major demographic event — Civil War stall, immigration surges of 1880-1910, Depression slowdown, post-war boom — is visible in the data.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"HSUS: Aa1-5.xls — Total US population by census decade 1790-2000, continued with Census 2020",
  "section":"Population","ext":["US Census Bureau: historical census data (census.gov - free)"],
  "vars":["total_us_population_by_decade","population_growth_rate_by_decade"],
  "join":["immigration_rate","birth_rate","war_years"],
  "sc":{"emotional":70,"relatability":70,"clarity":90,"surprise":70,"tension":50,"visual":80,"originality":60,"data_ready":100},
  "vs":0,"tags":"US population 1790 2020 3.9 million 331 million 85-fold growth rate immigration baby boom Civil War Depression visible",
  "notes":"","topics":["population","history","demographics","immigration","data"],"status":"idea"
},
{
  "id":"hsus_slave_population_state_1790_1860",
  "title":"Enslaved population by state 1790–1860: the geographic spread of American slavery before the Civil War",
  "sub":"The enslaved population grew from 697K in 1790 to 3.95 million in 1860 — a 466% increase while the free population grew 350%. The geographic spread tells the cotton and tobacco story: Deep South states had enslaved populations exceeding 40% of total state population by 1860. South Carolina and Mississippi both exceeded 55% enslaved.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"HSUS: Aa1930-1945.xls — Slave population by state 1790-1860 by decade",
  "section":"Population","ext":["National Humanities Center: slavery data (nationalhumanitiescenter.org - free)"],
  "vars":["slave_population_by_state","slave_pct_of_state_population"],
  "join":["cotton_production","tobacco_production","free_population_by_state"],
  "sc":{"emotional":90,"relatability":60,"clarity":80,"surprise":70,"tension":90,"visual":90,"originality":60,"data_ready":90},
  "vs":0,"tags":"enslaved population state 1790 1860 697K 3.95 million 466 percent Deep South South Carolina Mississippi 55 percent cotton tobacco",
  "notes":"","topics":["history","race","inequality","politics","geography","population"],"status":"idea"
},
{
  "id":"hsus_rural_urban_shift_1790_2000",
  "title":"US rural vs. urban population 1790–2000: the 200-year story of the Great Migration to cities",
  "sub":"In 1790, 95% of Americans were rural. By 1920, the US crossed the 50% urban threshold for the first time. By 2000, 79% were urban. The shift happened fastest during industrialization (1870-1920) and again post-WWII. The rural America that now feels 'left behind' was the entire country just five generations ago.",
  "type":"CHART","geo":"us_national","fmt":"Area chart",
  "tbl":"HSUS: Aa684-698.xls through Aa1884-1895.xls — rural and urban population by decade 1790-2000",
  "section":"Population","ext":["US Census Bureau: historical census data (census.gov - free)"],
  "vars":["rural_population_pct","urban_population_pct"],
  "join":["manufacturing_employment_share","farm_employment_share","immigration_rate"],
  "sc":{"emotional":70,"relatability":80,"clarity":90,"surprise":70,"tension":60,"visual":90,"originality":70,"data_ready":90},
  "vs":0,"tags":"rural urban 1790 95 percent rural 1920 50 percent urban 2000 79 percent industrialization five generations left behind",
  "notes":"","topics":["history","population","geography","rural","demographics","labor"],"status":"idea"
},
{
  "id":"hsus_immigration_waves_by_origin",
  "title":"US immigrants by continent of origin 1820–2020: every wave of American immigration in one chart",
  "sub":"American immigration happened in distinct waves with completely different origins: Europeans dominated 1820-1965 (Ireland/Germany in 1840s-1880s, Southern/Eastern Europe 1880-1920). Post-1965 Hart-Celler Act shifted the source to Asia and Latin America. The US has been continuously remade by different cultures in each generation — the 'traditional America' of any era was itself a recent immigrant culture.",
  "type":"CHART","geo":"us_national","fmt":"Area chart",
  "tbl":"HSUS: Aa1896-2025 immigration files + modern Census/DHS data — immigrants by continent 1820-2020",
  "section":"Population","ext":["DHS: Yearbook of Immigration Statistics (dhs.gov - free)"],
  "vars":["immigrants_by_continent_of_origin"],"join":["immigration_policy_changes","economic_push_pull_factors"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":80,"tension":70,"visual":100,"originality":70,"data_ready":90},
  "vs":0,"tags":"immigration waves 1820 2020 Europe Ireland Germany Southern Eastern Asia Latin America 1965 Hart-Celler remade cultures",
  "notes":"","topics":["immigration","history","population","politics","race","demographics"],"status":"idea"
},
{
  "id":"hsus_birth_rate_order_1940_2000",
  "title":"US birth order composition 1940–2000: the collapse of the large American family",
  "sub":"In 1940, third, fourth, and fifth+ births made up 35% of all US births. By 1980 they made up under 20%. First births held relatively steady while higher-order births collapsed — meaning the family shrinkage wasn't about delaying first children but about stopping at one or two. The two-child norm replaced the four-child norm in a single generation.",
  "type":"CHART","geo":"us_national","fmt":"Area chart",
  "tbl":"HSUS: Ab11-30.xls — births by order (first through fifth+) and race 1940-2000",
  "section":"Births Deaths","ext":["CDC: National Vital Statistics System (cdc.gov/nchs - free)"],
  "vars":["birth_rate_by_order","first_birth_rate","higher_order_birth_rate"],
  "join":["contraceptive_access","female_labor_participation","housing_cost"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":50,"visual":80,"originality":70,"data_ready":90},
  "vs":0,"tags":"birth order 1940 2000 third fourth fifth 35 percent 20 percent two-child norm replaced four-child single generation collapse",
  "notes":"","topics":["demographics","history","health","gender","population","data"],"status":"idea"
},
{
  "id":"hsus_internal_migration_born_out_of_state",
  "title":"Share of Americans living outside their birth state 1850–2000: how mobile has the country really been",
  "sub":"In 1870, 23% of Americans lived in a state different from where they were born. By 2000 it was 32%. The Great Migration of Black Americans northward (1910-1970) shows up as a massive state-of-birth shift in Census data. The Dust Bowl exodus, the Sun Belt migration of the 1970s-80s, all visible. Americans have always been geographically mobile — 'flyover country' was built by people who flew in.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"HSUS: Ac1-8.xls — population born in state of residence vs. born elsewhere by decade 1850-2000",
  "section":"Population","ext":["US Census Bureau: historical census data (census.gov - free)"],
  "vars":["pct_living_outside_birth_state"],"join":["great_migration_timeline","dust_bowl_timeline","sun_belt_growth"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":70,"tension":50,"visual":70,"originality":70,"data_ready":90},
  "vs":0,"tags":"internal migration born out of state 1870 23 percent 2000 32 percent Great Migration Dust Bowl Sun Belt mobile flyover",
  "notes":"","topics":["history","population","geography","race","demographics"],"status":"idea"
},
{
  "id":"hsus_household_size_collapse_1850_2000",
  "title":"Average American household size 1850–2000: from 5.6 people per household to 2.6 in 150 years",
  "sub":"The average US household contained 5.6 people in 1850. By 2000 it was 2.6. The biggest single-decade drop was 1970-1980 as divorce rates surged and the Baby Boom generation started living alone. The nuclear family of 4 was actually a transitional form between the multigenerational farm household and the modern 2-person household — not a permanent baseline.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"HSUS: aeFamily files — average household size, family composition by decade 1850-2000",
  "section":"Births Deaths","ext":["US Census Bureau: American Housing Survey (census.gov - free)"],
  "vars":["avg_household_size","family_household_pct","nonfamily_household_pct"],
  "join":["divorce_rate","urbanization_rate","female_labor_participation"],
  "sc":{"emotional":70,"relatability":90,"clarity":90,"surprise":80,"tension":40,"visual":80,"originality":70,"data_ready":90},
  "vs":0,"tags":"household size 1850 5.6 people 2000 2.6 1970-1980 biggest drop divorce Baby Boom nuclear family transitional not permanent",
  "notes":"","topics":["demographics","history","housing","population","gender","data"],"status":"idea"
},
{
  "id":"hsus_state_population_rank_1790_2020",
  "title":"State population rank changes 1790–2020: which states rose and fell over 230 years",
  "sub":"Virginia was the most populous state in 1790. New York took over in 1820 and held for 150 years. California overtook New York in 1970 and Texas is now on track to overtake California by 2030. The state population ranking map animates the entire westward expansion, the industrial revolution, and the Sun Belt shift in one visualization.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"HSUS: State Populations files (53 XLS) — state population by decade 1790-2000 + Census 2010/2020",
  "section":"Population","ext":["US Census Bureau: historical census data (census.gov - free)"],
  "vars":["state_population_rank_by_decade"],"join":["westward_expansion_timeline","industrial_revolution","sun_belt_migration"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":40,"visual":90,"originality":80,"data_ready":90},
  "vs":0,"tags":"state population rank 1790 2020 Virginia 1790 New York 1820 California 1970 Texas 2030 westward expansion Sun Belt animated",
  "notes":"","topics":["population","history","geography","demographics","data"],"status":"idea"
},
{
  "id":"hsus_naturalization_rate_1900_2020",
  "title":"US naturalization rate by country of origin 1900–2020: who becomes American fastest",
  "sub":"HSUS naturalization data shows enormous variation by country of origin. Vietnamese immigrants naturalize at 80%+ rates. Mexican immigrants at under 40%. Indian immigrants at 75%. The differences track not just time-in-country but English proficiency, education level, and — most importantly — whether the country of origin offers dual citizenship. Naturalization is a policy choice as much as a personal one.",
  "type":"CHART","geo":"us_national","fmt":"Bar chart",
  "tbl":"HSUS: Naturalization files — naturalization rates by country of origin, extended with DHS modern data",
  "section":"Population","ext":["DHS: Yearbook of Immigration Statistics (dhs.gov - free)"],
  "vars":["naturalization_rate_by_origin_country"],
  "join":["english_proficiency","education_level","dual_citizenship_policy","time_in_us"],
  "sc":{"emotional":70,"relatability":70,"clarity":80,"surprise":80,"tension":50,"visual":70,"originality":70,"data_ready":80},
  "vs":0,"tags":"naturalization rate country origin Vietnamese 80 percent Mexican 40 percent Indian 75 dual citizenship English proficiency policy",
  "notes":"","topics":["immigration","history","demographics","law","politics","data"],"status":"idea"
},
{
  "id":"hsus_hispanic_population_growth_1970_2020",
  "title":"Hispanic population growth by state 1970–2020: the demographic transformation that changed America",
  "sub":"The Hispanic population of the US grew from 9.6 million in 1970 to 62.1 million in 2020 — a 547% increase while the total population grew 63%. California, Texas, and Florida absorbed the majority, but the fastest growth was in states like North Carolina, Georgia, and Tennessee — the New South destinations that few predicted. Hispanic America now spans well beyond the border states.",
  "type":"MAP","geo":"us_state","fmt":"State choropleth",
  "tbl":"HSUS: Aa2189-2243 Hispanic Population files — Hispanic population by state decade 1970-2000, extended with Census 2010/2020",
  "section":"Population","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["hispanic_population_pct","hispanic_population_growth_rate"],
  "join":["immigration_rate","labor_demand","housing_cost","rep_pct"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":60,"visual":90,"originality":60,"data_ready":100},
  "vs":0,"tags":"Hispanic population 1970 9.6 million 2020 62.1 million 547 percent growth NC Georgia Tennessee New South destinations border states",
  "notes":"","topics":["demographics","history","immigration","race","population","geography"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
