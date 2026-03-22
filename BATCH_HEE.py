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
mk("hee01","Rural Maternity Ward Closures","Obstetric units closed in rural hospitals mapped with driving time to nearest delivery facility","MAP","usa","dot-density","Health & Wellbeing","March of Dimes: Maternity Care Desert (marchofdimes.org)",80,72,72,68,80,72,62,82),
mk("hee02","One-Room Schoolhouses Still Operating","Remaining one-room schoolhouses in the US mapped with student count and location isolation","MAP","usa","dot-density","Education","NCES: Small Schools Data (nces.ed.gov)",52,62,65,78,45,76,75,72),
mk("hee03","Rural Suicide Rate Crisis","Suicide rates in rural vs. urban counties mapped with mental health provider access","MAP","usa","bivariate-choropleth","Health & Wellbeing","CDC WONDER + HRSA (wonder.cdc.gov)",80,68,72,62,82,68,58,88),
mk("hee04","Town Without a Doctor","Rural communities where the nearest physician is 30+ miles away mapped with health outcomes","MAP","usa","dot-density","Health & Wellbeing","HRSA: HPSA Data (data.hrsa.gov)",75,70,70,68,76,72,60,85),
mk("hee05","Rural Water System Violations","Small rural water systems with Safe Drinking Water Act violations per capita by county","MAP","usa","choropleth","Health & Wellbeing","EPA: SDWIS (epa.gov/sdwis)",72,68,72,68,76,70,58,88),
mk("hee06","Forest Service Road Maintenance Backlog","National Forest road miles open vs. maintainable vs. closed due to budget mapped by forest","MAP","usa","choropleth","Environment & Climate","USFS: Infrastructure Data (fs.usda.gov)",55,52,70,68,58,74,62,82),
mk("hee07","Rural Electric Co-op Territory Map","Electric cooperative service territories mapped with broadband deployment and energy rates","MAP","usa","choropleth","Infrastructure & Systems","NRECA: Co-op Data (electric.coop)",50,58,72,62,48,74,58,85),
mk("hee08","Anchoring Bias in Real Estate","How listing price anchors affect final sale price by market temperature — hot vs. cold markets","CHART","usa","scatter","Economy & Trade","Zillow: Transaction Data (zillow.com/research)",52,68,70,74,48,58,72,78),
mk("hee09","Sunk Cost Fallacy in Infrastructure","Mega-projects that continued despite cost overruns exceeding original estimates by 200%+","CHART","world","bar-chart","Infrastructure & Systems","Oxford: Megaproject Database (eureka.sbs.ox.ac.uk)",60,62,70,78,65,60,76,78),
mk("hee10","Availability Heuristic and Risk Perception","What Americans fear most vs. actual probability of death from those causes","CHART","usa","bar-chart","Health & Wellbeing","Chapman: Fear Survey + CDC Mortality (chapman.edu)",58,78,72,82,55,60,72,82),
mk("hee11","Choice Overload in Healthcare Plans","Number of health insurance plan options by state exchange vs. enrollment decision time and satisfaction","CHART","usa","scatter","Health & Wellbeing","KFF: Marketplace Data (kff.org)",55,72,68,72,52,55,70,80),
mk("hee12","Groupthink Disasters Timeline","Major policy and corporate failures attributed to groupthink mapped on a timeline with cost","CHART","world","timeline","Politics & Governance","Case Study Analysis + NTSB (ntsb.gov)",62,60,65,78,60,62,80,72),
mk("hee13","Mere Exposure Effect in Politics","Candidate name recognition vs. policy agreement — how familiarity drives preference in primaries","CHART","usa","scatter","Politics & Governance","ANES: Feeling Thermometer (electionstudies.org)",52,62,65,74,55,55,72,75),
mk("hee14","Cognitive Load and Financial Decisions","Payday loan usage rates mapped against job types requiring high cognitive load at work","MAP","usa","bivariate-choropleth","Economy & Trade","CFPB: Payday Lending Data (consumerfinance.gov)",65,68,65,74,60,62,72,78),
mk("hee15","Childhood Obesity and Park Access","Childhood obesity rates by county mapped against public park acreage per child","MAP","usa","bivariate-choropleth","Health & Wellbeing","CDC: Youth Risk Behavior + TPL (cdc.gov/yrbs)",72,72,70,62,68,70,58,85),
mk("hee16","Children in Immigrant Detention","Children held in immigration detention facilities by location with average length of stay","MAP","usa","proportional-symbol","Migration & Borders","ORR: Unaccompanied Children (acf.hhs.gov)",82,60,65,68,85,66,65,78),
mk("hee17","Pre-K Access Inequality","States with universal pre-K vs. states with zero public pre-K mapped with 3rd grade reading scores","MAP","usa","bivariate-choropleth","Education","NIEER: State of Preschool (nieer.org)",72,72,74,62,68,66,58,88),
mk("hee18","Kids and Guns in the Home","Estimated children living in homes with unsecured firearms by state mapped with accidental shooting rates","MAP","usa","bivariate-choropleth","Public Safety","RAND + Everytown: Child Access (rand.org/gun-policy)",82,72,68,68,84,64,58,80),
mk("hee19","School Bus Route Extremes","Longest school bus routes in America by distance and ride time mapped with district size","MAP","usa","dot-density","Education","School Bus Fleet: Route Data (schoolbusfleet.com)",58,72,65,72,52,74,66,72),
mk("hee20","Child Labor Law Rollbacks","States that weakened child labor protections since 2020 mapped with violation data","MAP","usa","choropleth","Law & Justice","EPI: Child Labor Report (epi.org)",78,68,70,74,80,64,68,82),
mk("hee21","Abandoned Children in ER Waiting Rooms","Emergency departments reporting children left by overwhelmed parents by metro with wait times","MAP","usa","dot-density","Health & Wellbeing","ACEP: ER Boarding Data (acep.org)",80,65,62,75,78,62,72,65),
mk("hee22","Lunar South Pole Landing Race","Planned lunar south pole missions by space agency and company mapped with landing site targets","MAP","world","special","Science & Discovery","NASA: Artemis + ESA + ISRO (nasa.gov)",55,48,72,74,62,80,70,80),
mk("hee23","Space Station Population Over Time","Number of humans in orbit at any given moment over 25 years with station identification","CHART","world","area-chart","Science & Discovery","NASA: ISS Crew Archives (nasa.gov/iss)",50,50,72,68,45,68,62,90),
mk("hee24","Asteroid Mining Feasibility","Near-Earth asteroids ranked by estimated mineral value and mission difficulty","CHART","world","scatter","Science & Discovery","NASA: CNEOS Asteroid Database (cneos.jpl.nasa.gov)",48,42,68,78,52,65,80,78),
mk("hee25","Voyager Distance Visualization","Current distance of Voyager 1 and 2 from Earth compared to familiar distance benchmarks","CHART","world","bar-chart","Science & Discovery","NASA: Voyager Mission Status (voyager.jpl.nasa.gov)",52,55,74,72,48,72,65,92),
mk("hee26","Space Junk Ownership","Countries responsible for tracked orbital debris objects by launch decade","CHART","world","area-chart","Science & Discovery","ESA: Space Debris Statistics (esa.int/debris)",55,48,72,74,62,68,70,85),
mk("hee27","Telescope Light Gathering Power Timeline","Light collecting area of worlds largest telescopes over 400 years with discoveries enabled","CHART","world","line-chart","Science & Discovery","IAU: Telescope Registry (iau.org)",48,45,72,70,48,65,65,88),
mk("hee28","Planetary Protection Contamination Risk","Missions to potentially habitable worlds ranked by contamination risk with sterilization protocols","CHART","world","bar-chart","Science & Discovery","NASA: Planetary Protection (planetaryprotection.nasa.gov)",48,42,68,78,55,60,80,78),
mk("hee29","Rural Library as Last Public Space","Rural counties where the public library is the only free public gathering space mapped","MAP","usa","dot-density","Education","IMLS: Library Data (imls.gov)",65,72,65,70,58,68,68,80),
mk("hee30","Loss Aversion in Policy","Policies that failed because framing emphasized losses rather than equivalent gains — case studies","CHART","world","bar-chart","Politics & Governance","Kahneman: Prospect Theory Applications (nobelprize.org)",55,58,62,78,52,55,78,70),
mk("hee31","Infant Mortality by ZIP Code","Infant mortality rates by ZIP code within the same metro area showing extreme neighborhood disparities","MAP","usa","choropleth","Health & Wellbeing","CDC: Linked Birth/Infant Death (cdc.gov/nchs)",82,72,74,70,78,70,62,88),
mk("hee32","Space Tourism Price Trajectory","Cost per seat to space by provider over time with projected future pricing","CHART","world","line-chart","Economy & Trade","Space Foundation: Space Report (spacefoundation.org)",48,52,72,70,48,62,62,80),
mk("hee33","Rural Dentist Shortage","Counties with zero dentists per 10,000 residents mapped with childhood dental emergency rates","MAP","usa","bivariate-choropleth","Health & Wellbeing","HRSA: Dental HPSA (data.hrsa.gov)",70,68,70,65,68,68,58,85),
mk("hee34","Helicopter Parenting Index","Free-range play laws vs. supervision expectations by state mapped with child independence metrics","MAP","usa","choropleth","Culture & Religion","Let Grow: Policy Map (letgrow.org)",55,75,62,72,50,62,72,72),
mk("hee35","Radio Telescope Dead Zones","National Radio Quiet Zones and proposed radio-free areas for astronomy mapped with population","MAP","usa","special","Science & Discovery","NRAO: Radio Quiet Zone (nrao.edu)",48,42,70,74,50,78,72,82),
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
print(f"Injected {len(new)} new ideas (HEE batch)")
