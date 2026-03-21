"""
BATCH_GA: Kaggle Data Batch — 105 new ideas from newly downloaded datasets
Sources: Global homicide, inequality, ICE detention, prosperity/politics,
         animals slaughtered, temperature, fuel/oil prices, Iran war,
         Spotify, religious beliefs, military ops, modern slavery,
         football/FIFA, Steam games, mental health, student burnout,
         Asia macro, population, Boston housing
"""
import os, re

DATA = r"D:\projects\mapzimus-board\data.js"

def mk(id,title,sub,typ,geo,fmt,sect,tbl,e,r,c,s,t,v,o,dr):
    raw=e*2+r*2+c*2+s*1.5+t*1+v*1.25+o*1
    vs=int((raw/10.75)*(1-0.3*(1-dr/100)))
    return ('{id:"'+id+'",title:"'+title+'",sub:"'+sub+'",type:"'+typ+'",'
            'geo:"'+geo+'",fmt:"'+fmt+'",section:"'+sect+'",tbl:"'+tbl+'",'
            'sc:{emotional:'+str(e)+',relatability:'+str(r)+',clarity:'+str(c)
            +',surprise:'+str(s)+',tension:'+str(t)+',visual:'+str(v)
            +',originality:'+str(o)+',data_ready:'+str(dr)+'}'
            ',vs:'+str(vs)+',topics:[],ext:[],status:"idea",notes:""}')

ideas = [
    # ===== IRAN WAR + OIL CRISIS (timely, high tension) =====
    mk("iran_war_oil_price_timeline","Oil Price Surge During Iran War 2026","Brent crude went from $67 to $110 in three weeks","CHART","worldwide","Line chart","History","Kaggle Iran War Oil Prices 2026 + https://www.kaggle.com",85,80,90,90,90,85,80,95),
    mk("iran_war_gas_price_state_map","Gas Prices by State During Iran War","Which states got hit hardest at the pump after the strikes began","MAP","us_state","State choropleth","Energy","Kaggle Iran War Gas Prices by State 2026 + https://www.kaggle.com",90,95,85,80,85,90,75,95),
    mk("iran_war_strait_hormuz_shipping","Strait of Hormuz Ship Traffic Collapse","Daily vessel transits through the worlds most critical oil chokepoint","CHART","middle_east","Area chart","History","Kaggle Iran War Oil Prices 2026 + https://www.kaggle.com",80,70,85,90,90,85,85,90),
    mk("iran_war_brent_vs_us_gas_lag","How Fast Do Oil Spikes Hit Your Gas Station","Brent crude vs US gas prices day by day during the Iran war","XREF","us_national","Scatter plot","Energy","Kaggle Iran War Oil Prices 2026 + https://www.kaggle.com",80,90,85,75,70,75,75,95),
    mk("iran_war_timeline_key_events","21 Days That Changed Global Energy","Every major strike escalation and market reaction mapped to the calendar","CHART","worldwide","Line chart","History","Kaggle Iran War Key Events Timeline 2026 + https://www.kaggle.com",85,75,90,85,90,85,85,95),
    mk("iran_war_gas_spike_vs_katrina","Iran War Gas Spike vs Hurricane Katrina","The largest monthly gas price rises in US history compared","XREF","us_national","Bar chart","Energy","Kaggle Iran War Gas Prices + EIA Historical + https://www.kaggle.com",85,85,85,85,80,80,80,90),
    mk("iran_war_weapon_types_breakdown","Every Weapon Used in the Iran-Israel Strikes","Drones cruise missiles and ballistic missiles by wave and operation","CHART","middle_east","Bar chart","History","Kaggle Iran War Incidents + https://www.kaggle.com",75,60,85,90,85,90,85,95),
    mk("iran_war_interception_rate","Iron Dome vs Iranian Missiles: Interception Rates","What percentage of each weapon type was intercepted by wave","CHART","middle_east","Bar chart","History","Kaggle Iran War Incidents + https://www.kaggle.com",80,70,85,95,90,85,90,90),
    mk("iran_war_international_reaction_map","How Every Country Responded to the Iran Strikes","World map of diplomatic stances from condemnation to support","MAP","worldwide","World choropleth","History","Kaggle Iran War International Reactions + https://www.kaggle.com",75,65,80,80,85,90,80,95),
    mk("iran_war_diesel_price_trucking","Diesel Hit $5: What the Iran War Means for US Trucking","Diesel price surge mapped against major freight corridors","MAP","us_national","State choropleth","Transportation","Kaggle Iran War Oil Prices + EIA Diesel + https://www.kaggle.com",80,85,80,75,80,80,75,85),

    # ===== GLOBAL HOMICIDE =====
    mk("global_homicide_rate_world_map","Global Homicide Rates by Country","The Caribbean has murder rates 10x higher than most of Europe","MAP","worldwide","World choropleth","Crime and Law Enforcement","Kaggle Global Homicide Rates + https://www.kaggle.com",85,70,85,80,90,90,70,95),
    mk("homicide_rate_change_1990_2023","How Murder Rates Changed in Every Country Since 1990","Some countries got dramatically safer while others collapsed","MAP","worldwide","World choropleth","Crime and Law Enforcement","Kaggle Global Homicide Rates + https://www.kaggle.com",80,65,80,85,85,90,80,95),
    mk("homicide_rate_gender_gap","Men Are 4x More Likely to Be Murdered Than Women","Homicide rates by sex across every country on earth","XREF","worldwide","Scatter plot","Crime and Law Enforcement","Kaggle Global Homicide Rates + https://www.kaggle.com",80,75,80,80,80,75,75,95),
    mk("caribbean_murder_rate_crisis","The Caribbean Murder Crisis Nobody Talks About","Small island nations with the highest homicide rates in the world","RANK","latin_america","Ranked list","Crime and Law Enforcement","Kaggle Global Homicide Rates + https://www.kaggle.com",85,60,85,90,90,80,85,95),
    mk("homicide_vs_gdp_per_capita","Does Wealth Prevent Murder","Homicide rate vs GDP per capita for every country","XREF","worldwide","Scatter plot","Crime and Law Enforcement","Kaggle Global Homicide Rates + World Bank GDP + https://www.kaggle.com",75,65,80,75,80,75,70,85),

    # ===== GLOBAL INEQUALITY =====
    mk("gini_world_map_2024","Global Inequality Map 2024: Who Shares the Wealth","Gini coefficient for every country with available data","MAP","worldwide","World choropleth","Economy","Kaggle Global Inequality 1980-2024 + https://www.kaggle.com",80,70,85,75,80,90,70,95),
    mk("top1_income_share_world","Where the Top 1% Takes the Biggest Slice","Income share of the richest 1% mapped globally","MAP","worldwide","World choropleth","Economy","Kaggle Global Inequality 1980-2024 + https://www.kaggle.com",90,80,85,85,90,90,80,95),
    mk("bottom50_income_share_world","What the Bottom Half Actually Earns","Income share of the poorest 50% in every country","MAP","worldwide","World choropleth","Economy","Kaggle Global Inequality 1980-2024 + https://www.kaggle.com",90,85,85,80,85,85,75,95),
    mk("inequality_trend_1980_2024","The World Got Richer but Less Equal","How the Gini index changed in major economies over 44 years","CHART","worldwide","Line chart","Economy","Kaggle Global Inequality 1980-2024 + https://www.kaggle.com",80,75,80,75,80,80,70,95),
    mk("xref_poverty_rate_vs_top1_share","When the Rich Get Richer Do the Poor Get Poorer","Poverty rate vs top 1% income share by country","XREF","worldwide","Scatter plot","Economy","Kaggle Global Inequality 1980-2024 + https://www.kaggle.com",85,75,80,80,85,75,80,95),
    mk("xref_gini_vs_homicide_rate","Inequality Kills: Gini Index vs Homicide Rate","Countries with higher inequality have dramatically more murder","XREF","worldwide","Scatter plot","Crime and Law Enforcement","Kaggle Global Inequality + Global Homicide Rates + https://www.kaggle.com",90,70,85,90,90,80,85,90),

    # ===== ICE DETENTION =====
    mk("ice_detention_release_reasons","Why ICE Releases People: The Data","Breakdown of every release reason from 672000 detention stays","CHART","us_national","Bar chart","Demographics","Kaggle ICE Detention Stays + https://www.kaggle.com",80,70,85,80,90,75,80,95),
    mk("ice_detention_stay_length","How Long Does ICE Hold You","Distribution of detention stay lengths in the United States","CHART","us_national","Area chart","Demographics","Kaggle ICE Detention Stays + https://www.kaggle.com",80,75,80,75,85,75,75,90),
    mk("ice_detention_by_nationality","Where Detainees Come From","Countries of origin for ICE detention stays","MAP","worldwide","World choropleth","Demographics","Kaggle ICE Detention Stays + https://www.kaggle.com",75,65,80,70,85,85,70,85),
    mk("ice_detention_gender_age","The Demographics Inside ICE Detention","Age and gender breakdown of 672000 immigration detention stays","CHART","us_national","Bar chart","Demographics","Kaggle ICE Detention Stays + https://www.kaggle.com",75,70,80,70,80,70,70,90),
    mk("ice_detention_bond_amounts","The Price of Freedom: ICE Bond Amounts","How much detainees must pay to get out and how many actually can","CHART","us_national","Bar chart","Demographics","Kaggle ICE Detention Stays + https://www.kaggle.com",85,75,80,80,90,70,80,90),
    mk("xref_ice_detention_vs_crime_rate","Does Detention Actually Reduce Crime","ICE detention volume vs local crime rates over time","XREF","us_state","Scatter plot","Crime and Law Enforcement","Kaggle ICE Detention Stays + FBI Crime Data + https://www.kaggle.com",80,70,75,80,95,70,80,75),

    # ===== ANIMALS SLAUGHTERED =====
    mk("animals_slaughtered_global_scale","490 Billion Chickens: Animals Killed for Meat Annually","The staggering scale of global meat production visualized","CHART","worldwide","Bar chart","Food & Nutrition","OWID Land Animals Slaughtered + https://www.kaggle.com",90,75,90,95,80,90,85,95),
    mk("animals_slaughtered_trend_1961_2022","The Exponential Rise in Animals Slaughtered","From 1961 to 2022 global meat production quintupled","CHART","worldwide","Area chart","Food & Nutrition","OWID Land Animals Slaughtered + https://www.kaggle.com",80,70,85,80,75,85,75,95),
    mk("animals_slaughtered_per_capita","Which Countries Kill the Most Animals Per Person","Animals slaughtered per capita reveals very different food cultures","MAP","worldwide","World choropleth","Food & Nutrition","OWID Land Animals Slaughtered + https://www.kaggle.com",85,75,85,85,80,90,80,90),
    mk("china_meat_explosion","Chinas Meat Revolution: 0 to 50 Billion Animals","How Chinas industrialization transformed global animal agriculture","CHART","asia","Line chart","Food & Nutrition","OWID Land Animals Slaughtered + https://www.kaggle.com",80,65,85,85,75,80,80,95),
    mk("xref_meat_slaughter_vs_gdp","As Countries Get Richer They Kill More Animals","GDP per capita vs animals slaughtered per capita","XREF","worldwide","Scatter plot","Food & Nutrition","OWID Land Animals Slaughtered + World Bank GDP + https://www.kaggle.com",80,70,80,80,75,75,75,85),

    # ===== GLOBAL TEMPERATURE =====
    mk("fastest_warming_countries_map","The Fastest Warming Countries on Earth","Central Asia and Canada are warming 3x faster than the global average","MAP","worldwide","World choropleth","Climate","Kaggle Global Temperature 1950-2024 + https://www.kaggle.com",85,75,85,90,80,90,80,95),
    mk("temperature_change_1950_2024","Every Country Got Warmer: Temperature Change Since 1950","Mean annual temperature change mapped for 196 countries","MAP","worldwide","World choropleth","Climate","Kaggle Global Temperature 1950-2024 + https://www.kaggle.com",85,80,85,80,80,90,75,95),
    mk("xref_warming_rate_vs_co2_emissions","The Countries Warming Fastest Arent the Ones Causing It","Temperature change vs cumulative CO2 emissions per capita","XREF","worldwide","Scatter plot","Climate","Kaggle Global Temperature + OWID CO2 + https://www.kaggle.com",90,75,80,90,85,80,90,85),
    mk("arctic_vs_tropical_warming","The Arctic Warms 4x Faster Than the Tropics","Temperature trends by latitude band from 1950 to 2024","CHART","worldwide","Line chart","Climate","Kaggle Global Temperature 1950-2024 + https://www.kaggle.com",80,70,85,85,80,80,80,95),
    mk("uzbekistan_warming_anomaly","Why Uzbekistan Is the Fastest Warming Country on Earth","Central Asian landlocked nations are climate change ground zero","MAP","asia","Special map","Climate","Kaggle Global Temperature 1950-2024 + https://www.kaggle.com",75,55,80,90,70,80,85,95),

    # ===== CRUDE OIL PRICES =====
    mk("crude_oil_price_history_1970_2026","56 Years of Oil: Every Crisis Spike and Crash","Crude oil prices from $1.21 to $132 annotated with world events","CHART","worldwide","Line chart","Energy","Kaggle Fuel Prices 1970-2026 + https://www.kaggle.com",80,75,90,75,80,85,70,95),
    mk("oil_price_vs_recession","Every Oil Spike Preceded a Recession","Crude oil price shocks mapped against US economic downturns","XREF","us_national","Line chart","Energy","Kaggle Fuel Prices 1970-2026 + NBER Recession Dates + https://www.kaggle.com",85,80,80,85,80,80,80,85),
    mk("oil_price_inflation_adjusted","Oil Isnt Actually at a Record High When You Adjust for Inflation","Real vs nominal crude oil prices since 1970","CHART","worldwide","Line chart","Energy","Kaggle Fuel Prices 1970-2026 + CPI Data + https://www.kaggle.com",75,75,85,80,60,75,75,90),

    # ===== SPOTIFY =====
    mk("spotify_top100_by_country_treemap","Which Countries Dominate Spotify","USA and UK account for 70% of all-time top 100 streams","CHART","worldwide","Treemap","Entertainment","Kaggle Spotify All-Time Top 100 + https://www.kaggle.com",75,80,85,70,50,80,70,95),
    mk("spotify_streams_vs_release_year","Old Songs Are Dominating Spotify","When the most-streamed songs of all time were actually released","CHART","worldwide","Bar chart","Entertainment","Kaggle Spotify All-Time Top 100 + https://www.kaggle.com",70,80,85,80,55,75,75,95),
    mk("spotify_genre_dominance_shift","How Pop Ate Everything on Spotify","Genre breakdown of top 100 most streamed songs ever","CHART","worldwide","Bar chart","Entertainment","Kaggle Spotify All-Time Top 100 + https://www.kaggle.com",65,75,80,70,50,75,70,95),
    mk("spotify_danceability_vs_streams","Do Danceable Songs Get More Streams","Danceability score vs total streams for the top 100","XREF","worldwide","Scatter plot","Entertainment","Kaggle Spotify All-Time Top 100 + https://www.kaggle.com",60,70,80,65,40,70,70,95),
    mk("spotify_explicit_vs_clean_streams","Explicit Songs Now Dominate Streaming","Percentage of top songs that are explicit over time","CHART","worldwide","Line chart","Entertainment","Kaggle Spotify All-Time Top 100 + https://www.kaggle.com",65,75,80,70,55,70,70,95),
    mk("spotify_wrapped_2025_country_map","Where 2025s Biggest Artists Come From","World map of artist countries from Spotify Wrapped 2025","MAP","worldwide","World choropleth","Entertainment","Kaggle Spotify Wrapped 2025 + https://www.kaggle.com",65,70,80,65,45,85,70,95),

    # ===== PROSPERITY vs POLITICS =====
    mk("democracy_vs_prosperity_scatter","Democracies Are Richer: Political Regime vs Prosperity","Liberal democracies cluster at the top of every prosperity metric","XREF","worldwide","Scatter plot","Economy","Kaggle Global Prosperity + Politics + https://www.kaggle.com",80,70,85,75,80,80,75,95),
    mk("autocracy_prosperity_world_map","The Prosperity Cost of Autocracy","World map colored by political regime overlaid with prosperity score","MAP","worldwide","World choropleth","Economy","Kaggle Global Prosperity + Politics + https://www.kaggle.com",80,65,80,75,85,90,80,95),
    mk("personal_freedom_vs_safety","Freedom vs Safety: The Global Tradeoff","Do countries that restrict freedom actually keep people safer","XREF","worldwide","Scatter plot","Economy","Kaggle Global Prosperity + Politics + https://www.kaggle.com",80,70,80,80,80,75,80,95),
    mk("closed_autocracy_bottom_rankings","Every Metric Closed Autocracies Rank Last","How the worlds least free countries perform across 12 prosperity dimensions","RANK","worldwide","Ranked list","Economy","Kaggle Global Prosperity + Politics + https://www.kaggle.com",75,60,85,80,80,75,80,95),

    # ===== RELIGIOUS BELIEFS =====
    mk("belief_in_god_by_demographics","Who Still Believes in God in America","Belief in God by age income education party and gender","CHART","us_national","Bar chart","Demographics","Gallup Religious Beliefs Survey + https://www.kaggle.com",80,90,85,75,70,75,70,95),
    mk("belief_hell_vs_heaven_gap","More Americans Believe in Heaven Than Hell","The gap between belief in positive vs negative afterlife concepts","CHART","us_national","Bar chart","Demographics","Gallup Religious Beliefs Survey + https://www.kaggle.com",75,85,85,80,60,70,75,95),
    mk("young_vs_old_belief_gap","The God Gap: 59% of Young Adults vs 83% of Seniors","Generational collapse in religious belief across every category","CHART","us_national","Bar chart","Demographics","Gallup Religious Beliefs Survey + https://www.kaggle.com",85,85,85,80,75,75,80,95),
    mk("republican_vs_democrat_afterlife","Republicans Are 20 Points More Likely to Believe in Hell","Political party and belief in the supernatural","XREF","us_national","Bar chart","Demographics","Gallup Religious Beliefs Survey + https://www.kaggle.com",80,80,85,80,80,75,75,95),
    mk("income_vs_belief_in_god","Richer Americans Are Less Religious","Household income vs belief in God angels heaven and hell","XREF","us_national","Bar chart","Demographics","Gallup Religious Beliefs Survey + https://www.kaggle.com",80,80,85,80,70,70,75,95),

    # ===== MILITARY OPERATIONS =====
    mk("us_military_ops_timeline_1989_2026","Every US Military Operation Since the Cold War","290 operations mapped by year duration and weapon type","CHART","worldwide","Line chart","History","Kaggle Military Operations Strategic + https://www.kaggle.com",80,70,85,80,85,85,80,95),
    mk("drone_warfare_rise","The Rise of Drone Warfare","Percentage of US military operations using drones by decade","CHART","worldwide","Area chart","History","Kaggle Military Operations Strategic + https://www.kaggle.com",80,70,85,85,80,80,85,95),
    mk("civilian_casualties_by_operation","Civilian Casualties in Every US Military Operation","The human cost of 35 years of American military intervention","CHART","worldwide","Bar chart","History","Kaggle Military Operations Strategic + https://www.kaggle.com",90,65,80,80,95,80,80,85),
    mk("us_military_ops_world_map","Where America Has Fought Since 1989","Every military operation plotted on a world map by lat/lon","MAP","worldwide","Dot map","History","Kaggle Military Operations Strategic + https://www.kaggle.com",80,70,85,75,85,90,75,90),
    mk("urban_vs_rural_warfare_shift","Modern Wars Moved Into Cities","Urban vs rural military operations over time","CHART","worldwide","Area chart","History","Kaggle Military Operations Strategic + https://www.kaggle.com",70,55,80,80,75,75,80,95),

    # ===== MODERN SLAVERY / FISHING =====
    mk("modern_slavery_fishing_world_map","Modern Slavery in the Global Fishing Industry","Which countries fishing fleets are most linked to forced labor","MAP","worldwide","World choropleth","Crime and Law Enforcement","Global Slavery Index 2018 + Kaggle + https://www.kaggle.com",90,60,80,90,90,85,90,90),
    mk("xref_gdp_vs_slavery_vulnerability","Poverty Breeds Slavery: GDP vs Modern Slavery Vulnerability","Countries with lower GDP per capita have dramatically higher slavery risk","XREF","worldwide","Scatter plot","Crime and Law Enforcement","Global Slavery Index 2018 + Kaggle + https://www.kaggle.com",85,60,80,80,85,75,80,90),
    mk("unreported_fishing_catch_map","The Worlds Unreported Fish Catch","Percentage of fish catch that goes unreported by country","MAP","worldwide","World choropleth","Environment","Global Slavery Index 2018 + Kaggle + https://www.kaggle.com",75,55,80,85,70,85,80,90),

    # ===== INTERNATIONAL FOOTBALL =====
    mk("football_home_advantage_world","Home Field Advantage: 150 Years of International Football","Win rates at home vs away for every national team since 1872","MAP","worldwide","World choropleth","Sports & Recreation","Kaggle International Football Results + https://www.kaggle.com",70,75,80,70,55,80,70,95),
    mk("football_most_lopsided_results","The Most Lopsided Matches in Football History","Every match with a 10+ goal difference from 49000 internationals","RANK","worldwide","Ranked list","Sports & Recreation","Kaggle International Football Results + https://www.kaggle.com",65,70,85,80,50,70,75,95),
    mk("football_goals_per_match_trend","Football Is Getting Less Exciting","Goals per match in international football from 1872 to 2026","CHART","worldwide","Line chart","Sports & Recreation","Kaggle International Football Results + https://www.kaggle.com",65,65,85,75,55,75,70,95),
    mk("fifa_rankings_vs_world_cup_titles","FIFA Points Dont Match World Cup Wins","Current FIFA ranking vs number of World Cup titles won","XREF","worldwide","Scatter plot","Sports & Recreation","Kaggle FIFA World Rankings Jan 2026 + https://www.kaggle.com",65,70,85,75,50,75,75,95),
    mk("fifa_confederation_power_ranking","UEFA Dominates: FIFA Rankings by Confederation","Average ranking points by continental confederation","CHART","worldwide","Bar chart","Sports & Recreation","Kaggle FIFA World Rankings Jan 2026 + https://www.kaggle.com",60,60,85,65,50,75,65,95),

    # ===== STEAM GAMES =====
    mk("steam_most_played_games_2026","The Most Played Games on Steam Right Now","Counter-Strike 2 still has 1M concurrent players in 2026","RANK","worldwide","Ranked list","Entertainment","Kaggle Steam Games 2026 + https://www.kaggle.com",60,75,85,60,40,75,60,95),
    mk("steam_free_vs_paid_player_counts","Free Games Dominate Steam","Free-to-play games have 10x the player base of paid games","XREF","worldwide","Scatter plot","Entertainment","Kaggle Steam Games 2026 + https://www.kaggle.com",55,70,80,65,40,70,65,95),
    mk("steam_price_vs_review_score","Do Expensive Games Get Better Reviews","Price vs review score for 1000 Steam games","XREF","worldwide","Scatter plot","Entertainment","Kaggle Steam Games 2026 + https://www.kaggle.com",55,70,80,65,40,70,65,95),
    mk("steam_deck_compatibility_rate","How Many Steam Games Work on the Steam Deck","Compatibility status breakdown for 1000 top games","CHART","worldwide","Bar chart","Entertainment","Kaggle Steam Games 2026 + https://www.kaggle.com",55,65,80,60,35,70,60,95),

    # ===== GLOBAL POPULATION =====
    mk("population_shift_1950_2024","The World Rebalanced: Population Share by Country Since 1950","How India overtook China and Africa is surging","CHART","worldwide","Area chart","Demographics","Kaggle Global Population 1950-2024 + https://www.kaggle.com",80,70,85,80,70,85,75,95),
    mk("population_growth_rate_world_map","Where the World Is Still Growing Fast","Annual population growth rate mapped globally","MAP","worldwide","World choropleth","Demographics","Kaggle Global Population 1950-2024 + https://www.kaggle.com",75,65,85,70,65,90,65,95),
    mk("population_shrinking_countries","The Countries That Are Disappearing","Nations with negative population growth rates","MAP","worldwide","World choropleth","Demographics","Kaggle Global Population 1950-2024 + https://www.kaggle.com",80,70,85,85,75,85,80,95),
    mk("xref_population_growth_vs_gdp","Fast Growth Poor Countries: Population vs Prosperity","Population growth rate vs GDP per capita globally","XREF","worldwide","Scatter plot","Demographics","Kaggle Global Population + Economic Growth + https://www.kaggle.com",75,65,80,75,70,75,70,90),

    # ===== MENTAL HEALTH =====
    mk("screen_time_vs_mental_health","More Screen Time Worse Mental Health","Hours of screen time vs mental health risk score","XREF","worldwide","Scatter plot","Health","Kaggle Mental Health Risk Dataset + https://www.kaggle.com",85,90,80,70,75,70,65,90),
    mk("sleep_hours_vs_mental_health","Less Sleep Higher Risk: The Mental Health Sleep Connection","Sleep hours vs overall mental health risk score","XREF","worldwide","Scatter plot","Health","Kaggle Mental Health Risk Dataset + https://www.kaggle.com",80,90,80,65,65,70,60,90),
    mk("social_support_vs_mental_health","Social Support Is the Best Predictor of Mental Health","Social support score vs mental health risk across 25000 people","XREF","worldwide","Scatter plot","Health","Kaggle Mental Health Risk Dataset + https://www.kaggle.com",85,85,80,75,70,70,70,90),
    mk("work_stress_vs_mental_health","Work Stress Is Destroying Mental Health","Work stress level vs mental health risk score","XREF","worldwide","Scatter plot","Health","Kaggle Mental Health Risk Dataset + https://www.kaggle.com",85,90,80,65,80,70,65,90),
    mk("mental_health_employment_status","Unemployed People Have 3x the Mental Health Risk","Mental health outcomes by employment status","CHART","worldwide","Bar chart","Health","Kaggle Mental Health Risk Dataset + https://www.kaggle.com",85,80,85,75,75,70,70,90),

    # ===== STUDENT BURNOUT =====
    mk("student_burnout_screen_time","Student Burnout Correlates with Screen Time","Hours of screen time vs burnout score in college students","XREF","worldwide","Scatter plot","Education","Kaggle Student Mental Health Burnout + https://www.kaggle.com",80,85,80,65,70,70,65,90),
    mk("student_sleep_vs_academic_performance","Students Who Sleep Less Get Worse Grades","Daily sleep hours vs GPA across thousands of students","XREF","worldwide","Scatter plot","Education","Kaggle Student Mental Health Burnout + https://www.kaggle.com",75,85,80,60,60,70,60,90),
    mk("student_anxiety_by_course","Which College Majors Have the Most Anxiety","Anxiety scores by field of study","CHART","worldwide","Bar chart","Education","Kaggle Student Mental Health Burnout + https://www.kaggle.com",80,85,85,75,65,75,75,85),

    # ===== CROSS-DATASET XREF (the gold) =====
    mk("xref_homicide_vs_inequality_world","Murder Follows Inequality: Homicide Rate vs Gini Index","The strongest predictor of national murder rates is income inequality","XREF","worldwide","Scatter plot","Crime and Law Enforcement","Kaggle Homicide Rates + Inequality Data + https://www.kaggle.com",90,70,85,90,90,80,85,90),
    mk("xref_warming_vs_prosperity","The Hottest Countries Are the Poorest","Temperature change since 1950 vs prosperity index","XREF","worldwide","Scatter plot","Climate","Kaggle Temperature + Prosperity Data + https://www.kaggle.com",80,65,80,80,80,75,80,85),
    mk("xref_democracy_vs_homicide","Democracies Have Lower Murder Rates","Political regime type vs national homicide rate","XREF","worldwide","Scatter plot","Crime and Law Enforcement","Kaggle Prosperity + Homicide Data + https://www.kaggle.com",80,65,80,80,85,75,80,85),
    mk("xref_oil_price_vs_iran_gas_state","Which States Feel Oil Shocks the Most","State-level gas price sensitivity to Brent crude movements","XREF","us_state","Scatter plot","Energy","Kaggle Iran War Data + https://www.kaggle.com",75,85,80,70,70,75,70,90),
    mk("xref_slavery_vs_unreported_fishing","Modern Slavery Hides in Unreported Fish","Countries with more unreported fishing have higher slavery prevalence","XREF","worldwide","Scatter plot","Crime and Law Enforcement","Kaggle Modern Slavery + Fishing Data + https://www.kaggle.com",85,55,80,90,85,75,90,90),
    mk("xref_meat_slaughter_vs_climate","The Countries Killing the Most Animals Are Warming the Fastest","Animals slaughtered per capita vs temperature change since 1950","XREF","worldwide","Scatter plot","Climate","Kaggle Animals Slaughtered + Temperature + https://www.kaggle.com",80,65,75,85,75,75,85,80),
    mk("xref_student_social_media_vs_gpa","Every Hour on Social Media Costs 0.1 GPA Points","Social media hours vs academic performance in college students","XREF","worldwide","Scatter plot","Education","Kaggle Student Habits + Performance + https://www.kaggle.com",80,90,80,70,65,70,65,90),
    mk("xref_belief_god_vs_income_state","The Poorer the State the More Religious","State-level income vs belief in God","XREF","us_state","Scatter plot","Demographics","Gallup Beliefs + Census Income + https://www.kaggle.com",85,80,80,75,75,75,75,80),
    mk("xref_football_home_advantage_vs_altitude","Does Altitude Explain Home Field Advantage in Football","Win rate at home vs stadium altitude for international venues","XREF","worldwide","Scatter plot","Sports & Recreation","Kaggle Football Results + Elevation Data + https://www.kaggle.com",65,60,75,80,50,70,80,75),
    mk("xref_oil_spike_vs_presidential_approval","Oil Spikes Tank Presidents","Crude oil price shocks vs presidential approval ratings","XREF","us_national","Line chart","Energy","Kaggle Fuel Prices + Gallup Approval + https://www.kaggle.com",80,80,80,80,75,75,75,80),
    mk("xref_asylum_seekers_vs_war_events","War Creates Refugees: Military Ops vs Asylum Applications","US military operations timeline vs USCIS asylum applications","XREF","worldwide","Line chart","Demographics","Kaggle Military Ops + USCIS Asylum Data + https://www.kaggle.com",85,70,80,80,85,80,85,85),

    # ===== ASIA MACRO ECONOMICS =====
    mk("asia_gdp_growth_race","The Asian Economic Miracle in One Chart","GDP growth rates for every Asian country 2000-2024","CHART","asia","Line chart","Economy","Kaggle Asia Macro Economic Dataset + https://www.kaggle.com",70,60,85,70,60,80,65,95),
    mk("asia_fdi_vs_gdp_growth","Foreign Money Fuels Asian Growth","FDI as percent of GDP vs GDP growth rate","XREF","asia","Scatter plot","Economy","Kaggle Asia Macro Economic Dataset + https://www.kaggle.com",65,55,80,70,55,70,65,95),
    mk("asia_debt_vs_growth","Asias Debt Timebomb","External debt vs GDP growth for Asian economies","XREF","asia","Scatter plot","Economy","Kaggle Asia Macro Economic Dataset + https://www.kaggle.com",75,60,80,75,70,70,70,95),

    # ===== FREEDOM INDEX (countries.csv) =====
    mk("world_freedom_trend","The World Is Getting Less Free","Percentage of free vs partly free vs not free countries over time","CHART","worldwide","Area chart","Demographics","Freedom in the World Survey + https://www.kaggle.com",80,70,85,80,80,80,75,90),

    # ===== BONUS: CROSS-PLATFORM COMBOS =====
    mk("xref_iran_gas_spike_vs_ev_sales","Did the Iran War Boost Electric Car Sales","Gas price surge mapped against EV registration trends by state","XREF","us_state","Scatter plot","Energy","Kaggle Iran Gas Prices + DOE EV Registration + https://www.kaggle.com",80,80,75,80,70,70,80,70),
    mk("xref_spotify_country_vs_gdp","Rich Countries Dominate Global Music","GDP per capita vs Spotify streams by artist country of origin","XREF","worldwide","Scatter plot","Entertainment","Kaggle Spotify + World Bank GDP + https://www.kaggle.com",65,60,75,70,55,70,70,80),
    mk("xref_detention_religion_vs_origin","What Religion Are ICE Detainees","Religious demographics inside US immigration detention","CHART","us_national","Bar chart","Demographics","Kaggle ICE Detention Stays + https://www.kaggle.com",70,65,80,75,80,70,75,85),
    mk("oil_price_every_war_annotated","Every War Moved Oil Prices: 1970-2026","Crude oil with every military conflict annotated on the timeline","CHART","worldwide","Line chart","Energy","Kaggle Fuel Prices + Military Ops + https://www.kaggle.com",85,75,85,80,85,85,80,85),
    mk("global_population_vs_meat_slaughter","Humanity Doubled but Meat Killing Quintupled","Population growth vs animal slaughter growth since 1961","XREF","worldwide","Line chart","Food & Nutrition","Kaggle Population + Animals Slaughtered + https://www.kaggle.com",85,70,85,85,80,80,80,90),
]

# ============================================================
# INJECT INTO DATA.JS
# ============================================================

with open(DATA, 'r', encoding='utf-8') as f:
    content = f.read()

# Check for existing IDs (dedupe guard)
existing = set(re.findall(r'id:"([^"]+)"', content))
new_ideas = []
dupes = []
for idea_str in ideas:
    idea_id = re.search(r'id:"([^"]+)"', idea_str).group(1)
    if idea_id in existing:
        dupes.append(idea_id)
    else:
        new_ideas.append(idea_str)
        existing.add(idea_id)

print("Total ideas generated: %d" % len(ideas))
print("Duplicates skipped: %d (%s)" % (len(dupes), ', '.join(dupes)))
print("New ideas to inject: %d" % len(new_ideas))

if new_ideas:
    # Strip the closing marker
    tail = ']; // end D'
    if tail in content:
        content = content[:content.rindex(tail)]
    else:
        content = content.rstrip().rstrip('];').rstrip()

    # Append new ideas
    for idea_str in new_ideas:
        content += '\n' + idea_str + ','

    # Re-add tail
    content += '\n' + tail + '\n'

    with open(DATA, 'w', encoding='utf-8') as f:
        f.write(content)

    print("SUCCESS: Injected %d new ideas into data.js" % len(new_ideas))
    print("Total ideas now: %d" % (len(re.findall(r'id:"', content))))
else:
    print("No new ideas to inject.")

print("\nNow run: & $py maintain.py")
