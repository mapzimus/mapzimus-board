"""
BATCH_GE.py — Deep OWID dive + HSUS historical ideas
Targets: global development, demographic transitions, historical US data
Gap-fill: more World choropleths, more Africa/Asia/Latin America geo
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
# OWID — DEMOGRAPHIC TRANSITIONS (deep dive into population CSVs)
# ============================================================
ideas.append(mk("owid_population_growth_vs_median_age","Young Countries Grow Old Countries Shrink","Population growth rate vs median age shows two demographic worlds diverging","XREF","worldwide","Scatter plot","Demographics","OWID population-growth-rate-vs-median-age.csv https://ourworldindata.org/age-structure",65,65,80,70,55,60,65,95))
ideas.append(mk("owid_population_with_vs_without_migration","Where Migration Saves Countries From Decline","Population growth with vs without migration shows which nations depend on immigration","XREF","worldwide","World choropleth","Demographics","OWID population-growth-rate-with-and-without-migration.csv https://ourworldindata.org/migration",70,65,75,80,70,85,75,95))
ideas.append(mk("owid_elderly_share_projected_2100","The Coming Age Tsunami","Projected share of population 65+ by 2100 - Japan and Korea lead the way","MAP","worldwide","World choropleth","Demographics","OWID population-young-working-elderly-with-projections.csv https://ourworldindata.org/age-structure",75,70,80,70,65,85,60,95))
ideas.append(mk("owid_under_5_population_projected","Where the Worlds Children Will Be in 2100","Projected under-5 population shifts almost entirely to Sub-Saharan Africa","MAP","worldwide","World choropleth","Demographics","OWID projected-population-under-age-5.csv https://ourworldindata.org/population-growth",70,60,80,75,60,85,65,95))
ideas.append(mk("owid_working_age_share_declining","The Working-Age Population Is Shrinking in 40 Countries","Share of population aged 15-64 is falling across the developed world","MAP","worldwide","World choropleth","Demographics","OWID population-young-working-elderly.csv https://ourworldindata.org/age-structure",70,70,80,70,65,85,60,95))
ideas.append(mk("owid_population_by_income_level","Rich Countries Are Shrinking Poor Countries Are Booming","Population trends by World Bank income classification diverge dramatically","CHART","worldwide","Area chart","Demographics","OWID population-by-income-level.csv https://ourworldindata.org/population-growth",70,65,80,65,60,70,55,95))
ideas.append(mk("owid_population_10000_bc_to_now","10000 Years of Human Population Growth","From 5 million to 8 billion in one breathtaking chart","CHART","worldwide","Area chart","History","OWID population-long-run-with-projections.csv https://ourworldindata.org/population-growth",60,60,85,70,35,70,55,95))
ideas.append(mk("owid_un_projection_revisions","How Wrong Were Population Predictions","UN population projections from 1968 vs 1980 vs 2000 vs reality","CHART","worldwide","Line chart","Demographics","OWID world-population-projections-by-un-prospects-revision.csv https://ourworldindata.org/population-growth",50,55,75,80,40,65,75,95))
ideas.append(mk("owid_time_spent_alone_by_age","Americans Spend Most of Their Lives Alone","Time spent with friends drops to near zero after age 40","CHART","us_national","Area chart","Demographics","OWID time-spent-with-relationships-by-age-us.csv https://ourworldindata.org/time-use",85,90,80,70,60,75,60,95))
ideas.append(mk("owid_parity_progression","Why People Stop at 2 Kids","Parity progression ratios show the cliff drop from 2 to 3 children","CHART","worldwide","Line chart","Demographics","OWID women-who-have-next-birth-parity-progression-ratio.csv https://ourworldindata.org/fertility-rate",65,80,70,75,45,60,70,90))
ideas.append(mk("owid_england_population_millennium","Englands Population From 1000 AD to Today","A thousand years of boom bust and the Industrial Revolution","CHART","europe","Line chart","History","OWID population-of-england-millennium.csv https://ourworldindata.org/population-growth",55,50,80,65,35,65,65,95))
ideas.append(mk("owid_co2_share_vs_population_share","Countries That Emit More Than Their Fair Share","Comparing each nations share of CO2 emissions vs share of global population","MAP","worldwide","World choropleth","Climate","OWID share-of-global-consumption-based-co-emissions.csv https://ourworldindata.org/co2-emissions",80,65,80,70,80,85,65,95))
ideas.append(mk("owid_primary_enrollment_1800s","The March of Universal Education","Primary school enrollment from the 1800s to today for select countries","CHART","worldwide","Line chart","Education","OWID primary-enrollment-selected-countries.csv https://ourworldindata.org/global-education",60,55,80,55,35,65,55,95))
ideas.append(mk("owid_births_by_region_projected","Africa Will Have More Births Than Asia by 2060","Annual births by world region with projections show a massive shift","CHART","worldwide","Area chart","Demographics","OWID annual-number-of-births-by-world-region.zip https://ourworldindata.org/population-growth",70,55,80,80,60,70,65,95))
ideas.append(mk("owid_deaths_by_region","Where People Die Is Shifting","Annual deaths by world region over time as populations age differently","CHART","worldwide","Area chart","Health","OWID annual-number-of-deaths-by-world-region.zip https://ourworldindata.org/causes-of-death",60,55,80,60,45,70,55,95))
ideas.append(mk("owid_birth_rate_vs_death_rate","The Demographic Transition in One Chart","Birth rate vs death rate scatter for every country shows classic transition theory","XREF","worldwide","Scatter plot","Demographics","OWID birth-rate-vs-death-rate.zip https://ourworldindata.org/demographic-transition",55,55,80,65,40,60,65,95))
ideas.append(mk("owid_gdp_per_capita_maddison","2000 Years of Economic History","GDP per capita from year 1 to today using Maddison Project data","CHART","worldwide","Line chart","Economy","OWID gdp-per-capita-maddison-project-database.zip https://ourworldindata.org/economic-growth",55,55,85,65,35,65,60,95))
ideas.append(mk("owid_human_development_index","The Human Development Index World Map","HDI combines life expectancy education and income into one number","MAP","worldwide","World choropleth","Economy","OWID human-development-index.zip https://ourworldindata.org/human-development-index",60,60,85,50,40,85,45,95))
ideas.append(mk("owid_cost_genome_sequencing","Sequencing a Human Genome Went From 100M to 100 Dollars","The fastest cost decline in technology history","CHART","worldwide","Line chart","Science & Technology","OWID cost-of-sequencing-a-full-human-genome.zip https://ourworldindata.org/human-genome-project-cost",55,55,80,85,30,65,70,95))
ideas.append(mk("owid_global_energy_substitution","How the Worlds Energy Mix Has Changed Since 1800","From biomass to coal to oil to gas with renewables just beginning","CHART","worldwide","Area chart","Environment","OWID global-energy-substitution.zip https://ourworldindata.org/energy-mix",55,55,85,55,45,70,50,95))

# ============================================================
# HSUS — Historical Statistics of the United States (1790-2000)
# ============================================================
ideas.append(mk("hsus_population_density_1790_2000","How America Filled Up","US population density from 3 people per sq mile in 1790 to 80 by 2000","CHART","us_national","Line chart","History","HSUS A-Population Aa1-5.xls https://hsus.cambridge.org",55,65,85,55,30,65,55,90))
ideas.append(mk("hsus_us_birth_death_rate_200yr","200 Years of American Births and Deaths","Crude birth and death rates from the founding to 2000","CHART","us_national","Line chart","History","HSUS A-Population Aa15-21.xls https://hsus.cambridge.org",60,60,85,55,35,65,55,90))
ideas.append(mk("hsus_us_racial_composition_200yr","Americas Changing Racial Composition Since 1790","White Black and Other race shares over two centuries of Census data","CHART","us_national","Area chart","History","HSUS A-Population Aa22-35.xls https://hsus.cambridge.org",75,70,80,60,70,70,55,90))
ideas.append(mk("hsus_region_population_shift","How Americas Population Center Moved West","Census region population shares from 1790 to 2000","CHART","us_national","Area chart","History","HSUS A-Population Aa36-92.xls https://hsus.cambridge.org",60,65,80,60,40,70,60,90))
ideas.append(mk("hsus_foreign_born_share_200yr","Americas Immigrant Share Over 200 Years","Foreign-born population share from 1850 to 2000 shows waves and troughs","CHART","us_national","Line chart","History","HSUS A-Population Nativity tables https://hsus.cambridge.org",70,75,80,60,65,65,55,90))
ideas.append(mk("hsus_slave_population_map","The Geography of American Slavery","Slave population by state from 1790 to 1860","MAP","us_state","State choropleth","History","HSUS A-Population Slave Population tables https://hsus.cambridge.org",85,65,80,55,90,80,60,90))
ideas.append(mk("hsus_slave_population_growth","From 700000 to 4 Million: The Growth of American Slavery","Total enslaved population from 1790 to 1860 Census counts","CHART","us_national","Bar chart","History","HSUS A-Population Slave Population tables https://hsus.cambridge.org",85,60,85,60,90,65,55,90))
ideas.append(mk("hsus_urban_rural_shift_200yr","When America Stopped Being Rural","Urban vs rural population share from 1790 to 2000","CHART","us_national","Area chart","History","HSUS A-Population Rural and Urban Places tables https://hsus.cambridge.org",65,70,85,60,40,70,55,90))
ideas.append(mk("hsus_metro_area_growth_1900_2000","The Rise of Americas Metro Areas","Population growth of the top 20 metro areas from 1900 to 2000","CHART","us_national","Line chart","History","HSUS A-Population Rural and Urban Places Aa1471-1663.xls https://hsus.cambridge.org",55,65,80,55,35,65,55,90))
ideas.append(mk("hsus_hispanic_population_growth","The Hispanic Population Explosion","Hispanic population growth in America from 1850 to 2000","CHART","us_national","Area chart","Demographics","HSUS A-Population Hispanic Population Aa2189.xls https://hsus.cambridge.org",65,75,80,60,55,65,55,90))
ideas.append(mk("hsus_state_population_rankings_change","Which States Rose and Fell Over 200 Years","State population rankings from 1790 to 2000 - Virginia was #1","RANK","us_state","Ranked list","History","HSUS A-Population State Populations tables https://hsus.cambridge.org",60,70,75,70,45,60,65,90))
ideas.append(mk("hsus_net_immigration_waves","Americas Three Great Immigration Waves","Net immigration by decade from 1820 to 2000 shows three distinct surges","CHART","us_national","Bar chart","History","HSUS A-Population Aa9-14.xls https://hsus.cambridge.org",65,65,80,60,55,65,55,90))
ideas.append(mk("hsus_life_expectancy_1900_2000","Americans Live 30 Years Longer Than They Did in 1900","Life expectancy at birth from 1900 to 2000","CHART","us_national","Line chart","Health","HSUS A-Population Vital Statistics tables https://hsus.cambridge.org",70,80,85,50,40,65,45,90))
ideas.append(mk("hsus_infant_mortality_century","Americas Infant Mortality Miracle","From 100 per 1000 to 7 per 1000 in one century","CHART","us_national","Line chart","Health","HSUS A-Population Vital Statistics tables https://hsus.cambridge.org",80,75,85,55,50,65,50,90))
ideas.append(mk("hsus_marriage_divorce_200yr","200 Years of Marriage and Divorce in America","Marriage and divorce rates per 1000 from 1800 to 2000","CHART","us_national","Line chart","Demographics","HSUS A-Population Vital Statistics tables https://hsus.cambridge.org",65,80,80,60,55,65,55,90))
ideas.append(mk("hsus_outlying_territories_pop","Americas Forgotten Populations","Population of US outlying territories and possessions from 1900 to 2000","CHART","us_national","Bar chart","History","HSUS A-Population Aa93-109.xls https://hsus.cambridge.org",50,50,75,70,55,55,70,90))
ideas.append(mk("hsus_internal_migration_great","The Great Migration in Numbers","Black population movement from South to North 1910-1970","MAP","us_state","State choropleth","History","HSUS A-Population Internal Migration tables https://hsus.cambridge.org",85,70,80,60,80,80,60,85))

# ============================================================
# OWID — AFRICA-FOCUSED (gap fill: africa geo only has 64 ideas)
# ============================================================
ideas.append(mk("owid_africa_population_boom","Africa Will Have 4 Billion People by 2100","The continents population trajectory dwarfs every other region","CHART","africa","Area chart","Demographics","OWID population-regions-with-projections.csv https://ourworldindata.org/population-growth",70,55,85,75,55,70,55,95))
ideas.append(mk("owid_africa_child_mortality_map","Child Mortality Across Africa","Under-5 mortality rates vary 20x between the best and worst African nations","MAP","africa","Special map","Health","OWID child-mortality.zip https://ourworldindata.org/child-mortality",80,55,85,60,65,80,50,95))
ideas.append(mk("owid_africa_fertility_rates","Africas Fertility Rates Are Finally Falling","Children per woman by African country from 1960 to present","MAP","africa","Special map","Demographics","OWID children-born-per-woman.zip https://ourworldindata.org/fertility-rate",65,50,85,60,50,80,55,95))
ideas.append(mk("owid_africa_armed_conflicts","Where Wars Are Killing People in Africa","Deaths in armed conflicts by African country since 1946","MAP","africa","Special map","History","OWID deaths-in-armed-conflicts-by-country.zip https://ourworldindata.org/war-and-peace",80,50,80,60,85,80,55,95))
ideas.append(mk("owid_africa_internet_penetration","The Digital Divide Within Africa","Internet access ranges from 5% to 85% across the continent","MAP","africa","Special map","Science & Technology","OWID share-of-individuals-using-the-internet.csv https://ourworldindata.org/internet",60,55,80,65,45,80,55,95))
ideas.append(mk("owid_africa_electricity_access","Hundreds of Millions of Africans Still Live in the Dark","Electricity access by country in Sub-Saharan Africa","MAP","africa","Special map","Environment","OWID share-of-the-population-with-access-to-electricity.csv https://ourworldindata.org/energy-access",75,55,85,60,60,80,50,95))

# ============================================================
# OWID — ASIA-FOCUSED (gap fill: asia geo only has 56 ideas)
# ============================================================
ideas.append(mk("owid_asia_aging_crisis","Asias Aging Crisis","Japan South Korea and China face the fastest population aging in history","MAP","asia","Special map","Demographics","OWID population-young-working-elderly.csv https://ourworldindata.org/age-structure",75,65,80,70,65,80,60,95))
ideas.append(mk("owid_asia_fertility_collapse","Asias Fertility Collapse","South Korea hit 0.72 children per woman - the lowest in human history","CHART","asia","Bar chart","Demographics","OWID children-born-per-woman.zip https://ourworldindata.org/fertility-rate",75,70,80,85,70,65,65,95))
ideas.append(mk("owid_asia_gdp_growth_since_1950","Asias Economic Miracle in One Chart","GDP per capita growth in Asian tigers vs rest of Asia since 1950","CHART","asia","Line chart","Economy","OWID gdp-per-capita-maddison-project-database.zip https://ourworldindata.org/economic-growth",55,55,80,65,40,65,55,95))
ideas.append(mk("owid_asia_literacy_transformation","Asias Literacy Transformation","From 30% literate to 95% in two generations","CHART","asia","Line chart","Education","OWID cross-country-literacy-rates.zip https://ourworldindata.org/literacy",60,55,80,60,35,65,55,95))
ideas.append(mk("owid_asia_military_spending","Asias Military Buildup","Military spending as share of GDP across Asian nations","MAP","asia","Special map","History","OWID military-spending-as-a-share-of-gdp-sipri.zip https://ourworldindata.org/military-spending",60,55,80,65,75,80,55,95))

# ============================================================
# OWID — LATIN AMERICA-FOCUSED (gap fill: latin_america only 36 ideas)
# ============================================================
ideas.append(mk("owid_latam_homicide_crisis","Latin Americas Murder Crisis","The region has 8% of the worlds population but 33% of its murders","MAP","latin_america","Special map","Crime and Law Enforcement","OWID homicide-rate-unodc.zip https://ourworldindata.org/homicides",85,65,85,65,90,80,55,95))
ideas.append(mk("owid_latam_poverty_decline","Latin Americas Poverty Decline Then Reversal","Extreme poverty fell for two decades then rose again after 2015","CHART","latin_america","Line chart","Economy","OWID share-of-population-in-extreme-poverty.csv https://ourworldindata.org/extreme-poverty",70,60,80,65,65,60,60,95))
ideas.append(mk("owid_latam_democracy_backsliding","Democracy Is Backsliding in Latin America","Several countries have shifted from democracy to hybrid or authoritarian regimes","MAP","latin_america","Special map","History","OWID political-regime.csv https://ourworldindata.org/democracy",75,60,80,70,80,80,65,95))
ideas.append(mk("owid_latam_deforestation","Latin Americas Vanishing Forests","Agricultural expansion is driving deforestation across the region","MAP","latin_america","Special map","Environment","OWID + FAO Forest Resources Assessment https://ourworldindata.org/forests-and-deforestation",75,55,80,60,75,80,55,90))

# ============================================================
# OWID — MIDDLE EAST-FOCUSED (gap fill: middle_east only 49 ideas)
# ============================================================
ideas.append(mk("owid_mideast_water_crisis","The Middle Easts Water Crisis","Per capita renewable water resources in the driest region on Earth","MAP","middle_east","Special map","Environment","OWID + FAO AQUASTAT https://ourworldindata.org/water-use-stress",80,55,80,65,80,80,65,90))
ideas.append(mk("owid_mideast_oil_dependency","Oil as Share of GDP in Middle Eastern Economies","Some nations get 50% of GDP from petroleum","MAP","middle_east","Special map","Economy","OWID + World Bank https://ourworldindata.org/fossil-fuels",60,55,80,60,60,80,55,90))
ideas.append(mk("owid_mideast_youth_bulge","The Middle Easts Youth Bulge","Median age under 25 in several nations with no jobs for young people","MAP","middle_east","Special map","Demographics","OWID population-by-age-group.csv https://ourworldindata.org/age-structure",70,55,80,70,75,80,65,90))
ideas.append(mk("owid_mideast_womens_rights","Womens Legal Rights Across the Middle East","Legal protections for women vary enormously across MENA nations","MAP","middle_east","Special map","Demographics","OWID + World Bank Women Business and Law https://ourworldindata.org/women-s-rights",75,55,80,65,75,80,65,85))

# ============================================================
# OWID — MORE GLOBAL THEMES
# ============================================================
ideas.append(mk("owid_age_largest_population","Which Age Group Is Biggest in Each Country","In Africa its under 15 in Europe its 25-64 in Japan its 65+","MAP","worldwide","World choropleth","Demographics","OWID age-group-with-the-largest-population.zip https://ourworldindata.org/age-structure",60,60,80,70,50,85,60,95))
ideas.append(mk("owid_agriculture_productivity","Farm Worker Productivity Varies 100x Across Countries","Agriculture value added per worker from 200 dollars to 80000","MAP","worldwide","World choropleth","Labor","OWID agriculture-value-added-per-worker-wdi.zip https://ourworldindata.org/employment-in-agriculture",55,55,80,75,40,85,60,95))
ideas.append(mk("owid_natural_pop_growth_map","Where Births Still Far Exceed Deaths","Natural population growth rate shows Africa and MENA growing fastest","MAP","worldwide","World choropleth","Demographics","OWID natural-population-growth.zip https://ourworldindata.org/population-growth",55,55,80,55,40,85,50,95))
ideas.append(mk("owid_child_mortality_vs_pop_growth","The Paradox: Lower Child Mortality Means Slower Population Growth","Countries where fewer children die actually have fewer children","XREF","worldwide","Scatter plot","Demographics","OWID child-mortality-vs-population-growth.zip https://ourworldindata.org/population-growth",65,55,75,80,45,60,75,95))
ideas.append(mk("owid_births_registered_map","Where Births Go Unregistered","Millions of children are born without any official record of their existence","MAP","worldwide","World choropleth","Demographics","OWID births-registered.zip https://ourworldindata.org/births-and-deaths",70,55,80,70,60,85,60,90))
ideas.append(mk("owid_contraceptive_modern_vs_any","The Contraceptive Access Gap","Difference between any contraceptive method and modern methods by country","MAP","worldwide","World choropleth","Health","OWID contraceptive-prevalence-any-methods-vs-modern-methods.zip https://ourworldindata.org/contraceptives",60,55,80,60,50,85,60,90))
ideas.append(mk("owid_children_under_5_declining","The World Is Running Out of Toddlers","Under-5 population has peaked globally and is now declining","CHART","worldwide","Line chart","Demographics","OWID children-under-age-5.zip https://ourworldindata.org/population-growth",65,65,80,80,55,60,65,95))
ideas.append(mk("owid_demographic_transition_england","England Invented the Demographic Transition","Birth and death rates in England from 1541 to present","CHART","europe","Line chart","History","OWID demographic-transition-england-wales.zip https://ourworldindata.org/demographic-transition",50,45,80,65,35,65,65,95))
ideas.append(mk("owid_births_and_deaths_global","When Deaths Will Exceed Births Globally","Projected year when global deaths surpass births - the population peak","CHART","worldwide","Line chart","Demographics","OWID births-and-deaths-projected-to-2100.zip https://ourworldindata.org/population-growth",70,65,80,80,65,65,70,95))
ideas.append(mk("owid_children_per_woman_vs_growth","More Babies Doesnt Mean More Growth","Fertility rate vs population growth rate shows a complex relationship","XREF","worldwide","Scatter plot","Demographics","OWID children-per-woman-vs-population-growth.zip https://ourworldindata.org/population-growth",50,50,75,70,40,60,65,95))
ideas.append(mk("owid_poverty_threshold_distribution","Where the Worlds Poor Live","Distribution of population across different poverty thresholds","MAP","worldwide","World choropleth","Economy","OWID distribution-of-population-poverty-thresholds.zip https://ourworldindata.org/extreme-poverty",75,60,80,55,60,85,50,95))
ideas.append(mk("owid_literate_vs_illiterate_world","The World Went From 12% Literate to 87%","Literate vs illiterate world population from 1800 to today","CHART","worldwide","Area chart","Education","OWID literate-and-illiterate-world-population.zip https://ourworldindata.org/literacy",70,60,85,60,40,70,55,95))
ideas.append(mk("owid_number_births_declining","The World Is Having Fewer Babies Each Year","Annual births peaked around 2012 and are now falling","CHART","worldwide","Line chart","Demographics","OWID number-of-births-per-year.zip https://ourworldindata.org/population-growth",65,65,80,70,55,60,55,95))
ideas.append(mk("owid_one_year_olds_declining","Fewer One-Year-Olds Each Year","The number of 1-year-olds alive globally has peaked and is declining","CHART","worldwide","Line chart","Demographics","OWID number-of-one-year-olds.zip https://ourworldindata.org/population-growth",60,60,75,75,50,55,65,95))

# ============================================================
# INJECTION LOGIC
# ============================================================
with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
print("Existing ideas: %d" % len(existing_ids))

new_ideas = []
dupes = 0
for idea in ideas:
    m = re.search(r'id:"([^"]+)"', idea)
    if m and m.group(1) not in existing_ids:
        new_ideas.append(idea)
    else:
        dupes += 1

print("New ideas to inject: %d (skipped %d dupes)" % (len(new_ideas), dupes))
if len(new_ideas) == 0:
    print("Nothing to inject.")
    sys.exit(0)

tail = "]; // end D"
if tail not in raw:
    print("ERROR: Cannot find tail marker")
    sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print("Injected %d ideas. Total now: %d" % (len(new_ideas), len(existing_ids) + len(new_ideas)))
