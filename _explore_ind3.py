import csv, sys, os
sys.stdout = open(r"D:\projects\mapzimus-board\_ind_results.txt", "w", encoding="utf-8")
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
    sys.stdout.write(f"\n{fname}: {len(indicators)} indicators\n")
    for ind in sorted(indicators):
        sys.stdout.write(f"  {ind}\n")
sys.stdout.close()
