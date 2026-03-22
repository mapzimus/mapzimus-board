"""Replace ALL backslashes in data.js with forward slashes."""
fp = r"D:\projects\mapzimus-board\data.js"
with open(fp, encoding="utf-8") as f:
    lines = f.readlines()

fixed = 0
for i, line in enumerate(lines):
    if "tbl:" in line and "\\" in line:
        # Replace all backslashes with forward slashes in this line
        new_line = line.replace("\\", "/")
        if new_line != line:
            lines[i] = new_line
            fixed += 1

with open(fp, "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"Fixed {fixed} lines with backslashes in tbl fields")
