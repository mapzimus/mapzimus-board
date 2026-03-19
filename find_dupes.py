import re
with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f: content=f.read()

for target in ['nuclear_warheads_2025_map','global_port_throughput_by_location']:
    matches = list(re.finditer(r'\{id:"%s"' % target, content))
    print('\n=== %s ===' % target)
    for m in matches:
        end = min(len(content), m.end()+120)
        print('  %r' % content[m.start():end])
