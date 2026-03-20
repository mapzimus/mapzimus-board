"""
inject_e_batches.py — Inject BATCH_EA through BATCH_EJ into data.js
"""
import re, os, importlib.util

base = os.path.dirname(os.path.abspath(__file__))
batches = ['BATCH_EA','BATCH_EB','BATCH_EC','BATCH_ED','BATCH_EE',
           'BATCH_EF','BATCH_EG','BATCH_EH','BATCH_EI','BATCH_EJ']

all_ideas = []
for name in batches:
    path = os.path.join(base, name + '.py')
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    print(f'  {name}: {len(mod.ideas)} ideas (top vs={max(i["vs"] for i in mod.ideas)})')
    all_ideas.extend(mod.ideas)

print(f'Total new ideas: {len(all_ideas)}')

with open(os.path.join(base, 'data.js'), 'r', encoding='utf-8') as f:
    existing = f.read()

existing_ids = set(re.findall(r'id:"([^"]+)"', existing))
new_ideas = [i for i in all_ideas if i['id'] not in existing_ids]
print(f'New (not already in data.js): {len(new_ideas)}')

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

def to_js(idea):
    return '{' + ','.join(f'{k}:{jsval(v)}' for k,v in idea.items()) + '}'

last = existing.rfind(']')
new_lines = '\n'.join(f',{to_js(i)}' for i in new_ideas)
new_content = existing[:last] + '\n' + new_lines + '\n' + existing[last:]
with open(os.path.join(base, 'data.js'), 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Done. data.js now contains ~{len(existing_ids)+len(new_ideas)} ideas.')
