"""Fix backslash paths in BATCH_GJ.py mk() calls to use forward slashes."""
fp = r"D:\projects\mapzimus-board\BATCH_GJ.py"
with open(fp, encoding="utf-8") as f:
    content = f.read()
# Replace D:\raw_data paths with forward slashes
content = content.replace("D:\\\\raw_data\\\\kaggle\\\\", "D:/raw_data/kaggle/")
content = content.replace("D:\\raw_data\\kaggle\\", "D:/raw_data/kaggle/")
# Fix remaining filename backslashes
import re
content = re.sub(r'(?<=kaggle/)([^"]*?)\\', lambda m: m.group(0).replace("\\", "/"), content)
with open(fp, "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed BATCH_GJ.py paths")
