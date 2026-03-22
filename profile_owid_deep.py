import warnings
warnings.filterwarnings("ignore")
import pandas as pd, os, re

out = []
def p(s): out.append(s)

owid_dir = r"D:\raw_data\Our World In Data"

# Profile all extracted directories (contain CSVs from unzipped files)
dirs = sorted([d for d in os.listdir(owid_dir) if os.path.isdir(os.path.join(owid_dir, d))])
p("OWID extracted directories: %d" % len(dirs))

for d in dirs:
    dp = os.path.join(owid_dir, d)
    csvs = [f for f in os.listdir(dp) if f.endswith(".csv")]
    if csvs:
        for csv_fn in csvs[:2]:  # max 2 CSVs per dir
            fp = os.path.join(dp, csv_fn)
            try:
                df = pd.read_csv(fp, nrows=5)
                p("\n[%s/%s]" % (d[:50], csv_fn[:40]))
                p("  cols: %s" % str(list(df.columns)[:8]))
                # Count full rows
                nrows = sum(1 for _ in open(fp, encoding="utf-8")) - 1
                p("  ~%d rows" % nrows)
            except Exception as e:
                p("\n[%s/%s] ERROR: %s" % (d[:50], csv_fn[:40], str(e)[:50]))

with open(r"D:\projects\mapzimus-board\profile_owid_deep.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Done. %d lines -> profile_owid_deep.txt" % len(out))
