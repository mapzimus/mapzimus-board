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
mk("HDG01","The Rural Hospital Crisis: Closures Since 2010 Mapped Against Population","Every rural hospital that closed mapped with the population now driving 30+ miles to the nearest ER","MAP","US","Dot map","rural","Chartis Center for Rural Health: Rural Hospital Closures (chartis.com/resources/rural-health)",82,72,75,68,82,80,66,88),
mk("HDG02","The Dunning-Kruger Atlas: Self-Assessed vs Actual Competence by Country","Survey data on self-rated skills vs standardized test performance — which nations most overestimate their abilities","RANK","World","Scatter plot","psychology","OECD: Survey of Adult Skills PIAAC (oecd.org/skills/piaac)",58,72,65,80,55,62,82,72),
mk("HDG03","Crop Monoculture Risk: Counties Where a Single Crop Dominates 80%+ of Farmland","Americas most vulnerable agricultural counties — corn-only belts in Iowa, cotton-only in West Texas, rice-only in Arkansas","MAP","US","County choropleth","agriculture","USDA: Cropland Data Layer (nassgeodata.gmu.edu/CropScape)",62,58,72,70,68,80,72,88),
mk("HDG04","Fentanyl Seizure Heatmap: Where Border Patrol Intercepts the Most Product","Pounds of fentanyl seized by port of entry and border sector — Nogales and San Diego dominating the map","MAP","US","Dot map","drugs","CBP: Drug Seizure Statistics (cbp.gov/newsroom/stats/drug-seizure-statistics)",72,65,70,68,80,78,62,85),
mk("HDG05","Dollar General Nation: One Store Per 46 Americans in Rural Counties","Dollar General and Dollar Tree store density by county — some rural counties have more dollar stores than grocery stores","MAP","US","County choropleth","rural","SEC: Dollar General 10-K Store Count + Census (sec.gov)",65,78,72,78,65,78,72,80),
mk("HDG06","Nostalgia Bias: When People Think Their Country Was Greatest by Generation","Survey responses to when was your country at its best by birth cohort — everyone picks their childhood decade","CHART","World","Line chart","psychology","Gallup: Global Attitudes (gallup.com)",62,78,65,75,55,58,78,68),
mk("HDG07","The Pollinator Crisis: Honeybee Colony Losses by State and Year","Annual percentage of managed honeybee colonies lost by state — some states losing 40%+ per year since 2006","MAP","US","State choropleth","agriculture","USDA: Honey Bee Colony Reports (usda.gov/nass/honey-bees)",72,65,72,68,75,75,62,85),
mk("HDG08","Psychedelic Therapy Legalization Wave: States Decriminalizing Psilocybin","Map of psilocybin legal status — Oregon legalized therapeutic use, Colorado decriminalized, cities leading the way","MAP","US","State choropleth","drugs","MAPS: Psychedelic Policy Reform (maps.org)",62,58,68,72,65,72,74,72),
mk("HDG09","Broadband Desert: Percentage of Households Without 25 Mbps Internet by County","The digital divide mapped at the county level — Appalachia, Tribal lands, and the Delta still largely disconnected","MAP","US","County choropleth","rural","FCC: Broadband Deployment Data (broadbandmap.fcc.gov)",70,75,78,62,68,80,58,88),
mk("HDG10","The Bystander Effect in Data: Emergency Response Time vs Number of Witnesses","Meta-analysis of bystander intervention studies — how the probability of help decreases as crowd size increases","CHART","World","Scatter plot","psychology","APA: Psychological Bulletin Meta-Analysis (apa.org)",65,72,72,68,62,60,72,75),
mk("HDG11","Soil Erosion Hotspots: Tons of Topsoil Lost Per Acre by Agricultural Region","Americas most eroded farmland — the Mississippi Delta, Palouse, and Texas Blackland Prairie losing soil faster than it forms","MAP","US","County choropleth","agriculture","NRCS: National Resources Inventory (nrcs.usda.gov/nri)",68,55,70,68,72,78,70,82),
mk("HDG12","Meth Lab Map: Clandestine Lab Seizures by County 2004 vs 2024","The dramatic shift from domestic meth labs to Mexican cartel super-labs — rural counties that were hotspots are now quiet","MAP","US","County choropleth","drugs","DEA: National Clandestine Laboratory Register (dea.gov)",68,62,72,72,75,78,68,82),
mk("HDG13","Teacher Shortage by Subject: Unfilled Teaching Positions in Rural vs Urban Schools","Which subjects cant find teachers — math, special education, foreign language — and how rural districts suffer 3x the vacancy rate","CHART","US","Bar chart","rural","DOE: Teacher Shortage Area Report (tsa.ed.gov)",72,75,72,65,72,62,62,80),
mk("HDG14","The Marshmallow Test Replication: Does Delayed Gratification Predict Success?","Updated data on the marshmallow test — original claims about self-control predicting life outcomes largely driven by socioeconomic confounds","CHART","World","Bar chart","psychology","Watts et al: Revisiting the Marshmallow Test (doi.org/10.1177/0956797618761661)",62,68,68,78,58,55,80,72),
mk("HDG15","Farm Size Polarization: Disappearing Mid-Size Farms in America","Average farm acreage over time showing the hollowing out of mid-size operations — either tiny hobby farms or 2000+ acre megafarms survive","CHART","US","Area chart","agriculture","USDA: Census of Agriculture (nass.usda.gov/AgCensus)",68,65,72,70,68,65,68,88),
mk("HDG16","Kratom Consumption Map: Where the Controversial Supplement Is Most Popular","Google Trends and sales data revealing the geography of kratom use — concentrated in rural areas with opioid histories","MAP","US","State choropleth","drugs","Google Trends + American Kratom Association (americankratom.org)",55,58,60,72,62,68,72,58),
mk("HDG17","One-Stoplight Towns: Americas Smallest Incorporated Places Still Holding On","The 500 smallest incorporated municipalities in America — some with populations under 10 — mapped with their founding dates","MAP","US","Dot map","rural","Census Bureau: Subcounty Population Estimates (census.gov)",58,68,65,72,58,75,75,85),
mk("HDG18","Cognitive Bias Frequency: Which Mental Shortcuts People Fall For Most Often","Survey and experimental data on how frequently people exhibit each cognitive bias — confirmation bias leads but anchoring is close","RANK","World","Horizontal bar chart","psychology","Behavioral Economics: Decision Lab (thedecisionlab.com)",62,75,68,68,52,58,72,65),
mk("HDG19","Aquifer Depletion Timeline: When Americas Underground Water Runs Out","Projected depletion dates for major agricultural aquifers — Ogallala, Central Valley, Mississippi Embayment — by section","MAP","US","Special map","agriculture","USGS: Groundwater Depletion (usgs.gov/mission-areas/water-resources)",78,65,72,72,82,78,68,80),
mk("HDG20","Overdose Reversal Map: Naloxone Doses Administered by EMS Per Capita","Where Narcan is being used most frequently by first responders — mapping the frontline of the opioid crisis","MAP","US","County choropleth","drugs","NEMSIS: National EMS Information System (nemsis.org)",75,68,72,62,78,78,60,78),
mk("HDG21","Veterinarian Desert: Rural Counties With No Practicing Vet Within 50 Miles","Livestock-heavy counties where the nearest veterinarian is hours away — a food security risk hiding in plain sight","MAP","US","County choropleth","rural","AVMA: Veterinary Workforce Study (avma.org)",62,58,68,75,65,78,74,72),
mk("HDG22","The Loneliness Epidemic: Self-Reported Loneliness by Age Group and Country","Percentage of people who say they feel lonely often or always — young adults now lonelier than seniors in most nations","CHART","World","Bar chart","psychology","Our World in Data: Loneliness and Social Connections (ourworldindata.org/social-connections)",78,82,72,72,68,58,65,78),
mk("HDG23","Farmland Foreign Ownership: Foreign-Held Agricultural Acreage by State","Which states have the most foreign-owned farmland — Texas leads at 4.4 million acres, and total foreign holdings doubled since 2010","MAP","US","State choropleth","agriculture","USDA: AFIDA Foreign Land Holdings Report (fsa.usda.gov)",65,62,70,75,72,75,68,82),
mk("HDG24","Xylazine Spread: The Zombie Drug Emerging in the US Drug Supply","Geographic spread of xylazine-positive drug samples over time — from Philadelphia epicenter to nationwide contamination","MAP","US","Dot map","drugs","DEA: Emerging Threat Reports (dea.gov)",72,58,65,78,80,75,72,72),
mk("HDG25","Post Office Closures: The Disappearing Federal Presence in Rural America","Every post office closed since 2000 mapped against the community populations they served — the shrinking civic footprint","MAP","US","Dot map","rural","USPS: Office of Inspector General Reports (uspsoig.gov)",68,72,72,65,65,78,68,82),
mk("HDG26","Decision Fatigue: How Parole Board Rulings Change Throughout the Day","The famous study showing judges grant parole at 65% after meals but near 0% before breaks — the data that shocked the legal world","CHART","World","Line chart","psychology","Danziger et al: Extraneous Factors in Judicial Decisions (pnas.org)",72,72,72,82,72,58,78,80),
mk("HDG27","Herbicide Resistance: Weed Species That Have Evolved to Survive Roundup","Map of confirmed glyphosate-resistant weed species by state — an evolutionary arms race playing out in real time on American farms","MAP","US","State choropleth","agriculture","Heap: International Herbicide-Resistant Weed Database (weedscience.org)",62,52,68,72,68,72,72,80),
mk("HDG28","Drug Price Comparison: What Americans Pay vs What Other Countries Pay for the Same Medication","Side-by-side pricing for the 50 most prescribed drugs — insulin, Humira, Eliquis — US price vs average OECD price","RANK","World","Bar chart","drugs","RAND: International Prescription Drug Price Comparisons (rand.org)",78,85,75,72,78,62,62,82),
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
print(f"Injected {len(new)} new ideas (HDG batch)")
