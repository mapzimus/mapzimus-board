import pandas as pd, numpy as np, re, os

# ============================================================
# DEEP DIVE: Profile each high-value Kaggle dataset
# ============================================================

print("="*60)
print("KAGGLE DATASET DEEP DIVE")
print("="*60)

# 1. GLOBAL HOMICIDE RATES
print("\n--- GLOBAL HOMICIDE RATES (22K rows) ---")
df = pd.read_csv(r"D:\raw_data\kaggle\archive (12)\tassi-di-omicidi-globali-per-paese.csv", encoding='latin-1')
print("Columns:", list(df.columns))
print("Years:", df.year.min(), "-", df.year.max())
print("Countries:", df.country.nunique())
print("Top 10 by latest homicide rate:")
latest = df[df.year == df.year.max()].groupby('country').homicide_rate.mean().nlargest(10)
print(latest.to_string())

# 2. GLOBAL INEQUALITY
print("\n--- GLOBAL INEQUALITY / POVERTY (9K rows) ---")
df2 = pd.read_csv(r"D:\raw_data\kaggle\archive (14)\disuguaglianza-economica-globale-e-povert-1980-2024.csv", encoding='latin-1')
print("Columns:", list(df2.columns))
print("Years:", df2.year.min(), "-", df2.year.max())
print("Top 10 GINI (most unequal, latest year):")
lat2 = df2[df2.year == df2.year.max()].nlargest(10, 'gini_index')[['country','gini_index','income_top1','income_bottom50']]
print(lat2.to_string())

# 3. ICE DETENTION
print("\n--- ICE DETENTION STAYS (672K rows) ---")
df3 = pd.read_csv(r"D:\raw_data\kaggle\archive (16)\detention-stays-latest.csv", nrows=5000, encoding='utf-8')
print("Columns:", list(df3.columns)[:20])
print("Release reasons:", df3.detention_release_reason.value_counts().head(10).to_string())
print("Religions:", df3.religion.value_counts().head(10).to_string())

# 4. GLOBAL PROSPERITY + POLITICS
print("\n--- GLOBAL PROSPERITY vs POLITICAL REGIME (159 rows) ---")
df4 = pd.read_csv(r"D:\raw_data\kaggle\archive (21)\global_prosperity_regions_politics.csv")
print("Columns:", list(df4.columns))
print("Regime types:", df4.political_regime.value_counts().to_string())
print("Top 10 prosperity:")
print(df4.nlargest(10, 'average_score')[['country','political_regime','average_score','personal_freedom','safety_and_security']].to_string())

# 5. ANIMALS SLAUGHTERED
print("\n--- ANIMALS SLAUGHTERED FOR MEAT (14K rows) ---")
df5 = pd.read_csv(r"D:\raw_data\kaggle\archive (23)\land-animals-slaughtered-for-meat.csv")
print("Years:", df5.Year.min(), "-", df5.Year.max())
latest5 = df5[df5.Year == df5.Year.max()].drop(columns=['Code','Year']).set_index('Entity').sum()
print("Global latest totals:")
print(latest5.to_string())

# 6. GLOBAL TEMPERATURE 1950-2024
print("\n--- GLOBAL TEMPERATURE (15K rows) ---")
df6 = pd.read_csv(r"D:\raw_data\kaggle\archive (9)\temperature-medie-annuali-1950-2024.csv", encoding='latin-1')
print("Years:", df6.year.min(), "-", df6.year.max())
print("Countries:", df6.country.nunique())
# Fastest warming countries
warming = df6.groupby('country').apply(lambda g: g.sort_values('year').mean_temperature.iloc[-1] - g.sort_values('year').mean_temperature.iloc[0] if len(g)>10 else np.nan).dropna().nlargest(10)
print("Fastest warming countries (temp change 1950-2024):")
print(warming.to_string())

# 7. FUEL PRICES 1970-2026
print("\n--- CRUDE OIL PRICES (675 rows) ---")
df7 = pd.read_csv(r"D:\raw_data\kaggle\archive (6)\fuel_prices_1970_2026.csv")
print("Date range:", df7.Date.iloc[0], "-", df7.Date.iloc[-1])
print("Price range: $%.2f - $%.2f" % (df7.Crude_Oil_Price.min(), df7.Crude_Oil_Price.max()))

# 8. IRAN WAR + OIL PRICES
print("\n--- IRAN WAR OIL PRICES (24 rows) ---")
df8 = pd.read_csv(r"D:\raw_data\kaggle\irankeyevents\iran_war_oil_prices_daily_2026.csv")
print(df8[['date','brent_usd_barrel','us_gas_avg_gallon','key_event']].to_string())

print("\n--- IRAN WAR GAS PRICES BY STATE (50 rows) ---")
df8b = pd.read_csv(r"D:\raw_data\kaggle\irankeyevents\iran_war_gas_prices_by_state.csv")
print("Top 5 increases:")
print(df8b.nlargest(5, 'pct_increase_since_war')[['state','gas_price_mar19_2026','pct_increase_since_war']].to_string())
print("Bottom 5 increases:")
print(df8b.nsmallest(5, 'pct_increase_since_war')[['state','gas_price_mar19_2026','pct_increase_since_war']].to_string())

# 9. SPOTIFY
print("\n--- SPOTIFY ALL-TIME TOP 100 ---")
df9 = pd.read_csv(r"D:\raw_data\kaggle\spotify\spotify_alltime_top100_songs.csv")
print("Top 10:")
print(df9.head(10)[['alltime_rank','song_title','artist','total_streams_billions','artist_country']].to_string())
print("\nBy country:")
print(df9.groupby('artist_country').total_streams_billions.sum().nlargest(10).to_string())

# 10. RELIGIOUS BELIEFS
print("\n--- RELIGIOUS BELIEFS SURVEY ---")
df10 = pd.read_csv(r"D:\raw_data\kaggle\archive (22)\data-TRrb5.csv")
print(df10.to_string())

# 11. IRAN WAR INCIDENTS
print("\n--- IRAN WAR INCIDENTS (weapon-level detail) ---")
df11 = pd.read_csv(r"D:\raw_data\kaggle\iranwar\incidents.csv", nrows=20)
print("Key columns:", [c for c in df11.columns if any(w in c.lower() for w in ['weapon','missile','drone','intercept','target','casualt','damage'])][:20])

# 12. MODERN SLAVERY
print("\n--- MODERN SLAVERY / FISHING ---")
df12 = pd.read_csv(r"D:\raw_data\kaggle\archive (24)\modern_slavery_final\GIS_2018_report.csv")
print(df12.head(10).to_string())

# 13. FOOTBALL RESULTS
print("\n--- INTERNATIONAL FOOTBALL RESULTS (49K matches) ---")
df13 = pd.read_csv(r"D:\raw_data\kaggle\FBRESULTS26\results.csv")
print("Date range:", df13.date.min(), "-", df13.date.max())
print("Tournaments:", df13.tournament.nunique())
top_winners = df13[df13.home_score > df13.away_score].home_team.value_counts().head(10)
print("Most home wins:", top_winners.to_string())

# 14. STEAM GAMES
print("\n--- STEAM GAMES 2026 (1000 rows) ---")
df14 = pd.read_csv(r"D:\raw_data\kaggle\steam\steam_games_2026.csv")
print("Top 10 by peak players:")
print(df14.nlargest(10, '24h_Peak_Players')[['Name','Primary_Genre','24h_Peak_Players','Review_Score_Pct','Price_USD']].to_string())

# 15. FIFA WORLD RANKINGS
print("\n--- FIFA WORLD RANKINGS JAN 2026 ---")
df15 = pd.read_csv(r"D:\raw_data\kaggle\archive (26)\fifa_world_rankings_jan_2026.csv")
print(df15.head(20).to_string())

# 16. MILITARY OPERATIONS
print("\n--- MILITARY OPERATIONS (290 rows) ---")
df16 = pd.read_csv(r"D:\raw_data\kaggle\archive (28)\Military_Operations_Strategic new.csv")
print("Columns:", list(df16.columns))
print(df16.head(5).to_string())

print("\n" + "="*60)
print("DEEP DIVE COMPLETE")
print("="*60)
