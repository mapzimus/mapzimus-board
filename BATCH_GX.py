"""BATCH_GX: Hyper-specific ideas mined from actual CSV column headers.
Each idea ties to specific fields in the datasets.
"""
import re, sys
DATA_JS = r"D:\projects\mapzimus-board\data.js"

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*1.25+s*1.5+t*1.5+v*2.0+o*1.5
    vs=int((raw/11.75)*(1-0.5*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

ideas = []

# === FBI CRIME: SPECIFIC CRIME TYPE MAPS ===
ideas.append(mk("gx001","Americas Car Theft Hotspots: Motor Vehicle Theft by State","Motor vehicle theft rates per 100k mapped by state, 2024","MAP","US-State","State choropleth","Crime and Law Enforcement","D:/raw_data/fbi/estimated_crimes col:motor_vehicle_theft",78,82,75,68,72,78,58,95))
ideas.append(mk("gx002","The Robbery Map: Armed Robbery Rates by State","Robbery rates per 100k population across all 50 states","MAP","US-State","State choropleth","Crime and Law Enforcement","D:/raw_data/fbi/estimated_crimes col:robbery",78,78,72,65,78,78,55,95))
ideas.append(mk("gx003","Burglary Is Dying: 45 Years of Declining Break-Ins","National burglary rate from 1979 to 2024 showing dramatic decline","CHART","US","Line chart","Crime and Law Enforcement","D:/raw_data/fbi/estimated_crimes col:burglary",68,82,78,72,62,72,62,95))
ideas.append(mk("gx004","Aggravated Assault: Americas Most Common Violent Crime","State-by-state map of aggravated assault, the #1 violent offense","MAP","US-State","State choropleth","Crime and Law Enforcement","D:/raw_data/fbi/estimated_crimes col:aggravated_assault",78,78,72,68,78,78,55,95))
ideas.append(mk("gx005","Property Crime vs Violent Crime: Which States Have More of Each?","Bivariate map of property vs violent crime rates by state","XREF","US-State","Bivariate choropleth","Crime and Law Enforcement","D:/raw_data/fbi/estimated_crimes cols:violent+property",75,80,75,72,72,82,68,95))
ideas.append(mk("gx006","Americas Crime Territories: Crime in U.S. Territories","Crime rates in Puerto Rico, Guam, USVI, American Samoa compared to states","MAP","US","Bar chart","Crime and Law Enforcement","D:/raw_data/fbi/territories_1995_2024.csv",72,72,72,75,68,72,72,88))
ideas.append(mk("gx007","Male vs Female Police Officers by State","Gender ratio of law enforcement officers across all states","MAP","US-State","Bivariate choropleth","Crime and Law Enforcement","D:/raw_data/fbi/lee col:male_officer+female_officer",68,72,72,72,62,78,72,88))

# === BAD DRIVERS: SPECIFIC METRICS ===
ideas.append(mk("gx008","Americas Speed Demons: States Where Drivers Kill by Speeding","Percentage of fatal collisions involving speeding by state","MAP","US-State","State choropleth","Transportation","D:/raw_data/fivethirtyeight/bad-drivers col:speeding%",72,85,78,68,68,78,58,95))
ideas.append(mk("gx009","Drunk Driving Deaths by State: The Alcohol-Impaired Map","Share of fatal crashes involving alcohol impairment by state","MAP","US-State","State choropleth","Transportation","D:/raw_data/fivethirtyeight/bad-drivers col:alcohol-impaired%",78,85,78,68,78,78,58,95))
ideas.append(mk("gx010","Car Insurance Premiums vs Actual Collision Losses by State","What drivers pay vs what insurance companies lose - who overpays?","XREF","US-State","Bivariate choropleth","Economy","D:/raw_data/fivethirtyeight/bad-drivers cols:premiums+losses",68,88,78,72,62,80,65,95))

# === HATE CRIMES: SPECIFIC CORRELATIONS ===
ideas.append(mk("gx011","The Trump Vote and Hate Crimes: State-Level Correlation","Share of voters who voted Trump vs hate crimes per 100k by state","XREF","US-State","Scatter plot","Elections","D:/raw_data/fivethirtyeight/hate_crimes cols:trump+hatecrime",82,78,68,78,85,75,72,95))
ideas.append(mk("gx012","Gini Index vs Hate Crimes: Inequality Breeds Hate","Income inequality measured by Gini coefficient vs hate crime rates","XREF","US-State","Scatter plot","Crime and Law Enforcement","D:/raw_data/fivethirtyeight/hate_crimes cols:gini+hatecrime",82,75,72,78,82,75,72,95))
ideas.append(mk("gx013","Metro Population vs Hate Crimes: Urban-Rural Divide","Share of population in metro areas vs hate crime rates by state","XREF","US-State","Scatter plot","Crime and Law Enforcement","D:/raw_data/fivethirtyeight/hate_crimes cols:metro+hatecrime",72,72,72,72,68,75,68,92))

# === DRUG USE: AGE-SPECIFIC ===
ideas.append(mk("gx014","When Americans Start Using Each Drug: Age of Initiation","First use age for marijuana, cocaine, hallucinogens, inhalants","CHART","US","Bar chart","Health","D:/raw_data/fivethirtyeight/drug-use-by-age all substances",78,82,75,72,72,75,68,95))
ideas.append(mk("gx015","The Heroin Age Curve: Usage Peaks at 22-23","Heroin use rates by age group showing the deadly sweet spot","CHART","US","Line chart","Health","D:/raw_data/fivethirtyeight/drug-use-by-age col:heroin_use",82,78,72,72,82,72,65,95))
ideas.append(mk("gx016","Alcohol vs Marijuana by Age: The Crossover Generation","How alcohol and marijuana usage rates compare across all age groups","CHART","US","Line chart","Health","D:/raw_data/fivethirtyeight/drug-use-by-age cols:alcohol+marijuana",72,85,78,72,62,75,65,95))

# === COLLEGE MAJORS: SPECIFIC FIELDS ===
ideas.append(mk("gx017","The Gender Pay Gap Starts at College: ShareWomen vs Median Earnings","College majors with more women consistently pay less","XREF","US","Scatter plot","Education","D:/raw_data/fivethirtyeight/recent-grads cols:ShareWomen+Median",82,85,72,78,78,75,68,95))
ideas.append(mk("gx018","The Most Unemployed College Grads: Majors With Worst Job Prospects","Top 20 majors by unemployment rate - some surprise entries","RANK","US","Bar chart","Education","D:/raw_data/fivethirtyeight/recent-grads col:Unemployment_rate",72,90,78,72,68,70,62,95))
ideas.append(mk("gx019","Full-Time vs Part-Time by Major: Who Gets Real Jobs?","Share of graduates working full-time varies wildly by major","RANK","US","Bar chart","Education","D:/raw_data/fivethirtyeight/recent-grads cols:Full_time+Part_time",68,85,75,68,62,70,62,95))

# === TIME WITH RELATIONSHIPS: EMOTIONAL CHART ===
ideas.append(mk("gx020","The Loneliness Curve: Time Spent Alone by Age","Americans spend 3.6 hours alone at 15 but 7+ hours alone at 80","CHART","US","Line chart","Demographics","D:/raw_data/Our World In Data/time-spent col:Alone",90,92,82,80,78,78,75,95))
ideas.append(mk("gx021","When You Stop Seeing Friends: Social Time Drops After 25","Time spent with friends peaks in teens and crashes after college","CHART","US","Line chart","Demographics","D:/raw_data/Our World In Data/time-spent col:With friends",88,90,80,78,78,75,72,95))
ideas.append(mk("gx022","The Partner Premium: Time With Partner by Age","Partnered time peaks at 50-60 then declines as partners die","CHART","US","Line chart","Demographics","D:/raw_data/Our World In Data/time-spent col:With partner",82,85,78,72,72,72,68,95))
ideas.append(mk("gx023","Time With Kids: A 20-Year Window That Closes Fast","Parents spend significant time with children for only about 20 years","CHART","US","Line chart","Demographics","D:/raw_data/Our World In Data/time-spent col:With children",88,88,80,75,78,72,72,95))
ideas.append(mk("gx024","Coworker Time Defines Your Adult Life (Then Vanishes)","Time with coworkers dominates ages 25-55, then drops to zero at retirement","CHART","US","Line chart","Demographics","D:/raw_data/Our World In Data/time-spent col:With coworkers",75,85,78,72,68,72,72,95))

# === GLOBAL PROSPERITY: 15 DIMENSIONS ===
ideas.append(mk("gx025","The Global Safety Index: Which Countries Are Safest?","Safety and security scores from the Legatum Prosperity Index","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (21) col:safety_and_security",72,78,78,68,68,82,58,88))
ideas.append(mk("gx026","Personal Freedom Around the World","Personal freedom dimension of the Legatum Prosperity Index mapped","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (21) col:personal_freedom",78,78,75,68,78,82,60,88))
ideas.append(mk("gx027","The Social Capital Map: Where People Trust Each Other","Social capital scores by country - trust, community, and civic participation","MAP","World","World choropleth","International Statistics","D:/raw_data/Kaggle/archive (21) col:social_capital",72,78,72,72,62,82,68,88))
ideas.append(mk("gx028","Governance Quality vs Economic Quality by Country","Good governance doesnt always mean good economy and vice versa","XREF","World","Scatter plot","International Statistics","D:/raw_data/Kaggle/archive (21) cols:governance+economic_quality",68,68,72,75,65,75,72,88))

# === ASIA MACRO SPECIFICS ===
ideas.append(mk("gx029","Asias FDI Magnets: Foreign Direct Investment as % of GDP","Which Asian countries attract the most foreign investment","MAP","Asia","World choropleth","Economy","D:/raw_data/Kaggle/archive (13) col:FDI_percent_GDP",65,68,72,68,62,78,65,85))
ideas.append(mk("gx030","Asias Current Account Surpluses and Deficits","Current account balance mapped across Asian economies","MAP","Asia","World choropleth","Economy","D:/raw_data/Kaggle/archive (13) col:Current_account_balance",62,65,72,68,62,78,65,82))

# === FOOTBALL RESULTS: SPECIFIC ANGLES ===
ideas.append(mk("gx031","150 Years of International Football: Every Match Since 1872","Heat map of match frequency between countries since Scotlands 0-0 with England","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/Kaggle/FBRESULTS26/results.csv 1872-2026",65,72,78,72,48,82,72,95))
ideas.append(mk("gx032","The Worlds Best Football Stadiums by Attendance Records","Venues that have hosted the most-attended international matches","MAP","World","Dot map","Sports & Recreation","D:/raw_data/Kaggle/FBRESULTS26 col:Attendance+city",58,72,72,65,48,82,65,88))
ideas.append(mk("gx033","Home Advantage in International Football: The Numbers","Home win percentage by country - which nations dominate at home?","MAP","World","World choropleth","Sports & Recreation","D:/raw_data/Kaggle/FBRESULTS26 col:home_score+away_score",62,72,72,72,52,78,68,92))

# === PUBLIC SCHOOL SPECIFICS ===
ideas.append(mk("gx034","The Latitude of Learning: School Performance North vs South","Public school metrics mapped showing geographic patterns in education","MAP","US","Dot map","Education","D:/raw_data/Public_School cols:X+Y+performance",68,78,72,72,58,82,72,88))
ideas.append(mk("gx035","Americas Smallest Schools: Enrollment Under 50 Students","Mapping the tiniest public schools - mostly rural, some island","MAP","US","Dot map","Education","D:/raw_data/Public_School col:enrollment filter:<50",65,72,72,72,55,82,72,88))

# === CANDY DATA SPECIFICS ===
ideas.append(mk("gx036","Chocolate vs Fruity: The Great American Candy Divide","Win percentage for chocolate candies vs fruity candies head to head","CHART","US","Bar chart","Food & Nutrition","D:/raw_data/fivethirtyeight/candy cols:chocolate+fruity+winpercent",62,85,78,68,48,72,65,95))
ideas.append(mk("gx037","Does Expensive Candy Win? Price vs Popularity in Halloween Candy","Price percentile vs win percentage for 85 candy types","XREF","US","Scatter plot","Food & Nutrition","D:/raw_data/fivethirtyeight/candy cols:pricepercent+winpercent",58,82,75,72,45,72,68,95))

# === BIRTHS DATA SPECIFICS ===
ideas.append(mk("gx038","Tuesday Is Americas Birthday: Most Common Birth Day of Week","Day-of-week birth patterns from 10 years of CDC birth data","CHART","US","Bar chart","Demographics","D:/raw_data/fivethirtyeight/US_births col:day_of_week+births",60,82,80,72,42,72,65,95))
ideas.append(mk("gx039","September 16: Americas Most Common Birthday","Daily birth frequency heatmap revealing conception patterns","CHART","US","Heatmap calendar","Demographics","D:/raw_data/fivethirtyeight/US_births cols:month+date+births",65,85,78,75,45,82,72,95))
ideas.append(mk("gx040","The Christmas Baby Drought: Fewest Births Dec 25 Every Year","Birth rates plummet on Christmas, Thanksgiving, and July 4th","CHART","US","Line chart","Demographics","D:/raw_data/fivethirtyeight/US_births holiday analysis",68,85,78,78,52,72,72,95))

print(f"BATCH_GX: {len(ideas)} ideas generated")

# === INJECTION LOGIC ===
with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
new_ideas = []
skipped = 0
for idea in ideas:
    m = re.search(r'id:"([^"]+)"', idea)
    if m and m.group(1) not in existing_ids:
        new_ideas.append(idea)
    else:
        skipped += 1
tail = "]; // end D"
if tail not in raw:
    print("[BATCH_GX] ERROR: tail marker not found"); sys.exit(1)
raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)
print(f"[BATCH_GX] Injected {len(new_ideas)} new ideas (skipped {skipped} dupes)")
