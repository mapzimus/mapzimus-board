"""Scan entire computer for datasets: CSV, Excel, shapefiles, GeoJSON, GDB, etc."""
import os, sys, json, time
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EXTENSIONS = {
    # Tabular
    '.csv', '.tsv', '.xlsx', '.xls', '.xlsm',
    # GIS vector
    '.shp', '.geojson', '.gpkg', '.kml', '.kmz', '.gdb',
    '.topojson', '.fgb', '.tab', '.mif',
    # GIS raster (attribute tables in some)
    '.tif', '.tiff', '.img',
    # Data formats
    '.json', '.jsonl', '.ndjson', '.parquet', '.feather',
    '.sqlite', '.db', '.dta', '.sav', '.rds',
    # Text data
    '.dat', '.fixed',
}

SKIP_DIRS = {
    'node_modules', '.git', '__pycache__', 'venv', '.venv',
    'site-packages', 'AppData', 'Windows', 'Program Files',
    'Program Files (x86)', 'ProgramData', '$Recycle.Bin',
    'System Volume Information', '.npm', '.cache', '.conda',
    'anaconda3', 'miniconda3', '.nuget', 'Recovery',
}

results = []
scanned = 0
errors = 0
start = time.time()

# Scan all available drives
drives = []
for letter in 'CDEFGHIJKLMNOPQRSTUVWXYZ':
    drive = f"{letter}:\\"
    if os.path.exists(drive):
        drives.append(drive)

print(f"Scanning drives: {drives}")
print(f"Looking for: {sorted(EXTENSIONS)}")
print("="*80)

for drive in drives:
    for root, dirs, files in os.walk(drive, topdown=True):
        # Skip system/cache directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')]
        
        scanned += 1
        if scanned % 5000 == 0:
            elapsed = time.time() - start
            print(f"  [{elapsed:.0f}s] Scanned {scanned} dirs, found {len(results)} files so far...")
        
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTENSIONS:
                fp = os.path.join(root, f)
                try:
                    sz = os.path.getsize(fp)
                    results.append({
                        'path': fp,
                        'name': f,
                        'ext': ext,
                        'size_mb': round(sz / 1048576, 2),
                        'dir': root
                    })
                except:
                    errors += 1

elapsed = time.time() - start
print(f"\n{'='*80}")
print(f"SCAN COMPLETE in {elapsed:.1f}s")
print(f"Directories scanned: {scanned}")
print(f"Data files found: {len(results)}")
print(f"Errors: {errors}")

# Summary by extension
ext_counts = {}
for r in results:
    ext_counts[r['ext']] = ext_counts.get(r['ext'], 0) + 1
print(f"\nBy extension:")
for ext, count in sorted(ext_counts.items(), key=lambda x: -x[1]):
    print(f"  {ext}: {count}")

# Summary by drive
drive_counts = {}
for r in results:
    d = r['path'][:3]
    drive_counts[d] = drive_counts.get(d, 0) + 1
print(f"\nBy drive:")
for d, count in sorted(drive_counts.items()):
    print(f"  {d}: {count}")

# Filter out tiny files (<1KB) and known non-data
meaningful = [r for r in results if r['size_mb'] > 0.001]
print(f"\nMeaningful files (>1KB): {len(meaningful)}")

# Group by directory for easier browsing
dir_groups = {}
for r in meaningful:
    d = r['dir']
    if d not in dir_groups:
        dir_groups[d] = []
    dir_groups[d].append(r)

# Write full results
out_path = r"D:\projects\mapzimus-board\_scan_results.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump({
        'scan_time': elapsed,
        'total_files': len(results),
        'meaningful_files': len(meaningful),
        'by_extension': ext_counts,
        'by_drive': drive_counts,
        'files': meaningful
    }, f, indent=2)
print(f"\nFull results written to: {out_path}")

# Write human-readable summary grouped by directory
sum_path = r"D:\projects\mapzimus-board\_scan_summary.txt"
with open(sum_path, 'w', encoding='utf-8') as f:
    f.write(f"DATA FILE SCAN - {time.strftime('%Y-%m-%d %H:%M')}\n")
    f.write(f"{'='*80}\n")
    f.write(f"Total: {len(meaningful)} files across {len(dir_groups)} directories\n\n")
    
    # Sort dirs by file count descending
    for d, files in sorted(dir_groups.items(), key=lambda x: -len(x[1])):
        f.write(f"\n[{len(files)} files] {d}\n")
        for fi in sorted(files, key=lambda x: -x['size_mb'])[:20]:  # Top 20 per dir
            f.write(f"  {fi['size_mb']:>8.2f} MB  {fi['name']}\n")
        if len(files) > 20:
            f.write(f"  ... and {len(files)-20} more\n")

print(f"Summary written to: {sum_path}")
