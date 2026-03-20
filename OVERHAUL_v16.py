"""
OVERHAUL_v16.py - Run from D:\\projects\\mapzimus-board\\
Reads app.js and index.html from disk, patches them, writes back.
All new content lives in OVERHAUL_v16_app.js and OVERHAUL_v16_index.html
which are written separately.

PowerShell (one line at a time):
  cd D:\\projects\\mapzimus-board
  python OVERHAUL_v16.py
  python maintain.py
  git add .
  git commit -m "v16: 0-100 sc scores, sub-score filters, pastel palette, sort direction toggle"
  git push
"""
import re, os, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))

# ── STEP 1: Rescale sc fields 0-10 -> 0-100 in data.js ─────────────────────
print("Step 1: Rescaling sc fields in data.js...")
with open(os.path.join(BASE, 'data.js'), 'r', encoding='utf-8') as f:
    data = f.read()

sample = re.search(r'emotional:(\d+)', data)
if sample and int(sample.group(1)) > 10:
    print("  Already rescaled (values > 10). Skipping.")
else:
    fields = ['emotional','relatability','clarity','surprise','tension','visual','data_ready','originality']
    def rescale_sc_block(match):
        block = match.group(0)
        for field in fields:
            block = re.sub(
                r'(' + field + r'):(\d+)',
                lambda m: m.group(1) + ':' + str(int(m.group(2)) * 10),
                block
            )
        return block
    data = re.sub(r'sc:\{[^}]+\}', rescale_sc_block, data)
    sample2 = re.search(r'emotional:(\d+)', data)
    print(f"  Rescaled. Sample emotional value: {sample2.group(1) if sample2 else '?'}")

# ── STEP 2: Recalculate all vs scores ───────────────────────────────────────
print("Step 2: Recalculating vs scores (new formula: /10.5 for 0-100 output)...")

def parse_sc(sc_str):
    vals = {}
    for m in re.finditer(r'(\w+):(\d+)', sc_str):
        vals[m.group(1)] = int(m.group(2))
    return vals

def calc_vs(vals):
    raw = (vals.get('emotional',0)*2 + vals.get('relatability',0)*2 +
           vals.get('clarity',0)*2 + vals.get('surprise',0)*1.5 +
           vals.get('tension',0)*1 + vals.get('visual',0)*1 +
           vals.get('data_ready',0)*0.5 + vals.get('originality',0)*0.5)
    return int(raw / 10.5)

def replace_vs(line):
    sc_m = re.search(r'sc:\{([^}]+)\}', line)
    if not sc_m:
        return line
    new_vs = calc_vs(parse_sc(sc_m.group(0)))
    return re.sub(r',vs:\d+', f',vs:{new_vs}', line)

new_lines = []
for line in data.split('\n'):
    if line.startswith('{id:') or line.startswith(',{id:'):
        new_lines.append(replace_vs(line))
    else:
        new_lines.append(line)
data = '\n'.join(new_lines)
samples = re.findall(r',vs:(\d+)', data)[:5]
print(f"  Sample vs values: {samples}")

with open(os.path.join(BASE, 'data.js'), 'w', encoding='utf-8') as f:
    f.write(data)
print("  data.js written.")

# ── STEP 3: Copy new app.js ─────────────────────────────────────────────────
print("Step 3: Installing new app.js...")
src_app = os.path.join(BASE, 'OVERHAUL_v16_app.js')
if not os.path.exists(src_app):
    print(f"  ERROR: {src_app} not found. Did you copy all OVERHAUL files?")
    sys.exit(1)
import shutil
shutil.copy(src_app, os.path.join(BASE, 'app.js'))
# Syntax check
r = subprocess.run(['node','--check','app.js'], capture_output=True, text=True, cwd=BASE)
if r.returncode == 0:
    print("  app.js syntax: OK")
else:
    print("  app.js syntax ERROR:", r.stderr[:200])
    sys.exit(1)

# ── STEP 4: Copy new index.html ──────────────────────────────────────────────
print("Step 4: Installing new index.html...")
src_html = os.path.join(BASE, 'OVERHAUL_v16_index.html')
if not os.path.exists(src_html):
    print(f"  ERROR: {src_html} not found.")
    sys.exit(1)
shutil.copy(src_html, os.path.join(BASE, 'index.html'))
print("  index.html installed.")

# ── STEP 5: Patch maintain.py vscore formula ────────────────────────────────
print("Step 5: Patching maintain.py vscore formula...")
with open(os.path.join(BASE, 'maintain.py'), 'r', encoding='utf-8') as f:
    maintain = f.read()

OLD_VS = ("    return int(sc['emotional']*2 + sc['relatability']*2 + sc['clarity']*2 +\n"
          "            sc['surprise']*1.5 + sc['tension']*1 + sc['visual']*1 +\n"
          "            sc['data_ready']*0.5 + sc['originality']*0.5)")
NEW_VS = ("    raw = (sc.get('emotional',0)*2 + sc.get('relatability',0)*2 + sc.get('clarity',0)*2 +\n"
          "           sc.get('surprise',0)*1.5 + sc.get('tension',0)*1 + sc.get('visual',0)*1 +\n"
          "           sc.get('data_ready',0)*0.5 + sc.get('originality',0)*0.5)\n"
          "    return int(raw / 10.5)")
if OLD_VS in maintain:
    maintain = maintain.replace(OLD_VS, NEW_VS)
    with open(os.path.join(BASE, 'maintain.py'), 'w', encoding='utf-8') as f:
        f.write(maintain)
    print("  maintain.py vscore formula updated.")
else:
    print("  NOTE: vscore formula pattern not matched - may already be updated or different format.")

print("\nDone. Run:")
print("  python maintain.py")
print("  git add .")
print('  git commit -m "v16: 0-100 sc scores, sub-score filters, pastel palette, sort toggle"')
print("  git push")
