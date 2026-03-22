"""Profile all Kaggle archives 34+ and named folders for mapzimus idea extraction.
Special focus on geographic data fields (state, county, country, lat/lon, FIPS, etc.)"""
import os, csv, json, sys, io

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"D:\raw_data\kaggle"

GEO_KEYWORDS = ['state','county','country','city','region','province','lat','lon',
    'latitude','longitude','fips','zip','zipcode','postal','iso','geo','location',
    'place','address','district','territory','continent','municipality','metro',
    'coordinates','geometry','nation','capital','code_state','state_code',
    'country_code','iso3','iso2','admin','subdivision']

targets = []
for name in os.listdir(BASE):
    fp = os.path.join(BASE, name)
    if os.path.isdir(fp):
        if name.startswith("archive ("):
            try:
                num = int(name.replace("archive (","").replace(")",""))
                if num >= 34:
                    targets.append((f"archive_{num:02d}", fp))
            except:
                pass
        elif name not in (".",".."):
            targets.append((name, fp))

targets.sort(key=lambda x: x[0])
print(f"Found {len(targets)} targets to profile\n")

def detect_geo_columns(columns):
    """Flag columns that look geographic."""
    geo = []
    for c in columns:
        cl = c.lower().strip()
        for kw in GEO_KEYWORDS:
            if kw in cl:
                geo.append(c)
                break
    return geo

def profile_csv(filepath, max_rows=100000):
    try:
        with open(filepath, encoding="utf-8", errors="replace") as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if not headers:
                return None
            # Clean BOM
            if headers[0].startswith('\ufeff'):
                headers[0] = headers[0].lstrip('\ufeff')
            rows = []
            count = 0
            for row in reader:
                count += 1
                if count <= 5:
                    rows.append(row)
                if count > max_rows:
                    break
            geo_cols = detect_geo_columns(headers)
            return {"file": os.path.basename(filepath), "columns": headers,
                    "rows": count, "sample": rows[:3], "geo_cols": geo_cols}
    except Exception as e:
        return {"file": os.path.basename(filepath), "error": str(e)}

def profile_json(filepath):
    try:
        with open(filepath, encoding="utf-8", errors="replace") as f:
            data = json.load(f)
        if isinstance(data, list) and data and isinstance(data[0], dict):
            keys = list(data[0].keys())
            geo_cols = detect_geo_columns(keys)
            return {"file": os.path.basename(filepath), "type": "array",
                    "length": len(data), "keys": keys, "geo_cols": geo_cols}
        elif isinstance(data, dict):
            return {"file": os.path.basename(filepath), "type": "dict",
                    "top_keys": list(data.keys())[:20], "geo_cols": []}
    except Exception as e:
        return {"file": os.path.basename(filepath), "error": str(e)}

results = {}
geo_rich = []  # datasets with geographic columns

for label, dirpath in targets:
    print(f"{'='*70}")
    print(f"  {label}: {dirpath}")
    print(f"{'='*70}")
    
    files_info = []
    for root, dirs, files in os.walk(dirpath):
        for fname in sorted(files):
            fpath = os.path.join(root, fname)
            ext = fname.lower().rsplit(".", 1)[-1] if "." in fname else ""
            try:
                size_kb = os.path.getsize(fpath) / 1024
            except:
                continue
            
            if ext == "csv" and size_kb < 500000:
                info = profile_csv(fpath)
                if info and "error" not in info:
                    info["size_kb"] = round(size_kb, 1)
                    files_info.append(info)
                    cols = info["columns"]
                    geo = info["geo_cols"]
                    geo_tag = f" *** GEO: {geo}" if geo else ""
                    print(f"  CSV: {fname} | {info['rows']} rows | {len(cols)} cols | {size_kb:.0f} KB{geo_tag}")
                    print(f"       Cols: {', '.join(cols[:20])}")
                    if info["sample"]:
                        for s in info["sample"][:2]:
                            print(f"       Row:  {[str(x)[:40] for x in s[:10]]}")
                    if geo:
                        geo_rich.append((label, fname, geo, info['rows'], cols))
                elif info and "error" in info:
                    print(f"  CSV: {fname} | ERROR: {info['error']}")
            elif ext == "json" and size_kb < 100000:
                info = profile_json(fpath)
                if info:
                    info["size_kb"] = round(size_kb, 1)
                    files_info.append(info)
                    geo = info.get("geo_cols", [])
                    geo_tag = f" *** GEO: {geo}" if geo else ""
                    print(f"  JSON: {fname} | {info.get('type','')} | {size_kb:.0f} KB{geo_tag}")
                    keys = info.get("keys", info.get("top_keys", []))
                    print(f"       Keys: {', '.join(str(k) for k in keys[:20])}")
                    if geo:
                        geo_rich.append((label, fname, geo, info.get('length',0), keys))
            elif ext in ("xlsx", "xls"):
                print(f"  EXCEL: {fname} | {size_kb:.0f} KB")
                files_info.append({"file": fname, "type": "excel", "size_kb": round(size_kb, 1)})
            elif ext in ("geojson", "shp", "dbf", "kml", "gpkg"):
                print(f"  GEO FILE: {fname} | {size_kb:.0f} KB")
                files_info.append({"file": fname, "type": "geo_file", "size_kb": round(size_kb, 1)})
                geo_rich.append((label, fname, ["NATIVE_GEO"], 0, []))
            elif ext == "tsv" and size_kb < 500000:
                print(f"  TSV: {fname} | {size_kb:.0f} KB")
                files_info.append({"file": fname, "type": "tsv", "size_kb": round(size_kb, 1)})
    
    if not files_info:
        print(f"  (no data files found)")
    results[label] = files_info
    print()

# Summary
print("\n" + "="*70)
print("  SUMMARY")
print("="*70)
total_files = sum(len(v) for v in results.values())
print(f"Total datasets profiled: {len(results)}")
print(f"Total data files found: {total_files}")
for label, files in sorted(results.items()):
    if files:
        csv_count = sum(1 for f in files if f.get("file","").endswith(".csv"))
        total_rows = sum(f.get("rows",0) for f in files)
        print(f"  {label}: {len(files)} files, ~{total_rows:,} rows")

print(f"\n{'='*70}")
print(f"  GEO-RICH DATASETS (have geographic columns)")
print(f"{'='*70}")
for label, fname, geo, rows, cols in geo_rich:
    print(f"  [{label}] {fname} | geo_cols={geo} | {rows:,} rows")
    print(f"    all_cols: {', '.join(str(c) for c in cols[:25])}")
print(f"\nTotal geo-rich files: {len(geo_rich)}")
