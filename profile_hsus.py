import warnings
warnings.filterwarnings("ignore")
import pandas as pd, os

out = []
def p(s): out.append(s)

hsus_dir = r"D:\raw_data\HSUS\A-Population"
p("=== HSUS A-Population ===")

for root, dirs, files in os.walk(hsus_dir):
    for fn in sorted(files):
        if fn.endswith((".csv", ".xls", ".xlsx")):
            fp = os.path.join(root, fn)
            rel = os.path.relpath(fp, hsus_dir)
            p("\n[%s]" % rel)
            try:
                if fn.endswith(".csv"):
                    df = pd.read_csv(fp, nrows=5, encoding="utf-8", on_bad_lines="skip")
                else:
                    df = pd.read_excel(fp, nrows=5)
                p("  cols: %s" % str(list(df.columns)[:10]))
                nrows = len(pd.read_csv(fp, encoding="utf-8", on_bad_lines="skip")) if fn.endswith(".csv") else "?"
                p("  rows: %s" % str(nrows))
            except:
                try:
                    df = pd.read_csv(fp, nrows=5, encoding="latin-1", on_bad_lines="skip")
                    p("  cols: %s" % str(list(df.columns)[:10]))
                except Exception as e:
                    p("  ERROR: %s" % str(e)[:60])

# Also check Pew and ProQuest
pew_dir = r"D:\raw_data\Pew"
if os.path.exists(pew_dir):
    p("\n=== PEW ===")
    for fn in sorted(os.listdir(pew_dir)):
        fp = os.path.join(pew_dir, fn)
        sz = os.path.getsize(fp)
        p("  %s (%.0fKB)" % (fn, sz/1024))

pq_dir = r"D:\raw_data\ProQuest Statistical Abstract"
if os.path.exists(pq_dir):
    p("\n=== PROQUEST STATISTICAL ABSTRACT ===")
    for fn in sorted(os.listdir(pq_dir)):
        p("  %s" % fn)

with open(r"D:\projects\mapzimus-board\profile_hsus.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Done. %d lines" % len(out))
