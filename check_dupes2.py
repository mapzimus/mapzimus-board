import re
with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f: content=f.read()
lines = [l for l in content.split('\n') if l.startswith(',{id:') or l.startswith('{id:')]

dupes = ['nuclear_warheads_2025_map','global_port_throughput_by_location','union_density_by_state_trend_1980_2024']
for d in dupes:
    matches = [(i,l) for i,l in enumerate(lines) if ('id:"%s"' % d) in l]
    print('\n=== %s ===' % d)
    for idx,(i,l) in enumerate(matches):
        title_m = re.search(r'title:"([^"]+)"', l)
        print('  [%d] title: %s' % (idx, title_m.group(1) if title_m else 'NO TITLE FOUND'))
        # Show the raw id portion
        id_start = l.find('id:"')
        print('  [%d] raw id+title start: %r' % (idx, l[id_start:id_start+80]))
