import re

with open(r"D:\projects\mapzimus-board\data.js", "r", encoding="utf-8") as f:
    blob = f.read()

# Extract all ideas with id and vs
pattern = r'id:"([^"]+)".*?vs:(\d+)'
matches = list(re.finditer(pattern, blob))

print(f"Total ideas found: {len(matches)}")
print()

# Show last 40 entries
print("=== LAST 40 ENTRIES ===")
for m in matches[-40:]:
    print(f"  {m.group(1):12s}  vs={m.group(2)}")

print()

# Count vs distribution
vs_vals = [int(m.group(2)) for m in matches]
under10 = [m.group(1) for m in matches if int(m.group(2)) < 10]
under20 = [m.group(1) for m in matches if int(m.group(2)) < 20]
under30 = [m.group(1) for m in matches if int(m.group(2)) < 30]

print(f"=== V-SCORE DISTRIBUTION ===")
print(f"  Under 10: {len(under10)}")
print(f"  Under 20: {len(under20)}")
print(f"  Under 30: {len(under30)}")
print(f"  30-50:    {len([v for v in vs_vals if 30 <= v < 50])}")
print(f"  50-70:    {len([v for v in vs_vals if 50 <= v < 70])}")
print(f"  70-90:    {len([v for v in vs_vals if 70 <= v < 90])}")
print(f"  90+:      {len([v for v in vs_vals if v >= 90])}")
print(f"  Mean:     {sum(vs_vals)/len(vs_vals):.1f}")
print(f"  Min:      {min(vs_vals)}")
print(f"  Max:      {max(vs_vals)}")

print()
# Show ALL entries with vs < 20
print(f"=== ALL ENTRIES WITH vs < 20 ({len(under20)}) ===")
for m in matches:
    if int(m.group(2)) < 20:
        print(f"  {m.group(1):12s}  vs={m.group(2)}")

print()
# Show a few from each batch prefix to compare
prefixes = ["gz0","haa0","hab0","hac0","had0","hae0","haf0","hag0","hah0","hai0","haj0","hak0","hal0","ham0","han0"]
print("=== SAMPLE VS BY BATCH ===")
for pfx in prefixes:
    batch_vs = [(m.group(1), int(m.group(2))) for m in matches if m.group(1).startswith(pfx)]
    if batch_vs:
        avg = sum(v for _,v in batch_vs) / len(batch_vs)
        mn = min(v for _,v in batch_vs)
        mx = max(v for _,v in batch_vs)
        print(f"  {pfx}: count={len(batch_vs):3d}  avg={avg:.1f}  min={mn}  max={mx}")
