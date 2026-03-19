import re
with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f: content=f.read()
lines = [l for l in content.split('\n') if l.startswith(',{id:') or l.startswith('{id:')]
dupes = ['nuclear_warheads_2025_map','global_port_throughput_by_location','union_density_by_state_trend_1980_2024']
for d in dupes:
    matches = [i for i,l in enumerate(lines) if ('id:"%s"' % d) in l]
    print(d, '-> occurrences:', len(matches))
    for idx in matches:
        vs_m = re.search(r',vs:(\d+),', lines[idx])
        title_m = re.search(r'title:"([^"]+)"', lines[idx])
        print('   vs=%s  title=%s' % (vs_m.group(1) if vs_m else '?', title_m.group(1)[:70] if title_m else '?'))
