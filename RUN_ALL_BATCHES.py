"""
RUN_ALL_BATCHES.py
Run from D:\\projects\\mapzimus-board\\

PowerShell commands (one at a time):
  cd D:\\projects\\mapzimus-board
  python RUN_ALL_BATCHES.py
  python maintain.py
  git add .
  git commit -m "Batches AS-AW: global demographics, democracy, agriculture, retail, services (88 ideas)"
  git push

Don't forget to bump cache version in index.html script tags.
"""

import json, re, os, sys, importlib.util

def load_batch(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ideas

base = os.path.dirname(os.path.abspath(__file__))

batches = {
    'BATCH_AS': load_batch('BATCH_AS', os.path.join(base, 'BATCH_AS.py')),
    'BATCH_AT': load_batch('BATCH_AT', os.path.join(base, 'BATCH_AT.py')),
    'BATCH_AU': load_batch('BATCH_AU', os.path.join(base, 'BATCH_AU.py')),
    'BATCH_AV': load_batch('BATCH_AV', os.path.join(base, 'BATCH_AV.py')),
    'BATCH_AW': load_batch('BATCH_AW', os.path.join(base, 'BATCH_AW.py')),
}

all_ideas = []
for name, ideas in batches.items():
    print(f"  {name}: {len(ideas)} ideas")
    all_ideas.extend(ideas)

print(f"\nTotal new ideas: {len(all_ideas)}")

# Check for duplicates within new batch
ids = [i['id'] for i in all_ideas]
dupes = [x for x in set(ids) if ids.count(x) > 1]
if dupes:
    print(f"ERROR: Duplicate IDs in new batches: {dupes}")
    sys.exit(1)

# Check for collisions with existing data.js
data_js_path = os.path.join(base, 'data.js')
with open(data_js_path, 'r', encoding='utf-8') as f:
    existing = f.read()

existing_ids = re.findall(r'\bid:"([^"]+)"', existing)
print(f"Existing ideas in data.js: {len(existing_ids)}")

collisions = [i for i in ids if i in existing_ids]
if collisions:
    print(f"ERROR: IDs already exist in data.js: {collisions}")
    sys.exit(1)

print("Validation passed. Writing to data.js...")

def jsval(v):
    if isinstance(v, bool): return 'true' if v else 'false'
    if isinstance(v, str):
        # escape quotes and apostrophes
        v = v.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{v}"'
    if isinstance(v, int): return str(v)
    if isinstance(v, list):
        return '[' + ','.join(f'"{x}"' for x in v) + ']'
    if isinstance(v, dict):
        return '{' + ','.join(f'{k}:{jsval(val)}' for k, val in v.items()) + '}'
    return str(v)

def to_js_obj(idea):
    fields = ','.join(f'{k}:{jsval(v)}' for k, v in idea.items())
    return '{' + fields + '}'

last_bracket = existing.rfind(']')
if last_bracket == -1:
    print("ERROR: Could not find closing ] in data.js")
    sys.exit(1)

new_lines = '\n'.join(f',{to_js_obj(idea)}' for idea in all_ideas)
new_content = existing[:last_bracket] + '\n' + new_lines + '\n' + existing[last_bracket:]

with open(data_js_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

total = len(existing_ids) + len(all_ideas)
print(f"Done. data.js now contains {total} ideas.")
print("\nNext:")
print("  python maintain.py")
print("  git add .")
print('  git commit -m "Batches AS-AW: global demographics, democracy, agriculture, retail, services (88 ideas)"')
print("  git push")
print("  Bump cache version in index.html!")
