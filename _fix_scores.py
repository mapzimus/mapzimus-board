"""Fix v-scores for batches GZ through HAN.

Problem: mk() function used 0-10 scale for sc fields, but the formula
expects 0-100 scale. All entries from gz001 onward need sc values * 10.
"""
import re

DATA = r"D:\projects\mapzimus-board\data.js"

with open(DATA, "r", encoding="utf-8") as f:
    content = f.read()

# Affected ID prefixes (all new batches)
affected = ["gz","haa","hab","hac","had","hae","haf","hag","hah","hai","haj","hak","hal","ham","han"]

def is_affected(line):
    m = re.search(r'id:"([^"]+)"', line)
    if not m:
        return False
    id_val = m.group(1)
    for pfx in affected:
        if id_val.startswith(pfx):
            return True
    return False

def scale_sc(match):
    """Multiply each numeric value in sc:{...} by 10"""
    sc_str = match.group(0)
    def mult10(m):
        key = m.group(1)
        val = int(m.group(2))
        new_val = min(val * 10, 100)  # Cap at 100
        return f"{key}:{new_val}"
    return re.sub(r'(\w+):(\d+)', mult10, sc_str)

fixed = 0
new_lines = []
for line in content.split('\n'):
    if is_affected(line):
        # Scale the sc values
        new_line = re.sub(r'sc:\{[^}]+\}', scale_sc, line)
        if new_line != line:
            fixed += 1
        new_lines.append(new_line)
    else:
        new_lines.append(line)

result = '\n'.join(new_lines)

with open(DATA, "w", encoding="utf-8") as f:
    f.write(result)

print(f"Fixed {fixed} entries (scaled sc fields from 0-10 to 0-100)")
print()

# Verify a sample
m = re.search(r'\{[^}]*id:"gz001"[^}]*\}', result)
if m:
    print(f"gz001 after fix: {m.group()[:300]}")
