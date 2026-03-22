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
mk("HCQ01","The Vanishing Young: Counties Where the Median Age Is Over 55","US counties with the oldest populations, mostly rural Appalachia and Great Plains — who takes care of them","MAP","US","County choropleth","demographics","Census: ACS Median Age by County (data.census.gov)",78,72,75,78,80,82,72,82),
mk("HCQ02","Where Americas Babies Are Born: Birth Rate by County","County-level birth rates showing the stark urban/rural and regional divides in who is having kids","MAP","US","County choropleth","demographics","CDC: WONDER Natality Data (wonder.cdc.gov)",72,75,78,72,70,82,68,85),
mk("HCQ03","The Dependency Ratio Cliff: Workers Per Retiree by State","Ratio of working-age adults to 65+ population by state, showing which states face the worst caregiver crisis","MAP","US","State choropleth","demographics","Census: Age and Sex Tables (data.census.gov)",78,75,80,78,82,78,72,85),
mk("HCQ04","Americas Last One-Race Counties: Where Diversity Hasnt Arrived","Counties that are still 95%+ one racial group and how that number has changed since 1990","MAP","US","County choropleth","demographics","Census: Race by County Historical (data.census.gov)",72,68,75,80,72,82,75,82),
mk("HCQ05","The Twin Peaks: Americas Bimodal Age Distribution","Population pyramid showing the Baby Boom echo and Millennial bulge creating a double-peak workforce","CHART","US","Bar chart","demographics","Census: Population Estimates by Age (census.gov/data/tables/time-series)",68,72,78,75,70,75,72,88),
mk("HCQ06","Where English Is the Minority: Census Tracts Where Most Speak Another Language at Home","Census tracts where more than 50% of residents speak a language other than English at home","MAP","US","County choropleth","demographics","Census: ACS Language Spoken at Home (data.census.gov)",72,75,72,78,70,82,70,85),
mk("HCQ07","The Childless Map: Metro Areas Where Under-18 Population Is Shrinking Fastest","Cities losing children fastest — shrinking school enrollment, closing pediatric wards, empty playgrounds","MAP","US","Dot map","demographics","Census: Components of Population Change (census.gov)",78,75,75,80,78,78,75,82),
mk("HCQ08","Americas Centenarian Boom: Where the 100+ Population Lives","Geographic distribution of Americans aged 100 and older, per capita by state","MAP","US","State choropleth","demographics","Census: Centenarian Population Estimates (census.gov)",65,62,72,78,60,75,75,80),
mk("HCQ09","The Surname Map of America: Most Common Last Names by County","Dominant surnames by county revealing settlement patterns — Garcia belt, Nguyen clusters, Smith everywhere else","MAP","US","County choropleth","demographics","Census: Frequently Occurring Surnames (census.gov/topics/population/genealogy)",62,78,72,80,55,85,82,80),
mk("HCQ10","One-Person Nation: The Rise of Solo Households","Percentage of single-person households by state, 1960 vs. today — the atomization of American life","MAP","US","Bivariate choropleth","demographics","Census: Household Size Historical (data.census.gov)",75,80,78,78,72,78,72,85),
mk("HCQ11","Where Millennials Actually Moved: Net Migration by Metro for Ages 25-39","Which cities gained and lost millennials in the 2010s, showing the real migration story","MAP","US","Dot map","demographics","Census: County-to-County Migration Flows (census.gov/data/tables/2020/demo/geographic-mobility)",72,80,75,72,68,80,68,82),
mk("HCQ12","The Marriage Map Has Split in Two: Marriage Rates by Education","Marriage rate divergence between college-educated and non-college Americans over 40 years","CHART","US","Line chart","demographics","Census: Current Population Survey Marital Status (census.gov/data/tables/time-series/demo/families)",78,78,75,78,75,70,72,82),
mk("HCQ13","Grandparents Raising Grandchildren: The Silent Demographics Crisis","Counties where grandparents are primary caregivers for children under 18, concentrated in opioid-affected areas","MAP","US","County choropleth","demographics","Census: ACS Grandparents as Caregivers (data.census.gov)",85,78,72,78,82,80,72,80),
mk("HCQ14","The Fertility Collapse Is Global: Birth Rates Below Replacement in 100+ Countries","World map of total fertility rates showing how many countries are now below 2.1 replacement rate","MAP","World","World choropleth","demographics","World Bank: Fertility Rate Total (data.worldbank.org)",78,72,80,80,82,82,72,88),
mk("HCQ15","The Veteran Map: Where Americas 17 Million Veterans Live","Veteran population per capita by county, overlaid with VA facility locations and drive times","MAP","US","County choropleth","demographics","VA: National Center for Veterans Analysis (va.gov/vetdata)",72,70,78,68,70,82,65,85),
mk("HCQ16","Americas Religious Nones Are Now the Largest Group: Unaffiliated by State","States where religiously unaffiliated now outnumber any single denomination","MAP","US","State choropleth","demographics","Pew: Religious Landscape Study (pewresearch.org/religion)",70,72,78,78,68,78,72,80),
mk("HCQ17","The Disability Map: Working-Age Adults With Disabilities by County","Percentage of 18-64 year olds with a disability by county, showing enormous geographic variation","MAP","US","County choropleth","demographics","Census: ACS Disability Status (data.census.gov)",75,72,75,72,72,82,68,85),
mk("HCQ18","Where Women Outnumber Men: The Gender Ratio Map","Counties where female population significantly exceeds male, and the reverse — showing different demographic forces","MAP","US","Bivariate choropleth","demographics","Census: Sex by Age by County (data.census.gov)",65,68,75,78,62,82,72,88),
mk("HCQ19","The Education Sorting Machine: College Degree Rate by ZIP Code","Bachelor degree attainment rate by ZIP code showing hyperlocal educational segregation","MAP","US","County choropleth","demographics","Census: ACS Educational Attainment (data.census.gov)",72,75,78,75,72,82,68,88),
mk("HCQ20","Twin Countries: Nations With Identical Populations but Wildly Different Outcomes","Pairs of countries with nearly the same population but vastly different GDP, life expectancy, freedom scores","XREF","World","Scatter plot","demographics","World Bank: World Development Indicators (data.worldbank.org)",68,65,78,85,72,70,82,82),
mk("HCQ21","The Homeschool Explosion: Where 5%+ of Kids Are Educated at Home","Counties and states where homeschooling rates exceed 5%, mapped against school funding levels","MAP","US","State choropleth","demographics","NCES: Homeschool Statistics (nces.ed.gov/programs/schoolchoice)",72,72,72,78,70,78,72,72),
mk("HCQ22","Americas Most Linguistically Diverse ZIP Codes","ZIP codes where 10+ languages are spoken at home, concentrated in immigrant gateway cities","RANK","US","Bar chart","demographics","Census: ACS Detailed Language Tables (data.census.gov)",65,68,72,80,60,72,78,80),
mk("HCQ23","The Sandwich Generation Mapped: Where Adults Care for Both Kids and Parents","Counties with highest rates of adults simultaneously caring for children and aging parents","MAP","US","County choropleth","demographics","AARP: Caregiving in the US (aarp.org/research/topics/care)",82,85,72,72,78,78,70,70),
mk("HCQ24","Where Nobody Is Having Kids: Zero Natural Increase Counties","Counties where deaths outnumber births — natural population decline without immigration","MAP","US","County choropleth","demographics","Census: Components of Population Change (census.gov)",78,70,78,80,82,82,75,85),
mk("HCQ25","The Pet Parent Paradox: Counties With More Dogs Than Children","Counties where registered dogs outnumber children under 18, a demographic curio","MAP","US","County choropleth","demographics","AVMA: Pet Ownership Data (avma.org/resources-tools/reports-statistics)",62,78,68,85,58,78,82,60),
mk("HCQ26","Americas Oldest First-Time Moms: Average Maternal Age at First Birth by State","States where the average age at first birth has crossed 30, and where it is still under 24","MAP","US","State choropleth","demographics","CDC: NCHS Natality Reports (cdc.gov/nchs/data/nvsr)",72,78,78,75,72,78,70,85),
mk("HCQ27","The Shrinking Household: Average Household Size 1960 vs. Now by State","How American household size has shrunk from 3.3 to 2.5 people, mapped by state","MAP","US","Bivariate choropleth","demographics","Census: Historical Household Size (census.gov/data/tables/time-series/demo/families)",68,75,78,72,70,78,68,88),
mk("HCQ28","The Multigenerational Household Comeback: Three Generations Under One Roof","Counties with highest rates of multigenerational households, correlating with housing costs and cultural factors","MAP","US","County choropleth","demographics","Pew: Multigenerational Households (pewresearch.org/social-trends)",72,78,72,78,70,80,72,78),
mk("HCQ29","The Missing Men: Male Life Expectancy Gap by County","Gap between male and female life expectancy by county — some places over 8 years difference","MAP","US","County choropleth","demographics","IHME: US County Life Expectancy (healthdata.org)",78,72,75,78,80,82,72,82),
mk("HCQ30","Americas Fastest Growing Religion Is No Religion","Growth rate of religiously unaffiliated population by generation, from Silent to Gen Z","CHART","US","Bar chart","demographics","Pew: Religious Landscape Study (pewresearch.org/religion)",72,75,78,78,72,70,72,82),
mk("HCQ31","The Commuter Shed: Where People Sleep vs. Where They Work","Counties where more than 30% of workers commute to a different county — the real economic geography","MAP","US","County choropleth","demographics","Census: Commuting Flows (census.gov/topics/employment/commuting)",68,75,75,72,65,82,70,85),
mk("HCQ32","Where Americas Immigrants Come From Has Completely Flipped","Top country of origin for new immigrants by decade, 1960-2020 — from Europe to Latin America to Asia","CHART","US","Area chart","demographics","Census: Foreign-Born Population Historical (census.gov)",72,72,80,78,72,75,72,85),
mk("HCQ33","The Name Generation Gap: Most Popular Baby Names 1950 vs. 2000 vs. 2025","How Americas most popular baby names have shifted from Mary/James to Olivia/Liam, mapped by state","MAP","US","State choropleth","demographics","SSA: Baby Names by State (ssa.gov/oact/babynames)",60,78,72,72,55,78,72,88),
mk("HCQ34","Americas Fastest Shrinking Counties: Population Loss Champions","Counties that have lost more than 25% of their population since 2000, mapped and ranked","RANK","US","Bar chart","demographics","Census: Intercensal Population Estimates (census.gov)",75,68,78,75,80,78,72,85),
mk("HCQ35","The Demographic Inversion: Cities Where Core Is Now Richer Than Suburbs","Metro areas where median income in the urban core now exceeds suburban median income, reversing 50 years of patterns","MAP","US","Dot map","demographics","Census: ACS Income by Geography (data.census.gov)",70,75,75,82,72,78,80,80),
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
print(f"Injected {len(new)} new ideas (HCQ batch)")
