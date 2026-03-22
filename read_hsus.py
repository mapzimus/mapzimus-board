f = open(r"D:\projects\mapzimus-board\profile_hsus.txt", encoding="utf-8")
lines = f.readlines()
f.close()
for l in lines[:80]:
    print(l.rstrip())
