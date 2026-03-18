"""fix_vscores_robust.py - Recompute ALL V-scores robustly regardless of field order"""
import re

WEIGHTS = {
    'emotional':    2.5,
    'relatability': 2.0,
    'surprise':     1.5,
    'tension':      1.5,
    'visual':       1.0,
    'data_ready':   1.0,
    'originality':  0.5,
}

def compute_vs(sc: dict) -> int:
    return round(sum(sc.get(k, 0) * w for k, w in WEIGHTS.items()))

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Match each idea line: find sc:{...} and vs:NN
line_pattern = re.compile(
    r'(,\{id:"[^\n]+?\n?)',
    re.DOTALL
)

changed = 0
unchanged = 0
errors = 0

def fix_idea(line):
    global changed, unchanged, errors
    # Extract sc block
    sc_match = re.search(r'sc:\{([^}]+)\}', line)
    vs_match = re.search(r',vs:(\d+),', line)
    if not sc_match or not vs_match:
        errors += 1
        return line
    sc = {}
    for pair in re.finditer(r'(\w+):(\d+)', sc_match.group(1)):
        sc[pair.group(1)] = int(pair.group(2))
    new_vs = compute_vs(sc)
    old_vs = int(vs_match.group(1))
    if new_vs != old_vs:
        changed += 1
        line = re.sub(r',vs:\d+,', ',vs:%d,' % new_vs, line)
    else:
        unchanged += 1
    return line

# Split on idea boundaries (each idea is a comma-prefixed JSON object on one line)
# data.js lines: one idea per line starting with ','
lines = content.split('\n')
new_lines = []
for line in lines:
    if line.startswith(',{id:'):
        new_lines.append(fix_idea(line))
    else:
        new_lines.append(line)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print("Done.")
print("  Changed:   %d" % changed)
print("  Unchanged: %d" % unchanged)
print("  Errors:    %d" % errors)

# Show new top 15
results = []
for line in new_lines:
    if not line.startswith(',{id:'): continue
    id_m = re.search(r'id:"([^"]+)"', line)
    vs_m = re.search(r',vs:(\d+),', line)
    sc_m = re.search(r'sc:\{([^}]+)\}', line)
    if id_m and vs_m and sc_m:
        sc = {}
        for pair in re.finditer(r'(\w+):(\d+)', sc_m.group(1)):
            sc[pair.group(1)] = int(pair.group(2))
        results.append((int(vs_m.group(1)), id_m.group(1)))

results.sort(reverse=True)
print("\nNew top 15 V-scores:")
for vs, id_ in results[:15]:
    print("  vs:%d  %s" % (vs, id_))
