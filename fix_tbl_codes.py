"""
fix_tbl_codes.py
Replace bare ProQuest T-codes with actual source names and locations.
"""
import re

# ── COMPREHENSIVE T-CODE LOOKUP ────────────────────────────────────────────────
# Format: T-code -> "Source Name (url or description)"
TBL = {
# Population PDF
'T6':   'Census Bureau: County population change 1950-2020 (census.gov)',
'T7':   'Census Bureau: Metro vs non-metro population by state (census.gov)',
'T9':   'Census Bureau: Components of population change by state (census.gov)',
'T13':  'Census Bureau: Resident population estimates by state (census.gov)',
'T14':  'Census Bureau: Population projections by state 2025-2050 (census.gov)',
'T15':  'Census Bureau: Population projections by state 2025-2050 (census.gov)',
'T16':  'Census Bureau: Population projections by state 2025-2050 (census.gov)',
'T18':  'Census Bureau: Population characteristics by state (census.gov)',
'T21':  'Census Bureau: Large metropolitan statistical areas (census.gov)',
'T22':  'Census Bureau: Large metropolitan statistical areas (census.gov)',
'T24':  'Census Bureau: Foreign-born population share by metro (census.gov)',
'T26':  'Census Bureau: Income and poverty in large metro areas (census.gov)',
'T28':  'Census Bureau: Cities over 100K — population and land area (census.gov)',
'T79':  'Census Bureau: Net international migration by state (census.gov)',
'T80':  'CDC NCHS: Mean age at first birth by race (wonder.cdc.gov)',
'T81':  'CDC NCHS: Birth rates and fertility rates by state (wonder.cdc.gov)',
'T82':  'CDC NCHS: Birth characteristics by state (wonder.cdc.gov)',
'T85':  'CDC NCHS: Total fertility rate by race (wonder.cdc.gov)',
'T86':  'CDC NCHS: Teen birth rates by state (wonder.cdc.gov)',
'T87':  'CDC NCHS: Births to unmarried mothers by state (wonder.cdc.gov)',
'T92':  'CDC NCHS: Infant mortality rates by state (wonder.cdc.gov)',
'T93':  'CDC NCHS: Maternal mortality rates by state (wonder.cdc.gov)',
'T98':  'CDC NCHS: Death rates by cause and state (wonder.cdc.gov)',
# Health Nutrition PDF
'T100': 'CDC NCHS: Age-adjusted death rates by state (wonder.cdc.gov)',
'T103': 'CDC NCHS: Suicide rates by state (wonder.cdc.gov)',
'T105': 'CDC BRFSS: Chronic disease indicators by state (cdc.gov/brfss)',
'T112': 'CDC NCHS: Drug overdose deaths by state (wonder.cdc.gov)',
'T115': 'NCI SEER: Cancer incidence rates by state (seer.cancer.gov)',
'T116': 'CDC BRFSS: Self-reported health status by state (cdc.gov/brfss)',
'T117': 'CDC BRFSS: Obesity rates by state (cdc.gov/brfss)',
'T141': 'CMS National Health Expenditure Accounts: Per capita health spending by state (cms.gov)',
'T144': 'AMA: Active physicians per 100K by state (ama-assn.org)',
'T145': 'ADA: Dentists per 100K residents by state (ada.org)',
'T148': 'ACS/Census: Health insurance coverage by state (census.gov)',
'T150': 'CMS: Medicare enrollment by state (cms.gov)',
'T154': 'CMS: Nursing home data by state (cms.gov)',
'T157': 'CDC BRFSS: Disability statistics by state (cdc.gov/brfss)',
'T158': 'SAMHSA: Mental health treatment and disorders by state (samhsa.gov)',
'T160': 'UNOS: Organ transplants by state (unos.org)',
'T161': 'CDC NCHS: Cardiovascular disease death rates (wonder.cdc.gov)',
'T164': 'CDC: HIV diagnoses by state (cdc.gov)',
'T166': 'CDC: Sexually transmitted infections by state (cdc.gov)',
'T173': 'SAMHSA: Substance use disorders by state (samhsa.gov)',
'T174': 'SAMHSA: Substance use treatment facilities by state (samhsa.gov)',
'T179': 'CDC: Immunization rates by state (cdc.gov)',
'T183': 'CDC BRFSS: Physical activity rates by state (cdc.gov/brfss)',
'T185': 'CDC BRFSS: Smoking rates by state (cdc.gov/brfss)',
'T190': 'CDC NCHS: Preventable death rates by state (wonder.cdc.gov)',
'T191': 'CDC: Foodborne illness reports (cdc.gov)',
'T193': 'CDC NCHS: Life expectancy by state (wonder.cdc.gov)',
# Education PDF
'T253': 'NCES: Public school enrollment by state (nces.ed.gov)',
'T254': 'ACS/Census: Educational attainment by state (census.gov)',
'T258': 'NCES: Per-pupil expenditure and school revenue by state (nces.ed.gov)',
'T261': 'NCES: Largest school districts by enrollment (nces.ed.gov)',
'T268': 'NCES: Teacher salaries and teacher counts by state (nces.ed.gov)',
'T275': 'College Board: SAT scores by state (collegeboard.org)',
'T276': 'ACT: ACT composite scores by state (act.org)',
'T278': 'NCES IPEDS: College enrollment by state (nces.ed.gov/ipeds)',
'T280': 'NSF/SESTAT: STEM graduate education and stay rates (nsf.gov)',
'T281': 'NCES IPEDS: Graduate school enrollment by state (nces.ed.gov/ipeds)',
'T282': 'NCES IPEDS: 6-year college completion rates by state (nces.ed.gov/ipeds)',
'T283': 'IMLS: Public libraries per capita by state (imls.gov)',
'T287': 'NCES: School finance statistics (nces.ed.gov)',
'T294': 'Census ACS: Computer and internet use by state (census.gov)',
'T295': 'NCES NAEP: Reading and math proficiency by state (nces.ed.gov)',
# Law Enforcement PDF
'T336': 'BJS: Sentenced prisoners by state (bjs.ojp.gov)',
'T338': 'BJS: Prison and jail incarceration rates by state (bjs.ojp.gov)',
'T340': 'FBI UCR: Violent and property crime rates by state (ucr.fbi.gov)',
'T341': 'FBI UCR: Hate crime statistics by state (ucr.fbi.gov)',
'T342': 'BJS/DPIC: Executions by state since 1977 (dpic.org)',
'T344': 'BJS/DPIC: Prisoners under sentence of death by state (dpic.org)',
'T348': 'OJJDP: Juvenile arrests by state (ojjdp.gov)',
'T353': 'BJS: Probation and parole populations by state (bjs.ojp.gov)',
'T358': 'FBI UCR: Law enforcement officers by state (ucr.fbi.gov)',
'T362': 'CBP: Border patrol apprehensions by sector (cbp.gov)',
'T364': 'DHS: Deportations and removals by state (dhs.gov)',
'T368': 'USCIS: Naturalizations by state (uscis.gov)',
'T386': 'State Dept: Visas issued by category (travel.state.gov)',
'T388': 'DHS: Immigration enforcement statistics (dhs.gov)',
'T389': 'TRAC: Immigration court pending cases by state (trac.syr.edu)',
'T391': 'USCIS: Refugee admissions and asylum by state (uscis.gov)',
# Geography Environment PDF
'T408': 'NOAA/Census: Coastline and shoreline miles by state (coast.noaa.gov)',
'T409': 'USGS: Major river lengths and drainage areas (usgs.gov)',
'T410': 'Census Bureau: Mean elevation by state (census.gov)',
'T411': 'USGS: Elevation extremes by state (usgs.gov)',
'T412': 'Census Bureau: Water area by state (census.gov)',
'T413': 'NLCD/USGS: Land cover by state — cropland, forest, developed (mrlc.gov)',
'T414': 'NPS: National Park and public land acreage by state (nps.gov)',
'T415': 'USGS: Irrigation water withdrawal per day by state (usgs.gov)',
'T420': 'NOAA: Climate normals and weather data by state (ncei.noaa.gov)',
'T422': 'NOAA: Annual precipitation and temperature by state (ncei.noaa.gov)',
'T427': 'NOAA: Natural disasters and severe weather events (ncei.noaa.gov)',
'T428': 'FEMA: Disaster declarations by state (fema.gov)',
'T438': 'EPA AQS: Air quality index data by state (epa.gov/aqs)',
'T439': 'EPA: Greenhouse gas emissions by state (epa.gov)',
'T440': 'EPA: Water quality and impaired waters (epa.gov)',
'T441': 'EPA TRI: Toxic Release Inventory by state (epa.gov/tri)',
'T443': 'USDA ERS: Agricultural land area by state (ers.usda.gov)',
'T448': 'USGS: Water use and withdrawals by state (usgs.gov)',
# Elections PDF
'T449': 'MIT Election Lab + Census CPS: Voter turnout and registration by state (electionlab.mit.edu)',
'T454': 'MIT Election Lab: Presidential and congressional election results (electionlab.mit.edu)',
# State Local Government PDF
'T486': 'Census of Governments: State and local debt per capita (census.gov/govs)',
'T488': 'Census of Governments: State and local revenue and expenditures per capita (census.gov/govs)',
'T490': 'Census of Governments: State government revenue by source (census.gov/govs)',
'T491': 'Census of Governments: Property tax collections by state (census.gov/govs)',
'T492': 'Census of Governments: State expenditures by function (census.gov/govs)',
'T493': 'NASPL: State lottery and sports betting revenue by state (naspl.org)',
'T495': 'NASBO: State general fund balance and surplus/deficit (nasbo.org)',
'T497': 'Census of Governments: State individual income tax revenue (census.gov/govs)',
'T500': 'Census of Governments: State infrastructure and capital spending (census.gov/govs)',
'T505': 'BLS OES: State and local government average earnings by state (bls.gov)',
# Federal Government PDF
'T509': 'Treasury/OMB: Federal debt as % of GDP 1960-2024 (fiscaldata.treasury.gov)',
'T510': 'OMB: Federal budget overview (whitehouse.gov/omb)',
'T512': 'OMB: Federal budget outlays by function (whitehouse.gov/omb)',
'T513': 'Treasury IRS: Federal tax receipts by source (irs.gov)',
'T532': 'IRS Statistics of Income: Average AGI per return by state (irs.gov/statistics)',
'T533': 'IRS: Federal tax refunds by state (irs.gov/statistics)',
'T534': 'IRS: Unclaimed tax refunds by state (irs.gov/statistics)',
'T535': 'IRS Data Book: Audit rates by income level (irs.gov/statistics)',
'T537': 'OPM FedScope: Federal civilian employment by state (fedscope.opm.gov)',
'T543': 'DoD / SIPRI: Total US defense budget 1940-2024 (comptroller.defense.gov)',
'T545': 'DoD: Active duty military personnel by year and branch (dmdc.osd.mil)',
'T547': 'DoD: Retired military personnel and pension payments by state (dmdc.osd.mil)',
'T548': 'DoD: Military deaths by conflict and cause (dmdc.osd.mil)',
'T549': 'DoD: US military personnel stationed overseas by country (dmdc.osd.mil)',
'T550': 'DoD: National Guard strength by state (nationalguard.mil)',
'T551': 'DoD: Reserve forces by component and state (dmdc.osd.mil)',
'T552': 'DoD: Military installations and personnel by state (dmdc.osd.mil)',
'T553': 'DoD: Defense contracts and spending by state (usaspending.gov)',
'T557': 'VA: Veterans benefits and services by state (va.gov)',
'T568': 'GSA: Federal property and real estate by state (gsa.gov)',
# Social Insurance PDF
'T573': 'BEA/Census: Government transfer payments per capita by state (bea.gov)',
'T574': 'SSA: Social Security benefits paid by state (ssa.gov)',
'T575': 'SSA: Disability insurance beneficiaries by state (ssa.gov)',
'T576': 'USDA FNS + CMS: SNAP and Medicaid enrollment by state (fns.usda.gov / cms.gov)',
'T577': 'USDA FNS: Total SNAP households and participants (fns.usda.gov)',
'T579': 'HHS ACF: TANF (cash welfare) recipients by state (acf.hhs.gov)',
'T581': 'HHS OCSE: Child support enforcement statistics by state (acf.hhs.gov)',
'T582': 'HHS ACF: Child welfare and foster care statistics (acf.hhs.gov)',
'T586': 'HHS ACF: Head Start enrollment by state (acf.hhs.gov)',
'T588': 'USDA FNS: WIC (Women Infants Children) participation by state (fns.usda.gov)',
'T598': 'CMS: Medicare and Medicaid expenditures by state (cms.gov)',
'T613': 'SSA: Retirement and disability beneficiaries by state (ssa.gov)',
'T617': 'BLS/BEA: Unemployment insurance compensation by state (bls.gov)',
'T621': 'NCCI/DoL: Workers compensation by state (dol.gov)',
'T626': 'BLS: Labor force participation rate with disability by state (bls.gov)',
'T629': 'BLS LAUS: Unemployment rate and labor force by state (bls.gov/lau)',
'T630': 'BLS LAUS: Unemployment rates by metro area (bls.gov/lau)',
'T642': 'BLS OES: Occupational employment and wages by state (bls.gov/oes)',
'T643': 'BLS: Union membership and coverage rates by state (bls.gov)',
'T647': 'BLS: Work stoppages and strikes by industry (bls.gov)',
'T650': 'BLS NCS: Employee benefits by industry (bls.gov/ncs)',
'T651': 'BLS: Employment cost index (bls.gov)',
'T652': 'BLS: Labor productivity and unit labor costs (bls.gov)',
'T653': 'BLS CES: Employment by industry and state (bls.gov/ces)',
'T655': 'BLS QCEW: Quarterly employment and wages by state and industry (bls.gov/qcew)',
'T656': 'BLS JOLTS: Job openings and labor turnover by state (bls.gov/jlt)',
'T664': 'BLS SOII: Occupational safety and injury rates by state (bls.gov)',
# Income Poverty PDF
'T712': 'BEA Regional Economic Accounts: Industry share of GDP by state (apps.bea.gov)',
'T715': 'BEA Regional Economic Accounts: GDP per capita by state and metro (apps.bea.gov)',
'T717': 'BEA: Personal income by component and state (apps.bea.gov)',
'T720': 'BEA: Personal income by source and state (apps.bea.gov)',
'T723': 'BEA: Real per capita personal income by state (apps.bea.gov)',
'T725': 'BEA: Disposable personal income per capita by state (apps.bea.gov)',
'T726': 'BEA + ACS: Per capita income by metro area (apps.bea.gov)',
'T727': 'ACS/Census: Household income distribution by state (census.gov)',
'T731': 'Census SPM/ACS: Poverty rates by race and state (census.gov)',
'T732': 'Census: Official poverty thresholds and measures (census.gov)',
'T736': 'Census ACS: Gini income inequality coefficient by state (census.gov)',
'T739': 'Census ACS: Poverty rates by age group and state (census.gov)',
'T751': 'USDA ERS: Food insecurity rates by state (ers.usda.gov)',
'T754': 'HUD: Housing affordability and cost burden by state (huduser.gov)',
'T756': 'Census ACS: Homeownership rates by state and race (census.gov)',
'T767': 'Census ACS: Asset ownership and wealth by state (census.gov)',
# Prices PDF
'T769': 'BLS CPI: Housing CPI by major metropolitan area (bls.gov/cpi)',
'T770': 'BLS CPI: Consumer Price Index by expenditure category (bls.gov/cpi)',
'T771': 'FHFA House Price Index: Home prices and % change by state (fhfa.gov)',
'T772': 'NAR: Existing home sales and median price by state (nar.realtor)',
'T773': 'EIA + AAA: Retail gasoline prices by metropolitan area (eia.gov)',
'T775': 'BLS PPI: Producer Price Index by commodity (bls.gov/ppi)',
'T777': 'BLS: Import and export price indices (bls.gov)',
'T793': 'IRS + BEA: Corporate profits before tax and income taxes (bea.gov / irs.gov)',
'T794': 'IRS Data Book: Corporate and individual audit rates by income (irs.gov/statistics)',
'T800': 'BLS ECI: Employment Cost Index (bls.gov)',
'T806': 'BLS: Compensation in manufacturing by state (bls.gov)',
'T808': 'BLS OES: Wage growth by occupation category (bls.gov/oes)',
'T810': 'DoL: Federal and state minimum wage history (dol.gov/whd)',
'T812': 'BLS OES + Census: Earnings by education level (bls.gov/oes)',
'T816': 'Census ACS: Median earnings by age and gender (census.gov)',
'T818': 'Census ACS + BLS: Median earnings by occupation and state (census.gov)',
# Science Technology PDF
'T841': 'NSF: Science and engineering degrees conferred by state (nsf.gov)',
'T842': 'NSF + OECD: R&D expenditure as % of GDP by country (nsf.gov)',
'T844': 'NSF: Federal R&D budget by agency (nsf.gov)',
'T845': 'NSF + NIH: Biotech and health R&D funding by state (nsf.gov / nih.gov)',
'T846': 'USPTO: Patent applications and grants by state (patents.google.com / uspto.gov)',
'T848': 'NSF: STEM workforce and employment by state (nsf.gov)',
'T849': 'NSF: Science and technology statistics (nsf.gov)',
'T855': 'NSF: Research and development statistics (nsf.gov)',
'T858': 'FCC + NTIA: Broadband and internet access by state (fcc.gov / ntia.gov)',
'T860': 'NSF: R&D performance by sector (nsf.gov)',
# Agriculture PDF
'T869': 'USDA NASS Census of Agriculture: Farm statistics by state (nass.usda.gov)',
'T871': 'USDA NASS: Farm sales and income by size class (nass.usda.gov)',
'T872': 'USDA NASS: Farm operator demographics by state (nass.usda.gov)',
'T873': 'USDA ERS: Net farm income and cash receipts by state (ers.usda.gov)',
'T879': 'USDA NASS: Crop production value by state (nass.usda.gov)',
'T880': 'USDA NASS: Harvested acreage by principal crop and state (nass.usda.gov)',
'T882': 'USDA NASS: Crop prices received by farmers by state (nass.usda.gov)',
'T891': 'USDA ERS: Food expenditures by household and channel (ers.usda.gov)',
'T895': 'USDA FNS: School nutrition program participation by state (fns.usda.gov)',
'T900': 'USDA NASS: Corn production by state (nass.usda.gov)',
'T902': 'USDA NASS: Soybean production by state (nass.usda.gov)',
'T904': 'USDA NASS: Wheat production by state and type (nass.usda.gov)',
'T906': 'USDA NASS: Cotton production by state (nass.usda.gov)',
'T908': 'USDA NASS: Dairy cows and milk production by state (nass.usda.gov)',
'T910': 'USDA NASS: Cattle and hog inventory by state (nass.usda.gov)',
'T920': 'USDA NASS: Poultry production by state (nass.usda.gov)',
'T930': 'USDA NASS: Certified organic farm sales by state (nass.usda.gov)',
'T932': 'USDA Forest Service: National Forest acreage by state (fs.usda.gov)',
'T933': 'USDA Forest Service: Forestry output statistics (fs.usda.gov)',
'T934': 'USDA Forest Service: Timber harvest by state (fs.usda.gov)',
'T935': 'USDA Forest Service: Forest health statistics (fs.usda.gov)',
'T941': 'USGS: Mineral production value by state (usgs.gov/minerals)',
'T942': 'USGS: Mineral commodities summary by state (usgs.gov/minerals)',
'T944': 'NOAA Fisheries: Commercial fish landings by species (fisheries.noaa.gov)',
'T945': 'NOAA Fisheries: Commercial fish landings by port (fisheries.noaa.gov)',
'T948': 'NOAA: Aquaculture production and value (fisheries.noaa.gov)',
'T949': 'USGS + BLS: Mining employment and production by state (usgs.gov)',
# Energy PDF
'T950': 'EIA: Coal, oil, and gas production indices by state (eia.gov)',
'T954': 'EIA: Coal production and mines by state (eia.gov)',
'T955': 'EIA: Crude oil production by state (eia.gov)',
'T960': 'EIA: Natural gas production by state (eia.gov)',
'T962': 'EIA: Natural gas proven reserves by state (eia.gov)',
'T966': 'EIA: Petroleum refinery operations (eia.gov)',
'T971': 'NRC + EIA: Nuclear generating units and capacity by state (nrc.gov / eia.gov)',
'T973': 'EIA: Electric net generation by energy source and state (eia.gov)',
'T975': 'EIA SEDS: Energy consumption per capita by state (eia.gov/seds)',
'T976': 'EIA SEDS: Renewable energy and fossil fuel share by state (eia.gov/seds)',
'T977': 'EIA: Energy prices by fuel type and state (eia.gov)',
'T978': 'EIA + FHWA: Motor fuel consumption by state (eia.gov)',
'T984': 'EIA: Energy-related carbon emissions by state (eia.gov)',
'T990': 'EIA: Electric power industry generation and sales (eia.gov)',
'T991': 'EIA: Residential electricity rates by state (eia.gov)',
'T994': 'EIA: Energy efficiency and consumption trends (eia.gov)',
'T999': 'EIA: Renewable energy generating capacity by state (eia.gov)',
# Construction PDF
'T1011': 'Census Bureau: New residential housing permits by state (census.gov)',
'T1013': 'Census Bureau Construction: Spending by sector (census.gov/construction)',
'T1016': 'Census Bureau: Housing starts by region (census.gov)',
'T1017': 'Census Bureau: Housing completions and under construction (census.gov)',
'T1023': 'NAR + Census: Existing and new home sales by state (nar.realtor)',
'T1025': 'FHFA + Zillow: Home price index changes by state (fhfa.gov)',
'T1028': 'HUD: Housing affordability and cost burden index (huduser.gov)',
'T1034': 'Census: Rental and homeowner vacancy rates by state (census.gov)',
'T1039': 'CBRE + CoStar: Commercial real estate statistics (cbre.com)',
'T1041': 'Census: Manufactured and mobile housing by state (census.gov)',
'T1044': 'Census: Housing units by structure type and state (census.gov)',
'T1045': 'Census ACS: Housing characteristics and conditions (census.gov)',
# Manufactures PDF
'T1052': 'Census ASM: Manufacturing industry overview by state (census.gov/asm)',
'T1062': 'Census ASM: Manufacturing value added and payroll by state (census.gov/asm)',
'T1063': 'Census ASM: Manufacturing shipments value by state (census.gov/asm)',
'T1064': 'BLS QCEW: Manufacturing employment 2000-2024 by state (bls.gov/qcew)',
'T1067': 'BLS OES: Manufacturing hourly wages by state (bls.gov/oes)',
'T1083': 'Census: Merchant wholesaler sales and inventories (census.gov)',
'T1084': 'Census + BLS: Wholesale and retail trade employment by state (census.gov)',
'T1090': 'Census: Per capita retail sales by state (census.gov)',
'T1093': 'Census: E-commerce retail sales by category (census.gov)',
'T1096': 'FHWA: Highway mileage by state and functional system (fhwa.dot.gov)',
# Transportation PDF
'T1100': 'FTA National Transit Database: Transit ridership by agency (ntd.fta.dot.gov)',
'T1103': 'Census Nonemployer Statistics: Gig/app-based transport by state (census.gov)',
'T1110': 'BTS T-100: Airport on-time arrival and departure rates (bts.gov)',
'T1112': 'BTS T-100: Passengers enplaned by airport (bts.gov)',
'T1118': 'FAA: General aviation aircraft by state (faa.gov)',
'T1120': 'USACE: Waterway freight tonnage by waterway (usace.army.mil)',
'T1122': 'USACE: Port tonnage (domestic, foreign, total) by port (usace.army.mil)',
'T1123': 'USACE: Container port traffic in TEUs by port (usace.army.mil)',
'T1124': 'PHMSA: Pipeline mileage by state and type (phmsa.dot.gov)',
'T1126': 'FHWA: Structurally deficient bridge rate by state (fhwa.dot.gov)',
'T1128': 'NHTSA FARS: Traffic fatalities and rates by state (nhtsa.gov/fars)',
'T1130': 'NHTSA FARS: Alcohol-impaired driving fatalities by state (nhtsa.gov/fars)',
'T1139': 'NHTSA: Motor vehicle safety data by state (nhtsa.gov)',
'T1144': 'Census ACS: Commuting patterns and travel time by state (census.gov)',
'T1148': 'BTS Freight Analysis: Freight movement by mode and state (bts.gov)',
'T1151': 'AAR: Railroad statistics by state (aar.org)',
'T1152': 'Amtrak + FRA: Passenger rail ridership and on-time performance (amtrak.com / fra.dot.gov)',
'T1156': 'MARAD: Marine transportation statistics (maritime.dot.gov)',
'T1169': 'FAA: Air traffic control and operations statistics (faa.gov)',
# Information Communications PDF
'T1174': 'NAA + Pew Research: Newspaper revenue, employment, and closures (newspapers.org)',
'T1178': 'FCC: Broadband deployment and access by state (fcc.gov)',
'T1184': 'CTIA: Mobile phone subscriptions and wireless statistics (ctia.org)',
'T1187': 'FCC: Telephone service statistics by state (fcc.gov)',
'T1189': 'Census ACS: Computer and internet access by state (census.gov)',
'T1194': 'IAB + eMarketer: Digital advertising revenue by format (iab.com)',
'T1195': 'RIAA + IFPI: Music industry streaming and revenue (riaa.com)',
'T1196': 'FDIC: Bank branches by state and county (fdic.gov)',
'T1200': 'FDIC: Failed bank list 1934-present (fdic.gov/bank/individual/failed)',
'T1202': 'NCUA: Credit union membership and assets by state (ncua.gov)',
# Banking Finance PDF
'T1207': 'Federal Reserve Survey of Consumer Finances: Family financial asset ownership (federalreserve.gov/scf)',
'T1211': 'Federal Reserve: Flow of Funds — financial accounts of the US (federalreserve.gov)',
'T1222': 'Federal Reserve G.19: Consumer credit outstanding by type (federalreserve.gov)',
'T1223': 'Federal Reserve: Consumer credit interest rates by loan type (federalreserve.gov)',
'T1224': 'Federal Reserve: Mortgage debt outstanding by holder (federalreserve.gov)',
'T1225': 'MBA + FFIEC: Mortgage delinquency and foreclosure rates by state (mba.org)',
'T1226': 'FDIC + CFPB: Payday and consumer lending by state (cfpb.gov)',
'T1227': 'FDIC: Commercial bank summary statistics by state (fdic.gov)',
'T1236': 'FDIC: Commercial bank loan portfolios and performance (fdic.gov)',
'T1237': 'Federal Reserve: Reserve requirements and monetary policy data (federalreserve.gov)',
'T1246': 'Pew Charitable Trusts + NASRA: State pension funding ratios (pewtrusts.org)',
# Arts Recreation PDF
'T1259': 'Broadway League: Annual Broadway attendance and gross revenue (broadwayleague.com)',
'T1262': 'NEA + BEA: Arts and cultural production and participation (arts.gov)',
'T1263': 'SFIA: Sports and fitness participation rates by activity (sfia.org)',
'T1264': 'Outdoor Industry Association + BEA: Outdoor recreation economy by state (outdoorindustry.org)',
'T1267': 'Harris Poll + SFIA: Social and recreation participation statistics (harrispoll.com)',
'T1271': 'AECOM + TEA: Theme park annual attendance worldwide (aecom.com)',
'T1272': 'MLB + NBA + NFL + NHL: Professional sports team attendance (mlb.com)',
'T1273': 'SFIA + Harris Poll: Attendance at sports and live events (sfia.org)',
'T1274': 'NCAA: College sports revenue and attendance by conference (ncaa.org)',
'T1278': 'AAA: Motor vehicle recreation and travel statistics (aaa.com)',
'T1280': 'Harvard T.H. Chan School of Public Health: Gun ownership rates by state (hsph.harvard.edu)',
'T1281': 'NFHS: High school sports participation by state and sport (nfhs.org)',
'T1290': 'US Travel Association: Travel and tourism spending by state (ustravel.org)',
'T1291': 'STR: Hotel occupancy and RevPAR by market (str.com)',
'T1293': 'US Travel Association: Domestic and international visitor statistics (ustravel.org)',
# Foreign Commerce PDF
'T1303': 'USITC + Census: US trade by commodity category (usitc.gov)',
'T1305': 'Census: US exports by destination country (census.gov/foreign-trade)',
'T1306': 'BEA: Balance of payments and current account (bea.gov)',
'T1307': 'BEA: US trade in services by category (bea.gov)',
'T1309': 'BEA: Balance on services by category (bea.gov)',
'T1310': 'Census + BEA: Trade balance on goods by country (census.gov/foreign-trade)',
'T1311': 'BEA: Employment at foreign-owned US affiliates by state (bea.gov)',
'T1318': 'Census: Leading export commodity by state (census.gov/foreign-trade)',
'T1320': 'Census: Exports by state and destination country (census.gov/foreign-trade)',
'T1322': 'Census: Imports by state and origin country (census.gov/foreign-trade)',
'T1325': 'BEA: Foreign direct investment in the US by country (bea.gov)',
'T1332': 'Census + BEA: International trade data (census.gov)',
'T1338': 'World Bank + UN DESA: International birth and vital statistics by country (data.worldbank.org)',
'T1340': 'UN Population Division: Population by age group by country (population.un.org)',
'T1342': 'UN + World Bank: Urban population and urbanization by country (data.worldbank.org)',
'T1344': 'IMF + World Bank: GDP and GNI per capita at PPP by country (data.worldbank.org)',
'T1346': 'IMF + World Bank: Real GDP growth rates and inflation by country (imf.org)',
'T1352': 'IEA + EIA: Energy production, consumption, and CO2 by country (iea.org)',
'T1354': 'World Steel Association: Steel production by country (worldsteel.org)',
'T1356': 'OICA: Motor vehicle production and sales by country (oica.net)',
'T1358': 'UNCTAD: Merchant fleet by country and flag state (unctad.org)',
'T1360': 'UN DESA + World Bank: Net migration rate by country (data.worldbank.org)',
'T1362': 'IMF: Foreign exchange and gold reserves by country (imf.org)',
'T1364': 'World Bank: External debt stocks by country (data.worldbank.org)',
'T1365': 'World Bank: Trade openness — trade as % of GDP by country (data.worldbank.org)',
'T1366': 'IMF + World Bank: Consumer price index and inflation by country (imf.org)',
'T1367': 'WHO + World Bank: Health statistics by country (who.int)',
'T1368': 'UNESCO + OECD: Educational attainment and literacy by country (uis.unesco.org)',
'T1370': 'WHO + World Bank: Health expenditure per capita by country (who.int)',
'T1374': 'FAO + Global Forest Watch: Forest area and deforestation rates (globalforestwatch.org)',
'T1376': 'SIPRI: Arms transfer volumes by supplier and recipient (sipri.org)',
'T1377': 'SIPRI: Military expenditure by country (sipri.org)',
'T1378': 'IISS Military Balance: Armed forces personnel by country (iiss.org)',
'T1379': 'World Bank: International development indicators (data.worldbank.org)',
'T1380': 'World Prison Brief + ICPS: Prison population rates by country (prisonstudies.org)',
'T1381': 'World Bank: Development and governance indicators (data.worldbank.org)',
'T1382': 'UNHCR: Refugees and displaced persons by country of origin (unhcr.org)',
'T1383': 'UNHCR: Asylum seekers and refugee determinations by country (unhcr.org)',
'T1385': 'UNESCO + OECD: Education spending as % of GDP by country (uis.unesco.org)',
'T1392': 'ITU: Internet users and telecommunications by country (itu.int)',
'T1401': 'WIPO: Patent applications by origin country (wipo.int)',
'T1402': 'WTO: Merchandise trade statistics by country (wto.org)',
}

def resolve_tbl(tbl_raw):
    """Replace T-codes in a tbl string with descriptive source names."""
    parts = re.split(r'\s*[-–—|+]\s*', tbl_raw)
    resolved = []
    for part in parts:
        part = part.strip()
        # Pure T-code match (e.g. "T454", "T1126")
        if re.fullmatch(r'T\d+', part):
            if part in TBL:
                resolved.append(TBL[part])
            else:
                resolved.append(part)  # keep unknown codes as-is
        else:
            # Has a T-code prefix but also descriptive text
            # e.g. "T1063 Manufactures PDF + Federal Reserve..."
            # Replace any T-codes in it
            def sub_code(m):
                code = m.group(0)
                return TBL.get(code, code)
            part_resolved = re.sub(r'T\d+', sub_code, part)
            # Remove leftover PDF category labels since we have real names now
            part_resolved = re.sub(
                r'\b(Health Nutrition|Education|Law Enforcement|Geography|Elections|'
                r'State Local Government|Federal Government|Social Insurance|'
                r'Income Poverty|Prices|Science Technology|Agriculture|Forestry Fishing Mining|'
                r'Forestry Mining|Energy|Construction|Manufactures|Wholesale Retail|'
                r'Transportation|Information Communications|Banking Finance|Arts Recreation Travel|'
                r'Arts Recreation|Foreign Commerce|International Statistics|National Security|'
                r'Metropolitan Areas|Population|Banking|Health Births|Income|Health) PDF\b',
                '', part_resolved
            ).strip().strip('+- ').strip()
            if part_resolved:
                resolved.append(part_resolved)

    # Join multiple sources with " + "
    joined = ' + '.join(r for r in resolved if r)
    # Clean up double spaces and stray punctuation
    joined = re.sub(r'\s{2,}', ' ', joined).strip()
    return joined

# ── APPLY TO DATA.JS ───────────────────────────────────────────────────────────
with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
new_lines = []
changed = 0

for line in lines:
    if not (line.startswith(',{id:') or line.startswith('{id:')):
        new_lines.append(line)
        continue

    tbl_m = re.search(r',tbl:"([^"]+)"', line)
    if not tbl_m:
        new_lines.append(line)
        continue

    tbl_orig = tbl_m.group(1)

    # Only process if it contains a T-code
    if not re.search(r'T\d', tbl_orig):
        new_lines.append(line)
        continue

    tbl_new = resolve_tbl(tbl_orig)

    if tbl_new and tbl_new != tbl_orig:
        line = line[:tbl_m.start(1)] + tbl_new + line[tbl_m.end(1):]
        changed += 1

    new_lines.append(line)

with open(r'D:\projects\mapzimus-board\data.js','w',encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print('Done. tbl fields updated: %d' % changed)

# Spot-check 10 examples
import random
sample = [(l, re.search(r',tbl:"([^"]+)"', l)) for l in new_lines
          if l.startswith(',{id:') and re.search(r',tbl:"([^"]+)"', l)]
random.shuffle(sample)
print('\nSample of updated tbl fields:')
for line, m in sample[:12]:
    id_m = re.search(r'id:"([^"]+)"', line)
    print('  [%s]' % (id_m.group(1) if id_m else '?'))
    print('   -> %s' % m.group(1)[:100])
    print()
