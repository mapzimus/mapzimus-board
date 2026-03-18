import re

with open('data.js','r',encoding='utf-8') as f: raw=f.read()

formula = lambda sc: (sc.get('emotional',0)*2.5 + sc.get('relatability',0)*2.0 +
                      sc.get('surprise',0)*1.5 + sc.get('tension',0)*1.5 +
                      sc.get('visual',0)*1.0 + sc.get('data_ready',0)*1.0 +
                      sc.get('originality',0)*0.5)

high = []
pattern = re.compile(r'\{id:"([^"]+)".*?vs:(\d+).*?sc:\{([^}]+)\}', re.DOTALL)
for m in pattern.finditer(raw):
    id_ = m.group(1)
    vs = int(m.group(2))
    if vs >= 86:
        sc = {}
        for pair in m.group(3).split(','):
            kv = pair.strip().split(':')
            if len(kv) == 2:
                try: sc[kv[0].strip()] = float(kv[1].strip())
                except: pass
        computed = formula(sc)
        high.append((vs, round(computed,1), id_))

high.sort(reverse=True)
for vs, comp, id_ in high[:25]:
    diff = vs - comp
    print("vs:%d | computed:%.1f | diff:%.1f | %s" % (vs, comp, diff, id_))
