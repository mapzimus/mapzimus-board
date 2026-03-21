import re, collections

with open(r"D:\projects\mapzimus-board\data.js", encoding="utf-8") as f:
    raw = f.read()

# Extract sections, types, formats, geos
sections = re.findall(r'section:"([^"]*)"', raw)
types = re.findall(r'type:"([^"]*)"', raw)
fmts = re.findall(r'fmt:"([^"]*)"', raw)
geos = re.findall(r'geo:"([^"]*)"', raw)

print("=== SECTION DISTRIBUTION ===")
for s, c in sorted(collections.Counter(sections).items(), key=lambda x: -x[1]):
    print("  %4d  %s" % (c, s))

print("\n=== TYPE DISTRIBUTION ===")
for s, c in sorted(collections.Counter(types).items(), key=lambda x: -x[1]):
    print("  %4d  %s" % (c, s))

print("\n=== FORMAT DISTRIBUTION ===")
for s, c in sorted(collections.Counter(fmts).items(), key=lambda x: -x[1]):
    print("  %4d  %s" % (c, s))

print("\n=== GEO DISTRIBUTION ===")
for s, c in sorted(collections.Counter(geos).items(), key=lambda x: -x[1]):
    print("  %4d  %s" % (c, s))

print("\n=== TOTAL IDEAS: %d ===" % len(types))
