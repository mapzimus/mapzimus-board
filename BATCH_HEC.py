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
mk("hec01","Autocracy Spread Contagion Map","Countries that shifted toward authoritarianism within 5 years of a neighboring countrys democratic backslide","MAP","world","choropleth","Politics & Governance","V-Dem: Autocratization Waves (v-dem.net)",68,55,70,74,76,72,72,82),
mk("hec02","Protest Movement Success Rates","Outcomes of major protest movements worldwide — regime change, policy reform, repression — over 50 years","CHART","world","bar-chart","Politics & Governance","NAVCO: Nonviolent Campaigns (navcocampaigns.org)",72,60,68,70,65,62,68,80),
mk("hec03","Local Election Turnout vs. Policy Impact","Voter turnout in local elections vs. budget decisions made per capita by municipality","CHART","usa","scatter","Politics & Governance","ICMA: Municipal Election Data (icma.org)",58,68,72,70,55,60,68,78),
mk("hec04","Constitutional Amendment Difficulty","How hard it is to amend the constitution by country ranked with successful amendment frequency","RANK","world","bar-chart","Politics & Governance","Constitute Project (constituteproject.org)",52,50,74,72,58,58,72,85),
mk("hec05","Term Limit Effects on Legislation","Legislative productivity and bill quality metrics before and after term limit implementation by state","CHART","usa","grouped-bar","Politics & Governance","NCSL: Term Limits (ncsl.org/term-limits)",55,55,70,72,60,55,68,80),
mk("hec06","Citizen Assembly Outcomes","Policy proposals from citizens assemblies worldwide mapped with adoption rates and topics","MAP","world","dot-density","Politics & Governance","OECD: Deliberative Democracy (oecd.org)",58,52,68,74,52,64,76,75),
mk("hec07","Free Speech Index vs. Social Media Censorship","National free speech protections mapped against government social media censorship actions","MAP","world","bivariate-choropleth","Politics & Governance","Freedom House: FOTN (freedomhouse.org/report/freedom-net)",65,58,68,72,70,68,66,82),
mk("hec08","Synthetic Opioid Evolution","New synthetic opioid analogs detected per year by DEA with potency relative to morphine","CHART","usa","area-chart","Health & Wellbeing","DEA: Emerging Threat Reports (dea.gov)",72,58,70,78,80,62,72,80),
mk("hec09","Needle Exchange Program Coverage","Syringe service program locations per 100,000 PWID by state mapped with HIV transmission rates","MAP","usa","bivariate-choropleth","Health & Wellbeing","NASEN: SSP Directory (nasen.org)",68,55,70,62,65,66,60,82),
mk("hec10","Alcohol Deaths vs. Drug Deaths","Age-adjusted death rates from alcohol vs. all drugs by county over 20 years","MAP","usa","bivariate-choropleth","Health & Wellbeing","CDC WONDER: Multiple Cause of Death (wonder.cdc.gov)",72,68,74,65,70,68,58,90),
mk("hec11","Psychedelic Research Trial Locations","Active clinical trials for psilocybin, MDMA, and ketamine therapy by research institution","MAP","world","dot-density","Science & Discovery","ClinicalTrials.gov (clinicaltrials.gov)",58,55,70,72,55,66,70,85),
mk("hec12","Tobacco Settlement Spending Betrayal","How states actually spent tobacco settlement money vs. intended anti-smoking programs","CHART","usa","bar-chart","Health & Wellbeing","Campaign for Tobacco-Free Kids (tobaccofreekids.org)",65,68,72,78,72,58,68,88),
mk("hec13","Vaping Illness Cluster Map","EVALI hospitalizations mapped by county with product type and THC contamination data","MAP","usa","dot-density","Health & Wellbeing","CDC: EVALI Data (cdc.gov/tobacco/evali)",70,65,68,62,72,68,58,82),
mk("hec14","Drug Decriminalization Outcomes","Countries and states that decriminalized personal drug use mapped with usage and OD rate changes","MAP","world","choropleth","Health & Wellbeing","Transform: Drug Policy (transformdrugs.org)",62,58,72,74,62,64,70,78),
mk("hec15","Topsoil Loss Economic Cost","Estimated annual economic cost of topsoil erosion per acre by agricultural region","MAP","usa","choropleth","Agriculture & Food","USDA NRCS: Soil Health (nrcs.usda.gov)",62,55,72,70,68,72,64,82),
mk("hec16","Pesticide Drift Complaints","Pesticide drift incident reports mapped against crop type and residential proximity","MAP","usa","dot-density","Agriculture & Food","EPA: Pesticide Incident Data (epa.gov/pesticides)",72,65,68,70,76,70,64,78),
mk("hec17","Vertical Farm Proliferation","Indoor vertical farming operations by metro area with crop type and production volume","MAP","usa","proportional-symbol","Agriculture & Food","AVF: Vertical Farm Census (vertical-farming.net)",48,50,70,74,52,72,72,75),
mk("hec18","Farm Succession Crisis","Average farmer age by county mapped with percentage of farms with no identified successor","MAP","usa","bivariate-choropleth","Agriculture & Food","USDA: Census of Agriculture (nass.usda.gov/AgCensus)",68,62,72,70,68,70,66,88),
mk("hec19","Agricultural Subsidy Distribution","USDA farm subsidies per acre by county mapped against farm size and crop type","MAP","usa","choropleth","Agriculture & Food","EWG: Farm Subsidy Database (farm.ewg.org)",62,65,74,72,68,68,62,90),
mk("hec20","Bee Colony Collapse Recovery","Managed honeybee colony counts by state over 15 years with CCD loss rates","CHART","usa","line-chart","Agriculture & Food","USDA NASS: Honey Report (nass.usda.gov)",65,60,72,65,62,65,60,88),
mk("hec21","Lab-Grown Meat Investment Map","Cultured meat company locations and investment amounts by country","MAP","world","proportional-symbol","Agriculture & Food","GFI: Alternative Protein Data (gfi.org)",50,52,70,78,55,68,76,75),
mk("hec22","Immigration Judge Asylum Grant Rates","Asylum grant rates by individual immigration judge showing massive variation within same court","CHART","usa","bar-chart","Migration & Borders","TRAC: Immigration Judge Data (trac.syr.edu)",72,60,70,78,74,62,68,88),
mk("hec23","Border Wall Construction Progress","Sections of border wall built, planned, and unfunded mapped with terrain and crossing data","MAP","usa","special","Migration & Borders","CBP: Border Wall Status (cbp.gov)",65,62,72,60,70,80,55,82),
mk("hec24","Immigrant Detention Facility Map","ICE detention facilities by capacity and average length of stay with private vs. public operator","MAP","usa","proportional-symbol","Migration & Borders","TRAC: Detention Data (trac.syr.edu)",72,58,70,65,76,70,62,85),
mk("hec25","TPS Holder Geography","Temporary Protected Status holders by nationality and metro area with years in TPS status","MAP","usa","proportional-symbol","Migration & Borders","CMS: TPS Data (cmsny.org)",65,60,68,65,62,66,60,82),
mk("hec26","Migrant Farmworker Routes","Seasonal agricultural worker migration corridors mapped with crop harvest timing","MAP","usa","flow-map","Migration & Borders","DOL: NAWS (dol.gov/agencies/eta/national-agricultural-workers-survey)",68,58,70,68,62,78,66,80),
mk("hec27","Language Access Compliance","Federal agencies compliance with Executive Order 13166 on language access for LEP persons","CHART","usa","bar-chart","Migration & Borders","DOJ: LEP Guidance (lep.gov)",58,60,68,70,62,55,62,80),
mk("hec28","Citizenship Test Pass Rates","Naturalization test pass rates by country of origin and field office","CHART","usa","grouped-bar","Migration & Borders","USCIS: Immigration Statistics (uscis.gov)",55,62,72,68,52,58,60,88),
mk("hec29","Recall Election Frequency","Recall elections filed and completed by state over 20 years with success rates","MAP","usa","choropleth","Politics & Governance","Ballotpedia: Recall Elections (ballotpedia.org/Recall_elections)",55,58,72,68,60,62,65,85),
mk("hec30","Coca-Cola vs. Clean Water Access","Countries where Coca-Cola distribution reaches further than clean drinking water infrastructure","MAP","world","bivariate-choropleth","Health & Wellbeing","WHO/UNICEF: JMP (washdata.org)",68,65,65,82,62,70,78,72),
mk("hec31","Cover Crop Adoption Rates","Percentage of cropland planted with cover crops by county with soil health improvement data","MAP","usa","choropleth","Agriculture & Food","USDA NASS: Cover Crop Data (nass.usda.gov)",52,48,72,65,50,70,62,85),
mk("hec32","Visa Overstay vs. Border Crossing","Percentage of undocumented population from visa overstays vs. unauthorized border crossings by year","CHART","usa","area-chart","Migration & Borders","DHS: Entry/Exit Overstay Report (dhs.gov)",60,58,74,78,62,58,70,82),
mk("hec33","Ballot Initiative Industry","Money spent on ballot initiative campaigns per capita by state with outcome correlation","CHART","usa","scatter","Politics & Governance","Ballotpedia: Initiative Spending (ballotpedia.org)",58,62,70,72,60,58,66,82),
mk("hec34","Antibiotic Use in Livestock","Antibiotic sales for animal use per pound of meat produced by country with resistance trends","CHART","world","bar-chart","Agriculture & Food","WHO: Antimicrobial Resistance (who.int/amr)",65,58,72,74,70,60,70,82),
mk("hec35","Political Asylum Seeker Origin Shifts","Top 10 countries of origin for US asylum seekers by decade showing dramatic composition changes","CHART","world","area-chart","Migration & Borders","UNHCR + USCIS (unhcr.org)",65,58,72,70,62,64,62,88),
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
print(f"Injected {len(new)} new ideas (HEC batch)")
