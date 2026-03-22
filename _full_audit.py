"""
Full audit & recalc for mapzimus-board data.js
- Validates every entry's sc fields are on 0-100 scale
- Flags anomalies (missing fields, out-of-range values)
- Recalculates ALL vs scores from scratch using v4 formula
- Reports distribution stats and mismatches
- Writes corrected data.js
"""
import re, sys, os, json
from collections import Counter, defaultdict

DATA = os.path.join(os.path.dirname(__file__), 'data.js')

# ── canonical v4 formula (must match maintain.py) ──
FMT_BONUS = {
    'State choropleth': 3, 'County choropleth': 3, 'World choropleth': 3,
    'Bivariate choropleth': 2, 'Dot map': 2,
}
SC_FIELDS = ['emotional','relatability','clarity','surprise','tension','visual','originality','data_ready']
WEIGHTS = {'emotional':2.0,'relatability':2.0,'clarity':1.25,'surprise':1.5,'tension':1.5,'visual':2.0,'originality':1.5}

def calc_vs(vals, fmt):
    raw = sum(vals.get(k,0)*WEIGHTS[k] for k in WEIGHTS)
    base_vs = raw / 11.75
    penalty = 1.0 - 0.5*(1.0 - vals.get('data_ready',0)/100.0)
    return int(base_vs * penalty) + FMT_BONUS.get(fmt, 0)


# ── parse data.js ──
def parse_entries(text):
    """Extract every {...} entry from data.js, returning list of (line_num, raw_str, parsed_dict)."""
    entries = []
    # Match each object block on its own line
    for i, line in enumerate(text.split('\n'), 1):
        line = line.strip().lstrip(',')
        if not line.startswith('{id:'):
            continue
        # Extract fields via regex
        entry = {}
        entry['_line'] = i
        entry['_raw'] = line

        # Simple field extraction
        for key in ['id','title','sub','type','geo','fmt','section','tbl','status','notes']:
            m = re.search(r'\b' + key + r':"([^"]*)"', line)
            if m:
                entry[key] = m.group(1)

        # sc block
        sc_m = re.search(r'sc:\{([^}]+)\}', line)
        if sc_m:
            sc = {}
            for pair in re.finditer(r'(\w+):(\d+)', sc_m.group(1)):
                sc[pair.group(1)] = int(pair.group(2))
            entry['sc'] = sc
        else:
            entry['sc'] = {}

        # vs
        vs_m = re.search(r',vs:(\d+)', line)
        entry['vs'] = int(vs_m.group(1)) if vs_m else None

        entries.append(entry)
    return entries


def audit_and_recalc():
    with open(DATA, 'r', encoding='utf-8') as f:
        text = f.read()

    entries = parse_entries(text)
    print(f"Total entries parsed: {len(entries)}")

    # ── AUDIT PHASE ──
    issues = []
    scale_suspects = []  # entries where sc values look like 0-10 scale
    missing_sc = []
    vs_mismatches = []
    batch_stats = defaultdict(lambda: {'count':0, 'vs_sum':0, 'sc_low':0})

    for e in entries:
        eid = e.get('id','???')
        sc = e.get('sc', {})
        batch = re.match(r'([a-zA-Z]+)', eid)
        batch_key = batch.group(1).upper() if batch else 'UNKNOWN'

        # Check missing sc fields
        missing = [f for f in SC_FIELDS if f not in sc]
        if missing:
            missing_sc.append((eid, missing))
            issues.append(f"  {eid}: missing sc fields: {missing}")

        # Check scale: if ALL numeric sc values are <= 10, suspect 0-10 scale
        numeric_vals = [sc.get(f,0) for f in SC_FIELDS if f != 'data_ready']
        if numeric_vals and all(v <= 10 for v in numeric_vals) and any(v > 0 for v in numeric_vals):
            scale_suspects.append(eid)

        # Check out-of-range
        for f in SC_FIELDS:
            v = sc.get(f, 0)
            if v < 0 or v > 100:
                issues.append(f"  {eid}: {f}={v} OUT OF RANGE [0-100]")

        # Recalc vs
        fmt = e.get('fmt', '')
        recalced = calc_vs(sc, fmt)
        current_vs = e.get('vs', 0)
        if recalced != current_vs:
            vs_mismatches.append((eid, current_vs, recalced))

        # Batch stats
        batch_stats[batch_key]['count'] += 1
        batch_stats[batch_key]['vs_sum'] += recalced

    # ── REPORT ──
    print(f"\n{'='*60}")
    print(f"AUDIT REPORT")
    print(f"{'='*60}")


    print(f"\n[SCALE CHECK] Entries with ALL sc values <= 10 (suspect 0-10 scale): {len(scale_suspects)}")
    if scale_suspects:
        print(f"  First 20: {scale_suspects[:20]}")

    print(f"\n[MISSING SC] Entries missing sc fields: {len(missing_sc)}")
    if missing_sc:
        for eid, ms in missing_sc[:10]:
            print(f"  {eid}: missing {ms}")

    print(f"\n[VS MISMATCH] Entries where current vs != recalculated: {len(vs_mismatches)}")
    if vs_mismatches:
        print(f"  First 20 mismatches:")
        for eid, cur, rec in vs_mismatches[:20]:
            print(f"    {eid}: current={cur} recalced={rec}")

    print(f"\n[BATCH SUMMARY]")
    print(f"  {'Batch':<8} {'Count':>6} {'Avg VS':>8}")
    for b in sorted(batch_stats.keys()):
        s = batch_stats[b]
        avg = s['vs_sum']/s['count'] if s['count'] else 0
        print(f"  {b:<8} {s['count']:>6} {avg:>8.1f}")

    # Overall vs distribution
    all_vs = [calc_vs(e['sc'], e.get('fmt','')) for e in entries]
    print(f"\n[VS DISTRIBUTION] (recalculated)")
    print(f"  Min: {min(all_vs)}  Max: {max(all_vs)}  Mean: {sum(all_vs)/len(all_vs):.1f}")
    buckets = Counter()
    for v in all_vs:
        bucket = (v // 10) * 10
        buckets[bucket] += 1
    for b in sorted(buckets.keys()):
        bar = '#' * (buckets[b] // 5)
        print(f"  {b:>3}-{b+9:<3}: {buckets[b]:>5} {bar}")

    if issues:
        print(f"\n[OTHER ISSUES] ({len(issues)} total)")
        for iss in issues[:30]:
            print(iss)

    return entries, all_vs, vs_mismatches, scale_suspects


def recalc_and_write():
    """Recalculate ALL vs scores in data.js from sc fields and write back."""
    with open(DATA, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.split('\n')
    changed = 0
    for i, line in enumerate(lines):
        stripped = line.strip().lstrip(',')
        if not stripped.startswith('{id:'):
            continue

        # Extract sc block
        sc_m = re.search(r'sc:\{([^}]+)\}', line)
        if not sc_m:
            continue
        sc = {}
        for pair in re.finditer(r'(\w+):(\d+)', sc_m.group(1)):
            sc[pair.group(1)] = int(pair.group(2))

        # Extract fmt
        fmt_m = re.search(r'fmt:"([^"]*)"', line)
        fmt = fmt_m.group(1) if fmt_m else ''

        # Recalculate
        new_vs = calc_vs(sc, fmt)

        # Replace vs value in the line
        vs_m = re.search(r',vs:(\d+)', line)
        if vs_m:
            old_vs = int(vs_m.group(1))
            if old_vs != new_vs:
                line = line[:vs_m.start()] + f',vs:{new_vs}' + line[vs_m.end():]
                lines[i] = line
                changed += 1

    # Write back
    with open(DATA, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"\n[RECALC] Updated {changed} vs scores in data.js")
    return changed


if __name__ == '__main__':
    print("Phase 1: AUDIT")
    entries, all_vs, mismatches, suspects = audit_and_recalc()

    if mismatches:
        print(f"\nPhase 2: RECALC (fixing {len(mismatches)} mismatches)")
        changed = recalc_and_write()
        print(f"Done. {changed} entries updated.")
    else:
        print("\nPhase 2: RECALC — all vs scores already correct. No changes needed.")

    print("\nAudit complete.")
