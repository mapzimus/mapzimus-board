import importlib.util, re, sys, os
from collections import Counter

# Load DA batch
spec = importlib.util.spec_from_file_location('DA', 'BATCH_DA.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
ideas = mod.ideas
print(f'DA ideas: {len(ideas)}')
for i in sorted(ideas, key=lambda x: -x['vs'])[:5]:
    print(f'  vs={i["vs"]} {i["id"]}')

# Inject into data.js
with open('data.js', 'r', encoding='utf-8') as f:
    existing = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', existing))
new_ideas = [i for i in ideas if i['id'] not in existing_ids]
print(f'New to add: {len(new_ideas)}')

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

if new_ideas:
    last = existing.rfind(']')
    new_lines = '\n'.join(f',{to_js_obj(i)}' for i in new_ideas)
    new_content = existing[:last] + '\n' + new_lines + '\n' + existing[last:]
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Done. Added {len(new_ideas)} ideas.')
else:
    print('Already added.')
