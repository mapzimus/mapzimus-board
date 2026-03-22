import re
with open(r"D:\projects\mapzimus-board\data.js", encoding="utf-8") as f:
    lines = f.readlines()

# Find lines with backslashes (escape sequences in JS strings)
for i, line in enumerate(lines):
    if "\\u" in line or "\\x" in line or "\\" in line:
        # Check if it's inside an id/title/sub field
        if 'id:"' in line or 'title:"' in line:
            stripped = line.strip()[:120]
            print(f"Line {i+1}: {stripped}")

# Also check for raw_data paths with backslashes
print("\n--- Lines with backslash paths ---")
count = 0
for i, line in enumerate(lines):
    if "\\raw_data" in line or "\\kaggle" in line or "\\archive" in line:
        count += 1
        if count <= 5:
            print(f"Line {i+1}: {line.strip()[:150]}")
print(f"Total lines with backslash paths: {count}")
