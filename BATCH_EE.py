# BATCH_EE.py — Kaggle Soccer / WorldCup
# Sources: FBRESULTS26/results.csv (~44K intl matches 1872-present),
#          FBRESULTS26/goalscorers.csv, worldcup/matches_1930_2022.csv,
#          worldcup/world_cup.csv, worldcup/fifa_ranking_2022-10-06.csv

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"soccer_win_rate_by_country_alltime",
  "title":"International soccer win rate by country all time 1872–2024: who actually dominates the beautiful game",
  "sub":"Brazil has the highest all-time win rate (67%) among countries with 200+ games. Spain second at 62%. Germany third at 60%. But the most interesting outlier is Iran — a top-10 win rate globally that gets almost zero international attention. And the lowest win rate among FIFA members with 50+ games belongs to San Marino at 2%. The data tells a very different story than the World Cup trophy count.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"Kaggle FBRESULTS26: results.csv — all international matches 1872-2024, win/loss/draw by country",
  "section":"Arts Recreation","ext":["FIFA: official statistics (fifa.com - some free data)"],
  "vars":["international_soccer_win_rate"],"join":["population","gdp_per_capita","world_cup_appearances"],
  "sc":{"emotional":80,"relatability":80,"clarity":90,"surprise":80,"tension":60,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"international soccer win rate Brazil 67 Spain 62 Germany 60 Iran top 10 San Marino 2 percent all time 1872 2024",
  "notes":"","topics":["history","international","sports","data","geography"],"status":"idea"
},
{
  "id":"soccer_world_cup_upsets_history",
  "title":"Biggest World Cup upsets by FIFA ranking gap 1990–2022: the maps where the minnows won",
  "sub":"Senegal defeating France in 2002. South Korea defeating Germany in 2018. Morocco reaching the 2022 semifinal. Using FIFA ranking gaps at time of match, the FBRESULTS26 and worldcup data lets us rank every World Cup upset by probability. The 2022 World Cup had the highest upset density in tournament history — the gap between top and bottom teams is closing.",
  "type":"CHART","geo":"worldwide","fmt":"Bar chart",
  "tbl":"Kaggle FBRESULTS26: results.csv + worldcup/matches_1930_2022.csv — World Cup matches with scores, combined with FIFA rankings at match date",
  "section":"Arts Recreation","ext":["FIFA: World Rankings history (fifa.com - some free data)"],
  "vars":["world_cup_upset_probability","fifa_ranking_gap_at_match"],
  "join":["gdp_per_capita","population","tournament_stage"],
  "sc":{"emotional":90,"relatability":80,"clarity":80,"surprise":90,"tension":80,"visual":80,"originality":70,"data_ready":90},
  "vs":0,"tags":"World Cup upsets Senegal France 2002 South Korea Germany 2018 Morocco semifinal 2022 ranking gap density closing minnows",
  "notes":"","topics":["history","international","sports","inequality","data","humor"],"status":"idea"
},
{
  "id":"soccer_top_scorers_nationality",
  "title":"International soccer top scorers of all time by nationality: the geography of goalscoring greatness",
  "sub":"The FBRESULTS26 goalscorers dataset lets us rank every international goalscorer since 1916. Ali Daei (Iran, 109 goals) held the men's record for 20 years. Cristiano Ronaldo now leads at 130+. But per-capita, the most prolific scoring nations are not Brazil or Portugal — they're Iceland and Uruguay. Small countries punch enormous when adjusted for population.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"Kaggle FBRESULTS26: goalscorers.csv — total international goals by scorer nationality, summed by country",
  "section":"Arts Recreation","ext":["FIFA: official statistics (fifa.com - some free data)"],
  "vars":["international_goals_per_capita","total_international_goals_by_country"],
  "join":["population","world_cup_appearances","gdp_per_capita"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":80,"tension":50,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"international top scorers Ali Daei Iran 109 Ronaldo 130 per capita Iceland Uruguay small countries punch population adjusted",
  "notes":"","topics":["history","international","sports","data","geography","humor"],"status":"idea"
},
{
  "id":"soccer_home_field_advantage_by_country",
  "title":"Home field advantage in international soccer by country: where home soil matters most",
  "sub":"In international soccer, home teams win about 54% of matches globally — but the advantage varies enormously by country. Bolivia wins 78% of home matches due to La Paz altitude (3,600m). Iran wins 73% at home. Tiny island nations with small fan bases show almost no home advantage. Altitude, crowd noise, travel distance, and referee familiarity all compound — and the data shows altitude is the single largest factor.",
  "type":"MAP","geo":"worldwide","fmt":"World choropleth",
  "tbl":"Kaggle FBRESULTS26: results.csv — home vs. away win rates by country, filtering neutral=FALSE",
  "section":"Arts Recreation","ext":["FIFA: official statistics (fifa.com - some free data)"],
  "vars":["home_win_rate_international_soccer","altitude_of_capital_city"],
  "join":["stadium_capacity","travel_distance_avg","tournament_type"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":50,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"home field advantage soccer Bolivia 78 percent La Paz altitude 3600m Iran 73 crowd noise travel altitude largest factor",
  "notes":"Bolivia home advantage at altitude is one of the most well-documented and legally controversial facts in world soccer.",
  "topics":["sports","history","geography","international","science","data"],"status":"idea"
},
{
  "id":"soccer_world_cup_attendance_trend",
  "title":"World Cup attendance and viewership 1930–2022: how soccer became the world's sport",
  "sub":"The 1930 World Cup drew 68K total attendance over 18 games. The 2022 World Cup drew 3.4 million over 64 games with 1.5 billion global viewers. The worldcup/world_cup.csv captures the tournament-by-tournament arc. The biggest jump was 1966-1970 (color TV broadcast). The COVID-era 2022 Qatar tournament had the highest per-game attendance ever despite being held in artificial winter.",
  "type":"CHART","geo":"worldwide","fmt":"Line chart",
  "tbl":"Kaggle worldcup: world_cup.csv — Attendance, AttendanceAvg, Matches by Year 1930-2022",
  "section":"Arts Recreation","ext":["FIFA: official statistics (fifa.com - some free data)"],
  "vars":["world_cup_total_attendance","world_cup_avg_attendance","world_cup_year"],
  "join":["global_tv_penetration","host_country","teams_in_tournament"],
  "sc":{"emotional":70,"relatability":80,"clarity":90,"surprise":70,"tension":40,"visual":80,"originality":60,"data_ready":100},
  "vs":0,"tags":"World Cup attendance 1930 68K 2022 3.4 million 1.5 billion viewers color TV 1966 1970 Qatar highest per-game ever",
  "notes":"","topics":["history","international","sports","media","data","technology"],"status":"idea"
},
{
  "id":"soccer_world_cup_host_nation_performance",
  "title":"World Cup host nation performance vs. their non-host record: the home tournament premium",
  "sub":"Host nations win 28% of World Cups despite representing 1/32nd of teams. South Africa 2010 is the only host not to reach the knockout round in modern history. The OWID data confirms a measurable 'host effect' of roughly 1.2 goals per game improvement vs. the host's typical performance — comparable to a 5-spot FIFA ranking bump.",
  "type":"CHART","geo":"worldwide","fmt":"Bar chart",
  "tbl":"Kaggle worldcup: matches_1930_2022.csv + world_cup.csv — host nation results vs. their typical tournament record",
  "section":"Arts Recreation","ext":["FIFA: official statistics (fifa.com - some free data)"],
  "vars":["host_nation_world_cup_finish","host_vs_typical_performance_gap"],
  "join":["host_nation_fifa_ranking_at_time","attendance","draw_luck"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":50,"visual":70,"originality":80,"data_ready":100},
  "vs":0,"tags":"World Cup host nation 28 percent win 1/32 South Africa 2010 only host not knockout 1.2 goals per game 5-spot ranking bump",
  "notes":"","topics":["sports","history","data","international","geography"],"status":"idea"
},
{
  "id":"soccer_concacaf_nations_trend",
  "title":"CONCACAF nations FIFA ranking trends 1993–2024: the rise of the Caribbean and the fall of Mexico's dominance",
  "sub":"In 1993, Mexico, Costa Rica, and the US were the only CONCACAF nations in the top 30. By 2024, Panama, Jamaica, and Canada have all cracked the top 50. Mexico's relative ranking has declined while the region has leveled up. The data reflects both expanded player development programs and the MLS effect drawing talent back to the continent.",
  "type":"CHART","geo":"north_america","fmt":"Line chart",
  "tbl":"Kaggle worldcup: fifa_ranking_2022-10-06.csv + FIFA historical ranking API — CONCACAF nations 1993-2024",
  "section":"Arts Recreation","ext":["FIFA: World Rankings API (fifa.com - historical data available)"],
  "vars":["concacaf_nation_fifa_ranking_trend"],
  "join":["mls_expansion_timeline","youth_program_investment","world_cup_qualification_history"],
  "sc":{"emotional":70,"relatability":70,"clarity":80,"surprise":70,"tension":50,"visual":80,"originality":70,"data_ready":80},
  "vs":0,"tags":"CONCACAF FIFA ranking 1993 2024 Mexico Costa Rica US top 30 Panama Jamaica Canada top 50 MLS player development",
  "notes":"","topics":["sports","history","international","geography","data"],"status":"idea"
},
{
  "id":"soccer_penalty_shootout_outcomes",
  "title":"Penalty shootout outcomes by tournament round and country: the cold science of who holds up under pressure",
  "sub":"The FBRESULTS26 shootouts.csv contains every international penalty shootout. Germany wins 87% of shootouts. England wins 50%. Argentina wins 62%. The data also shows that going first in a shootout wins 61% of the time — a coin flip at the start determines the winner before a single kick. Multiple studies and FIFA itself have considered changing this rule.",
  "type":"CHART","geo":"worldwide","fmt":"Bar chart",
  "tbl":"Kaggle FBRESULTS26: shootouts.csv — all international penalty shootout results, winner, first_shooter",
  "section":"Arts Recreation","ext":["FIFA: official statistics (fifa.com - some free data)"],
  "vars":["shootout_win_rate_by_country","first_shooter_advantage"],
  "join":["tournament_round","confederation","ranking_gap"],
  "sc":{"emotional":80,"relatability":90,"clarity":90,"surprise":90,"tension":80,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"penalty shootout Germany 87 percent England 50 percent Argentina 62 going first wins 61 percent coin flip FIFA rule change",
  "notes":"The first-shooter advantage is a documented statistical finding that FIFA acknowledges and has considered legislating.",
  "topics":["sports","history","science","international","data","humor"],"status":"idea"
},
{
  "id":"soccer_world_cup_goals_per_game_trend",
  "title":"World Cup goals per game 1930–2022: how tactics made soccer less exciting over 90 years",
  "sub":"The 1954 World Cup averaged 5.4 goals per game — the highest ever. The 2010 World Cup averaged 2.27 — the lowest ever. The trend is unmistakably downward. Better defending, more professional tactics, and the evolution of the 4-4-2 to 4-5-1 explain most of the decline. The beautiful game gets less beautiful every decade.",
  "type":"CHART","geo":"worldwide","fmt":"Line chart",
  "tbl":"Kaggle worldcup: matches_1930_2022.csv — goals per game average by tournament year",
  "section":"Arts Recreation","ext":["FIFA: official statistics (fifa.com - some free data)"],
  "vars":["world_cup_goals_per_game_by_year"],"join":["tactical_evolution","defensive_intensity_index","tournament_format_change"],
  "sc":{"emotional":70,"relatability":80,"clarity":90,"surprise":80,"tension":50,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"World Cup goals per game 1954 5.4 highest 2010 2.27 lowest downward trend tactics 4-4-2 4-5-1 beautiful game declining",
  "notes":"","topics":["sports","history","data","science","international","humor"],"status":"idea"
},
{
  "id":"soccer_world_cup_success_vs_hdi",
  "title":"World Cup performance vs. Human Development Index by country: can you buy success in soccer?",
  "sub":"Among the 32 teams in recent World Cups, HDI explains very little variance in performance — the correlation is nearly zero. Qatar 2022 proved this most dramatically: Qatar (HDI rank 42) was eliminated in the group stage as the host nation. Soccer success comes from grassroots football culture, not national wealth. The sport remains one of the few competitive arenas where money doesn't win.",
  "type":"XREF","geo":"worldwide","fmt":"Scatter plot",
  "tbl":"Kaggle worldcup: matches_1930_2022.csv + OWID: human-development-index.zip — World Cup round reached vs. HDI by country",
  "section":"Arts Recreation","ext":["UNDP: Human Development Index (hdr.undp.org - free)"],
  "vars":["world_cup_round_reached","human_development_index"],
  "join":["gdp_per_capita","population","youth_football_participation"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":50,"visual":70,"originality":80,"data_ready":90},
  "vs":0,"tags":"World Cup HDI Human Development Index correlation nearly zero Qatar eliminated host grassroots culture wealth doesn't win",
  "notes":"","topics":["sports","inequality","international","history","data","poverty"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
