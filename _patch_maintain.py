lines = open('maintain.py', 'r', encoding='utf-8').readlines()

# Find and replace the recalc_vs function block
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Replace the section header
    if '# -- 4b. RECALC VS SCORES (v4 algorithm)' in line:
        new_lines.append('# -- 4b. RECALC VS SCORES (v5 algorithm) --------------------------------------\n')
        i += 1
        continue
    
    # Replace the FMT_BONUS comment and definition
    if '# FMT_BONUS removed' in line:
        i += 1
        continue
    if line.strip() == 'FMT_BONUS = {}  # no format bonus':
        i += 1
        continue
    
    # Replace the entire recalc_vs function
    if 'def recalc_vs():' in line:
        new_lines.append('''def recalc_vs():
    """Recalculate vs scores using virality formula v5.

    Changes from v4 (informed by multi-perspective audit):
      - visual weight:       2.0  -> 3.0   (thumbnail IS the content)
      - emotional weight:    2.0  -> 2.5   (sharing reflex driver)
      - surprise weight:     1.5  -> 2.0   ("wait WHAT" drives saves)
      - originality weight:  1.5  -> 1.75  (fresh ideas, but familiar topics can still pop)
      - tension weight:      1.5  -> 1.75  (outrage/urgency amplifier)
      - relatability weight: 2.0  -> 2.0   (unchanged — drives shares and comments)
      - clarity weight:      1.25 -> 1.5   (confusion kills virality)
      - data_ready penalty:  0.5  -> 0.35  (idea quality > data feasibility)
      - NEW: floor penalty if any score < 35 (one rotten dimension tanks everything)

    Formula:
      raw     = v*3.0 + e*2.5 + s*2.0 + o*1.75 + t*1.75 + r*2.0 + c*1.5
      base_vs = raw / 14.5
      floor   = 0.85 if min(e,r,c,s,t,v,o) < 35 else 1.0
      penalty = 1 - 0.35 * (1 - data_ready/100)
      vs      = int(base_vs * floor * penalty)
    """
    with open('data.js', 'r', encoding='utf-8') as f:
        content = f.read()

    def parse_sc(sc_str):
        vals = {}
        for m in re.finditer(r'(\\w+):(\\d+)', sc_str):
            vals[m.group(1)] = int(m.group(2))
        return vals

    def calc_vs(vals, fmt):
        e = vals.get('emotional', 0)
        r = vals.get('relatability', 0)
        c = vals.get('clarity', 0)
        s = vals.get('surprise', 0)
        t = vals.get('tension', 0)
        v = vals.get('visual', 0)
        o = vals.get('originality', 0)
        dr = vals.get('data_ready', 0)
        raw = (v * 3.0 + e * 2.5 + s * 2.0 + o * 1.75 +
               t * 1.75 + r * 2.0 + c * 1.5)
        base_vs = raw / 14.5
        floor = 0.85 if min(e, r, c, s, t, v, o) < 35 else 1.0
        penalty = 1.0 - 0.35 * (1.0 - dr / 100.0)
        return int(base_vs * floor * penalty)

    def replace_vs(line):
        sc_m = re.search(r'sc:\\{([^}]+)\\}', line)
        fmt_m = re.search(r'fmt:"([^"]*)"', line)
        if not sc_m:
            return line
        fmt = fmt_m.group(1) if fmt_m else ''
        new_vs = calc_vs(parse_sc(sc_m.group(0)), fmt)
        return re.sub(r',vs:\\d+', f',vs:{new_vs}', line)

    new_lines = []
    changed = 0
    for line in content.split('\\n'):
        if line.startswith('{id:') or line.startswith(',{id:'):
            new_line = replace_vs(line)
            if new_line != line:
                changed += 1
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    result = '\\n'.join(new_lines)
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(result)

    # Report stats
    all_vs = [int(x) for x in re.findall(r',vs:(\\d+)', result)]
    samples = all_vs[:5]
    if all_vs:
        import statistics
        print(f'  [recalc_vs] v5 algorithm | Recalculated {changed} scores')
        print(f'    Range: {min(all_vs)}-{max(all_vs)} | Mean: {statistics.mean(all_vs):.1f} | Median: {statistics.median(all_vs):.0f}')
        print(f'    Samples: {samples}')
        print(f'    Floor penalty (<35 on any dimension) | DR penalty coeff: 0.35')
    else:
        print(f'  [recalc_vs] Recalculated {changed} scores | samples: {samples}')

''')
        # Skip past the old function body until we hit the next section
        i += 1
        while i < len(lines) and not lines[i].startswith('# -- 5.'):
            i += 1
        continue
    
    # Update any remaining v4 references in other comments
    if 'v4 algorithm' in line and 'recalc_vs' not in line:
        line = line.replace('v4 algorithm', 'v5 algorithm')
    if 'recalculate all virality scores (v4' in line:
        line = line.replace('(v4 algorithm)', '(v5 algorithm)')
    
    new_lines.append(line)
    i += 1

with open('maintain.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("maintain.py updated to v5")
# Verify
content = open('maintain.py', 'r', encoding='utf-8').read()
print(f"v4 references remaining: {content.count('v4')}")
print(f"v5 references: {content.count('v5')}")
print(f"14.5 references: {content.count('14.5')}")
print(f"floor penalty references: {content.count('floor')}")
