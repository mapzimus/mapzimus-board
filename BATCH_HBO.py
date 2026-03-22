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
# === "The Comparison That Rewires Your Brain" ===
mk("HBO01","Americas Annual School Shooting Death Toll vs. Every Other Developed Nation Combined","The total is not even close","CHART","World","Bar chart","Guns|Education|International","Gun Violence Archive (gunviolencearchive.org); OECD: Violence Statistics (oecd.org)",90,78,80,78,88,65,68,82),
mk("HBO02","What the US Spends on Prisons vs. What It Spends on Public Schools","Per person the numbers will shock you","CHART","US-national","Bar chart","Crime|Education|Economy","BJS: Justice Expenditure (bjs.gov); NCES: Education Finance (nces.ed.gov)",85,82,82,82,82,65,70,90),
mk("HBO03","Amazon Revenue vs. Small Business Revenue in Every State","When one company earns more than all small businesses in some states combined","XREF","US-state","Bar chart","Economy|Technology","Amazon: Annual Reports (aboutamazon.com); SBA: Small Business Data (sba.gov)",78,78,78,82,75,65,75,78),
mk("HBO04","US Annual Drug War Spending vs. Drug Overdose Deaths","A trillion dollars spent and the problem got worse","CHART","US-national","Line chart","Drugs|Economy|Crime","DEA: Budget Data (dea.gov); CDC: Drug Overdose Deaths (wonder.cdc.gov)",82,72,78,78,82,68,72,82),
mk("HBO05","Cost of One F-35 Fighter Jet vs. Things That Cost Could Fund","One plane could fund X schools Y hospitals or Z clean water systems","CHART","US-national","Bar chart","Military|Economy|Education","GAO: F-35 Program Cost (gao.gov); Various: Program Costs",75,72,80,82,72,68,78,82),
# === Housing × Demographics ===
mk("HBO06","Average Age of First-Time Homebuyers by Decade","Its been climbing steadily as affordability deteriorated","CHART","US-national","Line chart","Housing|Demographics|Economy","NAR: Profile of Home Buyers (nar.realtor); Census: CPS Housing (census.gov)",82,88,78,75,78,65,68,82),
mk("HBO07","Multigenerational Households by State","The return of extended families living together is accelerating","MAP","US-state","State choropleth","Housing|Demographics","Census: ACS Multigenerational Households (census.gov); Pew: Multigenerational Living (pewresearch.org)",72,78,78,72,65,78,70,88),
mk("HBO08","Tiny Home and Accessory Dwelling Unit Permits by City","The micro-housing revolution mapped","MAP","US-city","Dot map","Housing|Demographics|Economy","Census: Building Permits (census.gov); Freddie Mac: ADU Analysis (freddiemac.com)",62,72,72,72,58,75,72,65),
# === Trade × Agriculture ===
mk("HBO09","Food Miles: How Far Your Grocery Cart Travels Before It Reaches You","Average distance food travels from farm to store shelf by item type","CHART","US-national","Bar chart","Trade|Agriculture|Food","USDA: Food Miles Study (ers.usda.gov); Leopold Center: Food Transport (leopold.iastate.edu)",65,78,78,72,55,65,72,78),
mk("HBO10","Americas Food Import Dependency Map","Which foods we produce enough of and which we rely on imports for","CHART","US-national","Treemap","Trade|Agriculture|Food","USDA: Agricultural Trade (fas.usda.gov); FDA: Import Data (fda.gov)",68,72,78,75,65,72,68,85),
# === Climate × Housing ===
mk("HBO11","The Home Insurance Crisis Map","Counties where major insurers have stopped writing new policies","MAP","US-county","County choropleth","Climate|Housing|Finance","NAIC: Insurance Market Data (naic.org); AM Best: Market Reports (ambest.com)",82,82,72,78,82,80,72,78),
mk("HBO12","Homes That Will Be Underwater by 2050","Properties below projected sea level rise mapped with current values","MAP","US-county","County choropleth","Climate|Housing|Economy","NOAA: Sea Level Rise Viewer (coast.noaa.gov); Zillow: Home Values (zillow.com/research)",82,75,72,78,82,82,72,78),
# === Education × Immigration ===
mk("HBO13","English Language Learner Enrollment by School District","Some districts are 60%+ ELL and funding hasnt caught up","MAP","US-county","County choropleth","Education|Immigration|Demographics","NCES: English Learner Data (nces.ed.gov); Census: ACS Language (census.gov)",72,68,72,72,68,78,68,85),
mk("HBO14","Immigrant Parents Education Level vs. Second-Generation Achievement","Children of immigrants often outperform their peers academically","XREF","US-national","Bar chart","Education|Immigration|Demographics","Census: ACS Education by Nativity (census.gov); NCES: Achievement Gaps (nces.ed.gov)",70,68,75,82,65,65,78,78),
# === Military × Geography ===
mk("HBO15","Every US Military Base in the World","Over 750 bases in 80 countries — the global footprint visualized","MAP","World","Dot map","Military|Geography|International","DoD: Base Structure Report (defense.gov); David Vine: Base Nation Research",72,62,78,78,72,85,68,82),
mk("HBO16","Nuclear Weapons Storage Sites in the United States","Declassified locations where Americas arsenal is kept","MAP","US-national","Dot map","Military|Geography|War","FAS: Nuclear Weapons Complex (fas.org); DoE: NNSA Locations (energy.gov)",72,58,72,82,75,82,72,72),
# === Health × Housing ===
mk("HBO17","Lead Paint Risk Map of America","Homes built before 1978 most likely to have lead paint by county","MAP","US-county","County choropleth","Health|Housing|Children","Census: Year Structure Built (census.gov); CDC: Lead Poisoning (cdc.gov/nceh/lead)",82,78,72,72,78,80,68,88),
mk("HBO18","Mold and Damp Housing Conditions vs. Childhood Asthma","Housing quality directly affects kids health","XREF","US-county","Scatter plot","Health|Housing|Children","Census: ACS Housing Quality (census.gov); CDC: Asthma Data (cdc.gov/asthma)",78,75,68,72,72,65,72,68),
# === Economy × Climate ===
mk("HBO19","Industries Most Vulnerable to Climate Change by State","Tourism agriculture fishing and outdoor rec mapped against warming projections","MAP","US-state","State choropleth","Economy|Climate|Labor","BEA: GDP by Industry by State (bea.gov); Fourth National Climate Assessment (nca2018.globalchange.gov)",72,68,72,78,72,78,72,78),
mk("HBO20","The Green Premium Map","How much more it costs to choose the climate-friendly option in every category","CHART","US-national","Bar chart","Economy|Climate|Energy","Gates Notes: Green Premium (gatesnotes.com); DOE: Cost Comparisons (energy.gov)",68,72,78,78,65,65,72,72),
# === Immigration × Demographics ===
mk("HBO21","Americas Most Linguistically Diverse ZIP Codes","Places where 50+ languages are spoken within a few square miles","MAP","US-city","Dot map","Immigration|Demographics|Geography","Census: ACS Language Spoken at Home (census.gov)",60,68,75,78,55,80,75,88),
mk("HBO22","The Second-Generation Surge","Children of immigrants as a growing share of the US workforce by decade","CHART","US-national","Area chart","Immigration|Demographics|Labor","Census: CPS Nativity Data (census.gov); Pew: Second Generation (pewresearch.org)",68,68,75,72,62,68,70,82),
# === Crime × Economy ===
mk("HBO23","Shoplifting Rates by Metro vs. Wealth Inequality","The metros with the biggest rich-poor gaps have the most retail theft","XREF","US-metro","Scatter plot","Crime|Economy|Inequality","FBI: NIBRS Property Crime (fbi.gov); Census: Gini Coefficient (census.gov)",72,75,72,78,72,65,72,72),
mk("HBO24","The Cost of Mass Incarceration Per Taxpayer by State","What each states residents pay annually to lock people up","MAP","US-state","State choropleth","Crime|Economy|Politics","Vera: Price of Prisons (vera.org); Census: State Population (census.gov)",80,78,78,75,78,78,68,85),
# === Science × Technology ===
mk("HBO25","Moores Law Visualized","Transistor count doubling every 2 years from 1971 to today","CHART","World","Line chart","Science|Technology|History","Intel: Processor History (intel.com); Wikipedia: Transistor Count",62,58,80,72,58,68,62,90),
mk("HBO26","The Speed of Technology Adoption","How long it took to reach 50 million users: radio vs TV vs internet vs ChatGPT","CHART","World","Bar chart","Science|Technology|History","Statista: Technology Adoption (statista.com); Our World in Data: Technology Diffusion",68,72,82,82,62,68,72,85),
# === Religion × Health ===
mk("HBO27","States With Highest Religious Attendance vs. Teen Pregnancy Rate","The Bible Belt paradox mapped","XREF","US-state","Scatter plot","Religion|Health|Children","Gallup: Religious Service Attendance (gallup.com); CDC: Teen Birth Rate (cdc.gov)",70,68,72,85,72,65,78,82),
mk("HBO28","Religious Exemption Vaccine Rates vs. Measles Outbreaks","Where faith-based opt-outs cluster and disease follows","XREF","US-state","Bivariate choropleth","Religion|Health|Children","CDC: Vaccination Coverage (cdc.gov); NCSL: Immunization Exemptions (ncsl.org)",78,68,72,80,78,78,75,78),
# === Law × International ===
mk("HBO29","Countries Where Blasphemy Is Still a Crime","Laws on the books that carry prison or death for religious speech","MAP","World","World choropleth","Law|International|Religion","Pew: Blasphemy Laws (pewresearch.org); USCIRF: Annual Report (uscirf.gov)",72,62,75,78,75,78,68,85),
mk("HBO30","Age of Criminal Responsibility by Country","Some countries prosecute children as young as 7","MAP","World","World choropleth","Law|International|Children|Crime","UNICEF: Justice for Children (unicef.org); CRIN: Minimum Ages (crin.org)",75,65,78,82,72,78,72,82),
# === Remaining novel combinations ===
mk("HBO31","The Friendship Paradox Map","Why your friends have more friends than you do — visualized with social network data","CHART","US-national","Scatter plot","Psychology|Science|Technology","Facebook: Social Connectedness (data.humdata.org); Pew: Social Media (pewresearch.org)",58,68,68,85,55,65,85,65),
mk("HBO32","Earths Biomass Distribution","All life on Earth by weight: plants dominate and humanity is a tiny sliver","CHART","World","Treemap","Science|Environment","PNAS: Bar-On Global Biomass Study; FAO: Forest Resources (fao.org)",60,55,75,88,55,75,82,85),
mk("HBO33","The Map of Nowhere","Most remote inhabited places on Earth by distance from any city over 100K","MAP","World","Dot map","Geography|International|Demographics","GeoNames: City Database (geonames.org); WorldPop: Population (worldpop.org)",55,55,72,78,48,82,80,82),
mk("HBO34","Police Response Time vs. Distance From Station","The further you are from a police station the longer you wait and the longer you wait the less likely a crime is solved","XREF","US-city","Scatter plot","Crime|Infrastructure|Geography","LEMAS: Law Enforcement Survey (bjs.gov); Local PD: CAD Data",72,72,70,72,72,68,72,62),
mk("HBO35","Public Library Density Map of America","Some counties have zero public libraries within 30 miles","MAP","US-county","County choropleth","Education|Infrastructure|Rural","IMLS: Public Library Survey (imls.gov); Census: County Population (census.gov)",68,72,78,72,62,80,68,88),
]

# --- inject ---
with open(DATA, 'r', encoding='utf-8') as f:
    txt = f.read()
ids = set(re.findall(r'id:"([^"]+)"', txt))
new = [i for i in IDEAS if re.search(r'id:"([^"]+)"', i).group(1) not in ids]
if not new:
    print("All HBO ideas already present"); exit()
tail = "]; // end D"
txt = txt.replace(tail, ",\n".join(new) + ",\n" + tail)
with open(DATA, 'w', encoding='utf-8') as f:
    f.write(txt)
print(f"Injected {len(new)} new ideas (HBO batch)")
