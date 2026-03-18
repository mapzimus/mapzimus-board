"""fix_issues.py - Fix all audit-identified issues in data.js and maintain.py"""
import re

WEIGHTS = {'emotional':2.5,'relatability':2.0,'surprise':1.5,'tension':1.5,
           'visual':1.0,'data_ready':1.0,'originality':0.5}

with open('data.js','r',encoding='utf-8') as f: content=f.read()
lines = content.split('\n')
new_lines = []
fixes = []

for line in lines:
    orig = line

    # Fix 1: RANKED_LIST -> RANK
    if 'type:"RANKED_LIST"' in line:
        line = line.replace('type:"RANKED_LIST"', 'type:"RANK"')
        fixes.append("RANKED_LIST->RANK: " + re.search('id:"([^"]+)"', line).group(1))

    # Fix 2: fmt:"Dual" -> fmt:"Line chart"
    if 'fmt:"Dual"' in line:
        line = line.replace('fmt:"Dual"', 'fmt:"Line chart"')
        fixes.append('fmt Dual->Line chart: ' + (re.search('id:"([^"]+)"', line).group(1) if re.search('id:"([^"]+)"', line) else '?'))

    # Fix 3: V-scores with >3pt drift (recompute from sc)
    if line.startswith(',{id:') or line.startswith('{id:'):
        sc_m = re.search('sc:\{([^}]+)\}', line)
        vs_m = re.search(',vs:(\d+),', line)
        id_m = re.search('id:"([^"]+)"', line)
        if sc_m and vs_m:
            sc = {}
            for pair in re.finditer(r'(\w+):(\d+)', sc_m.group(1)):
                sc[pair.group(1)] = int(pair.group(2))
            computed = round(sum(sc.get(k,0)*w for k,w in WEIGHTS.items()))
            stored = int(vs_m.group(1))
            if abs(computed - stored) > 3:
                line = re.sub(r',vs:\d+,', ',vs:%d,' % computed, line)
                fixes.append("vs fix %d->%d: %s" % (stored, computed, id_m.group(1) if id_m else '?'))

    new_lines.append(line)

with open('data.js','w',encoding='utf-8') as f: f.write('\n'.join(new_lines))

print("data.js fixes applied:")
for fix in fixes:
    print("  " + fix)
print("Total fixes:", len(fixes))
