"""Fast targeted scan for data files across all drives."""
import os, sys, json, time
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EXTENSIONS = {
    '.csv', '.tsv', '.xlsx', '.xls', '.xlsm',
    '.shp', '.geojson', '.gpkg', '.kml', '.kmz',
    '.topojson', '.fgb', '.tab',
    '.json', '.jsonl', '.parquet', '.feather',
    '.sqlite', '.db', '.dta', '.sav',
}

SKIP = {'node_modules','.git','__pycache__','venv','.venv',
        'site-packages','Windows','Program Files','Program Files (x86)',
        'ProgramData','$Recycle.Bin','System Volume Information',
        '.npm','.cache','.conda','anaconda3','Recovery','.nuget',
        'msys64','Packages','WindowsApps','WinSxS','assembly'}

# Find all drives
drives = [f"{c}:\\" for c in 'CDEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f"{c}:\\")]
print(f"Drives found: {drives}")

results = []
dir_count = 0
start = time.time()

for drive in drives:
    for root, dirs, files in os.walk(drive, topdown=True):
        # Aggressive skip
        base = os.path.basename(root)
        if base in SKIP or base.startswith('.'):
            dirs.clear()
            continue
        # Skip deep AppData except known data locations
        if 'AppData' in root and 'raw_data' not in root.lower() and 'projects' not in root.lower():
            dirs.clear()
            continue
        dirs[:] = [d for d in dirs if d not in SKIP and not d.startswith('.')]
        dir_count += 1
        
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTENSIONS:
                fp = os.path.join(root, f)
                try:
                    sz = os.path.getsize(fp)
                    if sz > 500:  # skip tiny files
                        results.append((fp, f, ext, sz))
                except:
                    pass
        
        # Progress every 2000 dirs
        if dir_count % 2000 == 0:
            print(f"  [{time.time()-start:.0f}s] {dir_count} dirs, {len(results)} files...")

elapsed = time.time() - start
print(f"\nDone in {elapsed:.1f}s - {len(results)} data files found in {dir_count} dirs")

# Group by extension
ext_map = {}
for fp, f, ext, sz in results:
    ext_map.setdefault(ext, []).append((fp, f, sz))

print("\nBy extension:")
for ext in sorted(ext_map, key=lambda e: -len(ext_map[e])):
    print(f"  {ext}: {len(ext_map[ext])} files")

# Group by top-level directory
dir_map = {}
for fp, f, ext, sz in results:
    parts = fp.replace('\\', '/').split('/')
    key = '/'.join(parts[:3]) if len(parts) >= 3 else '/'.join(parts[:2])
    dir_map.setdefault(key, []).append((fp, f, ext, sz))

print("\nBy top-level location:")
for d in sorted(dir_map, key=lambda k: -len(dir_map[k]))[:30]:
    total_mb = sum(s for _,_,_,s in dir_map[d]) / 1048576
    print(f"  [{len(dir_map[d]):>4} files, {total_mb:>8.1f} MB] {d}")

# Write detailed results
out = "D:\\projects\\mapzimus-board\\_scan_results.txt"
with open(out, 'w', encoding='utf-8') as fh:
    fh.write(f"FULL SCAN RESULTS - {len(results)} files\n{'='*80}\n\n")
    for d in sorted(dir_map, key=lambda k: -len(dir_map[k])):
        fh.write(f"\n[{len(dir_map[d])} files] {d}\n")
        for fp, f, ext, sz in sorted(dir_map[d], key=lambda x: -x[3]):
            fh.write(f"  {sz/1048576:>8.2f} MB  {fp}\n")
print(f"\nDetails: {out}")
