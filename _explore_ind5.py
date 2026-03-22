import csv, os

out = open(r"C:\Users\mhowe\Documents\_ind_results.txt", "w", encoding="utf-8")
BASE = r"D:\raw_data\kaggle\archive (35)\historysaid-global-economic-dataset\data\core"

for fname in ["imf_weo.csv", "world_bank_wgi.csv"]:
    fp = os.path.join(BASE, fname)
    indicators = set()
    with open(fp, encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            ind_name = row.get("indicator_name", "")
            ind_id = row.get("indicator_id", "")
            indicators.add(f"{ind_id} | {ind_name}")
            if i > 100000:
                break
    out.write(f"{fname}: {len(indicators)} indicators\n")
    for ind in sorted(indicators):
        out.write(f"  {ind}\n")
    out.write("\n")

# World Bank sample
fp = os.path.join(BASE, "world_bank.csv")
indicators = set()
with open(fp, encoding="utf-8", errors="replace") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        indicators.add(f"{row.get('indicator_id','')} | {row.get('indicator_name','')}")
        if i > 80000:
            break
out.write(f"world_bank.csv (80k sample): {len(indicators)} indicators\n")
for ind in sorted(indicators):
    out.write(f"  {ind}\n")

out.close()
print("DONE")
