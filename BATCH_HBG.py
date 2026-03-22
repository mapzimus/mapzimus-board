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
# === Housing × Climate ===
mk("HBG01","Homes Built in Flood Zones Before vs. After FEMA Maps Existed","Millions of homes were built before anyone mapped the risk","XREF","US-county","Bivariate choropleth","Housing|Climate|Infrastructure","FEMA: NFIP Policy Data (fema.gov); Census: Year Structure Built (census.gov)",78,75,72,80,78,78,75,78),
mk("HBG02","Home Insurance Costs by County vs. Climate Risk Score","The invisible climate tax already hitting homeowners","XREF","US-county","Bivariate choropleth","Housing|Climate|Economy","NAIC: Homeowners Insurance Data (naic.org); First Street: Climate Risk (firststreet.org)",80,82,72,75,78,78,72,75),
mk("HBG03","Coastal Property Value at Risk From Sea Level Rise","Trillions in real estate that may be underwater by 2060","MAP","US-county","County choropleth","Housing|Climate|Economy","NOAA: Sea Level Rise Viewer (coast.noaa.gov); Zillow: Home Values (zillow.com/research)",82,72,72,78,80,82,72,78),
# === Education × Technology ===
mk("HBG04","Schools That Banned Phones vs. Test Score Changes","Early data from phone-free schools shows measurable gains","XREF","US-state","Bar chart","Education|Technology","EdWeek: Phone Policy Tracker (edweek.org); NAEP: State Results (nces.ed.gov)",78,82,72,78,72,65,78,60),
mk("HBG05","Student Laptop Ratio by Country vs. PISA Scores","More screens doesnt mean better learning","XREF","World","Scatter plot","Education|Technology|International","OECD: PISA ICT Familiarity (oecd.org/pisa); UNESCO: ICT in Education (unesco.org)",72,70,75,80,68,65,78,80),
mk("HBG06","ChatGPT Usage Among Students by University","The AI cheating heat map of higher education","MAP","US-national","Dot map","Education|Technology","Turnitin: AI Writing Detection (turnitin.com); NCES: IPEDS (nces.ed.gov)",68,78,68,78,72,68,80,55),
# === Crime × Demographics ===
mk("HBG07","Age of Peak Criminal Activity in America","Most crime is committed by 18-24 year olds — the age-crime curve","CHART","US-national","Area chart","Crime|Demographics","FBI: UCR Arrests by Age (fbi.gov); Census: Population by Age (census.gov)",70,72,82,72,68,65,68,90),
mk("HBG08","Incarceration Rate by Race and State","Some states incarcerate Black men at 10x the rate of white men","XREF","US-state","Bar chart","Crime|Race|Inequality","BJS: Prisoners Series (bjs.gov); Sentencing Project: State Data (sentencingproject.org)",85,75,78,78,85,68,70,88),
mk("HBG09","Wrongful Convictions by State Per Capita","Which states get it wrong the most often","RANK","US-state","Bar chart","Crime|Law|Race","National Registry of Exonerations (law.umich.edu); Census: Population (census.gov)",82,72,75,78,80,65,75,82),
# === Food × International ===
mk("HBG10","Calories Per Person Per Day by Country","From Eritreas 1600 to Americas 3800","MAP","World","World choropleth","Food|International|Health","FAO: Food Balance Sheets (fao.org); WHO: Nutrition Data (who.int)",72,68,80,72,68,78,65,90),
mk("HBG11","Meat Consumption Per Capita by Country","Americans eat 4x the global average","MAP","World","World choropleth","Food|International|Agriculture","FAO: Food Balance Sheets (fao.org); OECD: Meat Consumption (oecd.org)",68,70,80,72,62,78,65,90),
mk("HBG12","Countries That Eat the Most Insects","Entomophagy is normal for 2 billion people","MAP","World","World choropleth","Food|International|Science","FAO: Edible Insects Database (fao.org); Wageningen: Insect Consumption (wur.nl)",58,62,72,82,55,78,80,72),
# === Poverty × Geography ===
mk("HBG13","The Persistent Poverty Map","Counties that have been in poverty for 30+ consecutive years","MAP","US-county","County choropleth","Poverty|Geography|History","USDA: Persistent Poverty Counties (ers.usda.gov); Census: SAIPE Historical (census.gov)",85,78,78,75,82,82,70,92),
mk("HBG14","Dollar General Density as a Poverty Proxy","Where Dollar General outnumbers grocery stores","MAP","US-county","Bivariate choropleth","Poverty|Geography|Food","ScrapeHero: Dollar General Locations; USDA: Food Access Research Atlas (ers.usda.gov)",78,78,72,80,72,78,78,72),
mk("HBG15","Food Desert Map of America","ZIP codes more than 10 miles from a grocery store","MAP","US-county","County choropleth","Poverty|Food|Geography","USDA: Food Access Research Atlas (ers.usda.gov); Census: ACS (census.gov)",80,78,78,72,75,82,68,90),
# === Politics × Economy ===
mk("HBG16","States That Give More Federal Tax Than They Receive Back","The donor vs. taker state paradox","MAP","US-state","State choropleth","Politics|Economy|Inequality","Rockefeller Institute: Balance of Payments (rockinst.org); IRS: SOI (irs.gov)",78,78,80,82,78,78,72,88),
mk("HBG17","How Congressmembers Stock Portfolios Outperform the Market","Lawmakers beat the S&P 500 with suspicious consistency","CHART","US-national","Line chart","Politics|Finance|Economy","Capitol Trades: Congressional Trading (capitoltrades.com); Yahoo Finance (finance.yahoo.com)",80,78,72,82,82,65,78,78),
mk("HBG18","Campaign Spending Per Vote Won in Every Congressional District","Some seats cost 100x more per vote than others","RANK","US-state","Bar chart","Politics|Economy|Democracy","OpenSecrets: Campaign Finance (opensecrets.org); MIT: Election Lab (electionlab.mit.edu)",72,68,78,78,72,65,75,85),
# === Climate × Economy ===
mk("HBG19","Annual Climate Disaster Costs in the US Since 1980","Billion-dollar disasters went from 3 per year to 25","CHART","US-national","Bar chart","Climate|Economy","NOAA: Billion-Dollar Disasters (ncei.noaa.gov)",78,72,82,75,78,68,65,95),
mk("HBG20","The Climate Migration Map","Where Americans are moving away from climate risk and where theyre moving to","MAP","US-county","Line map","Climate|Demographics|Housing","Redfin: Migration Data (redfin.com); First Street: Climate Risk (firststreet.org)",78,75,70,78,78,82,78,68),
# === Health × Education ===
mk("HBG21","Health Literacy Score by State vs. Preventable Hospital Visits","People who understand health info have fewer ER visits","XREF","US-state","Scatter plot","Health|Education","NCES: Health Literacy (nces.ed.gov); AHRQ: PQI Rates (ahrq.gov)",72,70,72,75,68,65,72,72),
mk("HBG22","Medical School Locations vs. Doctor Shortage Areas","We train doctors in cities but need them in rural areas","MAP","US-national","Bivariate choropleth","Health|Education|Rural","AAMC: Medical School Directory (aamc.org); HRSA: HPSA Data (data.hrsa.gov)",78,72,72,78,75,80,72,85),
# === Labor × International ===
mk("HBG23","Average Hours Worked Per Year by Country","Americans work 400 more hours per year than Germans","RANK","World","Bar chart","Labor|International","OECD: Hours Worked (oecd.org); ILO: Working Time (ilo.org)",78,82,82,78,72,65,65,92),
mk("HBG24","Paid Vacation Days Required by Law in Every Country","The US is the only developed country with zero mandatory days","MAP","World","World choropleth","Labor|International|Law","CEPR: No-Vacation Nation (cepr.net); ILO: Working Conditions (ilo.org)",82,85,80,80,78,78,68,90),
mk("HBG25","Minimum Wage Mapped as Purchasing Power Across Countries","A dollar amount means nothing without context","MAP","World","World choropleth","Labor|International|Prices","OECD: Real Minimum Wages (oecd.org); World Bank: PPP (worldbank.org)",72,78,78,72,68,78,68,88),
# === Environment × Health ===
mk("HBG26","Drinking Water Violations by County","Lead arsenic and PFAS contamination mapped nationwide","MAP","US-county","County choropleth","Environment|Health|Infrastructure","EPA: SDWIS Violations (epa.gov/sdwis); EWG: Tap Water Database (ewg.org)",82,80,72,75,80,82,70,88),
mk("HBG27","PFAS Forever Chemical Contamination Sites","Known sites of PFAS contamination across the United States","MAP","US-national","Dot map","Environment|Health|Science","ATSDR: PFAS Exposure Assessments (atsdr.cdc.gov); EWG: PFAS Map (ewg.org)",80,75,72,75,80,82,72,82),
mk("HBG28","Childhood Lead Exposure Risk by ZIP Code","The zip codes where children are still being poisoned by lead","MAP","US-county","County choropleth","Environment|Health|Children","CDC: Childhood Lead Poisoning (cdc.gov/nceh); Census: Housing Age (census.gov)",85,78,72,78,82,80,70,82),
# === Immigration × International ===
mk("HBG29","Where Americas Immigrants Come From by Decade","The animated shift from Europe to Latin America to Asia","CHART","US-national","Animated bar chart","Immigration|International|History","Census: ACS Place of Birth (census.gov); DHS: Yearbook of Immigration (dhs.gov)",72,68,78,72,68,72,68,90),
mk("HBG30","Remittance Flows From the US to Every Country","Where immigrant workers send money home","MAP","World","World choropleth","Immigration|International|Economy","World Bank: Bilateral Remittance Matrix (worldbank.org)",68,65,75,72,62,80,70,85),
# === Sports × Geography ===
mk("HBG31","NFL Team Fandom by County","The tribal map of American football loyalty","MAP","US-county","County choropleth","Sports|Geography|Entertainment","NYT: NFL Fan Map (nytimes.com); Reddit: r/nfl Survey Data",58,78,75,68,52,85,68,68),
mk("HBG32","Olympic Athletes Per Capita by Country","Small nations punch way above their weight","RANK","World","Bar chart","Sports|International|Demographics","IOC: Athlete Database (olympics.com); World Bank: Population (worldbank.org)",62,65,78,78,55,68,72,90),
mk("HBG33","High School Football Participation Rate by State","Texas and Ohio dominate but the per-capita leaders surprise","MAP","US-state","State choropleth","Sports|Geography|Education","NFHS: Participation Survey (nfhs.org); Census: Youth Population (census.gov)",58,72,78,68,52,78,65,82),
# === Religion × Geography ===
mk("HBG34","Dominant Religion by County in the United States","The denominational map of Americas religious landscape","MAP","US-county","County choropleth","Religion|Geography|Demographics","ARDA: Religious Congregations (thearda.com); Census: County Population (census.gov)",62,68,78,72,58,82,65,85),
mk("HBG35","The Secularization Map","Counties where the none religious affiliation grew fastest since 2000","MAP","US-county","County choropleth","Religion|Geography|Demographics","Pew: Religious Landscape (pewresearch.org); ARDA: County Data (thearda.com)",68,70,75,75,65,80,72,78),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBG ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBG batch)")
