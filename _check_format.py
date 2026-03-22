with open(r"D:\projects\mapzimus-board\data.js", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split('\n')
# Check the first few data lines
print("=== FIRST 5 DATA LINES (start chars) ===")
count = 0
for i, line in enumerate(lines):
    if 'id:"' in line and count < 5:
        print(f"  Line {i}: starts_with_brace={line.lstrip().startswith('{')}")
        print(f"    First 80 chars: {line[:80]}")
        count += 1

print()
# Check a new batch entry
print("=== FIRST gz ENTRY LINE ===")
for i, line in enumerate(lines):
    if 'id:"gz001"' in line:
        print(f"  Line {i}: starts_with_brace={line.lstrip().startswith('{')}")
        print(f"    First 80 chars: {line[:80]}")
        break

print()
# Now let me actually simulate what recalc_vs does for an old entry
import re
# Find the first entry and compute its vs
for line in lines:
    if 'id:"gop_transfers"' in line:
        sc_m = re.search(r'sc:\{([^}]+)\}', line)
        fmt_m = re.search(r'fmt:"([^"]*)"', line)
        if sc_m:
            vals = {}
            for m in re.finditer(r'(\w+):(\d+)', sc_m.group(0)):
                vals[m.group(1)] = int(m.group(2))
            fmt = fmt_m.group(1) if fmt_m else ''
            raw = (vals.get('emotional', 0) * 2.0 +
                   vals.get('relatability', 0) * 2.0 +
                   vals.get('clarity', 0) * 1.25 +
                   vals.get('surprise', 0) * 1.5 +
                   vals.get('tension', 0) * 1.5 +
                   vals.get('visual', 0) * 2.0 +
                   vals.get('originality', 0) * 1.5)
            FMT_BONUS = {'State choropleth':3,'County choropleth':3,'World choropleth':3,'Bivariate choropleth':2,'Dot map':2}
            base_vs = raw / 11.75
            penalty = 1.0 - 0.5 * (1.0 - vals.get('data_ready', 0) / 100.0)
            bonus = FMT_BONUS.get(fmt, 0)
            new_vs = int(base_vs * penalty) + bonus
            print(f"gop_transfers: sc={vals}")
            print(f"  fmt={fmt}, raw={raw}, base_vs={base_vs:.2f}, penalty={penalty:.2f}, bonus={bonus}")
            print(f"  Computed vs={new_vs}, Current vs in file=86")
            print(f"  MATCH? {new_vs == 86}")
        break
