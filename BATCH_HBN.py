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
# === "Scrollstopper" — one-image viral infographics ===
mk("HBN01","The US Economy Explained in One Treemap","Every sector sub-sector and major company sized by GDP contribution","CHART","US-national","Treemap","Economy|Technology|Labor","BEA: GDP by Industry (bea.gov)",68,72,82,72,62,78,68,92),
mk("HBN02","Every Nuclear Warhead on Earth on One Map","Which countries have them how many and where they point","MAP","World","Dot map","War|International|Military","SIPRI: Nuclear Forces (sipri.org); FAS: Nuclear Notebook (fas.org)",75,60,78,78,78,82,68,88),
mk("HBN03","The Full US Budget in One Visualization","Every dollar of federal spending sized proportionally","CHART","US-national","Treemap","Economy|Politics","CBO: Budget Projections (cbo.gov); OMB: Budget Data (whitehouse.gov/omb)",68,72,85,72,65,78,65,95),
mk("HBN04","All the Water on Earth Compared to All the Land","If you collected all water into a sphere it would be shockingly small","CHART","World","Infographic","Science|Environment|Geography","USGS: How Much Water (usgs.gov); NASA: Earth Data (earthdata.nasa.gov)",62,58,78,88,58,82,80,90),
mk("HBN05","The Timeline of Earth if 24 Hours Represented All of History","Humans appear in the last 1.5 seconds","CHART","World","Infographic","Science|History","Smithsonian: Geologic Time Scale (si.edu); USGS: Geologic Time (usgs.gov)",58,58,78,85,52,72,78,88),
# === Housing × Labor ===
mk("HBN06","Where Teachers Can Afford to Live Near Their School","In many districts teachers are priced out of the communities they serve","MAP","US-metro","Bivariate choropleth","Housing|Labor|Education","BLS: Teacher Salaries (bls.gov); Zillow: Home Values (zillow.com/research)",85,85,72,78,80,78,72,78),
mk("HBN07","Essential Worker Pay vs. Cost of Living by Metro","Nurses firefighters and teachers cant afford the cities that need them","XREF","US-metro","Scatter plot","Housing|Labor|Economy","BLS: OES Metro Area Data (bls.gov); BEA: Regional Price Parities (bea.gov)",82,85,78,78,78,68,72,82),
mk("HBN08","Average Commute Time for Low-Wage vs. High-Wage Workers","Low-income workers commute farther because they cant afford to live close","XREF","US-metro","Bar chart","Housing|Labor|Transportation|Inequality","Census: ACS Commuting by Income (census.gov); BLS: Occupational Employment (bls.gov)",78,82,78,78,72,65,72,85),
# === Science × International ===
mk("HBN09","R&D Spending as Percent of GDP by Country","Who is investing in the future","MAP","World","World choropleth","Science|International|Economy","UNESCO: R&D Data (uis.unesco.org); World Bank: Research Expenditure (worldbank.org)",65,60,78,72,62,78,65,90),
mk("HBN10","Scientific Papers Per Capita by Country","Small countries punch way above their weight","RANK","World","Bar chart","Science|International|Education","NSF: Science and Engineering Indicators (nsf.gov); World Bank: Population (worldbank.org)",60,58,78,78,55,65,70,88),
mk("HBN11","STEM Graduates by Country as Percent of All Graduates","China and India produce far more engineers per capita than the West","RANK","World","Bar chart","Science|International|Education","UNESCO: Education Data (uis.unesco.org); OECD: Education at a Glance (oecd.org)",65,62,78,78,62,65,72,88),
# === Crime × Geography deep dives ===
mk("HBN12","The Safest and Most Dangerous Neighborhoods Within Each City","Crime varies more within cities than between them","MAP","US-city","City map","Crime|Geography","FBI: NIBRS Incident Data (fbi.gov); Local PD: Open Data Portals",75,82,72,72,72,82,70,72),
mk("HBN13","Property Crime Heat Map of Every Major US City","Where car theft burglary and package theft cluster","MAP","US-city","City map","Crime|Geography|Economy","FBI: NIBRS (fbi.gov); SpotCrime: Crime Data (spotcrime.com)",72,80,75,68,68,82,65,72),
mk("HBN14","The Geography of Hate Crimes in America","FBI-reported hate crime incidents mapped by county","MAP","US-county","Dot map","Crime|Geography|Race","FBI: Hate Crime Statistics (fbi.gov); Census: Demographics (census.gov)",82,72,72,75,82,78,68,82),
# === Gender × Economy deep dives ===
mk("HBN15","The Unpaid Labor Gap","Hours of unpaid domestic and care work per week by gender in every country","MAP","World","World choropleth","Gender|Economy|International","OECD: Time Use Data (oecd.org); ILO: Care Work (ilo.org)",80,78,75,78,75,78,72,82),
mk("HBN16","Women CEO Percentage of Fortune 500 Over Time","From 0 in 1972 to 10% in 2023 — progress or embarrassment?","CHART","US-national","Area chart","Gender|Economy|History","Fortune: Fortune 500 Women CEOs (fortune.com); Catalyst: Women in Business (catalyst.org)",75,72,78,72,72,68,65,88),
mk("HBN17","Venture Capital Funding for Female vs. Male Founders","Women receive 2% of all VC dollars","CHART","US-national","Bar chart","Gender|Finance|Technology","Crunchbase: Funding Data (crunchbase.com); PitchBook: VC Data (pitchbook.com)",80,72,78,80,78,65,72,82),
# === Agriculture × Economy deep dives ===
mk("HBN18","Farm Income by County: Who Is Actually Making Money","Most farms lose money — the profitable ones are massive","MAP","US-county","County choropleth","Agriculture|Economy","USDA: Farm Income Data (ers.usda.gov); Census of Agriculture (nass.usda.gov)",72,68,75,78,72,80,68,88),
mk("HBN19","The Almond Water Paradox","California uses 10% of its water on almonds during a drought","CHART","US-state","Bar chart","Agriculture|Environment|Economy","USDA: Crop Water Use (ers.usda.gov); CDFA: Agricultural Statistics (cdfa.ca.gov)",72,72,78,82,72,65,78,82),
mk("HBN20","Americas Monoculture Problem","Percentage of farmland planted with just corn and soybeans by county","MAP","US-county","County choropleth","Agriculture|Environment|Economy","USDA: Crop Acreage Data (nass.usda.gov); Census of Agriculture (nass.usda.gov)",68,60,72,78,68,80,75,88),
# === Politics × Race ===
mk("HBN21","Voter Suppression Law Strength by State vs. Minority Population","The pattern is hard to ignore","XREF","US-state","Scatter plot","Politics|Race|Democracy|Law","Brennan Center: Voting Laws (brennancenter.org); Census: ACS Race (census.gov)",82,72,68,78,85,65,78,78),
mk("HBN22","Felony Disenfranchisement by State and Race","5.2 million Americans cant vote due to felony convictions","MAP","US-state","State choropleth","Politics|Race|Crime|Democracy","Sentencing Project: Felony Disenfranchisement (sentencingproject.org); Census: ACS (census.gov)",82,72,75,78,82,78,72,85),
# === Health × Economy ===
mk("HBN23","Deaths of Despair by County","Alcohol drugs and suicide mapped together reveal an economic crisis","MAP","US-county","County choropleth","Health|Economy|Drugs|Psychology","CDC: WONDER Mortality (wonder.cdc.gov); Case/Deaton: Deaths of Despair Research",88,78,72,78,85,80,72,85),
mk("HBN24","Medical Debt by State as Percent of Household Income","Over 100 million Americans carry medical debt","MAP","US-state","State choropleth","Health|Economy|Finance","CFPB: Medical Debt Data (consumerfinance.gov); Census: ACS Income (census.gov)",85,85,78,75,80,78,68,82),
mk("HBN25","Emergency Room Visits for Non-Emergency Care by State","People without insurance use ERs as primary care — its expensive for everyone","MAP","US-state","State choropleth","Health|Economy|Inequality","CMS: ER Utilization (data.cms.gov); AHRQ: HCUP Data (ahrq.gov)",78,78,78,72,75,78,68,82),
# === Technology × Economy ===
mk("HBN26","Big Tech Market Cap vs. Countries GDP","Apple alone is worth more than most nations","CHART","World","Bar chart","Technology|Economy|International","Yahoo Finance: Market Cap; World Bank: GDP (worldbank.org)",72,68,82,80,68,68,68,90),
mk("HBN27","AI Company Headquarters Map","Where artificial intelligence companies cluster globally","MAP","World","Dot map","Technology|Economy|International","CB Insights: AI Companies (cbinsights.com); Crunchbase: AI Startups (crunchbase.com)",62,58,72,72,60,78,68,78),
mk("HBN28","The Social Media Usage Map of the World","Which platforms dominate in which countries","MAP","World","World choropleth","Technology|International|Media","Statista: Social Media by Country (statista.com); DataReportal: Digital Reports (datareportal.com)",60,68,78,72,55,78,65,82),
# === "Did You Know" quick-hit facts ===
mk("HBN29","The Pacific Ocean Is Bigger Than All the Land on Earth Combined","A map projection that finally shows its true scale","MAP","World","Special map","Geography|Science","Natural Earth: Physical Data (naturalearthdata.com); NOAA: Ocean Facts (oceanservice.noaa.gov)",55,55,78,88,48,85,78,92),
mk("HBN30","Russia Has 11 Time Zones","The country so wide that one end is waking up while the other goes to sleep","MAP","World","Special map","Geography|International","IANA: Time Zone Database (iana.org); Natural Earth: Country Data (naturalearthdata.com)",50,55,78,82,42,82,72,92),
mk("HBN31","Africa Contains More Genetic Diversity Than the Rest of the World Combined","The Out of Africa theory visualized through DNA data","MAP","World","Special map","Science|International|History","1000 Genomes Project (internationalgenome.org); Nature: Human Genetic Diversity Studies",68,55,68,88,62,78,85,75),
mk("HBN32","More People Live Inside This Circle Than Outside It","The famous population circle centered on South China Sea","MAP","World","Special map","Demographics|Geography|International","WorldPop: Population (worldpop.org); UN: Population Data (population.un.org)",55,55,78,88,48,85,72,90),
mk("HBN33","The Entire Interstate Highway System Took 35 Years to Build","Construction timeline animated from 1956 to 1992","MAP","US-national","Animated choropleth","Infrastructure|History|Transportation","FHWA: Interstate History (fhwa.dot.gov); Census: TIGER Roads (census.gov)",65,68,78,75,60,82,72,85),
mk("HBN34","Every Active Volcano on Earth","Ring of Fire and hotspots mapped with eruption history","MAP","World","Dot map","Science|Geography","Smithsonian: Global Volcanism Program (volcano.si.edu); USGS: Volcano Hazards (usgs.gov/volcanoes)",58,55,72,72,52,88,68,92),
mk("HBN35","The Ocean Floor Is More Mapped Than You Think — But Still Only 25%","Bathymetric mapping progress shown as coverage percentage","MAP","World","Special map","Science|Geography|Technology","GEBCO: Seabed 2030 (seabed2030.org); NOAA: Bathymetry (ngdc.noaa.gov)",55,52,72,78,52,88,78,82),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBN ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBN batch)")
