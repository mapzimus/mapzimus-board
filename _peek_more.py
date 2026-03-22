import csv
files = [
    (r"D:\raw_data\Kaggle\archive (35)\historysaid-global-economic-dataset\data\unified\all_indicators.csv", 3),
    (r"D:\raw_data\Kaggle\archive (35)\historysaid-global-economic-dataset\data\aggregates\regional_aggregates.csv", 3),
    (r"D:\raw_data\Kaggle\pop\popolazione-globale-per-paese-1950-2024.csv", 3),
]
for fp, n in files:
    try:
        with open(fp, encoding="utf-8", errors="replace") as fh:
            r = csv.reader(fh)
            for i in range(n):
                row = next(r, None)
                if i == 0:
                    import os
                    print(f"=== {os.path.basename(fp)} ===")
                    print(f"  HDR: {row[:20]}")
                else:
                    print(f"  R{i}: {row[:20] if row else None}")
            print()
    except Exception as e:
        print(f"ERR: {e}")
