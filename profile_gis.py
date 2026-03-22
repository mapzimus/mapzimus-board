import warnings
warnings.filterwarnings("ignore")
import pandas as pd, os, re, sys

out = []
def p(s): out.append(s)

# Profile .dbf files (shapefile attribute tables) readable by pandas
import struct

def read_dbf(fp):
    try:
        df = pd.read_csv(fp.replace('.shp','.dbf'), encoding='latin-1')
        return None  # csv reader won't work for dbf
    except:
        pass
    return None

# Try reading shapefiles via their DBF files using a simpler approach
def profile_dbf(fp):
    """Read .dbf attribute table"""
    try:
        # DBF files can be read as fixed-width or we can use a simple parser
        import struct
        with open(fp, 'rb') as f:
            numrec, lenheader = struct.unpack('<xxxxII', f.read(12))
            numfields = (lenheader - 33) // 32
            fields = []
            f.read(20)  # rest of header
            for i in range(numfields):
                name = f.read(11).replace(b'\x00', b'').decode('latin-1')
                ftype = f.read(1).decode('latin-1')
                f.read(4)
                flen = struct.unpack('B', f.read(1))[0]
                f.read(15)
                fields.append((name, ftype, flen))
            p("  %d records, %d fields" % (numrec, numfields))
            p("  Fields: %s" % str([(n,t) for n,t,l in fields[:12]]))
    except Exception as e:
        p("  DBF ERROR: %s" % str(e)[:60])

# Scan for all .dbf files on F drive
p("=== F: DRIVE SHAPEFILES ===")
for root, dirs, files in os.walk(r"F:\\"):
    for fn in files:
        if fn.endswith(".dbf") and not fn.startswith("."):
            fp = os.path.join(root, fn)
            p("\n[%s]" % os.path.relpath(fp, "F:\\"))
            profile_dbf(fp)

# Scan downloaded spatial data
p("\n=== D: DRIVE SPATIAL DATA ===")
spatial_dir = r"F:\03 - GIS Data\_Downloaded Spatial Data"
if os.path.exists(spatial_dir):
    for fn in sorted(os.listdir(spatial_dir)):
        if fn.endswith((".xlsx", ".csv")):
            fp = os.path.join(spatial_dir, fn)
            p("\n[%s]" % fn)
            try:
                if fn.endswith(".csv"):
                    df = pd.read_csv(fp, nrows=5)
                else:
                    df = pd.read_excel(fp, nrows=5)
                p("  cols: %s" % str(list(df.columns)[:10]))
            except Exception as e:
                p("  ERROR: %s" % str(e)[:60])

# Check NE counties, MA towns, etc
p("\n=== DGL KEY DATASETS ===")
dgl_dirs = [
    r"F:\DGL_FILES_31426\odieneedsamap",
    r"F:\03 - GIS Data\DGL\NE Counties",
    r"F:\03 - GIS Data\DGL\MA towns",
    r"F:\03 - GIS Data\DGL\USCongress",
    r"F:\03 - GIS Data\DGL\Vermont_GIS_data",
]
for d in dgl_dirs:
    if os.path.exists(d):
        p("\n[%s]" % os.path.basename(d))
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".dbf"):
                fp = os.path.join(d, fn)
                p("  %s:" % fn)
                profile_dbf(fp)

# Check EV charging stations
p("\n=== EV CHARGING STATIONS ===")
ev_dir = r"F:\03 - GIS Data\_Downloaded Spatial Data\Electric_Vehicle_Charging_Stations"
if os.path.exists(ev_dir):
    for fn in sorted(os.listdir(ev_dir)):
        if fn.endswith(".dbf"):
            profile_dbf(os.path.join(ev_dir, fn))

# Check Route 24 CSVs
p("\n=== ROUTE 24 DATA ===")
r24_dir = r"F:\DGL_FILES_31426\Route 24"
if os.path.exists(r24_dir):
    for fn in sorted(os.listdir(r24_dir)):
        if fn.endswith(".csv"):
            fp = os.path.join(r24_dir, fn)
            p("\n[%s]" % fn)
            try:
                df = pd.read_csv(fp)
                p("  %d rows x %d cols: %s" % (len(df), len(df.columns), str(list(df.columns)[:8])))
            except Exception as e:
                p("  ERROR: %s" % str(e)[:40])

# Check Population xlsx
p("\n=== POPULATION PROJECTIONS ===")
pop_fp = r"F:\03 - GIS Data\_Downloaded Spatial Data\Population_1930_to_2023.xlsx"
if os.path.exists(pop_fp):
    try:
        df = pd.read_excel(pop_fp, nrows=10)
        p("  cols: %s" % str(list(df.columns)[:12]))
        p("  rows(sample): %d" % len(df))
    except Exception as e:
        p("  ERROR: %s" % str(e)[:60])

pop_fp2 = r"F:\03 - GIS Data\_Downloaded Spatial Data\UMDI_V2024_Long-Term_Population_Projections_MCD,_County,_RPA_Totals_2010-2050_a.xlsx"
if os.path.exists(pop_fp2):
    try:
        df = pd.read_excel(pop_fp2, nrows=10)
        p("  cols: %s" % str(list(df.columns)[:12]))
    except Exception as e:
        p("  ERROR: %s" % str(e)[:60])

# Check Datasets folder
p("\n=== F: DATASETS (PL Data, Pokemon, etc) ===")
ds_dir = r"F:\03 - GIS Data\Datasets"
if os.path.exists(ds_dir):
    for root2, dirs2, files2 in os.walk(ds_dir):
        for fn in sorted(files2):
            if fn.endswith((".csv",".xlsx")):
                fp = os.path.join(root2, fn)
                p("\n[%s]" % os.path.relpath(fp, ds_dir))
                try:
                    if fn.endswith(".csv"):
                        df = pd.read_csv(fp, nrows=5, encoding="utf-8", on_bad_lines="skip")
                    else:
                        df = pd.read_excel(fp, nrows=5)
                    p("  %d+ rows x %d cols: %s" % (len(df), len(df.columns), str(list(df.columns)[:8])))
                except:
                    try:
                        df = pd.read_csv(fp, nrows=5, encoding="latin-1", on_bad_lines="skip")
                        p("  %d+ rows x %d cols: %s" % (len(df), len(df.columns), str(list(df.columns)[:8])))
                    except Exception as e:
                        p("  ERROR: %s" % str(e)[:40])

# Write output
with open(r"D:\projects\mapzimus-board\profile_gis_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Done. %d lines -> profile_gis_results.txt" % len(out))
