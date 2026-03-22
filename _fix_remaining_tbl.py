"""Fix the 3 remaining local path tbl values."""
import re, os

DATA = os.path.join(os.path.dirname(__file__), 'data.js')
with open(DATA, 'r', encoding='utf-8') as f:
    text = f.read()

fixes = {
    'D:/eBay + thrift.xls': 'eBay/Thrift Store: Market pricing data (ebay.com)',
    "Kaggle: Raw Data/Sage Data + D:/Raw Data/Fivethirtyeight (kaggle.com/datasets/archive-(39)-+-d:)": 'Sage Data + FiveThirtyEight: Combined dataset (sagepub.com + fivethirtyeight.com)',
    "Kaggle: Raw Data/Sage Data + D:/Raw Data/Kaggle/Archive (48)/Fuel Prices 1970 2026 (kaggle.com/datas": 'Sage Data + Kaggle: Fuel Prices 1970-2026 (sagepub.com + kaggle.com/datasets/fuel-prices)',
}

lines = text.split('\n')
changed = 0
for i, line in enumerate(lines):
    for old, new in fixes.items():
        if old in line:
            line = line.replace(old, new)
            lines[i] = line
            changed += 1
            print(f"Fixed: {old[:60]} -> {new[:60]}")

with open(DATA, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print(f"\nFixed {changed} remaining entries")
