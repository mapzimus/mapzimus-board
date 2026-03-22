import csv, os

out = open(r"C:\Users\mhowe\Documents\_ind_results2.txt", "w", encoding="utf-8")
BASE = r"D:\raw_data\kaggle\archive (35)"

for fname in ["imf_weo.csv", "world_bank_wgi.csv"]:
    fp = os.path.join(BASE, fname)
    if not os.path.exists(fp):
        out.write(f"SKIP: {fname}\n")
        continue
    indicators = set()
    with open(fp, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            ind_name = row.get("indicator_name", "")
            ind_id = row.get("indicator_id", "")
            indicators.add(f"{ind_id} | {ind_name}")
            if i > 100000:
                break
    out.write(f"\n{fname}: {len(indicators)} indicators\n")
    for ind in sorted(indicators):
        out.write(f"  {ind}\n")

# World Bank - just get first 50000 rows
fp = os.path.join(BASE, "world_bank.csv")
indicators = set()
with open(fp, encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        ind_name = row.get("indicator_name", "")
        ind_id = row.get("indicator_id", "")
        indicators.add(f"{ind_id} | {ind_name}")
        if i > 50000:
            break
out.write(f"\nworld_bank.csv (sample 50k rows): {len(indicators)} indicators\n")
for ind in sorted(indicators):
    out.write(f"  {ind}\n")

out.close()
print("DONE")
