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
# === "The World Is Stranger Than You Think" ===
mk("HBR01","Countries Where You Drive on the Left","The split between left and right driving and the colonial history behind it","MAP","World","World choropleth","International|Transportation|History","World Standards: Driving Side; Various Historical Sources",50,58,78,78,42,82,68,90),
mk("HBR02","Countries That Use Fahrenheit","There are only 5 and the map is hilarious","MAP","World","World choropleth","International|Science","NIST: Temperature Scales (nist.gov); Various Metrication Sources",48,62,82,85,40,78,72,92),
mk("HBR03","The Date Format Chaos Map","MM/DD/YYYY vs. DD/MM/YYYY vs. YYYY-MM-DD by country","MAP","World","World choropleth","International|Technology","ISO: Date Format Standards (iso.org); Wikipedia: Date Formats by Country",48,65,80,82,40,78,75,88),
mk("HBR04","Countries That Use the Metric System vs. Those That Dont","Its basically the US Myanmar and Liberia","MAP","World","World choropleth","International|Science","BIPM: Metric Convention (bipm.org); CIA: World Factbook (cia.gov)",48,62,82,82,40,78,72,95),
mk("HBR05","Where Toilet Paper Goes in the Toilet vs. the Trash","A map of plumbing infrastructure that surprises Westerners","MAP","World","World choropleth","International|Infrastructure","WHO/UNICEF: Sanitation Data (washdata.org); Various Travel Guides",48,68,72,85,42,78,82,68),
# === Economy × Transportation deep dives ===
mk("HBR06","The True Cost of Car Ownership by City","Insurance gas maintenance parking — the total ranges from 5K to 15K","RANK","US-city","Bar chart","Economy|Transportation","AAA: Driving Costs (aaa.com); Bankrate: Car Insurance (bankrate.com)",75,85,78,72,68,65,68,78),
mk("HBR07","How Much Time Americans Lose to Traffic Per Year","Average hours wasted in congestion by metro area","RANK","US-metro","Bar chart","Economy|Transportation|Geography","INRIX: Global Traffic Scorecard (inrix.com); Census: ACS Commuting (census.gov)",72,85,78,72,68,65,68,85),
mk("HBR08","Pedestrian Death Rate by City","Sun Belt cities designed for cars are killing walkers at record rates","MAP","US-city","Dot map","Transportation|Health|Infrastructure","GHSA: Pedestrian Traffic Fatalities (ghsa.org); NHTSA: FARS (nhtsa.gov)",78,75,72,78,78,78,72,85),
# === Health × Finance ===
mk("HBR09","Medical Debt in Collections by County","Where Americans are drowning in healthcare bills","MAP","US-county","County choropleth","Health|Finance|Poverty","Urban Institute: Debt in America (apps.urban.org); CFPB: Medical Debt (consumerfinance.gov)",85,82,72,72,80,80,68,85),
mk("HBR10","The Cost of Dying in America by State","Average end-of-life medical costs plus funeral expenses","MAP","US-state","State choropleth","Health|Finance|Economy","CMS: Medicare Spending by State (data.cms.gov); NFDA: Funeral Costs (nfda.org)",75,78,78,78,72,78,72,78),
# === Education × Economy ===
mk("HBR11","The College Wealth Premium Is Shrinking","Lifetime earnings advantage of a degree vs. high school is smaller than it was","CHART","US-national","Line chart","Education|Economy|Inequality","Georgetown CEW: Education and Earnings (cew.georgetown.edu); BLS: Education Pays (bls.gov)",78,82,78,78,75,65,72,85),
mk("HBR12","Adjunct Professor Pay Per Course by State","The PhD who teaches your kids class might be making poverty wages","MAP","US-state","State choropleth","Education|Labor|Economy","AAUP: Faculty Compensation (aaup.org); NCES: IPEDS Staffing (nces.ed.gov)",80,72,75,78,78,78,72,78),
# === Crime × Politics deep dive ===
mk("HBR13","Prosecutor Win Rate by County","Some DAs convict at 99%+ rates raising questions about justice","MAP","US-county","County choropleth","Crime|Politics|Law","Measures for Justice: County Data (measuresforjustice.org); BJS: Prosecutors in State Courts (bjs.gov)",72,68,72,80,78,78,75,75),
mk("HBR14","Civil Asset Forfeiture Revenue by State","Police seize billions in property from people never convicted of a crime","MAP","US-state","State choropleth","Crime|Economy|Law","Institute for Justice: Policing for Profit (ij.org); Various State Comptroller Reports",78,72,72,82,80,78,78,72),
# === Health × Demographics ===
mk("HBR15","Life Expectancy by Income Percentile","The top 1% lives 15 years longer than the bottom 1%","CHART","US-national","Line chart","Health|Demographics|Inequality","Chetty et al: JAMA Life Expectancy Study; Census: ACS Income (census.gov)",88,78,78,82,85,65,72,82),
mk("HBR16","Deaths of Despair by Education Level","Non-college-educated Americans are dying at alarming rates","CHART","US-national","Line chart","Health|Demographics|Education","CDC: WONDER Mortality (wonder.cdc.gov); Census: ACS Education (census.gov)",85,78,78,78,82,65,72,85),
# === Economy × Housing deep dives ===
mk("HBR17","The Investor Landlord Map","Percentage of homes purchased by institutional investors by metro","MAP","US-metro","Dot map","Economy|Housing|Finance","Redfin: Investor Data (redfin.com/news); CoreLogic: Investor Activity (corelogic.com)",82,82,72,78,82,78,75,75),
mk("HBR18","Vacant Homes vs. Homeless Population by City","Some cities have 6 empty homes for every homeless person","XREF","US-city","Bar chart","Housing|Poverty|Economy","Census: ACS Vacancy (census.gov); HUD: Point-in-Time Count (hudexchange.info)",85,78,78,85,82,65,78,82),
# === International × Economy ===
mk("HBR19","Countries Where a Years Salary Buys a House vs. Where It Takes 50 Years","The global home price to income ratio","MAP","World","World choropleth","International|Economy|Housing","Numbeo: Property Prices (numbeo.com); OECD: Housing Prices (oecd.org)",78,78,78,78,72,78,68,82),
mk("HBR20","Global Gini Coefficient Map","The worlds most and least equal countries by income","MAP","World","World choropleth","International|Inequality|Economy","World Bank: Gini Index (worldbank.org)",72,65,80,72,68,78,65,92),
# === Energy × Politics ===
mk("HBR21","Fossil Fuel Campaign Donations vs. Climate Voting Record","Which congressmembers receive the most oil money and how they vote","XREF","US-national","Scatter plot","Energy|Politics|Climate","OpenSecrets: Oil and Gas (opensecrets.org); LCV: Environmental Scorecard (lcv.org)",78,68,72,78,80,65,72,82),
mk("HBR22","State Renewable Energy Mandates vs. Actual Renewable Adoption","Which states are meeting their green energy goals","XREF","US-state","Scatter plot","Energy|Politics|Climate","DSIRE: Renewable Portfolio Standards (dsireusa.org); EIA: Renewable Generation (eia.gov)",68,65,75,72,68,68,68,85),
# === Demographics × Geography ===
mk("HBR23","Americas Twin Cities: Metros That Straddle State Lines","Where state borders split metropolitan economies in two","MAP","US-metro","Special map","Demographics|Geography|Economy","Census: Combined Statistical Areas (census.gov); BEA: Metro GDP (bea.gov)",55,65,75,72,48,82,72,88),
mk("HBR24","Counties Where More People Move Out Than Move In","The net domestic migration losers mapped","MAP","US-county","County choropleth","Demographics|Geography|Economy","Census: ACS Migration (census.gov); IRS: SOI Migration (irs.gov)",72,72,78,72,68,80,68,90),
# === Science × Health ===
mk("HBR25","Antibiotic Overprescription Rate by State","Some states prescribe 2x more antibiotics per capita than others","MAP","US-state","State choropleth","Science|Health","CDC: Outpatient Antibiotic Prescriptions (cdc.gov/antibiotic-use); Census: Population (census.gov)",72,72,78,72,68,78,68,85),
mk("HBR26","Clinical Trial Participation by Race vs. Disease Burden","Minorities bear more disease burden but are underrepresented in research","XREF","US-national","Bar chart","Science|Health|Race","FDA: Drug Trials Snapshots (fda.gov); NIH: Clinical Trial Diversity (nih.gov)",80,68,72,80,78,65,78,75),
# === Last unique combos ===
mk("HBR27","Water Price Per Gallon by City","Municipal water costs vary 10x between the cheapest and most expensive cities","RANK","US-city","Bar chart","Prices|Infrastructure|Geography","Circle of Blue: Water Pricing (circleofblue.org); AWWA: Rate Survey (awwa.org)",68,78,78,72,65,65,68,85),
mk("HBR28","The Sleep Deprivation Map of America","Average sleep hours by county and how it correlates with everything","MAP","US-county","County choropleth","Health|Geography|Psychology","CDC: BRFSS Sleep Data (cdc.gov/sleep); Fitbit/Apple Health Aggregate Studies",72,78,72,72,65,78,72,72),
mk("HBR29","Where Americas Electricity Actually Comes From","Power generation source mix for every state in one visualization","MAP","US-state","State choropleth","Energy|Geography|Environment","EIA: Electricity Data (eia.gov)",62,68,80,68,58,78,62,95),
mk("HBR30","The Most Common Business Type in Every ZIP Code","Restaurants in cities farms in rural areas but the edge cases surprise","MAP","US-county","County choropleth","Economy|Geography","Census: County Business Patterns (census.gov); SBA: Business Data (sba.gov)",58,68,75,72,52,80,70,85),
mk("HBR31","Charitable Giving Rate by Income Bracket","The poorest Americans give a higher percentage of income than the richest","CHART","US-national","Bar chart","Economy|Inequality|Finance","IRS: SOI Individual Income Tax (irs.gov); Giving USA (givingusa.org)",78,78,78,82,72,65,72,85),
mk("HBR32","Trash Generation Per Capita by Country","Americans produce 2x the waste of most developed nations","MAP","World","World choropleth","Environment|International","World Bank: What a Waste (worldbank.org); EPA: MSW Data (epa.gov)",68,68,78,78,65,78,65,88),
mk("HBR33","Daylight Saving Time Observation Map","The patchwork of who springs forward and who doesnt","MAP","World","World choropleth","International|Geography|Politics","timeanddate.com: DST Database; IANA: Time Zone Data",48,62,78,72,42,78,68,88),
mk("HBR34","Americas Flood Risk Is Wildly Underestimated","First Street Foundation estimates 2x more properties at risk than FEMA maps show","MAP","US-county","Bivariate choropleth","Climate|Housing|Infrastructure","First Street: Flood Factor (firststreet.org); FEMA: NFIP (fema.gov)",78,75,72,78,78,80,72,78),
mk("HBR35","Every City With a Population That Has Peaked and Is Now Declining","The shrinking cities of America mapped with their peak year","MAP","US-city","Dot map","Demographics|History|Economy","Census: Decennial Census Historical (census.gov); BEA: Metro GDP (bea.gov)",72,68,75,78,72,78,72,88),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBR ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBR batch)")
