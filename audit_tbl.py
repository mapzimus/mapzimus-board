"""audit_tbl.py - Find all tbl fields that are just T-codes with no human-readable source name"""
import re, collections

with open(r'D:\projects\mapzimus-board\data.js','r',encoding='utf-8') as f:
    content = f.read()

lines = [l for l in content.split('\n') if l.startswith(',{id:') or l.startswith('{id:')]

tbl_pattern = re.compile(r',tbl:"([^"]+)"')
t_code_only = re.compile(r'^[T\d\s\-–—|]+$')  # only T-codes, numbers, dashes

t_code_tbls = collections.Counter()
total = 0
for line in lines:
    m = tbl_pattern.search(line)
    if m:
        tbl = m.group(1)
        total += 1
        if re.match(r'^T\d', tbl):  # starts with T followed by digit
            t_code_tbls[tbl] += 1

print('Total ideas:', total)
print('Ideas with T-code tbl:', sum(t_code_tbls.values()))
print()
print('All unique T-code tbl values:')
for tbl, count in sorted(t_code_tbls.items(), key=lambda x: x[0]):
    print('  %s  [%d]' % (tbl, count))
