with open(r"D:\projects\mapzimus-board\profile_kaggle_new_output.txt", encoding="utf-8", errors="replace") as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")
for line in lines[:200]:
    print(line, end="")
