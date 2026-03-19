"""patch_maintain_v2.py - inject add_clarity step into maintain.py"""

with open('maintain.py', 'r', encoding='utf-8') as f:
    content = f.read()

ADD_CLARITY_CODE = '''
# ── 5. ADD CLARITY & STATUS (for new ideas missing them) ─────────────────────
WEIGHTS_V2 = {
    'emotional':    2.0,
    'relatability': 2.0,
    'clarity':      2.0,
    'surprise':     1.5,
    'tension':      1.0,
    'visual':       1.0,
    'data_ready':   0.5,
    'originality':  0.5,
}
FMT_CLARITY_MAP = {
    'county choropleth':    8,
    'state choropleth':     8,
    'world choropleth':     8,
    'dot map':              7,
    'city map':             7,
    'line chart':           7,
    'bar chart':            7,
    'area chart':           7,
    'treemap':              6,
    'ranked list':          9,
    'scatter plot':         5,
    'special map':          5,
    'h3 hexbin map':        5,
    'quadrant chart':       5,
    'bivariate choropleth': 4,
}

def add_clarity():
    with open('data.js', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    out, added, recomputed = [], 0, 0
    for line in lines:
        if not (line.startswith(',{id:') or line.startswith('{id:')):
            out.append(line); continue
        sc_m   = re.search(r\'sc:\\{([^}]+)\\}\', line)
        vs_m   = re.search(r\',vs:(\\d+),\', line)
        fmt_m  = re.search(r\',fmt:"([^"]+)"\', line)
        type_m = re.search(r\',type:"([^"]+)"\', line)
        if not sc_m:
            out.append(line); continue
        sc_str = sc_m.group(1)
        sc = {}
        for pair in re.finditer(r\'(\\w+):(\\d+)\', sc_str):
            sc[pair.group(1)] = int(pair.group(2))
        if \'clarity\' not in sc:
            fmt_val  = fmt_m.group(1).lower()  if fmt_m  else \'\'
            type_val = type_m.group(1).upper()  if type_m else \'\'
            base = FMT_CLARITY_MAP.get(fmt_val, 6)
            if type_val == \'XREF\': base = max(1, base - 1)
            if type_val == \'RANK\': base = min(10, base + 1)
            sc[\'clarity\'] = base
            new_sc = \',\'.join(\'%s:%d\' % (k, sc[k]) for k in
                [\'emotional\',\'relatability\',\'surprise\',\'tension\',\'visual\',\'data_ready\',\'originality\',\'clarity\'])
            line = line.replace(sc_str, new_sc)
            added += 1
        if \',status:\' not in line:
            line = line.rstrip()
            if line.endswith(\'}\'): line = line[:-1] + \',status:"idea"}\\'
            line += \'\\n\'
        if \',notes:\' not in line:
            line = line.rstrip()
            if line.endswith(\'}\'): line = line[:-1] + \',notes:""}\'
            line += \'\\n\'
        sc2 = {}
        sc_m2 = re.search(r\'sc:\\{([^}]+)\\}\', line)
        if sc_m2:
            for pair in re.finditer(r\'(\\w+):(\\d+)\', sc_m2.group(1)):
                sc2[pair.group(1)] = int(pair.group(2))
        new_vs = round(sum(sc2.get(k,0)*w for k,w in WEIGHTS_V2.items()))
        old_vs = int(vs_m.group(1)) if vs_m else 0
        if new_vs != old_vs:
            line = re.sub(r\',vs:\\d+,\', \',vs:%d,\' % new_vs, line)
            recomputed += 1
        out.append(line)
    with open(\'data.js\', \'w\', encoding=\'utf-8\') as f:
        f.writelines(out)
    print(f\'  [add_clarity] New clarity added: {added} | vs recomputed: {recomputed}\')

'''

# Insert before validate()
TARGET = '\n# ── 5. VALIDATE'
if TARGET in content:
    content = content.replace(TARGET, ADD_CLARITY_CODE + '\n# ── 6. VALIDATE', 1)
    # Also update the main() call order
    content = content.replace(
        '    add_ext()\n    normalize_fmt()\n    validate()',
        '    add_ext()\n    add_clarity()\n    normalize_fmt()\n    validate()'
    )
    with open('maintain.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("maintain.py patched OK")
else:
    print("Target not found - checking content...")
    # find validate location
    idx = content.find('def validate()')
    print("def validate() at char:", idx)
    print("Context:", repr(content[max(0,idx-40):idx+20]))
