"""Runner appended to BATCH_AS.py — generates and appends JS lines to data.js"""

import re

WEIGHTS = {"emotional":2.0,"relatability":2.0,"clarity":2.0,"surprise":1.5,"tension":1.0,"visual":1.0,"data_ready":0.5,"originality":0.5}

def compute_vs(sc):
    return round(sum(sc.get(k,0)*w for k,w in WEIGHTS.items()))

def escape_js(s):
    return s.replace('\\','\\\\').replace('"','\\"')

def idea_to_js(d):
    vs = compute_vs(d["sc"])
    sc_str = ",".join(f'{k}:{v}' for k,v in d["sc"].items())
    vars_str = ",".join(f'"{v}"' for v in d.get("vars",[]))
    join_str = ",".join(f'"{v}"' for v in d.get("join",[]))
    ext_str  = ",".join(f'"{escape_js(e)}"' for e in d.get("ext",[]))
    topics_str = ",".join(f'"{t}"' for t in d.get("topics",[]))
    return (
        f',{{id:"{d["id"]}",'
        f'title:"{escape_js(d["title"])}",'
        f'sub:"{escape_js(d["sub"])}",'
        f'type:"{d["type"]}",'
        f'geo:"{d["geo"]}",'
        f'fmt:"{d["fmt"]}",'
        f'tbl:"{escape_js(d["tbl"])}",'
        f'section:"{d["section"]}",'
        f'vars:[{vars_str}],'
        f'join:[{join_str}],'
        f'sc:{{{sc_str}}},'
        f'vs:{vs},'
        f'topics:[{topics_str}],'
        f'status:"{d.get("status","idea")}",'
        f'notes:"{escape_js(d.get("notes",""))}",'
        f'tags:"{escape_js(d.get("tags",""))}",'
        f'ext:[{ext_str}]}}'
    )

with open(r"D:\projects\mapzimus-board\data.js","r",encoding="utf-8") as f:
    content = f.read()

# Find insertion point - just before ]; // end D
marker = "\n]; // end D"
assert marker in content, "End marker not found!"

new_lines = "\n".join(idea_to_js(d) for d in ideas)
content = content.replace(marker, "\n" + new_lines + marker)

with open(r"D:\projects\mapzimus-board\data.js","w",encoding="utf-8") as f:
    f.write(content)

print(f"Done! Appended {len(ideas)} ideas to data.js")

# Quick validate
import re as _re
all_ids = _re.findall(r'\{id:"([^"]+)"', content)
dupes = [x for x in set(all_ids) if all_ids.count(x) > 1]
print(f"Total ideas in file: {len(all_ids)}")
print(f"Duplicates: {dupes if dupes else 'none'}")
