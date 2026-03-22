"""Fix backslash paths in data.js tbl fields — replace \\ with / for JS safety."""
import re

fp = r"D:\projects\mapzimus-board\data.js"
with open(fp, encoding="utf-8") as f:
    raw = f.read()

# Count before
backslash_count = raw.count("D:\\\\raw_data") + raw.count("D:\\raw_data")
print(f"Backslash paths found: {backslash_count}")

# Replace D:\raw_data\kaggle\... paths with forward slashes in tbl fields
# The paths appear as: D:\raw_data\kaggle\archive (50)\uap_reports.csv
# In the JS string they appear as: D:\raw_data\...  (single backslashes)
raw = raw.replace("D:\\raw_data\\kaggle\\", "D:/raw_data/kaggle/")
raw = raw.replace("D:\\raw_data\\kaggle/", "D:/raw_data/kaggle/")

# Also fix any remaining single backslashes in archive paths
raw = raw.replace("\\archive ", "/archive ")
raw = raw.replace("\\iranwar\\", "/iranwar/")
raw = raw.replace("\\FBRESULTS26\\", "/FBRESULTS26/")
raw = raw.replace("\\mentalburnout\\", "/mentalburnout/")
raw = raw.replace("\\pop\\", "/pop/")
raw = raw.replace("\\spotify\\", "/spotify/")
raw = raw.replace("\\steam\\", "/steam/")

with open(fp, "w", encoding="utf-8") as f:
    f.write(raw)

# Verify
remaining = raw.count("D:\\raw_data")
print(f"Remaining backslash paths: {remaining}")
print("Done!")
