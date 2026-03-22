with open(r"D:\projects\mapzimus-board\maintain.py", "r", encoding="utf-8") as f:
    lines = f.readlines()
# Print lines 204-295 (the recalc_vs function area)
for i in range(203, min(295, len(lines))):
    print(f"{i+1:4d}: {lines[i].rstrip()}")
