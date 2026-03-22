import sys
fp = r"D:\projects\mapzimus-board\_ind_results.txt"
with open(fp, encoding="utf-8") as f:
    content = f.read()
# Write to stdout byte by byte to force flush
sys.stdout.buffer.write(content.encode("utf-8"))
sys.stdout.buffer.flush()
