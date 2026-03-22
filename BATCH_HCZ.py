import re, os
DATA = os.path.join(os.path.dirname(__file__), 'data.js')

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

IDEAS = [
mk("HCZ01","The Last White Majority: When Each State Becomes Majority-Minority","Projected year each state becomes majority-minority based on Census demographic projections","MAP","US","State choropleth","demographics","Census: Population Projections by Race (census.gov/programs-surveys/popproj.html)",72,72,78,82,78,78,72,78),
mk("HCZ02","Americas Twin Deficit: Where Birth Rates and Immigration Both Fell","Counties experiencing both declining birth rates and declining immigration — double demographic shrinkage","MAP","US","County choropleth","demographics","Census: Components of Population Change (census.gov)",78,72,78,78,80,82,75,80),
mk("HCZ03","The Graying Workforce: Median Age of Workers by Industry","Which industries have the oldest workers — farming, utilities, government — and which have the youngest","CHART","US","Bar chart","demographics","BLS: Current Population Survey Age Data (bls.gov/cps/demographics.htm)",72,75,78,75,72,70,72,85),
mk("HCZ04","Where Everybody Knows Your Name: Small Town America Is Disappearing","Number of incorporated places with population under 1,000 over time — the vanishing small town","CHART","US","Line chart","demographics","Census: Incorporated Places Population (census.gov/data/tables/time-series/demo/popest)",75,75,75,72,72,70,72,82),
mk("HCZ05","The College Town Demographic Distortion: How Students Warp Local Data","Cities where college students are 30%+ of population, distorting poverty rates, age, and income statistics","MAP","US","Dot map","demographics","NCES: College Enrollment by Institution (nces.ed.gov/ipeds)",62,68,75,78,58,80,75,78),
mk("HCZ06","Americas Most Ethnically Homogeneous vs. Diverse Counties","Counties at both extremes of the ethnic diversity index — from 99% one group to perfect demographic balance","MAP","US","County choropleth","demographics","Census: ACS Diversity Index (data.census.gov)",68,68,78,78,65,82,72,85),
mk("HCZ07","The Snowbird Effect: Seasonal Population Swings in Sun Belt Counties","Counties whose population doubles or triples during winter months due to seasonal migration","MAP","US","County choropleth","demographics","Census: Seasonal Estimates of Population (census.gov)",62,72,72,78,58,80,72,72),
mk("HCZ08","The Teacher Age Crisis: Average Teacher Age by State and Subject","States where the average teacher is over 50 — the mass retirement cliff for American education","MAP","US","State choropleth","demographics","NCES: Schools and Staffing Survey (nces.ed.gov/surveys/sass)",72,72,75,72,72,78,68,78),
mk("HCZ09","Americas Invisible Population: People Living in Group Quarters","Population in nursing homes, prisons, military barracks, college dorms, and shelters by state — people the census counts but neighborhoods dont see","MAP","US","State choropleth","demographics","Census: Group Quarters Population (census.gov/topics/income-poverty/poverty/guidance/group-quarters.html)",65,62,72,78,62,78,75,82),
mk("HCZ10","The Natalist Policy Scorecard: Countries Paying People to Have Babies","Government financial incentives for childbearing by country — from Hungarys tax exemptions to Japans cash bonuses — plotted against actual fertility impact","XREF","World","Scatter plot","demographics","OECD: Family Benefits Database (oecd.org/social/family/database.htm)",68,68,75,82,68,68,78,75),
mk("HCZ11","Where Gen Z Actually Lives: Youngest-Skewing ZIP Codes in America","ZIP codes with the highest percentage of population under 25, showing Gen Zs actual geography","MAP","US","County choropleth","demographics","Census: ACS Age by ZIP (data.census.gov)",62,72,75,72,58,82,68,85),
mk("HCZ12","The Demographic Cliff in Higher Education: Projected 18-Year-Old Population by State","How many fewer 18-year-olds each state will have in 2030 vs. 2020 — the enrollment cliff mapped","MAP","US","State choropleth","demographics","WICHE: Knocking at the College Door (wiche.edu/resources/knocking-at-the-college-door)",78,72,78,78,78,78,72,82),
mk("HCZ13","Americas Only Majority-Asian County and Other Demographic Singularities","Counties that are demographic outliers — majority Asian (Honolulu), majority Native (several), majority Hispanic (dozens)","MAP","US","Dot map","demographics","Census: ACS Race by County (data.census.gov)",62,65,75,78,58,82,75,85),
mk("HCZ14","The Commuter City Paradox: Cities Where Daytime Population Doubles","Cities where the weekday working population dramatically exceeds the residential population — Manhattan goes from 1.6M to 4M","RANK","US","Bar chart","demographics","Census: Commuter-Adjusted Population (census.gov/topics/employment/commuting)",65,72,78,78,60,72,72,82),
mk("HCZ15","The Interracial Marriage Map: Where Mixed-Race Couples Live","Percentage of married couples that are interracial by county, showing integration geography","MAP","US","County choropleth","demographics","Census: ACS Married Couple Characteristics (data.census.gov)",68,72,72,72,62,82,68,82),
mk("HCZ16","Where Nobody Has Kids Under 5: The Disappearing Toddler","Counties where less than 3% of the population is under age 5 — where babies are rare","MAP","US","County choropleth","demographics","Census: ACS Age Under 5 by County (data.census.gov)",72,72,75,78,72,82,72,85),
mk("HCZ17","Americas Population Center Has Moved 1,000 Miles Southwest Since 1790","The mean center of US population mapped for every census since 1790, showing the westward and southward drift","MAP","US","Special map","demographics","Census: Center of Population (census.gov/geographies/reference-files/time-series/geo/centers-population.html)",65,68,80,72,60,85,72,88),
mk("HCZ18","The Bachelor Tax: Countries That Have Taxed or Incentivized Single People","Historical and current countries that impose penalties on unmarried adults or incentivize marriage through tax policy","MAP","World","World choropleth","demographics","Tax Foundation: Marriage Penalty Studies (taxfoundation.org)",62,68,72,85,60,78,82,68),
mk("HCZ19","Americas Tallest and Shortest States: Average Height by State and Gender","Average adult height by state showing regional nutrition and genetic patterns","MAP","US","State choropleth","demographics","CDC: NHANES Anthropometric Data (cdc.gov/nchs/nhanes.htm)",55,72,72,72,50,78,68,78),
mk("HCZ20","The Citizenship Gap: Eligible but Not Naturalized Immigrants by Country of Origin","Percentage of green card holders eligible for citizenship who havent naturalized, by country of origin","CHART","US","Bar chart","demographics","DHS: Immigration Statistics Yearbook (dhs.gov/immigration-statistics/yearbook)",68,62,72,78,65,68,72,78),
mk("HCZ21","Where Americas Twins Live: Twin Birth Rate by State","Twin birth rates per 1,000 births by state, influenced by IVF access, maternal age, and race","MAP","US","State choropleth","demographics","CDC: NCHS Multiple Birth Data (cdc.gov/nchs/data/nvsr)",55,65,72,78,50,78,75,82),
mk("HCZ22","The Middle Class Mapped: Where Median Income Actually Gets You a Middle Class Life","Counties where the median household income affords a home, car, childcare, and retirement savings vs. those where it doesnt","MAP","US","County choropleth","demographics","EPI: Family Budget Calculator (epi.org/resources/budget)",78,85,78,72,72,82,72,75),
mk("HCZ23","Americas Most Transient ZIP Codes: Where Nobody Lives for More Than 3 Years","ZIP codes with the highest population turnover — military bases, college towns, and housing-unstable areas","MAP","US","Dot map","demographics","Census: ACS Geographic Mobility (data.census.gov)",65,68,72,78,62,80,72,78),
mk("HCZ24","The Empty Nester Explosion: Households With No Children Under 18","Percentage of households with no children under 18 by county — now the majority nationwide","MAP","US","County choropleth","demographics","Census: ACS Household Type (data.census.gov)",68,75,75,72,65,82,68,85),
mk("HCZ25","Where Americas LGBTQ+ Population Concentrates: Self-Identification Rates by State","Percentage of adults identifying as LGBTQ+ by state, showing concentration in urban coastal areas","MAP","US","State choropleth","demographics","Gallup: LGBT Identification (news.gallup.com/poll/lgbt.aspx)",65,72,72,72,62,78,68,78),
mk("HCZ26","The Boomer Inheritance Cliff: Estimated Wealth Transfer by State Over 20 Years","Projected intergenerational wealth transfer as Baby Boomers pass, by state — the biggest wealth event in history","MAP","US","State choropleth","demographics","Cerulli Associates: Great Wealth Transfer (cerulli.com)",72,75,78,78,72,78,72,68),
mk("HCZ27","Americas Oldest First-Time Homebuyers Ever: Age at First Home Purchase Over Time","Average age of first-time homebuyer by year, showing the steady climb from 29 in 1981 to 36 today","CHART","US","Line chart","demographics","NAR: Profile of Home Buyers and Sellers (nar.realtor/research-and-statistics)",72,82,78,72,72,68,68,82),
mk("HCZ28","The Two Americas of Life Expectancy: Gap Between Top and Bottom Counties","The 20-year gap in life expectancy between the healthiest and unhealthiest US counties, mapped","MAP","US","County choropleth","demographics","IHME: US County Life Expectancy (healthdata.org)",85,78,78,78,85,82,68,82),
mk("HCZ29","The Only Child Nation: Where Single-Child Families Dominate","Countries and US states where single-child families are the majority, driven by economics and policy","MAP","World","World choropleth","demographics","Census: ACS Family Size (data.census.gov)",68,72,72,75,65,78,72,78),
mk("HCZ30","Americas Youngest and Oldest Mayors: Age of Municipal Leadership","Average age of mayors in the 100 largest US cities — municipal leadership demographics","RANK","US","Bar chart","demographics","National League of Cities: Mayoral Database (nlc.org)",55,62,72,72,52,68,72,68),
mk("HCZ31","The Remote Work Migration Map: Where Americans Moved When Location Didnt Matter","Net migration patterns during 2020-2023 remote work era, showing who left where and who went where","MAP","US","County choropleth","demographics","Census: County-to-County Migration Flows (census.gov/data/tables/2023/demo/geographic-mobility)",72,78,75,72,68,82,68,80),
mk("HCZ32","Americas Population Density Extremes: From Manhattan to Loving County","The full spectrum of US population density — from 72,000 per sq mi in Manhattan to 0.1 in remote Nevada","MAP","US","County choropleth","demographics","Census: Population Density by County (data.census.gov)",62,68,78,78,58,85,68,88),
mk("HCZ33","The Reverse Migration: Black Americans Moving Back to the South","Net Black population migration back to the Southeast after decades of Great Migration northward","MAP","US","State choropleth","demographics","Census: ACS State-to-State Migration (census.gov/data/tables/time-series/demo/geographic-mobility)",72,68,78,78,70,80,72,80),
mk("HCZ34","When Your Country Gets Old Before It Gets Rich: The Aging Trap","Countries facing rapid population aging while still at low-to-middle income — China, Thailand, Brazil vs. rich aging nations","XREF","World","Scatter plot","demographics","World Bank: Age Dependency Ratio (data.worldbank.org)",72,65,75,82,75,70,78,78),
mk("HCZ35","Americas Next Megalopolis: Where the Supercities Are Forming","Metropolitan statistical areas merging into continuous urban corridors — Texas Triangle, Cascadia, Front Range","MAP","US","Special map","demographics","Census: Metropolitan Statistical Areas (census.gov/programs-surveys/metro-micro.html)",65,68,75,78,65,88,75,78),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All 35 ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HCZ batch)")
