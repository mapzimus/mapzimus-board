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
mk("HCX01","Child Poverty Is a Policy Choice: Child Poverty Rate by Country","Child poverty rates across OECD countries showing the US as an extreme outlier among wealthy nations","RANK","World","Bar chart","children","OECD: Child Well-Being Data (oecd.org/social/family/child-well-being)",88,78,82,78,85,70,72,88),
mk("HCX02","The Foster Care Map: Children in State Custody Per Capita by State","Foster care population per 1,000 children by state, showing enormous geographic variation","MAP","US","State choropleth","children","AFCARS: Adoption and Foster Care Statistics (acf.hhs.gov/cb/data-research)",85,72,78,72,85,78,68,85),
mk("HCX03","Where Kids Go Hungry: Food Insecurity Rates for Children Under 18 by County","County-level childhood food insecurity rates, with school meal program coverage overlaid","MAP","US","County choropleth","children","Feeding America: Map the Meal Gap (feedingamerica.org/research/map-the-meal-gap)",88,82,78,72,85,82,68,82),
mk("HCX04","The Kindergarten Readiness Gap: School Readiness Scores by ZIP Code","Kindergarten readiness assessment scores by ZIP code, showing how inequality starts before day one of school","MAP","US","County choropleth","children","Annie E. Casey Foundation: KIDS COUNT (datacenter.aecf.org)",82,78,72,78,80,80,72,72),
mk("HCX05","Child Labor in America: It Never Went Away","States that have weakened child labor laws since 2020, and industries employing minors in hazardous work","MAP","US","State choropleth","children","DOL: Child Labor Enforcement Data (dol.gov/agencies/whd/child-labor)",85,72,72,82,85,78,75,72),
mk("HCX06","The Lead Poisoning Map: Children With Elevated Blood Lead Levels by County","Percentage of tested children with elevated blood lead levels by county, concentrated in old housing stock","MAP","US","County choropleth","children","CDC: Childhood Lead Poisoning Prevention (cdc.gov/nceh/lead/data)",88,78,78,72,88,82,68,80),
mk("HCX07","Americas Childcare Affordability Crisis: Daycare Cost as Percent of Median Income","Average annual childcare cost as percentage of median household income by state — exceeds housing in many","MAP","US","State choropleth","children","EPI: Child Care Costs (epi.org/child-care-costs-in-the-united-states)",82,88,78,72,78,78,68,82),
mk("HCX08","Infant Mortality in America: Worse Than Cuba, Bosnia, and Botswana","US infant mortality rate ranked against every country, showing where America falls — below many developing nations","RANK","World","Bar chart","children","World Bank: Mortality Rate Infant (data.worldbank.org)",88,72,82,85,88,68,72,88),
mk("HCX09","The School Counselor Ratio: Students Per Counselor by State","Students per school counselor by state — some exceed 1,000:1 vs. the recommended 250:1","MAP","US","State choropleth","children","ASCA: Student-to-Counselor Ratios (schoolcounselor.org/about/ratios)",78,78,78,78,78,78,68,82),
mk("HCX10","Where Kids Get Expelled From Preschool: Suspension Rates for 3-5 Year Olds","Preschool suspension and expulsion rates by state, disproportionately affecting Black boys","CHART","US","Bar chart","children","Yale: Preschool Expulsion Study (ziglercenter.yale.edu)",85,72,72,85,85,68,78,72),
mk("HCX11","The Playground Desert: Parks and Playgrounds Per Child by City","Public park acreage and playground equipment per child under 12 by metro area","RANK","US","Bar chart","children","Trust for Public Land: ParkScore (tpl.org/parkscore)",72,78,72,72,68,78,72,72),
mk("HCX12","Child Marriage Is Legal in How Many US States: The Loophole Map","States that still allow marriage under 18 with parental consent or judicial approval, and minimum ages","MAP","US","State choropleth","children","Tahirih Justice Center: Child Marriage Laws (tahirih.org/our-work/policy/child-marriage)",85,68,78,85,88,78,72,78),
mk("HCX13","The Summer Slide: How Much Learning Kids Lose Over Summer by Income Level","Academic regression over summer break by household income quintile — inequality widens every June","CHART","US","Bar chart","children","Brookings: Summer Learning Loss (brookings.edu/research/summer-learning-loss)",78,78,75,78,78,68,72,72),
mk("HCX14","Americas Missing Kids: Amber Alert Statistics and Recovery Rates by State","Child abduction cases, Amber Alert activations, and recovery rates by state over time","MAP","US","State choropleth","children","NCMEC: Missing Children Statistics (missingkids.org/footer/media/keyfacts)",85,78,72,72,88,78,65,72),
mk("HCX15","Childhood Vaccination Rates Are Dropping: Exemption Rates by State","Non-medical vaccination exemption rates for kindergartners by state, showing the anti-vax geography","MAP","US","State choropleth","children","CDC: School Vaccination Assessment (cdc.gov/vaccines/imz-managers/coverage/schoolvaxview)",78,75,78,78,80,78,68,85),
mk("HCX16","The Screen Time Generation: Average Daily Screen Hours for Children by Age","Average daily screen time for children aged 0-2, 3-5, 6-12, and 13-17 — all well above guidelines","CHART","US","Bar chart","children","Common Sense Media: Media Use Census (commonsensemedia.org/research)",75,85,78,72,72,68,65,78),
mk("HCX17","Where Teens Work the Most Hours: Adolescent Employment by State","Percentage of 16-17 year olds employed more than 20 hours per week during the school year by state","MAP","US","State choropleth","children","BLS: Employment of Youth (bls.gov/opub/reports/youth-labor)",68,72,75,72,68,78,68,78),
mk("HCX18","The Youth Mental Health Crisis in Charts: Teen Depression and Anxiety 2000-2025","Rates of depression, anxiety, and self-harm among 12-17 year olds over time, stratified by gender","CHART","US","Line chart","children","CDC: Youth Risk Behavior Survey (cdc.gov/yrbs)",88,82,78,72,88,70,68,82),
mk("HCX19","Every Country That Bans Corporal Punishment of Children vs. Those That Dont","Global map of countries that have banned all corporal punishment of children vs. those allowing it","MAP","World","World choropleth","children","Global Initiative to End Corporal Punishment (endcorporalpunishment.org)",78,68,78,75,75,80,68,82),
mk("HCX20","The After-School Gap: Unsupervised Children Between 3pm and 6pm by County","Estimated number of children without after-school supervision, the riskiest hours for youth","MAP","US","County choropleth","children","Afterschool Alliance: America After 3PM (afterschoolalliance.org)",78,78,72,72,75,78,68,68),
mk("HCX21","How Far Kids Walk to School Now vs. 1970: The Death of Walking","Percentage of children who walk or bike to school, 1970 (48%) vs. today (11%), by state","CHART","US","Bar chart","children","SRTS: Safe Routes to School Data (saferoutespartnership.org)",68,78,72,78,65,70,72,72),
mk("HCX22","Juvenile Incarceration Per Capita: Where America Locks Up Its Children","Youth incarceration rate per 100,000 by state — US locks up more kids than almost any other nation","MAP","US","State choropleth","children","OJJDP: Census of Juveniles in Residential Placement (ojjdp.gov/ojstatbb/cjrp)",85,68,78,78,88,78,72,82),
mk("HCX23","The Preemie Map: Premature Birth Rates by State and Race","Premature birth rates by state, showing racial disparities — Black infants born premature at 1.5x the white rate","MAP","US","Bivariate choropleth","children","March of Dimes: Premature Birth Report Card (marchofdimes.org/peristats)",82,72,75,72,82,80,68,82),
mk("HCX24","Child Protective Services Overload: CPS Caseloads Per Worker by State","Average number of cases per child protective services worker by state — many 2-3x the recommended maximum","MAP","US","State choropleth","children","Child Welfare Information Gateway: State CPS Data (childwelfare.gov)",82,72,75,78,82,78,70,72),
mk("HCX25","The Homework Gap: Students Without Home Internet Access by School District","Percentage of K-12 students lacking home broadband access by school district, the digital homework divide","MAP","US","County choropleth","children","NCES: Student Internet Access (nces.ed.gov/pubs2021/2021023.pdf)",78,78,78,72,75,82,68,78),
mk("HCX26","Where Recess Disappeared: States With No Minimum Recess Requirement","States that have no mandated minimum recess time for elementary students, and average recess minutes provided","MAP","US","State choropleth","children","CDC: School Health Policies (cdc.gov/healthyyouth/data/shpps)",72,78,72,78,68,78,68,72),
mk("HCX27","The Child Tax Credit Experiment: Child Poverty Before, During, and After Expansion","Child poverty rate monthly during the 2021 expanded Child Tax Credit vs. before and after expiration","CHART","US","Line chart","children","Census: Supplemental Poverty Measure (census.gov/library/publications/supplemental-poverty-measure)",85,78,82,78,82,70,72,85),
mk("HCX28","Americas Forgotten Students: Chronic Absenteeism by School District","Percentage of students chronically absent (missing 10%+ of school days) by district post-pandemic","MAP","US","County choropleth","children","Attendance Works: Chronic Absence Data (attendanceworks.org)",78,78,75,72,78,80,68,78),
mk("HCX29","Pediatric Care Deserts: Counties With No Pediatrician","Counties with zero practicing pediatricians, overlaid with under-18 population","MAP","US","Bivariate choropleth","children","AAP: Pediatric Workforce Data (aap.org/en/research/pediatric-workforce)",82,75,75,78,82,82,70,72),
mk("HCX30","The Free Lunch Line: Percentage of Students Eligible for Free School Meals by District","School districts by percentage of students qualifying for free or reduced-price lunch — a proxy for child poverty","MAP","US","County choropleth","children","NCES: Free and Reduced Lunch Eligibility (nces.ed.gov/ccd/tables)",78,78,78,68,75,82,62,88),
mk("HCX31","Where Americas Children Are Shot: Firearm Deaths for Ages 1-17 by State","Firearms are now the leading cause of death for American children — mapped by state per capita","MAP","US","State choropleth","children","CDC: WISQARS Fatal Injury Reports (wisqars.cdc.gov)",92,75,80,78,92,78,68,85),
mk("HCX32","The Orphanage to Foster Care Pipeline: Children Aging Out of the System","Youth who age out of foster care at 18 with no family — outcomes for housing, employment, and incarceration","CHART","US","Bar chart","children","Jim Casey Youth Opportunities: Aging Out Data (jimcaseyyouth.org)",88,72,72,78,85,68,72,72),
mk("HCX33","Child Drowning Geography: Where Kids Die in Water by Type","Child drowning deaths by location type — pool, bathtub, open water — mapped by state and age group","MAP","US","State choropleth","children","CDC: WISQARS Drowning Data (wisqars.cdc.gov)",85,78,75,72,82,78,65,82),
mk("HCX34","The Reading Crisis: Fourth Graders Below Basic Reading Level by State","Percentage of 4th graders who cannot read at basic proficiency level, by state — some above 40%","MAP","US","State choropleth","children","NAEP: Nations Report Card (nationsreportcard.gov)",82,78,80,78,82,78,68,88),
mk("HCX35","Americas Youngest Workers: States That Lowered Child Labor Protections Since 2021","States that have rolled back child labor protections in the past 5 years, mapped with specific changes","MAP","US","State choropleth","children","EPI: Child Labor Law Changes (epi.org/child-labor-laws-by-state)",85,72,75,82,85,78,75,78),
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
print(f"Injected {len(new)} new ideas (HCX batch)")
