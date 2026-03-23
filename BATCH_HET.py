import re, os
DATA = os.path.join(os.path.dirname(__file__), 'data.js')

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=v*3.0+e*2.5+s*2.0+o*1.75+t*1.75+r*2.0+c*1.5
    base=raw/14.5
    fl=0.85 if min(e,r,c,s,t,v,o)<35 else 1.0
    pen=1.0-0.35*(1.0-dr/100.0)
    vs=int(base*fl*pen)
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

IDEAS = [
mk("het01","Eyewitness Misidentification Exonerations","Wrongful convictions overturned due to eyewitness misidentification mapped with lineup reform adoption","MAP","usa","dot-density","Law & Justice","Innocence Project: Eyewitness ID (innocenceproject.org)",72,55,70,74,72,66,68,85),
mk("het02","Prison Gerrymandering Map","State legislative districts where prison populations inflate political representation mapped with affected races","MAP","usa","choropleth","Law & Justice","Prison Policy Initiative (prisonpolicy.org)",58,48,65,78,72,68,74,82),
mk("het03","Legal Aid Funding per Capita","Civil legal aid funding per person in poverty by state showing access to justice gaps","MAP","usa","choropleth","Law & Justice","LSC: Legal Aid Funding (lsc.gov)",62,58,72,70,68,66,62,88),
mk("het04","Police Union Contract Transparency","Police union contract provisions that limit accountability mapped by department and provision type","MAP","usa","dot-density","Law & Justice","Campaign Zero: Police Contracts (joincampaignzero.org)",60,48,65,76,74,64,72,80),
mk("het05","Fines and Fees Revenue Dependence","Cities where fines and fees make up 20%+ of municipal revenue mapped with demographics","MAP","usa","dot-density","Law & Justice","Fines & Fees Justice Center (finesandfeesjusticecenter.org)",65,58,70,76,72,66,70,82),
mk("het06","Prosecutorial Discretion Black Box","Charge reduction and dismissal rates by prosecutor office showing hidden power in the system","CHART","usa","bar-chart","Law & Justice","Measures for Justice (measuresforjustice.org)",58,48,65,76,72,60,72,78),
mk("het07","Immigration Court Video Hearing Outcomes","Asylum case outcomes for in-person vs. video hearings by immigration court","CHART","usa","grouped-bar","Law & Justice","TRAC: Immigration Court (trac.syr.edu)",58,48,68,74,68,58,72,85),
mk("het08","Mandatory Reporter Failure Rate","Percentage of mandated reporters who fail to report suspected child abuse by profession and state","MAP","usa","choropleth","Law & Justice","NCANDS: Child Maltreatment (acf.hhs.gov)",72,55,68,72,76,62,68,78),
mk("het09","Legal Marijuana Expungement Backlog","States with cannabis expungement laws mapped with actual expungement completion rates vs. eligible cases","MAP","usa","choropleth","Law & Justice","ACLU + State Court Data (aclu.org)",58,58,70,72,62,64,68,82),
mk("het10","Grandparent-Headed Households","Grandparents raising grandchildren without parents present by county mapped with reason for arrangement","MAP","usa","choropleth","Demographics","Census ACS: Grandparents (census.gov)",72,62,72,70,65,68,62,90),
mk("het11","Zip Code Life Expectancy Gradient","Life expectancy variation within a single metro area showing 20-year gaps across zip codes","MAP","usa","choropleth","Demographics","IHME: US Health Map (healthdata.org)",72,68,74,74,72,72,60,90),
mk("het12","Biracial and Multiracial Population Surge","Census tracts with fastest growth in multiracial identification over 10 years","MAP","usa","choropleth","Demographics","Census: Race Alone or in Combination (census.gov)",48,58,72,72,42,68,68,92),
mk("het13","Adult Living With Parents Rate","Percentage of adults aged 25-34 living with parents by metro area mapped with housing costs","MAP","usa","bivariate-choropleth","Demographics","Census CPS + ACS (census.gov)",58,78,72,72,55,66,62,92),
mk("het14","Childfree by Choice Geography","Self-reported intentionally childfree adults by state mapped with fertility rate and average age","MAP","usa","choropleth","Demographics","Pew + Census Fertility (pewresearch.org)",52,65,68,72,48,66,70,80),
mk("het15","Seasonal Population Swing Counties","Counties where population doubles or more seasonally from tourism or snowbirds","MAP","usa","choropleth","Demographics","Census: Seasonal Estimates + Tourism Data (census.gov)",48,58,72,74,42,70,70,82),
mk("het16","Indigenous Language Endangerment Map","Native American and indigenous languages by number of remaining speakers mapped with revitalization programs","MAP","usa","dot-density","Demographics","Endangered Languages Project (endangeredlanguages.com)",68,42,68,72,68,72,72,78),
mk("het17","Americans Who Have Never Left Their State","Estimated percentage of residents who have never traveled outside their home state by state","MAP","usa","choropleth","Demographics","Pew + Travel Surveys (pewresearch.org)",45,68,68,78,42,66,74,72),
mk("het18","Mega-Commuter Growth","Workers commuting 90+ minutes each way by metro area mapped with housing cost differential","MAP","usa","choropleth","Demographics","Census ACS: Commuting (census.gov)",58,75,72,70,58,66,62,90),
mk("het19","Regenerative Agriculture Adoption Rate","Farms practicing regenerative agriculture by county mapped with soil carbon measurement improvements","MAP","usa","choropleth","Agriculture & Food Systems","USDA NRCS + Rodale Institute (rodaleinstitute.org)",48,42,68,68,48,68,68,78),
mk("het20","Food Recall Frequency by Company","Major food companies ranked by product recall frequency over 10 years mapped with facility locations","CHART","usa","bar-chart","Agriculture & Food Systems","FDA: Recalls (fda.gov/safety/recalls)",58,68,72,72,62,60,65,90),
mk("het21","Ag-Gag Law Map","States with ag-gag laws criminalizing undercover farm investigations mapped with factory farm density","MAP","usa","bivariate-choropleth","Agriculture & Food Systems","ALDF: Ag-Gag Laws (aldf.org)",62,48,70,76,72,68,72,85),
mk("het22","Farmland Value Bubble","Farmland price per acre by county over 20 years showing speculative bubbles vs. productive value","MAP","usa","choropleth","Agriculture & Food Systems","USDA NASS: Land Values (nass.usda.gov)",55,55,72,70,62,70,62,92),
mk("het23","Irrigation Efficiency Revolution","Water usage per bushel of crop by irrigation method showing efficiency gains mapped by region","MAP","usa","choropleth","Agriculture & Food Systems","USDA ERS: Irrigation (ers.usda.gov)",45,42,72,68,52,68,65,85),
mk("het24","Child Farmworker Injury Map","Farm injuries to workers under 18 by state mapped with child agricultural labor exemption laws","MAP","usa","choropleth","Agriculture & Food Systems","NIOSH: Childhood Agricultural Injuries (cdc.gov/niosh)",75,52,70,72,76,66,68,80),
mk("het25","Slaughterhouse Worker PTSD Rates","Psychological distress rates among slaughterhouse workers by facility type and location","MAP","usa","dot-density","Agriculture & Food Systems","OSHA + Public Health Studies (osha.gov)",68,48,65,74,72,62,72,72),
mk("het26","Lab-Grown Meat Facility Locations","Cultivated meat production facility locations worldwide mapped with regulatory approval status","MAP","world","dot-density","Agriculture & Food Systems","GFI: Cultivated Meat (gfi.org)",42,38,70,76,45,68,76,75),
mk("het27","Superfund Site Adjacent Manufacturing","Active manufacturing facilities operating within 1 mile of EPA Superfund sites mapped with contamination type","MAP","usa","dot-density","Manufacturing & Industry","EPA: Superfund + TRI (epa.gov)",62,52,68,72,72,70,65,88),
mk("het28","Apprenticeship Program Desert","Counties with zero registered apprenticeship programs mapped with manufacturing job openings","MAP","usa","bivariate-choropleth","Manufacturing & Industry","DOL: RAPIDS Apprenticeship (apprenticeship.gov)",55,58,70,70,58,66,65,82),
mk("het29","Single Use Plastic Production Map","Single-use plastic manufacturing facilities by product type mapped with local plastic ban legislation","MAP","usa","dot-density","Manufacturing & Industry","EPA + Break Free From Plastic (breakfreefromplastic.org)",58,55,68,72,65,70,68,80),
mk("het30","American Tool and Die Shop Decline","Tool and die manufacturing shops remaining in the US over 30 years by state","CHART","usa","line","Manufacturing & Industry","NTMA: Industry Survey (ntma.org)",58,52,68,72,62,62,68,82),
mk("het31","Lithium Processing Bottleneck","Global lithium processing capacity by country showing the refining bottleneck separate from mining","MAP","world","choropleth","Manufacturing & Industry","USGS + Benchmark Minerals (usgs.gov)",52,38,70,74,62,70,68,85),
mk("het32","Medical Device Recall Geography","Medical device recalls by manufacturing facility location and device classification severity","MAP","usa","dot-density","Manufacturing & Industry","FDA: MAUDE Database (fda.gov)",60,52,70,72,68,68,65,88),
mk("het33","Warehouse Mega-Complex Impact","Amazon and major warehouse complexes mapped with local traffic increase and wage impact radius","MAP","usa","dot-density","Manufacturing & Industry","MWPVL + Census LODES (mwpvl.com)",58,65,70,72,58,70,65,82),
mk("het34","Nuclear Fuel Supply Chain","Uranium mining, enrichment, and fuel fabrication facility locations worldwide showing dependency chains","MAP","world","flow-map","Manufacturing & Industry","WNA: Nuclear Fuel Cycle (world-nuclear.org)",52,35,68,72,65,72,68,82),
mk("het35","Craft Distillery Boom by County","Craft distillery openings by county over 10 years mapped with agricultural input sourcing radius","MAP","usa","dot-density","Manufacturing & Industry","ADI: Craft Spirits (distilling.com)",42,55,72,68,38,70,68,82),
]

raw = open(DATA, 'r', encoding='utf-8').read()
existing = set(re.findall(r'id:"(het\d+)"', raw))
new_ideas = [i for i in IDEAS if re.search(r'id:"(het\d+)"', i).group(1) not in existing]
print(f"Injecting {len(new_ideas)} new ideas (skipping {len(IDEAS)-len(new_ideas)} dupes)")
if new_ideas:
    tail = ']; // end D'
    assert tail in raw, "Cannot find tail marker"
    raw = raw.replace(tail, ',\n'.join(new_ideas) + ',\n' + tail)
    open(DATA, 'w', encoding='utf-8').write(raw)
    print("Done")
else:
    print("Nothing to inject")
