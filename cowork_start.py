# cowork_start.py -- Run this first in any new Cowork session.
# Reads live project state and prints a full briefing.
#
# Usage:
#   $py = "C:\Users\mhowe\AppData\Local\Python\pythoncore-3.14-64\python.exe"
#   cd D:\projects\mapzimus-board
#   & $py cowork_start.py

import re, pathlib, statistics, subprocess, sys

PY  = sys.executable
DIR = pathlib.Path(__file__).parent
DATA = DIR / 'data.js'
APP  = DIR / 'app.js'

SEP = '=' * 60

print(SEP)
print('  @mapzimus BOARD — COWORK SESSION BRIEFING')
print(SEP)

# ── 1. Git status ─────────────────────────────────────────────
print('\n[ GIT STATUS ]')
r = subprocess.run(['git', 'log', '--oneline', '-5'], cwd=DIR, capture_output=True, text=True)
print(r.stdout.strip())
r2 = subprocess.run(['git', 'status', '--short'], cwd=DIR, capture_output=True, text=True)
if r2.stdout.strip():
    print('Uncommitted changes:')
    print(r2.stdout.strip())
else:
    print('Working tree clean.')

# ── 2. Board health ───────────────────────────────────────────
print('\n[ BOARD HEALTH ]')
src = DATA.read_text(encoding='utf-8')

# Count ideas
idea_count = src.count('id:"')
print(f'  Total ideas   : {idea_count}')

# Dupe check
ids = re.findall(r'id:"([^"]+)"', src)
dupes = [id_ for id_ in set(ids) if ids.count(id_) > 1]
print(f'  Duplicate IDs : {len(dupes)}' + (f'  ← FIX: {dupes[:3]}' if dupes else ''))

# Non-ASCII
non_ascii = re.findall(r'[^\x00-\x7F]', src)
print(f'  Non-ASCII chars: {len(non_ascii)}' + (' ← RUN maintain.py' if non_ascii else ''))

# File size
kb = DATA.stat().st_size / 1024
print(f'  data.js size  : {kb:.1f} KB')

# JS check via node
node = subprocess.run(['node', '-e', f'const D=1; require(String.raw`{DATA}`)'],
                      capture_output=True, text=True)
# simpler JS check
node2 = subprocess.run(
    ['node', '--input-type=module'],
    input=f'import("{DATA.as_posix()}").then(()=>console.log("OK")).catch(e=>console.error(e.message))',
    capture_output=True, text=True, cwd=DIR
)
# fallback: just check ends correctly
ends_ok = src.rstrip().endswith(']; // end D')
print(f'  Ends with marker: {"YES" if ends_ok else "NO ← RUN maintain.py"}')

# ── 3. Score distribution ─────────────────────────────────────
print('\n[ SCORE DISTRIBUTION ]')
all_vs = [int(x) for x in re.findall(r',vs:(\d+),', src)]
if all_vs:
    print(f'  Mean: {statistics.mean(all_vs):.1f}  Median: {statistics.median(all_vs)}  '
          f'Min: {min(all_vs)}  Max: {max(all_vs)}')
    buckets = {}
    for v in all_vs:
        b = (v // 10) * 10
        buckets[b] = buckets.get(b, 0) + 1
    for b in sorted(buckets):
        bar = '#' * (buckets[b] // 15)
        print(f'  {b:3d}-{b+9}: {buckets[b]:4d}  {bar}')

# ── 4. Top 10 ideas by vs ─────────────────────────────────────
print('\n[ TOP 10 IDEAS BY VS SCORE ]')
pat = re.compile(r'id:"([^"]+)".*?title:"([^"]+)".*?vs:(\d+)')
all_ideas = [(m.group(1), m.group(2)[:55], int(m.group(3))) for m in pat.finditer(src)]
for id_, title, vs in sorted(all_ideas, key=lambda x: -x[2])[:10]:
    print(f'  vs:{vs:3d}  {title}')

# ── 5. Status breakdown ───────────────────────────────────────
print('\n[ STATUS BREAKDOWN ]')
for status in ['idea', 'building', 'done', 'skip']:
    n = src.count(f'status:"{status}"')
    print(f'  {status:10s}: {n}')

# ── 6. Section breakdown (top 15) ────────────────────────────
print('\n[ TOP 15 SECTIONS ]')
sections = re.findall(r'section:"([^"]+)"', src)
sec_counts = {}
for s in sections:
    # Use root section only (before any " - ")
    root = s.split('  -  ')[0].strip()
    sec_counts[root] = sec_counts.get(root, 0) + 1
for sec, n in sorted(sec_counts.items(), key=lambda x: -x[1])[:15]:
    print(f'  {n:4d}  {sec}')

# ── 7. Key file paths ─────────────────────────────────────────
print('\n[ KEY PATHS ]')
print(f'  Project dir : {DIR}')
print(f'  Python      : {PY}')
print(f'  data.js     : {DATA}')
print(f'  Site        : https://mapzimus.github.io/mapzimus-board')
print(f'  Repo        : https://github.com/mapzimus/mapzimus-board')
print(f'  Password    : gridline')

# ── 8. Quick commands ─────────────────────────────────────────
print('\n[ QUICK COMMANDS ]')
print('  Run pipeline  : & $py maintain.py')
print('  Full audit    : & $py full_audit.py')
print('  Score audit   : & $py score_audit.py')
print('  Push changes  : git add . ; git commit -m "..." ; git push')
print('  Read blueprint: Get-Content HANDOVER.md | more')

# ── 9. Reminders ─────────────────────────────────────────────
print('\n[ REMINDERS ]')
print('  - PowerShell: use ";" not "&&" between commands')
print('  - Never use Set-Content / Out-File (UTF-16 breaks JS)')
print('  - Always run maintain.py before pushing')
print('  - Only push after "[js_check] Valid JS" appears')
print('  - New ideas: use hand-crafted canonical sections (see HANDOVER.md sec 4d)')
print('  - data_ready drives score — bump it when data is acquired')

print(f'\n{SEP}')
print('  Read HANDOVER.md for full blueprint.')
print(SEP + '\n')
