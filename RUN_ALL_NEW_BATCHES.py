"""
RUN_ALL_NEW_BATCHES.py - Adds all BA-BZ + CA-CZ ideas to data.js
Run: python RUN_ALL_NEW_BATCHES.py
"""
import re, os, sys, importlib.util

base = os.path.dirname(os.path.abspath(__file__))

batch_names = [
    'BATCH_BA','BATCH_BB','BATCH_BC','BATCH_BD','BATCH_BE','BATCH_BF',
    'BATCH_BG','BATCH_BH','BATCH_BI','BATCH_BJ','BATCH_BK','BATCH_BL',
    'BATCH_BM','BATCH_BN','BATCH_BO','BATCH_BP','BATCH_BQ','BATCH_BR',
    'BATCH_BS','BATCH_BT','BATCH_BU','BATCH_BV','BATCH_BW','BATCH_BX',
    'BATCH_BY','BATCH_BZ',
    'BATCH_CA','BATCH_CB','BATCH_CC','BATCH_CD','BATCH_CE','BATCH_CF',
    'BATCH_CG','BATCH_CH','BATCH_CI','BATCH_CJ','BATCH_CK','BATCH_CL',
    'BATCH_CM','BATCH_CN','BATCH_CO','BATCH_CP','BATCH_CQ','BATCH_CR',
    'BATCH_CS','BATCH_CT','BATCH_CU','BATCH_CV','BATCH_CW','BATCH_CX',
    'BATCH_CY','BATCH_CZ',
]

all_ideas = []
for name in batch_names:
    path = os.path.join(base, name + '.py')
    if not os.path.exists(path):
        print(f"  MISSING: {name}.py - skipping")
        continue
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    ideas = mod.ideas
    print(f"  {name}: {len(ideas)} ideas")
    all_ideas.extend(ideas)

print(f"\nTotal ideas loaded: {len(all_ideas)}")

# Deduplicate within new batch
seen = set(); deduped = []
for i in all_ideas:
    if i['id'] not in seen:
        seen.add(i['id']); deduped.append(i)
if len(deduped) < len(all_ideas):
    print(f"Deduped {len(all_ideas)-len(deduped)} within-batch duplicates")
all_ideas = deduped

# Load existing data.js
data_js = os.path.join(base, 'data.js')
with open(data_js, 'r', encoding='utf-8') as f:
    existing = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', existing))
print(f"Existing ideas in data.js: {len(existing_ids)}")

new_ideas = [i for i in all_ideas if i['id'] not in existing_ids]
print(f"New ideas to add: {len(new_ideas)}")
if not new_ideas:
    print("Nothing to add.")
    sys.exit(0)

def jsval(v):
    if isinstance(v, bool): return 'true' if v else 'false'
    if v is None: return 'null'
    if isinstance(v, str):
        v = v.replace('\\','\\\\').replace('"','\\"').replace('\n',' ').replace('\r','')
        return f'"{v}"'
    if isinstance(v, (int, float)): return str(int(v))
    if isinstance(v, list): return '[' + ','.join(f'"{x}"' if isinstance(x,str) else str(x) for x in v) + ']'
    if isinstance(v, dict): return '{' + ','.join(f'{k}:{jsval(val)}' for k,val in v.items()) + '}'
    return str(v)

def to_js_obj(idea):
    return '{' + ','.join(f'{k}:{jsval(v)}' for k,v in idea.items()) + '}'

last = existing.rfind(']')
if last == -1:
    print("ERROR: Could not find closing ] in data.js"); sys.exit(1)

new_lines = '\n'.join(f',{to_js_obj(i)}' for i in new_ideas)
new_content = existing[:last] + '\n' + new_lines + '\n' + existing[last:]
with open(data_js, 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"Done. data.js now contains ~{len(existing_ids)+len(new_ideas)} ideas.")
print("\nNext: python maintain.py")
