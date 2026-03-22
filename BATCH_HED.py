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
mk("hed01","Ammunition Factory Locations","Active ammunition manufacturing plants in the US by caliber specialization and production volume","MAP","usa","dot-density","Economy & Trade","ATF: Licensed Manufacturers (atf.gov)",50,48,70,68,58,72,60,82),
mk("hed02","Furniture Manufacturing Migration","Shift of US furniture production from North Carolina to Asia and back via reshoring over 40 years","CHART","usa","area-chart","Economy & Trade","BLS QCEW: NAICS 337 (bls.gov/cew)",55,58,70,68,55,62,62,82),
mk("hed03","Craft Distillery Explosion","Craft distilleries opened per year by state mapped with spirits production volume","MAP","usa","dot-density","Economy & Trade","ACSA: Craft Spirits Data (americancraftspirits.org)",50,65,68,62,48,72,58,82),
mk("hed04","Concrete Plant Proximity to Schools","Concrete batch plants within 1 mile of schools mapped with air quality violations","MAP","usa","dot-density","Health & Wellbeing","EPA: TRI + NCES (epa.gov/tri)",72,68,68,72,76,72,66,78),
mk("hed05","Sawmill County Employment","Counties where sawmill and wood product jobs represent 5%+ of total employment with automation trend","MAP","usa","choropleth","Economy & Trade","BLS QCEW: NAICS 3211 (bls.gov/cew)",58,55,70,65,60,68,58,85),
mk("hed06","Solar Panel Manufacturing Independence","Percentage of solar panel supply chain manufactured domestically by country vs. Chinese dominance","CHART","world","bar-chart","Economy & Trade","IEA: Solar PV Supply Chain (iea.org)",60,52,74,72,68,62,68,82),
mk("hed07","Food Processing Plant Consolidation","Number of unique food processing companies vs. total plants over 30 years showing consolidation","CHART","usa","dual-axis","Agriculture & Food","USDA ERS: Food Industry Structure (ers.usda.gov)",62,60,72,70,68,58,64,85),
mk("hed08","Televangelism Revenue Map","Top televangelist ministries by annual revenue mapped with broadcast reach and donor geography","MAP","usa","proportional-symbol","Culture & Religion","MinistryWatch: Donor Alerts (ministrywatch.com)",60,58,65,74,62,68,70,72),
mk("hed09","Church Closure Wave","Houses of worship permanently closed per year by denomination and region","MAP","usa","dot-density","Culture & Religion","ARDA: National Congregations Study (thearda.com)",65,62,70,68,65,68,58,80),
mk("hed10","Sharia Law Misconceptions","What Americans think Sharia law means vs. actual legal applications by Muslim-majority country","CHART","world","grouped-bar","Culture & Religion","Pew: Global Attitudes Survey (pewresearch.org/global)",58,55,65,78,62,58,74,78),
mk("hed11","Religious Conversion Flows Globally","Net conversion flows between major religions by region as a Sankey diagram","CHART","world","flow-map","Culture & Religion","Pew: Religious Switching (pewresearch.org/religion)",55,52,68,75,55,70,72,80),
mk("hed12","Witchcraft Accusation Hotspots","Countries where witchcraft accusations still lead to violence mapped with incident count","MAP","world","dot-density","Culture & Religion","WHRIN: Witchcraft and Human Rights (whrin.org)",72,48,60,82,78,68,80,68),
mk("hed13","Religious School Voucher Growth","Students using public vouchers for religious schools by state over 10 years","CHART","usa","area-chart","Education","EdChoice: School Choice Data (edchoice.org)",62,65,72,68,68,60,62,85),
mk("hed14","Faith-Based Hospital Merger Restrictions","Hospitals acquired by faith-based systems that now restrict reproductive services mapped","MAP","usa","dot-density","Health & Wellbeing","Community Catalyst: Hospital Mergers (communitycatalyst.org)",72,68,65,74,76,66,68,78),
mk("hed15","Abandoned Theme Park Atlas","Defunct amusement parks worldwide mapped with peak attendance and closure reason","MAP","world","dot-density","Culture & Religion","Defunct Parks (defunctparks.com)",52,62,60,72,48,78,72,72),
mk("hed16","Reality TV Contestant Outcomes","Career and mental health outcomes for reality TV show contestants 5 years after appearance","CHART","usa","bar-chart","Media & Information","Academic Studies + Press Reports (journals.sagepub.com)",62,72,58,74,60,55,72,65),
mk("hed17","Vinyl Record Sales Geography","Vinyl record sales per capita by metro area mapped with independent record store density","MAP","usa","bivariate-choropleth","Economy & Trade","RIAA: Sales Data (riaa.com)",48,65,68,65,42,70,60,82),
mk("hed18","Film Tax Credit Brain Drain","States that eliminated film tax credits mapped with production job losses and migration to Georgia","MAP","usa","choropleth","Economy & Trade","MPAA: Film Production Data (motionpictures.org)",55,58,72,68,60,64,62,80),
mk("hed19","Podcast Advertising Revenue Concentration","Share of podcast ad revenue captured by top 1% of shows vs. remaining 99%","CHART","usa","bar-chart","Media & Information","IAB: Podcast Revenue Study (iab.com)",55,65,72,74,58,55,65,82),
mk("hed20","Live Music Venue Extinction","Independent live music venues that closed permanently since 2020 by city","MAP","usa","dot-density","Culture & Religion","NIVA: Save Our Stages (nivassoc.org)",68,72,65,62,65,70,58,78),
mk("hed21","AI Art Competition Controversy","Art competitions where AI-generated entries won or placed mapped with rule change timeline","MAP","world","dot-density","Technology & Data","AI Art News Archive (artnews.com)",52,58,62,78,60,60,78,68),
mk("hed22","Terrible Yelp Reviews by Business Type","Average 1-star review frequency by business category with most common complaint themes","CHART","usa","bar-chart","Economy & Trade","Yelp: Academic Dataset (yelp.com/dataset)",42,78,65,72,40,55,68,80),
mk("hed23","State Slogans Nobody Remembers","Official state tourism slogans mapped with tourism revenue — do catchy slogans actually correlate","MAP","usa","choropleth","Economy & Trade","State Tourism Offices + BEA (bea.gov)",40,72,62,78,38,68,76,78),
mk("hed24","Absurd Government Spending Items","Most ridiculed line items in federal and state budgets mapped by congressional district","MAP","usa","dot-density","Politics & Governance","Citizens Against Government Waste (cagw.org)",50,72,58,80,52,58,74,75),
mk("hed25","Worlds Most Overengineered Roundabouts","Extraordinarily complex traffic roundabouts mapped with satellite imagery and accident rates","MAP","world","dot-density","Transportation &tic","Google Maps + Traffic Safety Data (maps.google.com)",42,68,58,82,42,80,82,72),
mk("hed26","Daylight Saving Time Confusion Costs","Economic cost of DST transitions — car accidents, productivity loss, medical errors — by state","CHART","usa","bar-chart","Health & Wellbeing","Journal of Clinical Sleep Medicine (jcsm.aasm.org)",55,80,68,72,55,58,68,78),
mk("hed27","Town Names That Sound Made Up","Actual US towns with the most absurd names mapped with founding stories","MAP","usa","dot-density","Culture & Religion","USGS: GNIS Database (geonames.usgs.gov)",38,72,58,82,35,72,82,90),
mk("hed28","Pet Owners Who Spend More on Pets Than Themselves","Average annual spending on pet healthcare vs. own healthcare by income bracket and state","CHART","usa","grouped-bar","Health & Wellbeing","APPA: Pet Industry Data (americanpetproducts.org)",45,78,68,78,42,55,72,78),
mk("hed29","Microchip Fab Water Consumption","Water usage per semiconductor fab compared to local agricultural water usage in the same county","CHART","usa","bar-chart","Technology & Data","USGS: Water Use + SIA (usgs.gov)",58,52,72,78,65,60,74,78),
mk("hed30","Wedding Dress Price Geography","Average wedding dress cost by metro area mapped against local median household income","MAP","usa","choropleth","Economy & Trade","The Knot: Real Weddings Study (theknot.com)",45,72,68,65,42,64,58,82),
mk("hed31","Cement Plant Carbon Emissions","CO2 emissions from US cement plants mapped against green cement technology adoption","MAP","usa","dot-density","Environment & Climate","EPA: GHG Reporting Program (ghgdata.epa.gov)",62,48,72,68,65,68,66,85),
mk("hed32","Ugly Christmas Sweater Economic Index","Ugly Christmas sweater sales volume by state as a cultural participation metric","MAP","usa","choropleth","Economy & Trade","NRF: Holiday Spending Survey (nrf.com)",38,75,60,72,35,62,74,72),
mk("hed33","Tire Manufacturing Shift","US tire manufacturing plant locations and employment vs. imports by country of origin over 30 years","MAP","usa","dot-density","Economy & Trade","ITC: Tire Import Data (usitc.gov)",52,50,72,65,58,68,58,85),
mk("hed34","Religious Holiday Retail Spending","Consumer spending by religious holiday — Christmas, Hanukkah, Diwali, Eid — as share of annual retail","CHART","usa","bar-chart","Economy & Trade","NRF: Holiday Spending (nrf.com)",48,68,70,65,42,55,58,82),
mk("hed35","Americas Most Complained About Neighbors","Top neighbor complaints filed with municipalities by type — noise, parking, fences, trees — by region","MAP","usa","choropleth","Culture & Religion","311 Data: Complaint Categories (data.cityofnewyork.us)",42,82,62,68,42,62,68,78),
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
print(f"Injected {len(new)} new ideas (HED batch)")
