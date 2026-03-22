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
mk("HCW01","The Supreme Court Power Map: Which Justices Agree Most Often","Agreement matrix heatmap of current Supreme Court justices showing ideological clustering","CHART","US","Heatmap calendar","law","SCOTUSblog: Stat Pack (scotusblog.com/statistics-stat-pack)",68,62,78,72,72,75,72,82),
mk("HCW02","How Many People Are on Probation in Your State: The Shadow System","State-level probation populations per capita — more Americans are on probation than in prison","MAP","US","State choropleth","law","BJS: Probation and Parole in the United States (bjs.gov/index.cfm?ty=tp&tid=15)",78,72,75,80,78,78,72,82),
mk("HCW03","The Execution Map: Every Execution in America Since 1976","Map of every execution since Gregg v. Georgia, colored by method — lethal injection, electric chair, gas, hanging, firing squad","MAP","US","Dot map","law","Death Penalty Info Center: Execution Database (deathpenaltyinfo.org/executions)",82,65,78,72,85,80,68,85),
mk("HCW04","Exposed: Patent Troll Alley: Why So Many Lawsuits Are Filed in East Texas","Patent infringement cases filed by district, showing the Eastern District of Texas anomaly","MAP","US","State choropleth","law","Lex Machina: Patent Litigation Data (lexmachina.com)",62,55,72,85,62,72,82,72),
mk("HCW05","The Lawsuit Gap: Per Capita Civil Filings by State","Civil lawsuit filing rates per capita by state, showing massive variation in litigiousness","MAP","US","State choropleth","law","NCSC: Court Statistics Project (courtstatistics.org)",65,62,78,75,62,78,70,78),
mk("HCW06","Exposed: Mandatory Minimum Sentences: The Map of Inflexible Justice","States with mandatory minimum sentencing laws by crime type and their average sentence lengths","MAP","US","State choropleth","law","FAMM: State Mandatory Minimum Laws (famm.org/our-work/state-reforms)",80,68,75,72,82,78,68,78),
mk("HCW07","Immigration Court Backlog: Average Wait Time by Court Location","Immigration case backlog and average processing time by court, some over 4 years","MAP","US","Dot map","law","TRAC: Immigration Court Backlog (trac.syr.edu/phptools/immigration/court_backlog)",78,72,75,78,80,78,68,82),
mk("HCW08","The Consent Age Patchwork: Age of Consent Laws Across the US","Age of consent by state including exceptions like Romeo and Juliet laws and close-in-age exemptions","MAP","US","State choropleth","law","Cornell Law: Age of Consent by State (law.cornell.edu/wex/table_age_of_consent)",68,65,78,72,68,78,65,82),
mk("HCW09","Exposed: Exposed: The Debtors Prison Comeback: Jailed for Fines You Cant Pay","Rate of incarceration for unpaid fines and fees by state — a modern debtors prison system","MAP","US","State choropleth","law","ACLU: In for a Penny (aclu.org/report/in-for-penny)",85,78,72,78,85,78,72,72),
mk("HCW10","The Lawyer Surplus and the Justice Gap: Attorneys Per Capita vs. Unmet Legal Need","States with the most lawyers per capita plotted against rates of unmet civil legal need","XREF","US","Scatter plot","law","ABA: Legal Profession Statistics (americanbar.org/about_the_aba/profession_statistics)",72,68,72,80,70,68,78,72),
mk("HCW11","Exposed: States That Execute the Intellectually Disabled: The Atkins Loophole","States where IQ thresholds and definitions create loopholes allowing execution of people with intellectual disabilities","MAP","US","State choropleth","law","Death Penalty Info Center: Intellectual Disability (deathpenaltyinfo.org/policy-issues/intellectual-disability)",82,60,70,80,85,75,72,70),
mk("HCW12","The Tort Reform Map: States That Capped Lawsuit Damages","States with caps on medical malpractice, punitive damages, and personal injury awards, and the amounts","MAP","US","State choropleth","law","ATRA: Tort Reform Record (atra.org/resources/tort-reform-record)",65,62,78,72,68,78,68,80),
mk("HCW13","Exposed: The Cash Bail Abolition Experiment: Which Cities Ended Money Bail","Cities and states that have reformed or eliminated cash bail, with recidivism and appearance rate data","MAP","US","Dot map","law","Pretrial Justice Institute: Bail Reform Map (pretrial.org)",75,68,72,72,72,78,70,72),
mk("HCW14","Class Action Payouts vs. Lawyer Fees: Who Really Wins","Breakdown of class action settlement distributions — what goes to plaintiffs vs. attorney fees vs. administration","CHART","US","Bar chart","law","Consumer Financial Protection Bureau: Class Action Data (consumerfinance.gov)",72,75,72,80,72,68,72,68),
mk("HCW15","Exposed: Solitary Confinement Nation: Prisoners in Isolation by State","Number of prisoners in solitary confinement or restrictive housing per capita by state","MAP","US","State choropleth","law","Solitary Watch: State Data (solitarywatch.org/resources)",82,65,72,78,85,75,72,68),
mk("HCW16","The Regulatory State: Federal Regulations by Industry Sector","Total number of federal regulations by industry — banking, energy, healthcare, transportation — and growth over time","CHART","US","Treemap","law","RegInfo.gov: Unified Agenda of Regulatory Actions (reginfo.gov)",62,58,75,72,60,72,68,78),
mk("HCW17","Exposed: Your Employer Can Fire You for This: At-Will Employment Exceptions by State","Which states have added wrongful termination protections beyond basic at-will employment","MAP","US","State choropleth","law","NCSL: At-Will Employment Overview (ncsl.org/labor-and-employment/at-will-employment-overview)",72,78,75,72,72,78,68,78),
mk("HCW18","The Arbitration Trap: How Many Consumer Contracts Force Private Justice","Percentage of consumer financial contracts with mandatory arbitration clauses, by product type","CHART","US","Bar chart","law","CFPB: Arbitration Study (consumerfinance.gov/data-research)",72,75,72,78,72,68,72,72),
mk("HCW19","Exposed: Juvenile Life Without Parole: States That Still Lock Up Children Forever","States that still allow life without parole for offenders under 18, and current population serving JLWOP","MAP","US","State choropleth","law","Campaign for Fair Sentencing of Youth: State Laws (fairsentencingofyouth.org)",88,68,75,78,88,78,72,78),
mk("HCW20","The DNA Exoneration Timeline: Wrongful Convictions Overturned by Year","DNA exonerations by year, showing acceleration with technology and the Innocence Projects work","CHART","US","Line chart","law","Innocence Project: DNA Exonerations (innocenceproject.org/dna-exonerations-in-the-united-states)",82,68,78,72,82,70,70,82),
mk("HCW21","Exposed: The Prison Gerrymandering Problem: Counting Inmates Where They Are Locked Up","How prison populations inflate the political representation of rural prison-hosting districts","MAP","US","County choropleth","law","Prison Policy Initiative: Prison Gerrymandering (prisonersofthecensus.org)",72,62,70,82,72,78,78,72),
mk("HCW22","Eminent Domain Abuse Map: Private Property Seized for Private Development","Cases of eminent domain used to transfer property from one private owner to another since Kelo v. City of New London","MAP","US","Dot map","law","Institute for Justice: Eminent Domain Abuse (ij.org/issues/private-property/eminent-domain)",78,72,72,78,78,78,72,68),
mk("HCW23","Exposed: The Federal Sentencing Disparity: Same Crime Different Sentence by District","Average sentence length for the same federal offense varies by up to 3x across judicial districts","MAP","US","State choropleth","law","USSC: Sourcebook of Federal Sentencing Statistics (ussc.gov/research/sourcebook)",78,68,78,82,78,78,75,80),
mk("HCW24","Law Enforcement Officers Per Capita: The Blue Map","Sworn police officers per 1,000 residents by city, showing massive variation in policing density","MAP","US","Dot map","law","FBI: UCR Law Enforcement Officers Killed and Assaulted (ucr.fbi.gov/leoka)",65,65,78,72,65,80,65,82),
mk("HCW25","Exposed: Non-Compete Agreements: States Where Your Last Job Controls Your Next One","Non-compete agreement enforceability by state and percentage of workers bound by them","MAP","US","State choropleth","law","EPI: Non-Compete Agreements (epi.org/publication/noncompete-agreements)",72,78,75,75,72,78,68,78),
mk("HCW26","The Backlog Mountain: Untested Rape Kits by State","Estimated number of untested sexual assault evidence kits sitting in police storage by state","MAP","US","State choropleth","law","End the Backlog: Testing Progress (endthebacklog.org)",88,72,72,78,88,78,72,65),
mk("HCW27","Exposed: How Long It Takes to Get a Gun vs. an Abortion vs. a Drivers License by State","Comparative wait times for regulated activities by state, revealing priorities in regulatory burden","CHART","US","Bar chart","law","Guttmacher: State Abortion Policy (guttmacher.org/state-policy)",78,78,72,85,80,68,82,72),
mk("HCW28","The Wrongful Conviction Cost: Total Compensation Paid to Exonerees by State","Total dollars paid to wrongfully convicted people by state, and the per-year-of-wrongful-imprisonment rate","RANK","US","Bar chart","law","Innocence Project: Compensation Laws (innocenceproject.org/compensating-wrongly-convicted)",80,68,72,78,78,68,72,72),
mk("HCW29","Exposed: The Disenfranchisement Map: Felony Voting Restrictions by State","States that permanently strip voting rights from felons vs. those that restore them after sentence","MAP","US","State choropleth","law","Sentencing Project: State Felon Voting Laws (sentencingproject.org/publications/felony-disenfranchisement-laws-in-the-us)",80,72,78,72,80,78,68,82),
mk("HCW30","Supreme Court Overturning Itself: Every Time SCOTUS Reversed Its Own Precedent","Timeline of every time the Supreme Court explicitly overruled a previous decision, by topic area","CHART","US","Line chart","law","Congressional Research Service: Supreme Court Overruled Decisions (crsreports.congress.gov)",68,62,78,78,72,68,75,82),
mk("HCW31","Exposed: The SLAPP Map: States That Protect Against Strategic Lawsuits","States with anti-SLAPP statutes protecting free speech from intimidation lawsuits, strength compared","MAP","US","State choropleth","law","Reporters Committee: Anti-SLAPP Guide (rcfp.org/anti-slapp-guide)",68,58,72,78,68,78,72,78),
mk("HCW32","Sovereign Immunity: When You Cant Sue the Government Even When Its Wrong","Types of government actions shielded by sovereign immunity by state, and the exceptions","MAP","US","State choropleth","law","Cornell Law: Sovereign Immunity (law.cornell.edu/wex/sovereign_immunity)",68,58,68,78,72,75,72,72),
mk("HCW33","Exposed: The Private Prison Map: For-Profit Incarceration by State","Percentage of state prisoners held in private facilities, mapped against lobbying spending by prison companies","MAP","US","State choropleth","law","Sentencing Project: Private Prisons (sentencingproject.org/publications/private-prisons-united-states)",80,68,72,78,82,78,72,78),
mk("HCW34","Environmental Law Enforcement: EPA Inspections and Penalties by State","EPA enforcement actions per industrial facility by state — some states get 10x more scrutiny than others","MAP","US","State choropleth","law","EPA: ECHO Enforcement Data (echo.epa.gov)",68,58,72,78,72,78,72,78),
mk("HCW35","Exposed: The Legal Aid Funding Crisis: Federal Legal Aid Dollars Per Low-Income Person","LSC funding per eligible person by state, showing how little the system spends on civil legal help for the poor","MAP","US","State choropleth","law","Legal Services Corporation: Budget Data (lsc.gov/about-lsc/budget-appropriations)",78,72,75,78,78,78,70,78),
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
print(f"Injected {len(new)} new ideas (HCW batch)")
