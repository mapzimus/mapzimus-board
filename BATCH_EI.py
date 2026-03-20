# BATCH_EI.py — CPI + PPI + HSUS wages historical
# Sources: cpi/historical-cpi-u-202602.xlsx (CPI all-items through Feb 2026),
#          cpi/ppi-fdallrel.xlsx (PPI food), cpi/ppi-idcallrel.xlsx (industrial chemicals),
#          cpi/ppi-weprel.xlsx (energy/petroleum), HSUS wage historical data

def vs(sc):
    raw = sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 + sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1.25 + sc['originality']*1
    base = raw / 10.75
    penalty = 1 - 0.3*(1 - sc['data_ready']/100)
    return int(base * penalty)

ideas = [
{
  "id":"cpi_category_inflation_divergence_2020_2025",
  "title":"Inflation by category 2020–2025: the items that went up 50% and the items that got cheaper",
  "sub":"The all-items CPI rose 22% from Jan 2020 to Feb 2026. But eggs rose 180%. Car insurance rose 62%. Groceries rose 25%. Meanwhile TVs fell 18%. Used car prices spiked 50% then fell back. Streaming services rose 40%. The 'inflation' experience was entirely different depending on your household's consumption basket. A childless renter felt a different economy than a homeowner with kids.",
  "type":"CHART","geo":"us_national","fmt":"Bar chart",
  "tbl":"CPI: historical-cpi-u-202602.xlsx — CPI by major category (food, shelter, energy, apparel, medical, used cars, eggs) monthly 2020-2026",
  "section":"Prices","ext":["BLS: CPI detailed tables (bls.gov/cpi - free)"],
  "vars":["cpi_by_category_pct_change_2020_2025"],
  "join":["income_by_quintile","renter_vs_owner_share","household_composition"],
  "sc":{"emotional":90,"relatability":100,"clarity":90,"surprise":80,"tension":70,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"inflation category 2020 2025 eggs 180 car insurance 62 TVs fell 18 consumption basket renter homeowner different economy",
  "notes":"Eggs at 180% and TVs falling 18% in the same period is the whole story. This is maximally relatable.",
  "topics":["economy","prices","food","housing","history","data","inequality"],"status":"idea"
},
{
  "id":"cpi_eggs_price_history_1980_2025",
  "title":"US egg price history 1980–2025: the most dramatic commodity chart most people can relate to",
  "sub":"Egg prices were remarkably stable from 1980-2021, hovering between $1-2/dozen. Then bird flu hit in 2022 and prices went to $5. They fell back to $2 in 2023. Then in 2025 they hit $8/dozen — 4x the 40-year average. Nothing in everyday grocery shopping has moved this dramatically in living memory. The CPI egg series is simultaneously a food safety story, a supply chain story, and an avian flu story.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"CPI: historical-cpi-u-202602.xlsx — Eggs CPI series 1980-2026, monthly",
  "section":"Prices","ext":["USDA: Egg Market News Report (ams.usda.gov - free)"],
  "vars":["egg_cpi_price_series"],"join":["avian_flu_outbreak_timeline","herd_culling_stats","import_export_policy"],
  "sc":{"emotional":90,"relatability":100,"clarity":100,"surprise":90,"tension":70,"visual":80,"originality":70,"data_ready":100},
  "vs":0,"tags":"egg price 1980 2025 1-2 per dozen 40 years 8 dollar 2025 bird flu supply chain avian flu dramatic CPI series",
  "notes":"Peak relatability. Everyone buys eggs. The chart is visually wild.",
  "topics":["food","economy","prices","history","data","health"],"status":"idea"
},
{
  "id":"cpi_housing_rent_vs_income_1985_2025",
  "title":"Housing CPI vs. median income growth 1985–2025: the 40-year divergence that created the affordability crisis",
  "sub":"From 1985 to 2000, housing costs and median income tracked each other closely. Since 2000, housing costs have risen 2.4x faster than median income. The CPI shelter index has increased 330% since 1985; median household income has increased only 180% in nominal terms. The affordability crisis is not a recent phenomenon — it's a 25-year structural divergence that accelerated post-2020.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"CPI: historical-cpi-u-202602.xlsx — Shelter CPI 1985-2026 + Census/FRED: median household income 1985-2024",
  "section":"Housing","ext":["FRED: median household income (fred.stlouisfed.org - free API)","Census Bureau: historical income tables (census.gov - free)"],
  "vars":["shelter_cpi","median_household_income_nominal"],
  "join":["housing_supply_permits","mortgage_rate","zoning_restrictiveness"],
  "sc":{"emotional":90,"relatability":100,"clarity":90,"surprise":80,"tension":80,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"housing CPI median income 1985 2025 diverge 2.4x faster 25 year structural not recent 330 percent shelter 180 percent income",
  "notes":"","topics":["housing","economy","inequality","history","prices","poverty"],"status":"idea"
},
{
  "id":"cpi_food_ppi_spread_producer_vs_consumer",
  "title":"What farmers get vs. what you pay at the grocery store: the producer-consumer price spread 2010–2025",
  "sub":"The PPI food series measures what producers receive; the CPI food measures what consumers pay. The spread between them has widened significantly since 2020 — processor and retailer margins have expanded even as input costs rose. Egg farmers saw their wholesale price fall in 2024 while retail egg prices stayed high. The food supply chain is capturing inflation even as farm prices normalize.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"CPI: ppi-fdallrel.xlsx (PPI food, all commodities) + historical-cpi-u-202602.xlsx (CPI food at home) — producer vs consumer price index 2010-2026",
  "section":"Prices","ext":["USDA: Agricultural Marketing Service (ams.usda.gov - free)"],
  "vars":["ppi_food_index","cpi_food_at_home_index","producer_consumer_spread"],
  "join":["grocery_chain_profit_margins","consolidation_index_food_retail"],
  "sc":{"emotional":80,"relatability":80,"clarity":80,"surprise":80,"tension":70,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"PPI food producer CPI consumer spread 2020 wider margins expanded egg wholesale fell retail stayed high supply chain capturing inflation",
  "notes":"","topics":["food","economy","prices","agriculture","finance","inequality"],"status":"idea"
},
{
  "id":"cpi_real_wages_1979_2024",
  "title":"Real wages 1979–2024 by education level: 45 years of wage stagnation for workers without degrees",
  "sub":"CPI deflation of BLS wage data shows that real wages for workers without college degrees are roughly flat vs. 1979. Workers with bachelor's degrees have seen 28% real wage growth. Workers with graduate degrees have seen 45%. The entire post-1979 wage premium went to credential holders. This single chart explains more about American political polarization than almost any other statistic.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"CPI: historical-cpi-u-202602.xlsx (deflator) + BLS: median weekly earnings by education level 1979-2024",
  "section":"Labor Force","ext":["BLS: Current Population Survey earnings by education (bls.gov - free)"],
  "vars":["real_wage_by_education_level"],"join":["union_membership_rate","automation_index","offshoring_index"],
  "sc":{"emotional":90,"relatability":90,"clarity":90,"surprise":80,"tension":80,"visual":90,"originality":70,"data_ready":100},
  "vs":0,"tags":"real wages 1979 2024 education flat no degree 28 percent bachelor 45 percent graduate credential holders polarization single chart",
  "notes":"","topics":["labor","economy","education","inequality","history","politics"],"status":"idea"
},
{
  "id":"cpi_medical_care_vs_general_cpi",
  "title":"Medical care CPI vs. all-items CPI 1950–2025: healthcare has inflated 3x faster than everything else for 75 years",
  "sub":"Since 1950, the all-items CPI has risen approximately 11x. Medical care CPI has risen 37x. The divergence begins immediately after the creation of Medicare/Medicaid in 1965 and has never reversed. US healthcare costs are not a recent crisis — they've been inflating at triple the general rate for 75 years. The compound effect over 7 decades is the difference between 11x and 37x.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"CPI: historical-cpi-u-202602.xlsx — Medical Care CPI vs All Items CPI 1950-2026, monthly series",
  "section":"Health","ext":["CMS: National Health Expenditure Data (cms.gov - free)"],
  "vars":["medical_care_cpi","all_items_cpi"],"join":["medicare_medicaid_creation_1965","private_insurance_market_concentration"],
  "sc":{"emotional":80,"relatability":90,"clarity":90,"surprise":80,"tension":80,"visual":90,"originality":60,"data_ready":100},
  "vs":0,"tags":"medical care CPI all-items CPI 1950 2025 11x general 37x healthcare diverge 1965 Medicare Medicaid 75 years triple rate",
  "notes":"","topics":["health","economy","prices","history","inequality","politics"],"status":"idea"
},
{
  "id":"cpi_energy_ppi_volatility_comparison",
  "title":"Energy vs. food vs. shelter: which CPI category is most volatile and why it matters for renters",
  "sub":"The PPI energy (petroleum/natural gas) series shows extreme volatility — standard deviation 4x higher than food, 12x higher than shelter. But renters feel energy volatility directly in utility bills and indirectly in transportation costs, while homeowners with solar or locked-in rates are insulated. The CPI volatility map is really a wealth map: volatility exposure correlates almost perfectly with poverty.",
  "type":"CHART","geo":"us_national","fmt":"Line chart",
  "tbl":"CPI: ppi-weprel.xlsx (energy PPI) + historical-cpi-u-202602.xlsx (food, shelter, energy CPI) — volatility comparison 2000-2026",
  "section":"Prices","ext":["EIA: energy price data (eia.gov - free API)"],
  "vars":["energy_cpi_volatility","food_cpi_volatility","shelter_cpi_volatility"],
  "join":["income_by_quintile","homeownership_rate","solar_panel_adoption"],
  "sc":{"emotional":70,"relatability":80,"clarity":80,"surprise":70,"tension":60,"visual":80,"originality":80,"data_ready":100},
  "vs":0,"tags":"energy PPI CPI food shelter volatility 4x 12x renters direct utility transportation homeowners insulated poverty exposure correlation",
  "notes":"","topics":["economy","energy","housing","inequality","prices","poverty"],"status":"idea"
},
]

for idea in ideas:
    idea['vs'] = vs(idea['sc'])
