import warnings
warnings.filterwarnings("ignore")
import pandas as pd, os, struct, sys

out = []
def p(s): out.append(s)

def profile_dbf(fp):
    try:
        with open(fp, 'rb') as f:
            numrec, lenheader = struct.unpack('<xxxxII', f.read(12))
            numfields = (lenheader - 33) // 32
            fields = []
            f.read(20)
            for i in range(numfields):
                name = f.read(11).replace(b'\x00', b'').decode('latin-1')
                ftype = f.read(1).decode('latin-1')
                f.read(4)
                flen = struct.unpack('B', f.read(1))[0]
                f.read(15)
                fields.append((name, ftype, flen))
            p("  %d records, %d fields" % (numrec, numfields))
            p("  Fields: %s" % str([(n,t) for n,t,l in fields[:15]]))
    except Exception as e:
        p("  DBF ERROR: %s" % str(e)[:60])

# Only scan specific known directories, not the whole F: drive
scan_dirs = [
    r"F:\03 - GIS Data\_Downloaded Spatial Data",
    r"F:\03 - GIS Data\DGL",
    r"F:\03 - GIS Data\Datasets",
    r"F:\03 - GIS Data\MBTA Data 2025",
    r"F:\DGL_FILES_31426\odieneedsamap",
    r"F:\DGL_FILES_31426\qgis",
    r"F:\DGL_FILES_31426\Route 24",
    r"F:\DGL_FILES_31426\NYC",
    r"F:\DGL_FILES_31426\gee",
]

for scan_dir in scan_dirs:
    if not os.path.exists(scan_dir):
        continue
    p("\n=== %s ===" % scan_dir)
    for root, dirs, files in os.walk(scan_dir):
        for fn in sorted(files):
            fp = os.path.join(root, fn)
            if fn.endswith(".dbf"):
                p("\n[DBF] %s" % os.path.relpath(fp, scan_dir))
                profile_dbf(fp)
            elif fn.endswith(".csv"):
                p("\n[CSV] %s" % os.path.relpath(fp, scan_dir))
                try:
                    df = pd.read_csv(fp, nrows=5, on_bad_lines="skip", low_memory=False)
                    p("  cols: %s" % str(list(df.columns)[:10]))
                except:
                    try:
                        df = pd.read_csv(fp, nrows=5, encoding="latin-1", on_bad_lines="skip")
                        p("  cols: %s" % str(list(df.columns)[:10]))
                    except Exception as e:
                        p("  ERROR: %s" % str(e)[:50])
            elif fn.endswith(".xlsx"):
                p("\n[XLSX] %s" % os.path.relpath(fp, scan_dir))
                try:
                    df = pd.read_excel(fp, nrows=5)
                    p("  cols: %s" % str(list(df.columns)[:10]))
                except Exception as e:
                    p("  ERROR: %s" % str(e)[:50])

with open(r"D:\projects\mapzimus-board\profile_gis_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("Done. %d lines -> profile_gis_results.txt" % len(out))
