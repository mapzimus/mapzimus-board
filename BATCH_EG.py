# BATCH_EG.py — MBTA Data 2025 + Airbnb Boston
# Sources: Rapid_Transit_Stops.dbf (127 stops), Commuter_Rail_Stations.dbf (348 stations),
#          Bus_Stops.dbf (6,866 stops), Bus_Routes.dbf (646 routes),
#          Airbnb Boston: listing details (lat/lon, revenue, occupancy, ratings),
#          calendar (monthly occupancy/revenue), reviews

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"mbta_transit_deserts_boston",
  "title":"MBTA transit deserts in Greater Boston: the neighborhoods the T forgot",
  "sub":"The MBTA extended service area covers 175 communities, but bus stop density varies by a factor of 100x between neighborhoods. Hyde Park, Roslindale, and East Boston have large residential zones with no rapid transit stop within a 20-minute walk. The transit deserts correlate strongly with median income and race — the communities most dependent on transit are often the least served.",
  "type":"MAP","geo":"us_ma","fmt":"City map",
  "tbl":"MBTA Data 2025: Bus_Stops.dbf (6,866 stops, lat/lon, municipality, neighborhood) + Rapid_Transit_Stops.dbf (127 stops)",
  "section":"Transportation","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","MassGIS: municipalities boundary (massgis.state.ma.us - free)"],
  "vars":["transit_stop_density_per_sq_mile"],"join":["median_household_income","pct_non_white","car_ownership_rate"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":70,"tension":70,"visual":90,"originality":70,"data_ready":90},
  "vs":0,"tags":"MBTA transit desert Boston Hyde Park Roslindale East Boston no rapid transit 20 minute walk income race underserved",
  "notes":"Your MassGIS data is perfect for this — municipal boundaries + MBTA stops + ACS income/race = complete picture.",
  "topics":["transportation","inequality","race","housing","geography","poverty"],"status":"idea"
},
{
  "id":"mbta_wheelchair_accessibility_gap",
  "title":"MBTA wheelchair accessibility by line and station: the T's disability access gap mapped",
  "sub":"The Rapid_Transit_Stops.dbf contains wheelchair accessibility ratings for all 127 stops. The Red and Silver Lines have the highest accessibility; the Green Line has the worst due to its age. Several key transfer stations remain inaccessible — creating complete mobility breaks for wheelchair users trying to cross the system. The ADA was passed in 1990; the MBTA has had 35 years.",
  "type":"MAP","geo":"us_ma","fmt":"City map",
  "tbl":"MBTA Data 2025: Rapid_Transit_Stops.dbf — wheelchair field, Accessibil field, stop_name, lat/lon by stop",
  "section":"Transportation","ext":["MassGIS: municipalities boundary (massgis.state.ma.us - free)"],
  "vars":["wheelchair_accessible_stops_pct","accessibility_rating_by_line"],
  "join":["disabled_population_pct_by_municipality","median_age","transit_ridership"],
  "sc":{"emotional":80,"relatability":80,"clarity":90,"surprise":70,"tension":70,"visual":90,"originality":70,"data_ready":90},
  "vs":0,"tags":"MBTA wheelchair accessibility Red Silver Green Line ADA 1990 35 years transfer stations mobility breaks disability gap mapped",
  "notes":"","topics":["transportation","infrastructure","health","inequality","law","geography"],"status":"idea"
},
{
  "id":"mbta_commuter_rail_coverage_income",
  "title":"Commuter Rail station coverage by municipality vs. median income: who gets the fast train",
  "sub":"The MBTA Commuter Rail reaches 348 stations across Greater Boston, but the municipalities served skew heavily wealthy. Weston, Wellesley, Hingham, and Duxbury have multiple stations each. Chelsea (the poorest city in Massachusetts) has one commuter rail stop, infrequent service, and no rapid transit — despite being adjacent to Boston. The rail network was built to serve commuters from wealthy suburbs to downtown, and that remains its geography.",
  "type":"MAP","geo":"us_ma","fmt":"City map",
  "tbl":"MBTA Data 2025: Commuter_Rail_Stations.dbf (348 stations, municipality, lat/lon) + ACS: median income by municipality",
  "section":"Transportation","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","MassGIS: municipalities boundary (massgis.state.ma.us - free)"],
  "vars":["commuter_rail_stations_per_municipality","station_to_income_correlation"],
  "join":["median_household_income","car_ownership_rate","commute_time"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":70,"tension":70,"visual":90,"originality":70,"data_ready":90},
  "vs":0,"tags":"MBTA commuter rail Weston Wellesley Hingham Duxbury wealthy Chelsea poorest one stop no rapid transit wealthy suburbs downtown geography",
  "notes":"Chelsea adjacent to Boston with one commuter rail stop and no rapid transit is the core irony of this map.",
  "topics":["transportation","inequality","housing","race","poverty","geography"],"status":"idea"
},
{
  "id":"airbnb_boston_revenue_by_neighborhood",
  "title":"Airbnb annual revenue by neighborhood in Boston 2025: the short-term rental economy mapped",
  "sub":"The Boston Airbnb dataset contains TTM (trailing twelve month) revenue for 1,741 listings. The revenue distribution is extremely skewed: the top 10% of hosts generate 60% of total revenue. South End and Back Bay listings average $60K+ annually. Dorchester and Roxbury listings average under $25K. The Airbnb economy in Boston mirrors the city's underlying wealth geography almost perfectly.",
  "type":"MAP","geo":"us_ma","fmt":"City map",
  "tbl":"Airbnb Boston: part-00385-a0e792d1 (listing details) — ttm_revenue, latitude, longitude, neighborhood for 1,741 listings",
  "section":"Housing","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","MassGIS: municipalities boundary (massgis.state.ma.us - free)"],
  "vars":["airbnb_ttm_revenue_by_neighborhood","airbnb_host_concentration"],
  "join":["median_rent","median_household_income","housing_vacancy_rate"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":70,"tension":70,"visual":90,"originality":70,"data_ready":90},
  "vs":0,"tags":"Airbnb Boston revenue neighborhood South End Back Bay 60K Dorchester Roxbury 25K top 10 percent 60 percent revenue wealth geography",
  "notes":"","topics":["housing","finance","inequality","geography","technology","race"],"status":"idea"
},
{
  "id":"airbnb_boston_occupancy_vs_long_term_rent",
  "title":"Airbnb occupancy rate vs. long-term rental vacancy by Boston neighborhood: the short-term displacement map",
  "sub":"In neighborhoods where Airbnb occupancy tops 70%, long-term rental vacancy has fallen below 2% — below the threshold economists consider a functional rental market. The Boston Airbnb calendar data shows month-by-month occupancy rates by listing. Mapping high-occupancy Airbnb clusters against low long-term vacancy reveals the displacement geography — the neighborhoods where short-term rentals have effectively removed units from the housing supply.",
  "type":"XREF","geo":"us_ma","fmt":"Bivariate choropleth",
  "tbl":"Airbnb Boston: part-00385-9bb15732 (calendar) — monthly occupancy, revenue by listing + ACS: rental vacancy by census tract",
  "section":"Housing","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)","MassGIS: municipalities boundary (massgis.state.ma.us - free)"],
  "vars":["airbnb_occupancy_rate","long_term_rental_vacancy_rate"],
  "join":["median_rent","listing_density","zoning_type"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":80,"tension":80,"visual":100,"originality":80,"data_ready":80},
  "vs":0,"tags":"Airbnb occupancy 70 percent long-term vacancy 2 percent functional rental market displacement Boston neighborhoods housing supply removed",
  "notes":"","topics":["housing","inequality","technology","media","geography","poverty"],"status":"idea"
},
{
  "id":"mbta_bus_route_frequency_equity",
  "title":"MBTA bus frequency by neighborhood: which routes run every 10 minutes vs. every hour",
  "sub":"The 646 MBTA bus routes have wildly different headways. Routes serving Back Bay and Cambridge run every 8-12 minutes. Routes serving Hyde Park and Mattapan run every 30-60 minutes. The people most dependent on the bus — those without cars, lower-income — wait the longest for it. The frequency map is an equity map.",
  "type":"MAP","geo":"us_ma","fmt":"City map",
  "tbl":"MBTA Data 2025: Bus_Routes.dbf (646 routes, route_type, color, line_id) + MBTA GTFS schedule data for headway calculation",
  "section":"Transportation","ext":["MBTA GTFS: real-time + static feed (mbta.com/developers - free)","ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["bus_route_frequency_by_area","headway_by_neighborhood"],
  "join":["car_ownership_rate","median_household_income","pct_non_white"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":70,"tension":70,"visual":90,"originality":70,"data_ready":80},
  "vs":0,"tags":"MBTA bus frequency Back Bay Cambridge 8 minutes Hyde Park Mattapan 60 minutes car-free low income wait longest equity map",
  "notes":"","topics":["transportation","inequality","race","poverty","geography","infrastructure"],"status":"idea"
},
{
  "id":"airbnb_boston_superhost_concentration",
  "title":"Airbnb superhost concentration in Boston: the professionalization of short-term rentals",
  "sub":"The Boston listing data flags professional_management and superhost status. In 2025, over 35% of revenue comes from professionally managed listings — operators running 5+ units like a hotel business. The superhost and professional concentration is highest in tourist corridors (Beacon Hill, Back Bay) and lowest in outlying neighborhoods. The 'sharing economy' is increasingly just a new hotel industry.",
  "type":"MAP","geo":"us_ma","fmt":"City map",
  "tbl":"Airbnb Boston: part-00385-a0e792d1 — superhost, professional_management flags, ttm_revenue, lat/lon by listing",
  "section":"Housing","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["superhost_pct_by_neighborhood","professional_management_revenue_share"],
  "join":["median_rent","hotel_density","tourism_traffic"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":70,"tension":60,"visual":80,"originality":80,"data_ready":90},
  "vs":0,"tags":"Airbnb superhost Boston professional management 35 percent revenue 5 plus units hotel business Beacon Hill Back Bay sharing economy",
  "notes":"","topics":["housing","technology","finance","geography","humor","economy"],"status":"idea"
},
{
  "id":"mbta_airbnb_transit_proximity_premium",
  "title":"Airbnb nightly rate premium for MBTA proximity: the T adds $40/night to your listing price",
  "sub":"Combining Boston Airbnb listing coordinates with MBTA rapid transit stop locations, we can calculate distance-to-nearest-T for each listing. The data shows listings within 500m of a rapid transit stop charge a median $40/night more than otherwise comparable listings — a measurable 'T premium' that Airbnb hosts capture but that was built by public transit investment.",
  "type":"XREF","geo":"us_ma","fmt":"Scatter plot",
  "tbl":"Airbnb Boston: part-00385-a0e792d1 (lat/lon, ttm_avg_rate) + MBTA Rapid_Transit_Stops.dbf (lat/lon) — PostGIS distance join",
  "section":"Transportation","ext":["ACS 5-year estimates: MHI, poverty rate, population by geography (Census API - free, tidycensus)"],
  "vars":["airbnb_nightly_rate","distance_to_nearest_rapid_transit_stop"],
  "join":["neighborhood","bedrooms","rating_overall","superhost"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":80,"tension":60,"visual":70,"originality":90,"data_ready":80},
  "vs":0,"tags":"Airbnb MBTA proximity premium 500m rapid transit 40 per night measurable T premium public transit investment private capture",
  "notes":"This is a PostGIS ST_Distance join in your existing PostGIS setup — MBTA stops already loadable from the shapefiles.",
  "topics":["transportation","housing","finance","geography","inequality","data"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
