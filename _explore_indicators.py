"""Quick exploration of unique indicators in archive_35 datasets."""
import csv, os, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"D:\raw_data\kaggle\archive (35)"

for fname in ["world_bank.csv", "imf_weo.csv", "bis.csv", "world_bank_wgi.csv"]:
    fp = os.path.join(BASE, fname)
    if not os.path.exists(fp):
        continue
    indicators = {}
    with open(fp, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            ind = row.get("indicator_name","")
            iid = row.get("indicator_id","")
            if ind not in indicators:
                indicators[ind] = iid
            if i > 200000:
                break
    print(f"\n{'='*60}")
    print(f"  {fname}: {len(indicators)} unique indicators")
    print(f"{'='*60}")
    for name, iid in sorted(indicators.items()):
        print(f"  {iid}: {name}")
