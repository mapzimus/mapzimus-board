"""
BATCH_GG.py — High-virality, controversy, and shock value ideas
These are optimized for maximum engagement: emotional impact, surprise factor,
tension/debate, and visual appeal. Designed to go viral on Instagram/Reddit.
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
# WEALTH INEQUALITY & CLASS (high emotion + tension)
# ============================================================
ideas.append(mk("viral_billionaire_wealth_vs_median","If Bezos Spent 1 Dollar Per Second Hed Last 6300 Years","Visualizing billionaire wealth vs median American net worth","CHART","us_national","Bar chart","Economy","Forbes Real-Time Billionaires https://www.forbes.com/real-time-billionaires/",85,80,80,85,80,65,70,95))
ideas.append(mk("viral_ceo_pay_ratio_by_company","CEOs Make 344x Their Workers Pay","CEO-to-median-worker pay ratio at Americas largest companies","RANK","us_national","Bar chart","Economy","AFL-CIO Executive Paywatch https://aflcio.org/paywatch",85,85,80,70,85,60,50,95))
ideas.append(mk("viral_wealth_bottom_50_vs_top_1","The Bottom 50% Own Less Than the Top 0.1%","Distribution of US household wealth - the bottom half has almost nothing","CHART","us_national","Bar chart","Economy","Federal Reserve DFA https://www.federalreserve.gov/releases/z1/dataviz/dfa/",85,80,80,75,85,60,55,95))
ideas.append(mk("viral_housing_affordability_crisis","Homes Cost 7x Median Income Now vs 3x in 1980","Home price to income ratio by metro area over time","CHART","us_national","Line chart","Economy","FRED + Zillow + Census https://fred.stlouisfed.org",85,90,80,65,80,65,50,95))
ideas.append(mk("viral_rent_vs_wage_divergence","Rent Has Risen 3x Faster Than Wages Since 2000","Indexed growth of median rent vs median wage","CHART","us_national","Line chart","Economy","BLS + Census ACS https://www.bls.gov + https://data.census.gov",85,90,80,65,80,60,50,95))
ideas.append(mk("viral_tax_rate_richest_americans","Americas Richest Pay a Lower Tax Rate Than the Middle Class","Effective tax rate by income percentile shows a regressive reality","CHART","us_national","Bar chart","Economy","ProPublica + IRS SOI https://www.propublica.org + https://www.irs.gov/statistics/soi-tax-stats",80,80,75,80,90,60,65,90))

# ============================================================
# AMERICA VS OTHER COUNTRIES (shock comparisons)
# ============================================================
ideas.append(mk("viral_us_healthcare_spending","America Spends 2x More on Healthcare and Gets Worse Results","Healthcare spending per capita vs life expectancy","XREF","worldwide","Scatter plot","Health","CMS + WHO + OECD https://www.cms.gov + https://www.who.int",85,85,80,70,75,65,50,95))
ideas.append(mk("viral_us_gun_deaths_vs_peers","American Gun Deaths Dwarf Every Other Rich Nation","Annual gun deaths per 100K in US vs peer countries","CHART","worldwide","Bar chart","Crime and Law Enforcement","CDC WONDER + UN Office on Drugs and Crime https://wonder.cdc.gov",90,80,85,55,90,60,45,95))
ideas.append(mk("viral_us_paid_leave_vs_world","Every Developed Nation Guarantees Paid Parental Leave Except One","Weeks of paid parental leave by country","MAP","worldwide","World choropleth","Labor","OECD Family Database https://www.oecd.org/els/family/database.htm",85,80,85,60,80,85,50,95))
ideas.append(mk("viral_us_vacation_days_vs_world","Americans Get the Least Vacation Time in the Developed World","Mandatory paid vacation days by country - US is 0","MAP","worldwide","World choropleth","Labor","OECD + ILO Working Conditions https://www.ilo.org",80,85,85,60,70,85,50,95))
ideas.append(mk("viral_us_infant_mortality_vs_peers","American Babies Die at Higher Rates Than in Cuba or Croatia","Infant mortality rate US vs other countries over time","CHART","worldwide","Bar chart","Health","WHO + CDC https://www.who.int + https://www.cdc.gov",85,80,85,75,80,60,55,95))
ideas.append(mk("viral_us_math_scores_global","American Students Rank 28th in Math Globally","PISA math scores by country - US trails most of Europe and Asia","RANK","worldwide","Bar chart","Education","OECD PISA https://www.oecd.org/pisa/",75,85,85,65,65,60,45,95))
ideas.append(mk("viral_us_student_debt_vs_world","American Student Debt Is a Global Anomaly","Average student loan debt at graduation by country","CHART","worldwide","Bar chart","Education","OECD Education at a Glance + TICAS https://www.oecd.org/education/",80,85,80,70,75,60,55,90))
ideas.append(mk("viral_us_incarceration_timeline","Americas Prison Population Exploded in 1980","US incarceration rate from 1920 to present vs other countries","CHART","us_national","Line chart","Crime and Law Enforcement","BJS + The Sentencing Project https://www.sentencingproject.org",80,75,85,65,85,65,55,95))

# ============================================================
# RACE & JUSTICE (high tension + emotional)
# ============================================================
ideas.append(mk("viral_police_killings_by_race","Police Kill Black Americans at 3x the Rate","Rate of police killings per million by race","CHART","us_national","Bar chart","Crime and Law Enforcement","Mapping Police Violence https://mappingpoliceviolence.us",90,75,80,60,95,60,50,95))
ideas.append(mk("viral_wealth_gap_by_race","The Racial Wealth Gap Has Barely Changed in 60 Years","Median net worth by race from 1963 to present","CHART","us_national","Line chart","Economy","Federal Reserve SCF https://www.federalreserve.gov/econres/scfindex.htm",85,75,80,65,90,60,55,95))
ideas.append(mk("viral_redlining_still_visible","1930s Redlining Maps Predict Todays Neighborhood Wealth","HOLC redlining grades vs current median income by census tract","MAP","us_city","Bivariate choropleth","History","Mapping Inequality + Census ACS https://dsl.richmond.edu/panorama/redlining/",90,75,80,70,90,85,70,90))
ideas.append(mk("viral_school_segregation_2024","American Schools Are Resegregating","Share of Black students in majority-minority schools over time","CHART","us_national","Line chart","Education","NCES Common Core of Data https://nces.ed.gov/ccd/",80,75,80,65,85,60,60,90))
ideas.append(mk("viral_sentencing_disparity_race","Black Americans Get 20% Longer Sentences for the Same Crime","Average federal sentence length by race controlling for offense","CHART","us_national","Bar chart","Crime and Law Enforcement","US Sentencing Commission https://www.ussc.gov/research/research-reports/",85,70,80,70,90,55,60,95))

# ============================================================
# GENDER & SOCIAL (debate-generating)
# ============================================================
ideas.append(mk("viral_gender_pay_gap_by_occupation","Women Earn 83 Cents for Every Dollar Men Earn","Gender pay gap by detailed occupation","CHART","us_national","Bar chart","Labor","BLS Current Population Survey https://www.bls.gov/cps/",75,85,80,50,80,60,45,95))
ideas.append(mk("viral_women_in_parliament_world","Women Hold Just 26% of Parliamentary Seats Worldwide","Share of women in national parliament by country","MAP","worldwide","World choropleth","Demographics","IPU Parline Database https://data.ipu.org",70,60,80,55,70,85,50,95))
ideas.append(mk("viral_abortion_access_map","Abortion Access After Dobbs","Legal status of abortion by state as of 2025","MAP","us_state","State choropleth","Health","Guttmacher Institute https://www.guttmacher.org/state-policy/explore/overview-abortion-laws",85,80,80,50,95,80,45,95))
ideas.append(mk("viral_childcare_cost_vs_income","Childcare Now Costs More Than College in Most States","Average annual childcare cost vs median household income by state","MAP","us_state","State choropleth","Economy","DOL National Database of Childcare Prices https://www.dol.gov/agencies/wb/topics/childcare",85,90,80,65,75,80,55,95))
ideas.append(mk("viral_marriage_rate_collapse","Americans Stopped Getting Married","Marriage rate per 1000 from 1900 to present","CHART","us_national","Line chart","Demographics","CDC NCHS + Census https://www.cdc.gov/nchs/",65,80,80,60,55,60,50,95))

# ============================================================
# HEALTH CRISIS (emotional + relatable)
# ============================================================
ideas.append(mk("viral_depression_rates_teens","Teen Depression Has Doubled Since 2010","Share of teens reporting major depressive episode by year","CHART","us_national","Line chart","Health","SAMHSA NSDUH https://www.samhsa.gov/data/nsduh",85,85,80,60,70,60,50,95))
ideas.append(mk("viral_suicide_rate_by_state","Americas Suicide Crisis by State","Age-adjusted suicide rate varies 4x between states","MAP","us_state","State choropleth","Health","CDC WONDER https://wonder.cdc.gov",85,75,80,55,80,80,45,95))
ideas.append(mk("viral_life_expectancy_us_dropped","American Life Expectancy Has Dropped 3 Years Since 2019","Life expectancy decline 2019-2022 by cause of death","CHART","us_national","Bar chart","Health","CDC NCHS Life Expectancy data https://www.cdc.gov/nchs/",85,80,85,70,75,60,55,95))
ideas.append(mk("viral_diabetes_rate_map","Americas Diabetes Epidemic by State","Adult diabetes prevalence by state has more than doubled since 2000","MAP","us_state","State choropleth","Health","CDC Diabetes Atlas https://gis.cdc.gov/grasp/diabetes/diabetesatlas.html",75,80,85,50,55,80,45,95))
ideas.append(mk("viral_healthcare_bankruptcy","66% of US Bankruptcies Are Tied to Medical Bills","Medical debt as a factor in personal bankruptcy filings","CHART","us_national","Bar chart","Health","AJPH + Consumer Financial Protection Bureau https://www.consumerfinance.gov",85,85,75,70,80,55,55,85))
ideas.append(mk("viral_loneliness_epidemic","Americas Loneliness Epidemic","Share of Americans reporting having no close friends has quadrupled since 1990","CHART","us_national","Line chart","Health","Survey Center on American Life https://www.americansurveycenter.org",85,90,75,70,65,55,60,90))

# ============================================================
# GEOPOLITICAL SHOCK VALUE
# ============================================================
ideas.append(mk("viral_nuclear_warheads_map","Every Nuclear Warhead on Earth","Nuclear warhead stockpile by country mapped","MAP","worldwide","World choropleth","History","FAS Nuclear Notebook https://fas.org/initiative/nuclear-notebook/",75,60,80,60,85,85,55,95))
ideas.append(mk("viral_refugee_crisis_map","80 Million People Are Refugees or Displaced","Refugee population by country of origin and destination","MAP","worldwide","World choropleth","History","UNHCR Refugee Data Finder https://www.unhcr.org/refugee-statistics/",85,60,80,55,80,85,55,95))
ideas.append(mk("viral_press_freedom_map","Where Journalists Are Not Free","Press freedom index by country - most of the world restricts media","MAP","worldwide","World choropleth","History","Reporters Without Borders https://rsf.org/en/index",75,55,80,60,80,85,55,95))
ideas.append(mk("viral_death_penalty_world","Countries That Still Execute People","Legal status of the death penalty worldwide","MAP","worldwide","World choropleth","Crime and Law Enforcement","Amnesty International https://www.amnesty.org/en/what-we-do/death-penalty/",70,60,80,55,80,85,55,95))
ideas.append(mk("viral_surveillance_cameras_per_capita","The Most Surveilled Countries on Earth","CCTV cameras per 1000 people by country","MAP","worldwide","World choropleth","Science & Technology","Comparitech + IHS Markit https://www.comparitech.com",55,60,80,75,70,85,65,85))
ideas.append(mk("viral_territory_if_sea_level_rise","What the Map Looks Like With 3 Meters of Sea Level Rise","Coastal land area lost under moderate sea level rise scenarios","MAP","worldwide","Special map","Climate","Climate Central Coastal Risk https://www.climatecentral.org",80,70,80,75,80,85,70,90))
ideas.append(mk("viral_countries_never_invaded_by_uk","Countries Britain Has Never Invaded","Only 22 countries have never been invaded or occupied by Britain","MAP","worldwide","World choropleth","History","Stuart Laycock analysis + historical records https://www.stuartlaycock.co.uk",50,55,80,90,55,85,75,90))
ideas.append(mk("viral_age_of_consent_map","Age of Consent Laws Around the World","Legal age of consent varies from 12 to 21 across countries","MAP","worldwide","World choropleth","Crime and Law Enforcement","Ageofconsent.net + national legal codes https://www.ageofconsent.net",55,60,80,80,75,85,60,90))
ideas.append(mk("viral_countries_by_regime_change","How Many Times Each Country Changed Its Government Type","Number of regime changes since 1900 by country","MAP","worldwide","World choropleth","History","V-Dem Dataset + OWID https://www.v-dem.net + https://ourworldindata.org/democracy",55,50,75,80,60,85,75,90))

# ============================================================
# QUIRKY / HIGH-SURPRISE (Reddit-bait)
# ============================================================
ideas.append(mk("viral_left_handed_by_country","Where Left-Handed People Live","Prevalence of left-handedness by country","MAP","worldwide","World choropleth","Demographics","Papadatou-Pastou et al 2020 meta-analysis https://doi.org/10.1037/bul0000229",40,55,75,85,30,85,80,80))
ideas.append(mk("viral_most_common_birthday","The Most Common Birthday in America","September 9th wins - count back 9 months from New Years Eve","CHART","us_national","Special map","Demographics","CDC NCHS + SSA birth data https://www.cdc.gov/nchs/ + https://www.ssa.gov",50,80,80,80,30,70,70,95))
ideas.append(mk("viral_daylight_hours_by_latitude","How Much Daylight You Get Depends on Where You Live","Hours of daylight by latitude throughout the year","CHART","worldwide","Special map","Geography & Environment","NOAA Solar Calculator + astronomical data https://gml.noaa.gov/grad/solcalc/",45,70,80,55,25,80,60,95))
ideas.append(mk("viral_driving_side_map","Which Side of the Road Every Country Drives On","Left-hand vs right-hand traffic worldwide","MAP","worldwide","World choropleth","Transportation","World Standards day + national traffic codes https://worldstandards.eu",40,60,85,70,20,85,55,95))
ideas.append(mk("viral_countries_without_military","Countries With No Military","Nations that have no armed forces at all","MAP","worldwide","World choropleth","History","CIA World Factbook + SIPRI https://www.cia.gov/the-world-factbook/",45,45,80,85,45,85,75,90))
ideas.append(mk("viral_national_animals_map","Every Countrys National Animal","National animals mapped - from eagles to unicorns","MAP","worldwide","World choropleth","Entertainment","National symbols databases + government sources",40,60,80,70,20,85,65,90))
ideas.append(mk("viral_pizza_restaurants_per_capita","Americas Most Pizza-Obsessed States","Pizza restaurants per capita by state","MAP","us_state","State choropleth","Food & Nutrition","Census County Business Patterns NAICS 722513 https://www.census.gov/programs-surveys/cbp.html",45,80,80,60,25,80,55,90))
ideas.append(mk("viral_closest_country_to_every_point","The Nearest Foreign Country to Every Point in the US","Which foreign country is closest to each part of the continental US","MAP","us_national","Special map","Geography & Environment","Calculated from national boundary coordinates",40,60,75,85,25,85,85,90))
ideas.append(mk("viral_time_zones_world","The Worlds Time Zone Chaos","Not all time zones are one hour apart - India is +5:30 Nepal is +5:45","MAP","worldwide","World choropleth","Geography & Environment","IANA tz database https://www.iana.org/time-zones",40,55,80,80,25,85,70,95))
ideas.append(mk("viral_countries_drive_vs_fly","When It Becomes Faster to Fly Than Drive","Break-even distance where flying beats driving by country","MAP","worldwide","World choropleth","Transportation","Various aviation and road infrastructure data",40,70,75,75,25,80,80,75))
ideas.append(mk("viral_tallest_building_timeline","The Tallest Building in the World Over Time","From the Great Pyramid to the Burj Khalifa - who held the record when","CHART","worldwide","Bar chart","History","Council on Tall Buildings https://www.ctbuh.org",45,55,85,60,25,65,60,95))
ideas.append(mk("viral_landlocked_countries_map","Landlocked Countries and Their Closest Port","43 countries have no coastline - how far is their nearest ocean port","MAP","worldwide","World choropleth","Geography & Environment","CEPII + port authority data https://www.cepii.fr",40,40,80,75,30,85,75,90))
ideas.append(mk("viral_us_states_by_area_vs_population","If States Were Sized by Population Not Area","Cartogram of US states resized to match their population","MAP","us_state","Special map","Demographics","Census Population Estimates https://www.census.gov",55,75,80,70,35,80,65,95))
ideas.append(mk("viral_how_far_from_mcdonalds","The Farthest You Can Be From a McDonalds in America","McDesert - the point in the continental US most distant from any McDonalds","MAP","us_national","Special map","Food & Nutrition","McDonalds store locator data + geographic analysis",45,75,80,80,25,85,80,90))

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
