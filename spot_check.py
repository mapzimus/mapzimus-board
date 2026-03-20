import re
c = open('data.js', encoding='utf-8').read()
lines = [l for l in c.split('\n') if l.startswith('{id:') or l.startswith(',{id:')]
lines.sort(key=lambda x: -int(re.search(r',vs:(\d+)',x).group(1)))
print("Top 10 ideas + their topics:")
for l in lines[:10]:
    idea_id = re.search(r'id:"([^"]+)"', l).group(1)
    vs = re.search(r',vs:(\d+)', l).group(1)
    tm = re.search(r'topics:\[([^\]]*)\]', l)
    topics = re.findall(r'"([^"]+)"', tm.group(1)) if tm else []
    print(f"  vs={vs}  {idea_id}")
    print(f"         topics: {topics}")
