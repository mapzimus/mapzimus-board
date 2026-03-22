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
mk("HCO01","How Long You Wait for a Trial by State","Average days from arrest to trial disposition by state, showing where speedy trial rights are effectively meaningless","MAP","US","State choropleth","law","DOJ: Bureau of Justice Statistics Case Processing (bjs.gov/index.cfm?ty=tp&tid=23)",82,78,75,72,85,78,70,72),
mk("HCO02","The Exposed Middle: States With No Public Defender System","States that have no statewide public defender office, leaving indigent defense to underfunded county systems","MAP","US","State choropleth","law","Sixth Amendment Center: State Public Defense Reports (sixthamendment.org)",78,72,70,80,82,75,72,68),
mk("HCO03","Exposed: What Judges Get Paid vs. What They Sentence","Comparing judicial salaries to average sentence lengths by state, revealing economic context of punishment","XREF","US","Scatter plot","law","NCSC: Judicial Salary Survey (ncsc.org/__data/assets/pdf_file)",70,65,68,82,75,65,80,65),
mk("HCO04","Cash Register Justice: Court Fees as Municipal Revenue","Cities where court fines and fees make up more than 20% of general fund revenue","RANK","US","Bar chart","law","Governing: Fine Revenue by City (governing.com/finance)",85,80,72,78,82,70,72,70),
mk("HCO05","The Judge Lottery: Sentencing Disparity Within the Same Courthouse","How much your sentence varies depending on which judge you draw, same crime same courthouse","CHART","US","Bar chart","law","USSC: Inter-Judge Disparity Reports (ussc.gov/research)",80,75,78,85,80,68,82,65),
mk("HCO06","Elected vs. Appointed: How Judges Get Their Seats","Map of judicial selection methods — election, appointment, merit selection, partisan vs nonpartisan","MAP","US","State choropleth","law","Brennan Center: Judicial Selection Map (brennancenter.org/judicial-selection-map)",62,58,80,65,60,78,68,82),
mk("HCO07","Your Miranda Rights Are Effectively Optional","Percentage of interrogations where Miranda warnings are waived, by jurisdiction","CHART","US","Bar chart","law","Innocence Project: False Confession Research (innocenceproject.org)",82,75,70,80,85,65,75,60),
mk("HCO08","Jury of Your Peers? Jury Pool Demographics vs. Community Demographics","How representative jury pools actually are of the communities they serve","XREF","US","Bivariate choropleth","law","NCSC: Jury Demographics Studies (ncsc.org/__data/assets)",75,72,68,78,75,80,75,58),
mk("HCO09","Stand Your Ground: Where Self-Defense Is a Blank Check","States with stand your ground vs. duty to retreat, overlaid with justified homicide rates","MAP","US","Bivariate choropleth","law","RAND: Effects of Stand Your Ground Laws (rand.org/research)",80,72,75,75,85,80,72,75),
mk("HCO10","The Plea Bargain Machine: 97% Never See a Jury","Federal criminal cases resolved by plea bargain vs. trial over time, showing the vanishing jury trial","CHART","US","Area chart","law","Pew: Federal Criminal Cases (pewresearch.org)",78,70,80,82,78,68,75,80),
mk("HCO11","Three Strikes Laws: Who They Actually Lock Up","Demographics and offense types of people serving life under three-strikes laws","CHART","US","Bar chart","law","Stanford: Three Strikes Project (law.stanford.edu/three-strikes-project)",85,72,75,78,85,68,72,70),
mk("HCO12","Exposed: States Where You Can Be Jailed for Debt","States that still allow arrest warrants for unpaid civil debt, and how often it happens","MAP","US","State choropleth","law","ACLU: Debtors Prison Reports (aclu.org/issues/smart-justice)",88,82,72,80,85,75,70,68),
mk("HCO13","The Habeas Gap: How Long Death Row Inmates Wait for Federal Review","Average years between conviction and federal habeas corpus resolution by circuit","CHART","US","Bar chart","law","Death Penalty Info Center: Time on Death Row (deathpenaltyinfo.org)",75,60,72,78,82,65,70,72),
mk("HCO14","Exposed: Exposed Ankle Monitoring Costs Pushed to Defendants","Average monthly cost of electronic monitoring paid by defendants, by state","MAP","US","State choropleth","law","Brookings: Pretrial Electronic Monitoring (brookings.edu/research)",80,78,70,82,80,72,75,65),
mk("HCO15","Exposed: The Overcharged: Prosecutor Charge Stacking by District","Average number of charges filed per incident by federal district, showing how prosecutors leverage plea deals","CHART","US","Bar chart","law","TRAC: Federal Prosecutorial Data (trac.syr.edu/tracreports)",72,65,70,80,78,65,78,72),
mk("HCO16","Where Cops Investigate Themselves: Police Misconduct Review Models","Map of internal affairs vs. civilian oversight board jurisdiction by major city","MAP","US","Dot map","law","National Association for Civilian Oversight: Directory (nacole.org)",78,72,68,72,80,75,70,68),
mk("HCO17","The Forensic Junk Science Map: Convictions Based on Debunked Methods","Cases overturned due to bite mark analysis, hair microscopy, arson science, and other discredited forensics","MAP","US","Dot map","law","Innocence Project: Overturned Cases Database (innocenceproject.org/cases)",82,68,72,85,80,70,82,70),
mk("HCO18","Exposed: Where Prosecutors Never Lose: Conviction Rates by District","Federal prosecution conviction rates by district — some above 99.5%","MAP","US","State choropleth","law","TRAC: Federal Conviction Rates (trac.syr.edu/tracreports/crim)",70,62,78,75,72,72,68,80),
mk("HCO19","The Warrant Machine: No-Knock Raids Per Capita by City","Rate of no-knock warrant execution per 100k residents in major metro areas","RANK","US","Bar chart","law","NYT: No-Knock Warrant Database (nytimes.com/2024/no-knock-warrants)",85,75,72,78,88,70,75,60),
mk("HCO20","Exposed: Exposed Qualified Immunity: Cases Thrown Out Because Cops Had No Prior Warning","Section 1983 cases dismissed on qualified immunity grounds by circuit court","CHART","US","Bar chart","law","Reuters: Qualified Immunity Investigation (reuters.com/investigates/special-report/usa-police-immunity)",82,72,70,78,85,65,75,68),
mk("HCO21","The Misdemeanor Trap: How a Minor Charge Ruins Your Life","Cascading consequences of a misdemeanor conviction — job loss, housing denial, license revocation — by state","CHART","US","Bar chart","law","Collateral Consequences Resource Center (ccresourcecenter.org)",85,82,72,75,80,68,72,65),
mk("HCO22","Exposed: The Bail Bond Industry Only Exists in Two Countries","US and Philippines as only nations with commercial bail bond industry, world map","MAP","World","World choropleth","law","Prison Policy Initiative: Bail Industry (prisonpolicy.org/research)",72,68,78,88,70,80,82,75),
mk("HCO23","How Many Laws Did You Accidentally Break Today","Estimated daily federal regulatory violations committed by an average American without knowing","CHART","US","Infographic","law","Heritage Foundation: Overcriminalization (heritage.org/report/overcriminalization)",78,85,68,82,72,72,80,55),
mk("HCO24","The Exposed Exposed Expungement Lottery: Which States Actually Let You Clear Your Record","Expungement eligibility rules and actual completion rates by state","MAP","US","State choropleth","law","Collateral Consequences Resource Center: Expungement (ccresourcecenter.org)",80,78,72,70,75,78,68,70),
mk("HCO25","Where Cameras Watch the Watchers: Body Cam Mandate Map","States and cities requiring police body cameras vs. optional, overlaid with footage release policies","MAP","US","State choropleth","law","Upturn: Police Body Camera Policies (upturn.org/reports/2020/body-cameras)",72,70,75,68,72,78,65,72),
mk("HCO26","Exposed: The Exposed Exposed Statute of Limitations Patchwork: When Crimes Expire","Statute of limitations for sexual assault, fraud, and murder by state — some crimes literally expire","MAP","US","State choropleth","law","RAINN: State Statute of Limitations (rainn.org/state-state-guide)",78,72,75,78,80,78,70,75),
mk("HCO27","Exposed: Who Owns the Crime Lab: Independence of Forensic Labs by State","Whether state crime labs report to police, prosecutors, or independent agencies","MAP","US","State choropleth","law","National Commission on Forensic Science: Lab Independence (justice.gov/ncfs)",70,58,72,80,75,75,78,65),
mk("HCO28","The Exposed Exposed Exposed School-to-Prison Pipeline by District","School suspension and arrest rates vs. later incarceration rates by school district","XREF","US","Scatter plot","law","ACLU: School-to-Prison Pipeline (aclu.org/issues/juvenile-justice)",88,82,72,75,85,70,72,68),
mk("HCO29","Exposed: The Exposed Exposed Private Probation Racket: When Supervision Is a Profit Center","States and counties using private probation companies, overlaid with revocation rates","MAP","US","State choropleth","law","Human Rights Watch: Private Probation (hrw.org/report/2018/02/21/set-up-fail)",82,75,70,80,82,72,75,65),
mk("HCO30","The Right to a Lawyer vs. The Lawyer You Actually Get","Public defender caseloads vs. ABA recommended maximums by state","CHART","US","Bar chart","law","ABA: Public Defender Caseload Standards (americanbar.org/groups/legal_aid)",85,78,78,75,82,68,70,72),
mk("HCO31","Exposed: States Where the Victim Pays: Crime Victim Compensation Denial Rates","Percentage of crime victim compensation claims denied by state, and the reasons why","MAP","US","State choropleth","law","National Association of VOCA: Compensation Data (navoca.org)",80,78,72,78,80,75,72,65),
mk("HCO32","The Exposed Exposed Exposed Legal Desert Map: Counties With No Lawyers","Counties with fewer than 1 attorney per 1,000 residents, mostly rural America","MAP","US","County choropleth","law","ABA: Legal Deserts Report (americanbar.org/groups/legal_aid)",78,72,75,78,75,82,70,72),
mk("HCO33","Exposed: How Asset Forfeiture Built Police Departments","Total value of civil asset forfeiture seizures by state police agencies over 10 years","RANK","US","Bar chart","law","Institute for Justice: Policing for Profit (ij.org/report/policing-for-profit)",85,75,72,82,85,68,78,72),
mk("HCO34","The Exposed Exposed Exposed Exposed Innocence Map: Exonerations Per State Per Capita","Wrongful conviction exonerations per capita by state, colored by leading cause (eyewitness, false confession, forensic)","MAP","US","State choropleth","law","National Registry of Exonerations (law.umich.edu/special/exoneration)",82,70,75,80,82,78,75,78),
mk("HCO35","Exposed: Your Chances of Being Wrongly Convicted by Race","Exoneration rates by race relative to conviction rates, showing who the system fails most","CHART","US","Bar chart","law","National Registry of Exonerations: Race Data (law.umich.edu/special/exoneration)",88,75,78,80,88,68,75,78),
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
print(f"Injected {len(new)} new ideas (HCO batch)")
