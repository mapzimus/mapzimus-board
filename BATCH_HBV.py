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
# === "The Algorithm Decided" — tech/society ===
mk("HBV01","Where Facebook Marketplace Replaced Craigslist","The platform shift in local classifieds mapped by market dominance","MAP","US-metro","Dot map","Technology|Economy|Demographics","SimilarWeb: Traffic Data; Pew: Online Activities (pewresearch.org)",55,72,72,72,48,72,72,60),
mk("HBV02","Amazon Same-Day Delivery Coverage vs. Income","Same-day delivery zones cluster around wealthy neighborhoods","MAP","US-metro","Bivariate choropleth","Technology|Economy|Inequality","Amazon: Same-Day Delivery Areas (aboutamazon.com); Census: ACS Income (census.gov)",72,78,72,82,72,78,78,72),
mk("HBV03","Google Search Result Differences by Location","The same query returns different results in different states","CHART","US-state","Bar chart","Technology|Politics|Media","Google: Search Transparency (transparencyreport.google.com); Various Research Studies",62,68,68,82,65,65,82,58),
mk("HBV04","Algorithmic Bail Decisions vs. Human Judge Decisions by Race","AI recidivism scores show the same racial bias as human judges","XREF","US-national","Bar chart","Technology|Crime|Race|Law","ProPublica: Machine Bias (propublica.org); Various: COMPAS Algorithm Studies",80,68,68,82,82,65,82,72),
# === Environment × Demographics ===
mk("HBV05","Environmental Gentrification: Parks That Displaced the People They Were Built For","Green space investment raises rents and pushes out original residents","MAP","US-city","Dot map","Environment|Demographics|Housing|Inequality","Various: Urban Greening Studies; Zillow: Rent Data (zillow.com/research)",78,72,68,80,78,78,80,62),
mk("HBV06","Tree Canopy Coverage by Neighborhood Income","Rich neighborhoods have 3x more tree shade than poor ones","MAP","US-city","Bivariate choropleth","Environment|Demographics|Inequality","USFS: Urban Tree Canopy (fs.usda.gov); Census: ACS Income by Block Group (census.gov)",78,72,72,80,75,80,75,78),
# === Economy × Crime ===
mk("HBV07","Unemployment Spike Timing vs. Crime Spike Timing","Crime lags unemployment by 6-12 months — the delay mapped","XREF","US-metro","Line chart","Economy|Crime","BLS: LAUS (bls.gov); FBI: UCR Monthly Crime (fbi.gov)",68,68,72,78,72,65,75,82),
mk("HBV08","Minimum Wage Increases vs. Small Business Survival Rate","Do minimum wage hikes kill small businesses? The data says no","XREF","US-state","Scatter plot","Economy|Labor|Politics","Census: Business Dynamics Statistics (census.gov); DOL: Minimum Wage History (dol.gov)",72,72,78,82,72,65,78,78),
# === Health × Poverty deep dives ===
mk("HBV09","Dental Care Access by County Income","Poor counties have 1 dentist per 5000 people vs. 1 per 1200 in wealthy ones","MAP","US-county","Bivariate choropleth","Health|Poverty|Infrastructure","HRSA: HPSA Dental (data.hrsa.gov); Census: SAIPE (census.gov)",78,75,72,72,75,78,68,82),
mk("HBV10","Preventable Hospitalization Rate by Income Level","Poor neighborhoods send more people to the ER for conditions that shouldnt need it","XREF","US-county","Scatter plot","Health|Poverty|Economy","AHRQ: Prevention Quality Indicators (ahrq.gov); Census: ACS Income (census.gov)",78,72,72,72,75,65,68,82),
# === International × Crime ===
mk("HBV11","Countries Where Police Kill the Most People Per Capita","The US ranks among the worlds worst for police killings","RANK","World","Bar chart","International|Crime|Law","Mapping Police Violence (mappingpoliceviolence.us); Small Arms Survey (smallarmssurvey.org)",82,72,78,78,82,65,68,82),
mk("HBV12","Human Trafficking Routes Worldwide","The modern slave trade mapped from origin to destination","MAP","World","Line map","International|Crime|Immigration","UNODC: Human Trafficking (unodc.org); ILO: Forced Labour (ilo.org)",80,62,68,78,82,82,72,78),
# === Education × Geography ===
mk("HBV13","PhD Production Rate by County","A handful of counties produce most of Americas doctorates","MAP","US-county","County choropleth","Education|Geography|Science","NSF: Survey of Earned Doctorates (nsf.gov); Census: County Data (census.gov)",60,58,75,78,55,80,72,85),
mk("HBV14","Community College Enrollment Rate by State","The unsung backbone of American higher education","MAP","US-state","State choropleth","Education|Geography|Economy","AACC: Community College Data (aacc.nche.edu); NCES: IPEDS (nces.ed.gov)",62,68,78,68,58,78,65,88),
# === Finance × Health ===
mk("HBV15","Bankruptcy Filing Rate vs. Uninsured Rate by State","No insurance leads to medical debt leads to bankruptcy","XREF","US-state","Scatter plot","Finance|Health|Economy","US Courts: Bankruptcy Statistics (uscourts.gov); Census: ACS Health Insurance (census.gov)",80,78,75,72,78,65,68,88),
mk("HBV16","GoFundMe Medical Campaigns by State","Crowdfunding as a healthcare system — where people beg strangers for medical help","MAP","US-state","State choropleth","Finance|Health|Poverty","GoFundMe: Medical Campaign Data; Census: ACS Health Insurance (census.gov)",85,82,68,78,82,78,78,62),
# === History × Environment ===
mk("HBV17","Every Major Oil Spill on a World Map","From Deepwater Horizon to Exxon Valdez to the Niger Delta","MAP","World","Dot map","History|Environment|Energy","ITOPF: Oil Spill Database (itopf.org); NOAA: Incident News (incidentnews.noaa.gov)",72,58,72,72,72,82,68,82),
mk("HBV18","The Dust Bowl Then and Now","1930s erosion zones overlaid with current soil degradation data","MAP","US-state","Bivariate choropleth","History|Environment|Agriculture","USDA: Soil Erosion Maps Historical; NRCS: Soil Survey (nrcs.usda.gov)",72,62,72,78,72,80,75,78),
# === Demographics × International ===
mk("HBV19","Countries Where More People Leave Than Arrive","Net negative migration mapped globally","MAP","World","World choropleth","Demographics|International|Immigration","UN: International Migration (population.un.org); World Bank: Net Migration (worldbank.org)",65,60,78,72,62,78,68,88),
mk("HBV20","The Most Common Baby Name by Country","Cultural identity in a single data point per nation","MAP","World","World choropleth","Demographics|International|Geography","Various: National Statistics Offices; UN: Names Database",52,65,78,72,45,80,70,72),
# === Poverty × Health ===
mk("HBV21","Maternal Mortality in Rural vs. Urban America","Rural women die in childbirth at nearly double the rate","XREF","US-national","Bar chart","Poverty|Health|Rural|Gender","CDC: Pregnancy Mortality Surveillance (cdc.gov); Census: Urban-Rural (census.gov)",85,72,72,78,82,65,72,82),
mk("HBV22","Food Insecurity Rate vs. Proximity to Military Bases","Active-duty military families experience food insecurity at surprising rates","XREF","US-national","Scatter plot","Poverty|Health|Military","USDA: Food Security (ers.usda.gov); DoD: Military Family Studies (militaryonesource.mil)",78,68,68,85,75,65,82,68),
# === Infrastructure × Rural ===
mk("HBV23","Cell Phone Dead Zones in Rural America","The map of where you lose signal entirely","MAP","US-county","County choropleth","Infrastructure|Rural|Technology","FCC: Broadband Coverage (broadbandmap.fcc.gov); OpenSignal: Coverage Maps (opensignal.com)",72,75,72,72,68,82,68,78),
mk("HBV24","Miles to Nearest Hospital ER by County","Some rural Americans are over 60 miles from emergency care","MAP","US-county","County choropleth","Infrastructure|Rural|Health","CMS: Hospital Locations (data.cms.gov); Census: County Geography (census.gov)",82,78,72,72,80,82,68,88),
# === Sports × Economy deep dives ===
mk("HBV25","College Football Revenue vs. Academic Spending at the Same University","Some schools spend more on football than on all academics combined","XREF","US-national","Scatter plot","Sports|Education|Economy","NCAA: Financial Reports (ncaa.org); NCES: IPEDS Finance (nces.ed.gov)",78,75,78,82,78,65,78,82),
mk("HBV26","NBA Player Salaries vs. Teacher Salaries in the Same City","The contrast in how we value entertainment vs. education","CHART","US-city","Bar chart","Sports|Economy|Education|Inequality","Basketball Reference: Salaries; BLS: Teacher Pay by Metro (bls.gov)",78,82,78,78,72,65,72,82),
# === Final unique combos ===
mk("HBV27","Americas Nuclear Waste Storage Map","Where spent fuel rods are sitting with no permanent disposal plan","MAP","US-national","Dot map","Energy|Environment|Science","NRC: Spent Fuel Storage (nrc.gov); DOE: Nuclear Waste Policy (energy.gov)",72,62,72,78,75,82,72,85),
mk("HBV28","Countries by Number of Active Volcanoes","Indonesia has 127 and the Ring of Fire hosts 75% of all eruptions","MAP","World","World choropleth","Science|Geography|International","Smithsonian: Global Volcanism Program (volcano.si.edu); USGS: Volcano Hazards",55,55,78,72,52,80,65,90),
mk("HBV29","Americas Most Politically Competitive Counties","Places where elections are decided by less than 2 points every cycle","MAP","US-county","County choropleth","Politics|Democracy|Geography","MIT: Election Lab (electionlab.mit.edu); Cook Political Report (cookpolitical.com)",68,72,72,72,68,80,68,85),
mk("HBV30","The Pupil to Teacher Ratio Map of America","Some districts cram 35 kids in a classroom while others have 15","MAP","US-county","County choropleth","Education|Infrastructure|Inequality","NCES: Pupil-Teacher Ratio (nces.ed.gov); Census: School Data (census.gov)",75,78,78,68,72,78,65,88),
mk("HBV31","The Most Common Tree Species in Every State","Americas forest biodiversity mapped by dominant species","MAP","US-state","State choropleth","Environment|Geography|Science","USFS: Forest Inventory and Analysis (fia.fs.usda.gov)",50,55,75,72,42,80,68,90),
mk("HBV32","Average Age at Death by Cause","Heart disease kills at 75 but overdoses kill at 38","CHART","US-national","Bar chart","Health|Demographics|Science","CDC: WONDER Multiple Cause of Death (wonder.cdc.gov)",72,72,80,78,72,65,68,90),
mk("HBV33","Americas Vanishing Wetlands","Wetland loss acreage by state since 1950","MAP","US-state","State choropleth","Environment|History|Agriculture","USFWS: Wetland Status and Trends (fws.gov); NOAA: Coastal Wetlands (coast.noaa.gov)",72,58,72,72,72,80,68,82),
mk("HBV34","Pet Spending Per Capita by State","Americans spend more on their pets than many countries spend on healthcare per citizen","MAP","US-state","State choropleth","Economy|Demographics|Health","APPA: Pet Industry Data (americanpetproducts.org); BLS: Consumer Expenditure (bls.gov)",58,72,75,78,50,78,72,75),
mk("HBV35","Americas Ghost Towns Map","Census-designated places that once thrived and now have near-zero population","MAP","US-national","Dot map","History|Geography|Economy","Census: Decennial Historical (census.gov); Ghost Town databases (ghosttowns.com)",60,62,72,78,55,82,75,72),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBV ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBV batch)")
