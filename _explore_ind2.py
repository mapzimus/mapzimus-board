import csv, sys, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
BASE = r"D:\raw_data\kaggle\archive (35)"
for fname in ["world_bank.csv", "imf_weo.csv", "world_bank_wgi.csv"]:
    fp = os.path.join(BASE, fname)
    if not os.path.exists(fp):
        continue
    indicators = set()
    with open(fp, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            indicators.add(row.get("indicator_name","")[:80])
            if i > 200000:
                break
    print(f"\n{fname}: {len(indicators)} indicators")
    for ind in sorted(indicators):
        print(f"  {ind}")
