import warnings
warnings.filterwarnings("ignore")
import pandas as pd, numpy as np, os, re, sys

with open(r"D:\projects\mapzimus-board\data.js", encoding="utf-8") as f:
    raw = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
out = []
def p(s): out.append(s)

p("EXISTING IDEAS: %d" % len(existing_ids))

def prof(fp):
    try:
        if fp.endswith(".csv"):
            df = pd.read_csv(fp, encoding="utf-8", on_bad_lines="skip", low_memory=False)
        else:
            df = pd.read_excel(fp)
    except:
        try:
            df = pd.read_csv(fp, encoding="latin-1", on_bad_lines="skip", low_memory=False)
        except:
            p("  ERROR reading")
            return
    p("  %d rows x %d cols" % (len(df), len(df.columns)))
    p("  cols: %s" % str(list(df.columns)[:10]))
    nums = df.select_dtypes(include=[np.number])
    for c in list(nums.columns)[:4]:
        try: p("    %s: %.1f-%.1f (mean %.1f)" % (c, nums[c].min(), nums[c].max(), nums[c].mean()))
        except: pass

# 1. FIVETHIRTYEIGHT
p("\n=== FIVETHIRTYEIGHT ===")
d = r"D:\raw_data\fivethirtyeight"
for fn in sorted(os.listdir(d)):
    if fn.endswith(".csv"):
        p("\n[%s]" % fn)
        prof(os.path.join(d, fn))

# 2. FBI
p("\n=== FBI ===")
d = r"D:\raw_data\fbi"
for root, dirs, files in os.walk(d):
    for fn in sorted(files):
        if fn.endswith((".csv",".xlsx",".xls")):
            p("\n[%s]" % fn)
            prof(os.path.join(root, fn))

# 3. CPI
p("\n=== CPI/PPI ===")
d = r"D:\raw_data\cpi"
for fn in sorted(os.listdir(d)):
    if fn.endswith((".csv",".xlsx",".xls")):
        p("\n[%s]" % fn)
        prof(os.path.join(d, fn))

# 4. SAGE
p("\n=== SAGE DATA ===")
d = r"D:\raw_data\Sage_Data"
if os.path.exists(d):
    for fn in sorted(os.listdir(d)):
        if fn.endswith((".csv",".xlsx",".xls")):
            p("\n[%s]" % fn)
            prof(os.path.join(d, fn))

# 5. OWID (summary)
p("\n=== OUR WORLD IN DATA ===")
d = r"D:\raw_data\Our World In Data"
owid_files = sorted([f for f in os.listdir(d) if f.endswith(".csv")])
p("Total OWID CSVs: %d" % len(owid_files))
for fn in owid_files:
    fp = os.path.join(d, fn)
    try:
        df = pd.read_csv(fp, nrows=3)
        p("  %s | %d cols | %s" % (fn[:55], len(df.columns), str(list(df.columns)[:5])))
    except:
        p("  %s | ERROR" % fn)

# 6. WORLDCUP
p("\n=== WORLDCUP ===")
d = r"D:\raw_data\worldcup"
if os.path.exists(d):
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".csv"):
            p("\n[%s]" % fn)
            prof(os.path.join(d, fn))

# 7. ECONDATA
p("\n=== ECONDATA ===")
d = r"D:\raw_data\EconData"
if os.path.exists(d):
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".csv"):
            p("\n[%s]" % fn)
            prof(os.path.join(d, fn))

# 8. PUBLIC SCHOOLS
p("\n=== PUBLIC SCHOOLS ===")
fp = r"D:\raw_data\Public_School_Characteristics_2022-23.csv"
if os.path.exists(fp):
    prof(fp)

# 9. AIRBNB
p("\n=== AIRBNB ===")
d = r"D:\raw_data\airbnb"
if os.path.exists(d):
    for root, dirs, files in os.walk(d):
        for fn in sorted(files):
            if fn.endswith(".csv"):
                p("\n[%s]" % fn)
                prof(os.path.join(root, fn))

# 10. MBTA
p("\n=== MBTA DATA ===")
d = r"D:\raw_data\MBTA Data 2025"
if os.path.exists(d):
    for fn in sorted(os.listdir(d)):
        fp2 = os.path.join(d, fn)
        sz = "DIR" if os.path.isdir(fp2) else "%.0fKB" % (os.path.getsize(fp2)/1024)
        p("  %s (%s)" % (fn, sz))

# 11. WALKABILITY
p("\n=== WALKABILITY ===")
d = r"D:\raw_data\WalkabilityIndex"
if os.path.exists(d):
    for fn in sorted(os.listdir(d)):
        fp2 = os.path.join(d, fn)
        sz = "DIR" if os.path.isdir(fp2) else "%.0fKB" % (os.path.getsize(fp2)/1024)
        p("  %s (%s)" % (fn, sz))

# Write output
with open(r"D:\projects\mapzimus-board\profile_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Done. %d lines written to profile_results.txt" % len(out))
