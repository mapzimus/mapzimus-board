"""
BATCH_GJ.py — Standalone ideas from new Kaggle datasets (archives 34-50 + named folders)
Sources: UAP reports, football results, breakfast prices, Iran war, AI index,
         AI jobs, richest people, world pop, Spotify, asteroids, student burnout,
         gold prices, oil prices, World Bank/IMF/WGI, TSMC/NVDA, steam, McDonalds
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

# ============================================================
# UAP/UFO REPORTS (88,875 sightings, city/state/lat/lon)
# ============================================================
ideas.append(mk("uap_sightings_dot_map","Every UFO Sighting in America","88000+ civilian UAP reports mapped by location","MAP","us_national","Dot map","Science & Technology","Kaggle UAP Reports (NUFORC) D:/raw_data/kaggle/archive (50)/\uap_reports.csv",55,60,80,70,40,90,60,95))
ideas.append(mk("uap_sightings_by_state","UFO Sightings by State Per Capita","California leads with 10000+ reports but per capita tells a different story","MAP","us_state","State choropleth","Science & Technology","Kaggle UAP Reports D:/raw_data/kaggle/archive (50)/\uap_reports.csv",50,60,80,65,35,80,55,95))
ideas.append(mk("uap_shapes_breakdown","What Shape Are UFOs","Light triangle circle and fireball dominate 88000 sighting reports","CHART","us_national","Bar chart","Science & Technology","Kaggle UAP Reports D:/raw_data/kaggle/archive (50)/\uap_reports.csv",45,55,80,60,30,65,55,95))
ideas.append(mk("uap_sightings_by_decade","UFO Sightings Exploded After 2000","Reports went from 2000 per decade to 42000 in the 2000s alone","CHART","us_national","Area chart","Science & Technology","Kaggle UAP Reports D:/raw_data/kaggle/archive (50)/\uap_reports.csv",50,55,80,70,35,60,55,95))
ideas.append(mk("uap_hotspot_heatmap","Americas UFO Hotspots","Density heatmap of 88000 sighting reports reveals clusters","MAP","us_national","Dot map","Science & Technology","Kaggle UAP Reports D:/raw_data/kaggle/archive (50)/\uap_reports.csv",55,55,80,70,40,90,65,95))
ideas.append(mk("uap_sightings_worldwide","UFO Sightings Around the World","70000 US vs 3200 Canada vs 2000 UK vs 600 Australia","MAP","worldwide","World choropleth","Science & Technology","Kaggle UAP Reports D:/raw_data/kaggle/archive (50)/\uap_reports.csv",50,50,80,65,35,80,60,95))
ideas.append(mk("uap_triangle_sightings_map","Where People See Triangle UFOs","8489 triangle-shaped sighting reports mapped across America","MAP","us_national","Dot map","Science & Technology","Kaggle UAP Reports D:/raw_data/kaggle/archive (50)/\uap_reports.csv",55,50,75,70,45,90,70,95))

# ============================================================
# INTERNATIONAL FOOTBALL (49,071 matches since 1872, city/country)
# ============================================================
ideas.append(mk("fb_all_time_wins","The Worlds Most Successful Football Nations","All-time international win percentage by country since 1872","MAP","worldwide","World choropleth","Sports & Recreation","Kaggle Football Results D:/raw_data/kaggle/FBRESULTS26/\results.csv",50,65,80,55,40,80,50,95))
ideas.append(mk("fb_home_advantage_world","Home Advantage in International Football","Win rate at home vs away by country across 49000 matches","MAP","worldwide","World choropleth","Sports & Recreation","Kaggle Football Results D:/raw_data/kaggle/FBRESULTS26/\results.csv",45,60,80,55,40,80,55,95))
ideas.append(mk("fb_goals_per_match_century","Football Goals Per Match Over 150 Years","Average goals per match by decade from 1872 to 2025","CHART","worldwide","Line chart","Sports & Recreation","Kaggle Football Results D:/raw_data/kaggle/FBRESULTS26/\results.csv",40,55,80,55,30,60,50,95))
ideas.append(mk("fb_biggest_blowouts","The Biggest Blowouts in International Football","Matches with 10+ goal differentials mapped by location","MAP","worldwide","Dot map","Sports & Recreation","Kaggle Football Results D:/raw_data/kaggle/FBRESULTS26/\results.csv",50,55,80,70,35,80,65,95))
ideas.append(mk("fb_host_cities_map","Every City That Hosted an International Football Match","Thousands of unique cities across 150 years of matches","MAP","worldwide","Dot map","Sports & Recreation","Kaggle Football Results D:/raw_data/kaggle/FBRESULTS26/\results.csv",40,50,80,55,25,90,55,95))
ideas.append(mk("fb_penalty_shootout_kings","Which Countries Win Penalty Shootouts","665 shootouts analyzed by country win percentage","RANK","worldwide","Bar chart","Sports & Recreation","Kaggle Football Results D:/raw_data/kaggle/FBRESULTS26/\shootouts.csv",55,60,80,65,55,55,55,95))
ideas.append(mk("fb_top_scorers_by_country","International Football All-Time Top Scorers by Country","47000+ goals mapped by which nations produce the most scorers","MAP","worldwide","World choropleth","Sports & Recreation","Kaggle Football Results D:/raw_data/kaggle/FBRESULTS26/\goalscorers.csv",50,60,80,55,35,80,50,95))
ideas.append(mk("fb_world_cup_vs_friendly","World Cup Matches vs Friendlies Over Time","How the ratio of competitive to friendly matches has shifted","CHART","worldwide","Area chart","Sports & Recreation","Kaggle Football Results D:/raw_data/kaggle/FBRESULTS26/\results.csv",35,45,80,50,25,60,50,95))
ideas.append(mk("fb_countries_that_renamed","Countries That Changed Their Name","36 nations that played football under a different name","MAP","worldwide","Special map","History","Kaggle Football Results D:/raw_data/kaggle/FBRESULTS26/\former_names.csv",45,45,80,70,30,75,70,95))

# ============================================================
# BREAKFAST BASKET (10,248 rows, city/country/continent, 14 items)
# ============================================================
ideas.append(mk("breakfast_cost_world_map","The Cost of Breakfast Around the World","Price of a standard breakfast basket in USD by country","MAP","worldwide","World choropleth","Food & Nutrition","Kaggle Breakfast Basket D:/raw_data/kaggle/archive (38)/\breakfast basket.csv",55,75,80,60,35,80,55,95))
ideas.append(mk("breakfast_milk_price_world","A Liter of Milk Costs 10x More in Some Countries","Global milk price variation from under $0.50 to over $5","MAP","worldwide","World choropleth","Food & Nutrition","Kaggle Breakfast Basket D:/raw_data/kaggle/archive (38)/\breakfast basket.csv",55,75,80,65,35,80,55,95))
ideas.append(mk("breakfast_egg_price_world","The Price of a Dozen Eggs Around the World","Egg prices vary 20x from the cheapest to most expensive countries","MAP","worldwide","World choropleth","Food & Nutrition","Kaggle Breakfast Basket D:/raw_data/kaggle/archive (38)/\breakfast basket.csv",55,80,80,65,35,80,55,95))
ideas.append(mk("breakfast_beef_vs_chicken_world","Beef vs Chicken Price Ratio by Country","Some countries pay 5x more for beef than chicken while others are nearly equal","MAP","worldwide","Bivariate choropleth","Food & Nutrition","Kaggle Breakfast Basket D:/raw_data/kaggle/archive (38)/\breakfast basket.csv",45,65,80,60,30,85,60,95))
ideas.append(mk("breakfast_inflation_by_continent","Food Inflation Hits Hardest in Africa and Asia","Year-over-year food price inflation by continent","CHART","worldwide","Bar chart","Food & Nutrition","Kaggle Breakfast Basket D:/raw_data/kaggle/archive (38)/\breakfast basket.csv",65,60,80,55,55,60,50,95))
ideas.append(mk("breakfast_cheapest_cities","The Cheapest and Most Expensive Cities for Groceries","Full breakfast basket price ranked across world cities","RANK","worldwide","Bar chart","Food & Nutrition","Kaggle Breakfast Basket D:/raw_data/kaggle/archive (38)/\breakfast basket.csv",50,70,80,60,35,55,50,95))

# ============================================================
# IRAN WAR (gas prices by state, oil prices daily, attack waves with lat/lon)
# ============================================================
ideas.append(mk("iran_gas_price_by_state","How the Iran War Hit Gas Prices in Every State","Gas price increase since war began Feb 28 2026 mapped by state","MAP","us_state","State choropleth","Economy","Kaggle Iran War Gas Prices D:/raw_data/kaggle/archive (39)/\iran_war_gas_prices_by_state.csv",80,90,85,60,80,80,55,95))
ideas.append(mk("iran_oil_price_spike","Oil Prices Doubled in 3 Weeks","Brent crude daily price from pre-war $67 to peak mapped against key events","CHART","worldwide","Line chart","Economy","Kaggle Iran War Oil Prices D:/raw_data/kaggle/archive (39)/\iran_war_oil_prices_daily_2026.csv",75,80,85,65,85,60,55,95))
ideas.append(mk("iran_war_timeline_map","Iran War Attack Waves Mapped","79 missile and drone strike incidents mapped with launch and target locations","MAP","worldwide","Dot map","History","Kaggle Iran War Waves D:/raw_data/kaggle/iranwar/\incidents.csv",70,55,80,70,85,85,65,95))
ideas.append(mk("iran_war_world_reaction","How the World Reacted to the Iran War","210 countries classified by diplomatic stance from condemn to support","MAP","worldwide","World choropleth","History","Kaggle Iran War Reactions D:/raw_data/kaggle/iranwar/\international_reactions.csv",65,55,80,65,75,80,65,95))
ideas.append(mk("iran_strait_hormuz_shipping","Strait of Hormuz Shipping Collapsed During Iran War","Daily ship transits through the worlds most critical oil chokepoint","CHART","worldwide","Line chart","Economy","Kaggle Iran War Oil Prices D:/raw_data/kaggle/archive (39)/\iran_war_oil_prices_daily_2026.csv",65,55,80,70,80,60,60,95))
ideas.append(mk("iran_war_missile_types","What Iran Fired at Israel","Breakdown of missile types used in each attack wave - Emad Ghadr Sejjil Fattah","CHART","worldwide","Bar chart","History","Kaggle Iran War Waves D:/raw_data/kaggle/iranwar/\waves.csv",55,45,80,70,75,60,65,95))
ideas.append(mk("iran_gas_regional_disparity","West Coast Gas Hit $5.50 While South Stayed Under $3.50","Regional gas price disparity during Iran war by US region","MAP","us_state","State choropleth","Economy","Kaggle Iran War Gas Prices D:/raw_data/kaggle/archive (39)/\iran_war_gas_prices_by_state.csv",70,85,85,60,70,80,50,95))

# ============================================================
# AI INDEX (240 rows by country, 2015-2024, 25 AI metrics)
# ============================================================
ideas.append(mk("ai_adoption_world_map","Global AI Adoption by Country","Consumer and enterprise AI adoption rates mapped worldwide","MAP","worldwide","World choropleth","Science & Technology","Kaggle AI Index D:/raw_data/kaggle/archive (40)/\ai_index_main.csv",50,55,80,55,40,80,55,95))
ideas.append(mk("ai_readiness_index","Which Countries Are Ready for AI","AI readiness score combining infrastructure talent policy and investment","MAP","worldwide","World choropleth","Science & Technology","Kaggle AI Index D:/raw_data/kaggle/archive (40)/\ai_index_main.csv",50,55,80,60,45,80,55,95))
ideas.append(mk("ai_investment_by_country","Where AI Investment Dollars Flow","Billions in AI investment by country - US and China dominate","MAP","worldwide","World choropleth","Economy","Kaggle AI Index D:/raw_data/kaggle/archive (40)/\ai_index_main.csv",55,55,80,55,50,80,55,95))
ideas.append(mk("ai_research_papers_country","Who Publishes the Most AI Research","AI research paper output by country 2015-2024","MAP","worldwide","World choropleth","Science & Technology","Kaggle AI Index D:/raw_data/kaggle/archive (40)/\ai_index_main.csv",45,45,80,55,40,80,50,95))
ideas.append(mk("ai_startup_count_world","AI Startups by Country","Number of AI startups shows massive concentration in a few nations","MAP","worldwide","World choropleth","Science & Technology","Kaggle AI Index D:/raw_data/kaggle/archive (40)/\ai_index_main.csv",50,50,80,55,40,80,55,95))
ideas.append(mk("ai_regulation_vs_adoption","Countries That Regulate AI vs Those That Adopt It","AI regulation score vs adoption rate reveals a tension","XREF","worldwide","Scatter plot","Science & Technology","Kaggle AI Index D:/raw_data/kaggle/archive (40)/\ai_index_main.csv",50,50,80,65,50,60,65,95))
ideas.append(mk("ai_adoption_growth_2015_2024","AI Adoption Grew 10x in a Decade","Country-level AI adoption rates from 2015 to 2024","CHART","worldwide","Line chart","Science & Technology","Kaggle AI Index D:/raw_data/kaggle/archive (40)/\ai_index_main.csv",50,55,80,55,35,60,50,95))

# ============================================================
# AI JOB MARKET (10,345 jobs by country, industry, skill, salary)
# ============================================================
ideas.append(mk("ai_jobs_by_country","Where AI Jobs Are Being Posted","AI job postings by country in 2026","MAP","worldwide","World choropleth","Labor","Kaggle AI Jobs D:/raw_data/kaggle/archive (42)/\AI_Job_Market_Trends_2026.csv",50,60,80,55,40,80,50,95))
ideas.append(mk("ai_salary_by_country","AI Engineer Salaries Around the World","Average AI job salary varies 5x between countries","MAP","worldwide","World choropleth","Labor","Kaggle AI Jobs D:/raw_data/kaggle/archive (42)/\AI_Job_Market_Trends_2026.csv",55,70,80,60,40,80,50,95))
ideas.append(mk("ai_remote_vs_hybrid_by_country","Remote AI Jobs Are Not Equally Distributed","Percentage of AI jobs that are remote vs hybrid vs onsite by country","MAP","worldwide","World choropleth","Labor","Kaggle AI Jobs D:/raw_data/kaggle/archive (42)/\AI_Job_Market_Trends_2026.csv",50,65,80,55,35,80,55,95))
ideas.append(mk("ai_skills_demand_2026","Python SQL and ML Are the Most In-Demand AI Skills","Skill requirements across 10000+ AI job postings in 2026","CHART","worldwide","Bar chart","Labor","Kaggle AI Jobs D:/raw_data/kaggle/archive (42)/\AI_Job_Market_Trends_2026.csv",45,65,80,50,30,55,45,95))

# ============================================================
# RICHEST PEOPLE (1000 billionaires, city/state/country)
# ============================================================
ideas.append(mk("billionaire_city_map","Where the Worlds Billionaires Live","1000 richest people mapped by city - New York Moscow Hong Kong Beijing lead","MAP","worldwide","Dot map","Economy","Kaggle Richest People D:/raw_data/kaggle/archive (44)/\richest_people_dataset.csv",55,55,80,55,40,90,50,95))
ideas.append(mk("billionaire_industry_breakdown","How Billionaires Made Their Money","Manufacturing 153 Finance 148 Tech 125 Fashion 92 Food 76","CHART","worldwide","Bar chart","Economy","Kaggle Richest People D:/raw_data/kaggle/archive (44)/\richest_people_dataset.csv",55,60,80,55,45,55,50,95))
ideas.append(mk("billionaire_gender_gap","Only 14% of Billionaires Are Women","863 male vs 137 female among the worlds 1000 richest","CHART","worldwide","Bar chart","Economy","Kaggle Richest People D:/raw_data/kaggle/archive (44)/\richest_people_dataset.csv",65,60,80,50,55,55,50,95))
ideas.append(mk("billionaire_per_capita_country","Billionaires Per Capita by Country","Small nations punch above their weight in producing ultra-rich","MAP","worldwide","World choropleth","Economy","Kaggle Richest People D:/raw_data/kaggle/archive (44)/\richest_people_dataset.csv",50,50,80,65,45,80,60,95))
ideas.append(mk("billionaire_us_state_map","Which US States Have the Most Billionaires","California and New York dominate but Texas and Florida are catching up","MAP","us_state","State choropleth","Economy","Kaggle Richest People D:/raw_data/kaggle/archive (44)/\richest_people_dataset.csv",50,65,80,55,40,80,50,95))

# ============================================================
# WORLD POPULATION (14,925 rows, country/year 1950-2024)
# ============================================================
ideas.append(mk("world_pop_1950_vs_2024","World Population by Country 1950 vs 2024","How dramatically the global population map has shifted in 75 years","MAP","worldwide","World choropleth","Demographics","Kaggle World Population D:/raw_data/kaggle/pop/\popolazione-globale-per-paese-1950-2024.csv",55,55,80,60,40,80,55,95))
ideas.append(mk("world_pop_fastest_growing","The Fastest Growing Countries Since 1950","Population growth multipliers - some nations grew 20x","MAP","worldwide","World choropleth","Demographics","Kaggle World Population D:/raw_data/kaggle/pop/\popolazione-globale-per-paese-1950-2024.csv",50,50,80,65,45,80,55,95))
ideas.append(mk("world_pop_shrinking_countries","Countries That Are Shrinking","Nations with declining populations 2000-2024","MAP","worldwide","World choropleth","Demographics","Kaggle World Population D:/raw_data/kaggle/pop/\popolazione-globale-per-paese-1950-2024.csv",60,55,80,60,55,80,50,95))
ideas.append(mk("world_pop_animation_decades","Watch the World Population Explode","Population by country animated decade by decade 1950-2024","MAP","worldwide","World choropleth","Demographics","Kaggle World Population D:/raw_data/kaggle/pop/\popolazione-globale-per-paese-1950-2024.csv",60,55,80,60,40,80,60,95))

# ============================================================
# SPOTIFY (top 100 all-time songs, top 50 2025, artist_country)
# ============================================================
ideas.append(mk("spotify_top_songs_by_country","Which Countries Produce Spotifys Biggest Hits","Artist country of origin for top 100 all-time streamed songs","MAP","worldwide","World choropleth","Entertainment","Kaggle Spotify D:/raw_data/kaggle/spotify/\spotify_alltime_top100_songs.csv",45,65,80,55,30,80,55,95))
ideas.append(mk("spotify_genre_dominance","Pop Dominates Spotify But K-Pop Is Rising","Genre breakdown of Spotifys most streamed songs","CHART","worldwide","Bar chart","Entertainment","Kaggle Spotify D:/raw_data/kaggle/spotify/\spotify_alltime_top100_songs.csv",40,65,80,50,30,55,50,95))
ideas.append(mk("spotify_streams_vs_year","When Were Spotifys Biggest Hits Released","Release year distribution of top 100 all-time songs","CHART","worldwide","Bar chart","Entertainment","Kaggle Spotify D:/raw_data/kaggle/spotify/\spotify_alltime_top100_songs.csv",40,60,80,55,25,55,50,95))
ideas.append(mk("spotify_2025_wrapped_country_map","Where Spotifys 2025 Top Artists Come From","Country of origin for Spotify Wrapped 2025 top 50 artists","MAP","worldwide","World choropleth","Entertainment","Kaggle Spotify D:/raw_data/kaggle/spotify/\spotify_wrapped_2025_top50_artists.csv",45,65,80,55,30,80,55,95))
ideas.append(mk("spotify_danceability_vs_streams","Do More Danceable Songs Get More Streams","Danceability score vs total streams for top 100 songs","XREF","worldwide","Scatter plot","Entertainment","Kaggle Spotify D:/raw_data/kaggle/spotify/\spotify_alltime_top100_songs.csv",40,60,75,55,25,55,55,95))

# ============================================================
# ASTEROIDS (89,227 close approaches)
# ============================================================
ideas.append(mk("asteroid_close_calls_by_year","Asteroid Close Calls Are Increasing","Near-Earth asteroid approaches by year - detection improving or more threats","CHART","worldwide","Area chart","Science & Technology","Kaggle Asteroids D:/raw_data/kaggle/archive (47)/\asteroid_dataset_20251019.csv",65,50,80,70,65,60,55,95))
ideas.append(mk("asteroid_threat_categories","How Dangerous Are Near-Earth Asteroids","89000 asteroids categorized by threat level and panic score","CHART","worldwide","Bar chart","Science & Technology","Kaggle Asteroids D:/raw_data/kaggle/archive (47)/\asteroid_dataset_20251019.csv",65,50,80,65,70,55,55,95))
ideas.append(mk("asteroid_sentry_watchlist","Asteroids NASA Is Watching Right Now","Objects on the Sentry impact probability watchlist mapped by risk","RANK","worldwide","Ranked list","Science & Technology","Kaggle Asteroids D:/raw_data/kaggle/archive (47)/\asteroid_dataset_20251019.csv",70,50,80,70,75,50,60,95))
ideas.append(mk("asteroid_speed_vs_distance","The Faster They Are the Closer They Get","Asteroid velocity vs closest approach distance","XREF","worldwide","Scatter plot","Science & Technology","Kaggle Asteroids D:/raw_data/kaggle/archive (47)/\asteroid_dataset_20251019.csv",50,40,75,60,55,55,60,95))

# ============================================================
# STUDENT MENTAL HEALTH / BURNOUT (100k rows, no geo but high virality)
# ============================================================
ideas.append(mk("student_burnout_by_study_hours","More Study Hours Means More Burnout","Daily study hours vs burnout level across 100000 students","XREF","worldwide","Scatter plot","Education","Kaggle Student Burnout D:/raw_data/kaggle/mentalburnout/\student_mental_health_burnout.csv",75,80,80,50,55,55,50,95))
ideas.append(mk("student_screen_time_depression","Screen Time and Depression Are Linked","Screen time hours vs depression score in 100000 students","XREF","worldwide","Scatter plot","Health","Kaggle Student Burnout D:/raw_data/kaggle/mentalburnout/\student_mental_health_burnout.csv",75,80,80,50,55,55,50,95))
ideas.append(mk("student_sleep_vs_gpa","Sleep Predicts GPA Better Than Study Hours","Sleep quality and hours vs cumulative GPA","XREF","worldwide","Scatter plot","Education","Kaggle Student Burnout D:/raw_data/kaggle/mentalburnout/\student_mental_health_burnout.csv",65,80,80,65,40,55,55,95))
ideas.append(mk("student_financial_stress_burnout","Financial Stress Is the Biggest Driver of Student Burnout","Financial stress score is the strongest predictor of burnout level","CHART","worldwide","Bar chart","Education","Kaggle Student Burnout D:/raw_data/kaggle/mentalburnout/\student_mental_health_burnout.csv",75,80,80,55,55,55,50,95))
ideas.append(mk("student_social_support_protection","Social Support Protects Against Student Depression","Social support score vs depression and anxiety scores","XREF","worldwide","Scatter plot","Health","Kaggle Student Burnout D:/raw_data/kaggle/mentalburnout/\student_mental_health_burnout.csv",65,75,80,50,40,55,50,95))

# ============================================================
# WORLD BANK / IMF / WGI ECONOMIC INDICATORS (by country)
# ============================================================
ideas.append(mk("wb_gdp_per_capita_world","GDP Per Capita by Country","The economic map of the world - from $300 to $100000+","MAP","worldwide","World choropleth","Economy","Kaggle World Bank D:/raw_data/kaggle/archive (35)",50,55,85,50,35,80,40,95))
ideas.append(mk("wb_gdp_growth_world","Which Economies Are Growing Fastest","Annual GDP growth rate by country","MAP","worldwide","World choropleth","Economy","Kaggle World Bank D:/raw_data/kaggle/archive (35)",45,50,80,55,40,80,40,95))
ideas.append(mk("wb_govt_debt_world","Government Debt as Percent of GDP","Some nations owe more than their entire economy produces","MAP","worldwide","World choropleth","Economy","Kaggle IMF WEO D:/raw_data/kaggle/archive (35)",60,55,80,60,55,80,45,95))
ideas.append(mk("wgi_corruption_world","The Worlds Most and Least Corrupt Countries","Control of Corruption index by country","MAP","worldwide","World choropleth","International Statistics","Kaggle WGI D:/raw_data/kaggle/archive (35)",55,50,80,55,55,80,45,95))
ideas.append(mk("wgi_political_stability_map","Political Stability Around the World","Violence and terrorism risk index by country","MAP","worldwide","World choropleth","International Statistics","Kaggle WGI D:/raw_data/kaggle/archive (35)",60,50,80,55,65,80,45,95))
ideas.append(mk("wgi_rule_of_law_world","Where Rule of Law Is Strongest and Weakest","Rule of law estimate by country mapped globally","MAP","worldwide","World choropleth","International Statistics","Kaggle WGI D:/raw_data/kaggle/archive (35)",50,45,80,55,50,80,45,95))
ideas.append(mk("wb_agriculture_vs_industry","Agriculture vs Industry Share of GDP","How economies shift from farming to manufacturing mapped by country","MAP","worldwide","Bivariate choropleth","Economy","Kaggle World Bank D:/raw_data/kaggle/archive (35)",45,45,80,55,35,85,55,95))

# ============================================================
# OIL / GOLD / COMMODITY PRICES (long-term historical)
# ============================================================
ideas.append(mk("oil_price_56_years","56 Years of Oil Prices","Crude oil from $1.21 in 1970 to Iran war spike in 2026","CHART","worldwide","Line chart","Economy","Kaggle Oil Prices D:/raw_data/kaggle/archive (48)/\fuel_prices_1970_2026.csv",55,55,80,55,55,60,45,95))
ideas.append(mk("gold_price_200_years","200 Years of Gold Prices","Monthly gold price from 1833 to present","CHART","worldwide","Line chart","Economy","Kaggle Gold Prices D:/raw_data/kaggle/archive (36)/\monthly.csv",45,45,80,55,35,60,50,95))
ideas.append(mk("oil_crisis_comparison","Every Oil Crisis Compared","1973 Arab embargo vs 1979 Iran revolution vs 1990 Gulf War vs 2008 vs 2022 vs 2026","CHART","worldwide","Line chart","Economy","Kaggle Oil + Iran War D:/raw_data/kaggle/archive (48) + archive (39)",65,60,80,65,65,60,55,95))

# ============================================================
# TSMC / NVIDIA STOCK (tech giant trajectories)
# ============================================================
ideas.append(mk("tsmc_stock_27_years","TSMCs 27-Year Stock Journey","From $3 in 1997 to semiconductor superpower","CHART","worldwide","Line chart","Economy","Kaggle TSMC D:/raw_data/kaggle/archive (34)/\tsm_historical_data.csv",45,50,80,55,35,60,45,95))
ideas.append(mk("nvidia_stock_25_years","NVIDIAs Insane Stock Rise","From $0.04 in 1999 to $180+ powered by AI demand","CHART","worldwide","Line chart","Economy","Kaggle NVIDIA D:/raw_data/kaggle/archive (45)/\nvda_stock_data_daily_yahoo.csv",55,60,80,70,40,60,50,95))
ideas.append(mk("nvidia_earnings_beats","NVIDIA Has Beat Earnings Estimates 40+ Times","Estimated vs actual EPS for every quarter since 2015","CHART","worldwide","Bar chart","Economy","Kaggle NVIDIA D:/raw_data/kaggle/archive (45)/\nvda_earnings_history_alphaquery.csv",45,50,80,55,35,55,50,95))

# ============================================================
# STEAM TOP GAMES
# ============================================================
ideas.append(mk("steam_top_games_2026","The Most Popular PC Games in 2026","Top 1000 Steam games by peak players and reviews","RANK","worldwide","Ranked list","Entertainment","Kaggle Steam D:/raw_data/kaggle/steam/\steam_games_2026.csv",40,65,80,50,30,50,45,95))
ideas.append(mk("steam_price_vs_reviews","Do Expensive Games Get Better Reviews","Game price vs review score percentage for 1000 Steam games","XREF","worldwide","Scatter plot","Entertainment","Kaggle Steam D:/raw_data/kaggle/steam/\steam_games_2026.csv",40,65,80,55,30,55,55,95))
ideas.append(mk("steam_free_vs_paid","Free Games Dominate Steam Player Counts","Free-to-play games have dramatically higher peak player counts","CHART","worldwide","Bar chart","Entertainment","Kaggle Steam D:/raw_data/kaggle/steam/\steam_games_2026.csv",40,65,80,55,30,55,50,95))

# ============================================================
# MCDONALDS STOCK (as proxy for fast food economy)
# ============================================================
ideas.append(mk("mcdonalds_stock_25_years","McDonalds Stock Has 10x-ed Since 2000","From $21 in 2000 to $300+ a Big Mac-fueled juggernaut","CHART","worldwide","Line chart","Economy","Kaggle MCD D:/raw_data/kaggle/archive (43)/\MCD.csv",40,60,80,55,30,55,45,95))

# ============================================================
# BTC
# ============================================================
ideas.append(mk("btc_price_5_years","Bitcoin From $18K to $100K+ in 5 Years","Daily BTC price from late 2020 through 2026","CHART","worldwide","Line chart","Economy","Kaggle BTC D:/raw_data/kaggle/archive (49)/\BTC_prices.csv",55,60,80,55,45,55,45,95))

# ============================================================
# GLOBAL TRENDS SENTIMENT
# ============================================================
ideas.append(mk("global_trends_sentiment_map","Global News Sentiment by Country","Positive vs negative sentiment in trending topics by nation","MAP","worldwide","World choropleth","International Statistics","Kaggle Global Trends D:/raw_data/kaggle/archive (37)/\enhanced_global_trends_dataset.csv",50,50,80,55,45,80,55,90))

# ============================================================
# INJECTION LOGIC
# ============================================================
print(f"[BATCH_GJ] {len(ideas)} ideas ready")

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
    print("[BATCH_GJ] ERROR: tail marker not found in data.js")
    sys.exit(1)

raw = raw.replace(tail, "")
for idea in new_ideas:
    raw += idea + ",\n"
raw += tail + "\n"

with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(raw)

print(f"[BATCH_GJ] Injected {len(new_ideas)} new ideas ({skipped} dupes skipped)")
