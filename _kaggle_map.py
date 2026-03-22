"""Map Kaggle archive folders to their actual dataset names using metadata files."""
import os, json, glob

KAGGLE_DIR = r"D:\raw_data\Kaggle"

# List all directories
print("=== Kaggle directory listing ===")
for item in sorted(os.listdir(KAGGLE_DIR)):
    full = os.path.join(KAGGLE_DIR, item)
    if os.path.isdir(full):
        files = os.listdir(full)
        # Look for dataset-metadata.json or any json with metadata
        meta_files = [f for f in files if f.endswith('.json')]
        csv_files = [f for f in files if f.endswith('.csv')]
        other = [f for f in files if not f.endswith('.csv') and not f.endswith('.json')]
        
        meta_info = ""
        for mf in meta_files:
            try:
                with open(os.path.join(full, mf), 'r', encoding='utf-8') as fh:
                    md = json.load(fh)
                    title = md.get('title', md.get('name', ''))
                    slug = md.get('id', md.get('slug', ''))
                    if title or slug:
                        meta_info = f" METADATA: title='{title}' slug='{slug}'"
                        break
            except:
                pass
        
        print(f"\n[{item}]{meta_info}")
        for f in sorted(csv_files):
            size = os.path.getsize(os.path.join(full, f))
            print(f"  CSV: {f} ({size//1024}KB)")
        for f in sorted(other)[:5]:
            print(f"  OTHER: {f}")
    elif os.path.isfile(full) and item.endswith('.csv'):
        size = os.path.getsize(full)
        print(f"\n[FILE] {item} ({size//1024}KB)")
