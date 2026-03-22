import re

with open(r"D:\projects\mapzimus-board\data.js", "r", encoding="utf-8") as f:
    blob = f.read()

# Check the very first 20 entries
pattern = r'id:"([^"]+)".*?vs:(\d+)'
matches = list(re.finditer(pattern, blob))

print("=== FIRST 30 ENTRIES ===")
for m in matches[:30]:
    print(f"  {m.group(1):12s}  vs={m.group(2)}")

print()

# Check entries from earlier batches that are known to work
prefixes_old = ["ga0","gb0","gc0","gd0","ge0","gf0","gg0","gh0","gi0","gj0","gk0","gl0","gm0"]
print("=== SAMPLE VS BY OLD BATCH ===")
for pfx in prefixes_old:
    batch_vs = [(m.group(1), int(m.group(2))) for m in matches if m.group(1).startswith(pfx)]
    if batch_vs:
        avg = sum(v for _,v in batch_vs) / len(batch_vs)
        mn = min(v for _,v in batch_vs)
        mx = max(v for _,v in batch_vs)
        print(f"  {pfx}: count={len(batch_vs):3d}  avg={avg:.1f}  min={mn}  max={mx}")

# Also check some pre-batch entries (a001, b001 etc)
prefixes_pre = ["a0","b0","c0","d0","e0"]
print()
print("=== SAMPLE VS BY ORIGINAL ENTRIES ===")
for pfx in prefixes_pre:
    batch_vs = [(m.group(1), int(m.group(2))) for m in matches if m.group(1).startswith(pfx)]
    if batch_vs:
        avg = sum(v for _,v in batch_vs) / len(batch_vs)
        mn = min(v for _,v in batch_vs)
        mx = max(v for _,v in batch_vs)
        print(f"  {pfx}: count={len(batch_vs):3d}  avg={avg:.1f}  min={mn}  max={mx}")
