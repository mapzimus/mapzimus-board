import csv, os
files = [
    r"D:\raw_data\Kaggle\archive (34)\tsm_master_dataset.csv",
    r"D:\raw_data\Kaggle\archive (36)\monthly.csv",
    r"D:\raw_data\Kaggle\archive (37)\enhanced_global_trends_dataset.csv",
    r"D:\raw_data\Kaggle\archive (38)\breakfast basket.csv",
    r"D:\raw_data\Kaggle\archive (40)\ai_index_main.csv",
    r"D:\raw_data\Kaggle\archive (42)\AI_Job_Market_Trends_2026.csv",
    r"D:\raw_data\Kaggle\archive (43)\MCD.csv",
    r"D:\raw_data\Kaggle\archive (44)\richest_people_dataset.csv",
    r"D:\raw_data\Kaggle\archive (47)\asteroid_dataset_20251019.csv",
    r"D:\raw_data\Kaggle\archive (49)\BTC_prices.csv",
    r"D:\raw_data\Kaggle\archive (50)\uap_reports.csv",
    r"D:\raw_data\Kaggle\mentalburnout\student_mental_health_burnout.csv",
    r"D:\raw_data\Kaggle\spotify\spotify_alltime_top100_songs.csv",
    r"D:\raw_data\Kaggle\steam\steam_games_2026.csv",
    r"D:\raw_data\Kaggle\irankeyevents\iran_war_key_events_timeline.csv",
    r"D:\raw_data\Kaggle\iranwar\iran_war_gas_prices_by_state.csv",
    r"D:\raw_data\Kaggle\archive (39)\iran_war_gas_prices_by_state.csv",
    r"D:\raw_data\Kaggle\archive (41)\fuel_prices_2000_2026.csv",
    r"D:\raw_data\Kaggle\archive (48)\fuel_prices_1970_2026.csv",
]
for fp in files:
    try:
        with open(fp, encoding="utf-8", errors="replace") as fh:
            r = csv.reader(fh)
            hdr = next(r, None)
            row1 = next(r, None)
            print(f"=== {os.path.basename(fp)} ===")
            print(f"  HDR: {hdr[:15] if hdr else None}")
            print(f"  R1:  {row1[:15] if row1 else None}")
            print()
    except Exception as e:
        print(f"ERR {fp}: {e}")
