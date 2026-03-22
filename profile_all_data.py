import pandas as pd, numpy as np, os, re, glob, json, sys

# Existing idea IDs
with open(r"D:\projects\mapzimus-board\data.js", encoding="utf-8") as f:
    raw = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
existing_titles = set(t.lower() for t in re.findall(r'title:"([^"]+)"', raw))
print("=== EXISTING IDEAS: %d ===" % len(existing_ids))

def profile_csv(fp, label=""):
    try:
        df = pd.read_csv(fp, encoding="utf-8", on_bad_lines="skip", low_memory=False)
    except:
        try:
            df = pd.read_csv(fp, encoding="latin-1", on_bad_lines="skip", low_memory=False)
        except Exception as e:
            print("  ERROR: %s" % str(e)[:60])
            return None
    print("  Rows: %d | Cols: %d" % (len(df), len(df.columns)))
    print("  Columns: %s" % str(list(df.columns)[:12]))
    nums = df.select_dtypes(include=[np.number])
    if len(nums.columns) > 0:
        for c in list(nums.columns)[:6]:
            try:
                print("    %s: min=%.2f max=%.2f mean=%.2f" % (c, nums[c].min(), nums[c].max(), nums[c].mean()))
            except:
                pass
    # Show unique values for key categorical columns
    cats = df.select_dtypes(include=["object"])
    for c in list(cats.columns)[:3]:
        nuniq = cats[c].nunique()
        if nuniq < 60:
            print("    %s (%d unique): %s" % (c, nuniq, str(list(cats[c].unique())[:8])))
    return df

# ============================================================
# 1. FIVETHIRTYEIGHT CSVs
# ============================================================
print("\n" + "="*60)
print("1. FIVETHIRTYEIGHT DATASETS")
print("="*60)
fte_dir = r"D:\raw_data\fivethirtyeight"
for fn in sorted(os.listdir(fte_dir)):
    fp = os.path.join(fte_dir, fn)
    if fn.endswith(".csv"):
        print("\n--- %s ---" % fn)
        profile_csv(fp)

# ============================================================
# 2. FBI DATA
# ============================================================
print("\n" + "="*60)
print("2. FBI DATASETS")
print("="*60)
fbi_dir = r"D:\raw_data\fbi"
for root, dirs, files in os.walk(fbi_dir):
    for fn in sorted(files):
        if fn.endswith((".csv", ".xlsx", ".xls")):
            fp = os.path.join(root, fn)
            print("\n--- %s ---" % os.path.relpath(fp, fbi_dir))
            if fn.endswith(".csv"):
                profile_csv(fp)
            else:
                try:
                    df = pd.read_excel(fp)
                    print("  Rows: %d | Cols: %d" % (len(df), len(df.columns)))
                    print("  Columns: %s" % str(list(df.columns)[:10]))
                except Exception as e:
                    print("  EXCEL ERROR: %s" % str(e)[:60])

# ============================================================
# 3. CPI / PPI DATA
# ============================================================
print("\n" + "="*60)
print("3. CPI / PPI DATASETS")
print("="*60)
cpi_dir = r"D:\raw_data\cpi"
for fn in sorted(os.listdir(cpi_dir)):
    fp = os.path.join(cpi_dir, fn)
    print("\n--- %s ---" % fn)
    if fn.endswith(".csv"):
        profile_csv(fp)
    elif fn.endswith((".xlsx", ".xls")):
        try:
            xls = pd.ExcelFile(fp)
            print("  Sheets: %s" % str(xls.sheet_names[:5]))
            df = pd.read_excel(fp, sheet_name=0, nrows=5)
            print("  First sheet cols: %s" % str(list(df.columns)[:8]))
        except Exception as e:
            print("  EXCEL ERROR: %s" % str(e)[:60])

# ============================================================
# 4. SAGE DATA
# ============================================================
print("\n" + "="*60)
print("4. SAGE DATA DATASETS")
print("="*60)
sage_dir = r"D:\raw_data\Sage_Data"
for fn in sorted(os.listdir(sage_dir)):
    fp = os.path.join(sage_dir, fn)
    print("\n--- %s ---" % fn)
    if fn.endswith(".csv"):
        profile_csv(fp)
    elif fn.endswith((".xlsx", ".xls")):
        try:
            df = pd.read_excel(fp, nrows=50)
            print("  Rows(sample): %d | Cols: %d" % (len(df), len(df.columns)))
            print("  Columns: %s" % str(list(df.columns)[:10]))
        except Exception as e:
            print("  EXCEL ERROR: %s" % str(e)[:60])

# ============================================================
# 5. OUR WORLD IN DATA
# ============================================================
print("\n" + "="*60)
print("5. OUR WORLD IN DATA (first 40 files)")
print("="*60)
owid_dir = r"D:\raw_data\Our World In Data"
owid_files = sorted([f for f in os.listdir(owid_dir) if f.endswith(".csv")])
print("Total OWID CSVs: %d" % len(owid_files))
for fn in owid_files[:40]:
    fp = os.path.join(owid_dir, fn)
    try:
        df = pd.read_csv(fp, nrows=5, encoding="utf-8")
        print("  %s | cols=%d | %s" % (fn[:50], len(df.columns), str(list(df.columns)[:6])))
    except:
        print("  %s | ERROR" % fn[:50])

# ============================================================
# 6. WORLDCUP
# ============================================================
print("\n" + "="*60)
print("6. WORLDCUP DATA")
print("="*60)
wc_dir = r"D:\raw_data\worldcup"
for fn in sorted(os.listdir(wc_dir)):
    fp = os.path.join(wc_dir, fn)
    if fn.endswith(".csv"):
        print("\n--- %s ---" % fn)
        profile_csv(fp)

# ============================================================
# 7. ECONDATA
# ============================================================
print("\n" + "="*60)
print("7. ECONDATA")
print("="*60)
econ_dir = r"D:\raw_data\EconData"
if os.path.exists(econ_dir):
    for fn in sorted(os.listdir(econ_dir)):
        fp = os.path.join(econ_dir, fn)
        if fn.endswith(".csv"):
            print("\n--- %s ---" % fn)
            profile_csv(fp)

# ============================================================
# 8. PUBLIC SCHOOLS
# ============================================================
print("\n" + "="*60)
print("8. PUBLIC SCHOOL CHARACTERISTICS")
print("="*60)
school_fp = r"D:\raw_data\Public_School_Characteristics_2022-23.csv"
if os.path.exists(school_fp):
    profile_csv(school_fp)

# ============================================================
# 9. WALKABILITY INDEX
# ============================================================
print("\n" + "="*60)
print("9. WALKABILITY INDEX")
print("="*60)
walk_dir = r"D:\raw_data\WalkabilityIndex"
if os.path.exists(walk_dir):
    for fn in sorted(os.listdir(walk_dir)):
        print("  %s" % fn)

# ============================================================
# 10. AIRBNB BOSTON
# ============================================================
print("\n" + "="*60)
print("10. AIRBNB BOSTON")
print("="*60)
airbnb_dir = r"D:\raw_data\airbnb"
if os.path.exists(airbnb_dir):
    for root, dirs, files in os.walk(airbnb_dir):
        for fn in sorted(files):
            if fn.endswith(".csv"):
                fp = os.path.join(root, fn)
                print("\n--- %s ---" % fn)
                profile_csv(fp)

# ============================================================
# 11. MBTA DATA
# ============================================================
print("\n" + "="*60)
print("11. MBTA DATA 2025")
print("="*60)
mbta_dir = r"D:\raw_data\MBTA Data 2025"
if os.path.exists(mbta_dir):
    for fn in sorted(os.listdir(mbta_dir)):
        fp = os.path.join(mbta_dir, fn)
        print("  %s (%s)" % (fn, "DIR" if os.path.isdir(fp) else "%.0fKB" % (os.path.getsize(fp)/1024)))

# ============================================================
# 12. REMAINING OWID FILES (41-end)
# ============================================================
print("\n" + "="*60)
print("12. OUR WORLD IN DATA (files 41-end)")
print("="*60)
for fn in owid_files[40:]:
    fp = os.path.join(owid_dir, fn)
    try:
        df = pd.read_csv(fp, nrows=5, encoding="utf-8")
        print("  %s | cols=%d | %s" % (fn[:50], len(df.columns), str(list(df.columns)[:6])))
    except:
        print("  %s | ERROR" % fn[:50])

# ============================================================
# 13. MAPZIMUS OLD BATCHES
# ============================================================
print("\n" + "="*60)
print("13. MAPZIMUS OLD BATCHES")
print("="*60)
mz_dir = r"D:\raw_data\mapzimus"
if os.path.exists(mz_dir):
    for fn in sorted(os.listdir(mz_dir)):
        fp = os.path.join(mz_dir, fn)
        print("  %s (%s)" % (fn, "DIR" if os.path.isdir(fp) else "%.0fKB" % (os.path.getsize(fp)/1024)))

print("\n\n=== PROFILE COMPLETE ===")
