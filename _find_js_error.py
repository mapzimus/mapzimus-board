"""Find the exact line causing Invalid Unicode escape sequence."""
with open(r"D:\projects\mapzimus-board\data.js", encoding="utf-8") as f:
    content = f.read()

# Look for \u followed by non-hex chars (invalid JS unicode escapes)
import re
# Find all occurrences of backslash-u that aren't valid \uXXXX
lines = content.split("\n")
for i, line in enumerate(lines):
    # Check for literal \u in the line (not preceded by another backslash)
    pos = 0
    while True:
        idx = line.find("\\u", pos)
        if idx == -1:
            break
        # Check if next 4 chars are hex
        after = line[idx+2:idx+6]
        if len(after) < 4 or not all(c in "0123456789abcdefABCDEF" for c in after):
            print(f"Line {i+1}, col {idx}: \\u followed by '{after}' => {line[max(0,idx-20):idx+20]}")
        pos = idx + 2
    
    # Also check for \a \r \n \t etc that might be literal in strings
    for bad in ["\\a", "\\r", "\\n", "\\t", "\\b", "\\f", "\\v"]:
        if bad in line and "tbl:" in line:
            idx = line.find(bad)
            print(f"Line {i+1}: found {bad} in tbl field => ...{line[max(0,idx-30):idx+30]}...")
            break
