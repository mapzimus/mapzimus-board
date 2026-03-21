"""
BATCH_GD.py — Cross-dataset XREF ideas combining multiple sources
These ideas mash up two or more datasets for unique insights.
Run: cd D:\projects\mapzimus-board && $py BATCH_GD.py && $py maintain.py
"""
import re, os, sys

DATA_JS = r"D:\projects\mapzimus-board\data.js"

# v4 algorithm
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
# CROSS-DATASET XREFs: FBI crime + FiveThirtyEight socioeconomic
# ============================================================
ideas.append(mk("xref_murder_rate_vs_poverty","Murder Rates vs Poverty by State","FBI homicide rates mapped against Census poverty rates","XREF","us_state","Bivariate choropleth","Crime and Law Enforcement","FBI UCR + Census ACS https://cde.ucr.cjis.gov + https://data.census.gov",85,80,80,65,85,85,70,90))
ideas.append(mk("xref_crime_vs_gun_ownership","Violent Crime vs Gun Ownership by State","Do states with more guns have more violent crime","XREF","us_state","Scatter plot","Crime and Law Enforcement","FBI UCR + RAND gun ownership estimates https://cde.ucr.cjis.gov + https://www.rand.org",80,80,75,75,90,65,70,85))
ideas.append(mk("xref_hate_crimes_vs_diversity","Hate Crimes vs Racial Diversity by State","FiveThirtyEight hate crime rates vs share non-white population","XREF","us_state","Scatter plot","Crime and Law Enforcement","FiveThirtyEight + Census ACS https://github.com/fivethirtyeight/data",75,70,75,80,85,65,75,95))
ideas.append(mk("xref_drunk_driving_vs_alcohol_tax","Drunk Driving Deaths vs State Alcohol Tax","Do higher alcohol taxes actually reduce drunk driving fatalities","XREF","us_state","Scatter plot","Crime and Law Enforcement","FiveThirtyEight bad-drivers + Tax Foundation https://github.com/fivethirtyeight/data",70,75,70,80,60,60,80,85))

# ============================================================
# CROSS-DATASET XREFs: Schools + Demographics
# ============================================================
ideas.append(mk("xref_title_i_schools_vs_poverty","Title I Schools Track Poverty Almost Perfectly","Mapping school poverty classification against Census income data","XREF","us_county","Bivariate choropleth","Education","NCES Schools + Census ACS https://nces.ed.gov + https://data.census.gov",75,80,80,55,60,85,60,90))
ideas.append(mk("xref_school_density_vs_child_pop","Where Schools Are Missing","School density vs under-18 population reveals underserved areas","XREF","us_county","Bivariate choropleth","Education","NCES Schools + Census ACS https://nces.ed.gov + https://data.census.gov",75,80,75,70,65,85,70,85))

# ============================================================
# CROSS-DATASET XREFs: MBTA + Census equity
# ============================================================
ideas.append(mk("xref_mbta_access_vs_income","Transit Access vs Income in Greater Boston","Proximity to MBTA stops mapped against median household income","XREF","us_city","Bivariate choropleth","Transportation","MBTA GTFS + Census ACS https://www.mbta.com/developers + https://data.census.gov",80,80,80,70,75,85,75,85))
ideas.append(mk("xref_mbta_access_vs_race","Transit Access and Race in Metro Boston","MBTA rail access by census tract mapped against racial demographics","XREF","us_city","Bivariate choropleth","Transportation","MBTA GTFS + Census ACS https://www.mbta.com/developers + https://data.census.gov",80,75,75,70,80,85,75,85))
ideas.append(mk("xref_mbta_commute_vs_car_ownership","Who Rides the T vs Who Drives","MBTA ridership areas vs car ownership rates by tract","XREF","us_city","Bivariate choropleth","Transportation","MBTA GTFS + Census ACS + LODES https://www.mbta.com/developers",65,80,75,60,50,80,65,85))

# ============================================================
# CROSS-DATASET XREFs: Religion + Politics + Crime
# ============================================================
ideas.append(mk("xref_religion_vs_trump_vote","Church Attendance and the Trump Vote","County-level religious adherent rates vs 2020 Trump vote share","XREF","us_county","Bivariate choropleth","Elections","ARDA Religion Census 2020 + MIT Election Lab https://www.thearda.com + https://electionlab.mit.edu",75,75,75,70,80,85,70,85))
ideas.append(mk("xref_religion_vs_crime_rate","The Bible Belt Paradox: Religion and Crime","Counties with highest church attendance dont have lowest crime rates","XREF","us_county","Scatter plot","Crime and Law Enforcement","ARDA Religion Census 2020 + FBI UCR https://www.thearda.com + https://cde.ucr.cjis.gov",70,65,70,85,80,65,80,80))
ideas.append(mk("xref_religion_vs_teen_pregnancy","The Abstinence Paradox","Most religious states have highest teen pregnancy rates","XREF","us_state","Scatter plot","Health","ARDA Religion Census + CDC WONDER https://www.thearda.com + https://wonder.cdc.gov",75,70,70,85,85,60,80,80))

# ============================================================
# CROSS-DATASET XREFs: Walkability + Health + Economic
# ============================================================
ideas.append(mk("xref_walkability_vs_home_values","Walkable Neighborhoods Cost More","EPA walkability scores vs Zillow home value indices","XREF","us_county","Scatter plot","Economy","EPA Walkability Index + Zillow ZHVI https://www.epa.gov + https://www.zillow.com/research/data",65,80,75,65,50,60,70,85))
ideas.append(mk("xref_walkability_vs_car_dependence","Americas Most Car-Dependent Counties","Walkability index vs vehicles per household by county","XREF","us_county","Bivariate choropleth","Transportation","EPA Walkability Index + Census ACS https://www.epa.gov + https://data.census.gov",60,80,80,55,40,85,60,85))

# ============================================================
# CROSS-DATASET XREFs: Airbnb + Housing + Income
# ============================================================
ideas.append(mk("xref_airbnb_boston_vs_rent","Where Airbnb Revenue Exceeds Rent","Boston neighborhoods where short-term rental income beats long-term leases","XREF","us_city","City map","Economy","AirDNA + Census ACS https://www.airdna.co + https://data.census.gov",70,80,75,75,70,80,75,85))
ideas.append(mk("xref_airbnb_boston_vs_eviction","Airbnb Density and Eviction Rates in Boston","Do neighborhoods with more Airbnbs have higher eviction rates","XREF","us_city","Bivariate choropleth","Economy","AirDNA + Eviction Lab https://www.airdna.co + https://evictionlab.org",80,75,70,80,85,80,80,75))

# ============================================================
# CROSS-DATASET XREFs: CPI/Economic + Social
# ============================================================
ideas.append(mk("xref_inflation_vs_wages","Inflation vs Wage Growth Over 50 Years","CPI growth vs median wage growth - the divergence is staggering","XREF","us_national","Line chart","Economy","BLS CPI + BLS CES https://www.bls.gov/cpi/ + https://www.bls.gov/ces/",80,85,80,65,75,65,55,95))
ideas.append(mk("xref_food_inflation_vs_snap","Food Prices Rose While SNAP Benefits Stayed Flat","PPI food index vs SNAP benefit levels over time","XREF","us_national","Line chart","Economy","BLS PPI + USDA SNAP https://www.bls.gov/ppi/ + https://www.fns.usda.gov/snap",80,80,75,70,80,60,65,85))
ideas.append(mk("xref_energy_inflation_vs_renewables","Energy Prices vs Renewable Adoption","Do states with more renewable energy have more stable energy prices","XREF","us_state","Scatter plot","Environment","BLS PPI Energy + EIA Renewable Data https://www.bls.gov/ppi/ + https://www.eia.gov",60,65,70,75,55,60,75,80))

# ============================================================
# CROSS-DATASET XREFs: OWID global + FBI US comparison
# ============================================================
ideas.append(mk("xref_us_homicide_vs_world","Americas Murder Rate in Global Context","US homicide rate compared to every country - worse than any peer nation","XREF","worldwide","Bar chart","Crime and Law Enforcement","FBI UCR + OWID Homicide https://cde.ucr.cjis.gov + https://ourworldindata.org/homicides",85,80,85,70,85,60,55,95))
ideas.append(mk("xref_us_prison_rate_vs_world","America Locks Up More People Than Any Country on Earth","US incarceration rate dwarfs every nation including authoritarian regimes","XREF","worldwide","Bar chart","Crime and Law Enforcement","FBI/BJS + OWID Prison Rate https://bjs.ojp.gov + https://ourworldindata.org/incarceration",85,80,85,65,85,60,50,95))
ideas.append(mk("xref_us_child_mortality_vs_peers","Americas Child Mortality Problem Among Rich Nations","US has worst child mortality rate of any developed country","XREF","worldwide","Bar chart","Health","CDC + OWID Child Mortality https://www.cdc.gov + https://ourworldindata.org/child-mortality",85,80,80,75,80,60,60,90))
ideas.append(mk("xref_us_life_expectancy_vs_spending","America Spends the Most on Healthcare but Lives Shorter","US health spending vs life expectancy compared to peer nations","XREF","worldwide","Scatter plot","Health","CMS + OWID + WHO https://www.cms.gov + https://ourworldindata.org/life-expectancy",85,85,80,70,80,65,60,95))

# ============================================================
# CROSS-DATASET XREFs: Schools + Crime
# ============================================================
ideas.append(mk("xref_school_funding_vs_crime","Do Better-Funded Schools Reduce Crime","Per-pupil spending vs violent crime rate by county","XREF","us_county","Scatter plot","Education","NCES Schools + FBI UCR https://nces.ed.gov + https://cde.ucr.cjis.gov",70,70,70,75,65,60,75,75))
ideas.append(mk("xref_school_segregation_vs_income","School Segregation Mirrors Income Segregation","Title I school concentration vs median income by county","XREF","us_county","Bivariate choropleth","Education","NCES Schools + Census ACS https://nces.ed.gov + https://data.census.gov",80,75,75,65,80,85,65,85))

# ============================================================
# CROSS-DATASET XREFs: Multiple source mashups
# ============================================================
ideas.append(mk("xref_college_major_vs_state_industry","Which States Need Which Degrees","Dominant college major employment vs dominant state industry","XREF","us_state","State choropleth","Economy","FiveThirtyEight Majors + BEA NAICS https://github.com/fivethirtyeight/data + https://www.bea.gov",55,70,70,70,40,75,75,80))
ideas.append(mk("xref_bad_drivers_vs_road_quality","Bad Drivers or Bad Roads","Fatal crash rates vs state highway infrastructure quality ratings","XREF","us_state","Bivariate choropleth","Transportation","FiveThirtyEight bad-drivers + ASCE Infrastructure Report https://github.com/fivethirtyeight/data + https://infrastructurereportcard.org",65,80,70,75,55,80,75,80))
ideas.append(mk("xref_alcohol_consumption_vs_liver_disease","Countries That Drink the Most Die of Liver Disease","Total alcohol consumption vs liver disease mortality worldwide","XREF","worldwide","Scatter plot","Health","FiveThirtyEight drinks + OWID Causes of Death https://github.com/fivethirtyeight/data + https://ourworldindata.org/causes-of-death",70,65,75,70,55,60,70,85))
ideas.append(mk("xref_cousin_marriage_vs_birth_defects","Cousin Marriage Rates vs Birth Defect Prevalence","Do countries with higher consanguinity have more genetic disorders","XREF","worldwide","Scatter plot","Health","FiveThirtyEight cousin-marriage + WHO/OWID https://github.com/fivethirtyeight/data + https://www.who.int",65,60,70,85,70,60,80,75))
ideas.append(mk("xref_democracy_vs_co2","Democracies vs Autocracies on Climate","Do democratic nations emit more or less CO2 per capita than autocracies","XREF","worldwide","Scatter plot","Climate","OWID Political Regime + OWID CO2 https://ourworldindata.org/democracy + https://ourworldindata.org/co2-emissions",65,60,75,80,70,60,80,90))
ideas.append(mk("xref_internet_access_vs_democracy","Does Internet Access Strengthen Democracy","Share of population online vs political regime classification","XREF","worldwide","Scatter plot","Science & Technology","OWID Internet + OWID Democracy https://ourworldindata.org/internet + https://ourworldindata.org/democracy",60,55,70,75,65,60,80,90))
ideas.append(mk("xref_fertility_vs_education","More Education = Fewer Babies Everywhere","Years of schooling vs fertility rate by country","XREF","worldwide","Scatter plot","Demographics","OWID Education + OWID Fertility https://ourworldindata.org/global-education + https://ourworldindata.org/fertility-rate",70,65,80,60,50,60,60,95))
ideas.append(mk("xref_military_spending_vs_life_expectancy","Guns or Butter: Military Spending vs Life Expectancy","Countries that spend more on military tend to have shorter lives","XREF","worldwide","Scatter plot","History","OWID Military + OWID Life Expectancy https://ourworldindata.org/military-spending + https://ourworldindata.org/life-expectancy",65,60,70,75,70,60,75,90))
ideas.append(mk("xref_ev_stations_vs_ev_registrations","Do EV Chargers Follow the Cars or Lead Them","EV charging station density vs EV registration rates by state","XREF","us_state","Bivariate choropleth","Transportation","DOE AFDC + State DMV registrations https://afdc.energy.gov + https://afdc.energy.gov/vehicle-registration",55,70,75,70,40,80,70,85))

# ============================================================
# INJECTION LOGIC
# ============================================================
with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()

existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
print("Existing ideas: %d" % len(existing_ids))

# Dedupe
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
    print("ERROR: Cannot find tail marker '%s'" % tail)
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print("Injected %d ideas. Total now: %d" % (len(new_ideas), len(existing_ids) + len(new_ideas)))
print("Run maintain.py next!")
