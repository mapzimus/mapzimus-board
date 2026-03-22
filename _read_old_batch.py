import os
# Find a batch from before GX
for f in sorted(os.listdir(r"D:\projects\mapzimus-board")):
    if f.startswith("BATCH_G") and f.endswith(".py") and f < "BATCH_GX":
        fp = os.path.join(r"D:\projects\mapzimus-board", f)
        with open(fp, "r") as fh:
            content = fh.read()
        # Find the mk function
        if "def mk(" in content:
            start = content.index("def mk(")
            end = content.index("\n\n", start)
            print(f"=== {f} mk() function ===")
            print(content[start:end])
            print()
            break
        else:
            print(f"{f}: no mk() found")
