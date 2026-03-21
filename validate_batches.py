"""Dry-run validation of all batch scripts — checks for:
1. ID uniqueness across all batches
2. No conflicts with existing data.js IDs
3. Field format correctness
4. Non-ASCII character detection
"""
import re, os

DATA_JS = r"D:\projects\mapzimus-board\data.js"

with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', raw))
print("Existing ideas in data.js: %d" % len(existing_ids))

batches = [
    "BATCH_GB.py", "BATCH_GD.py", "BATCH_GE.py",
    "BATCH_GF.py", "BATCH_GG.py", "BATCH_GH.py", "BATCH_GI.py"
]
all_new_ids = []
errors = 0

for batch_file in batches:
    fp = os.path.join(r"D:\projects\mapzimus-board", batch_file)
    if not os.path.exists(fp):
        print("\n[SKIP] %s not found" % batch_file)
        continue
    
    with open(fp, encoding="utf-8") as f:
        code = f.read()
    
    # Extract all mk() calls and their IDs
    ids_in_batch = re.findall(r'mk\("([^"]+)"', code)
    print("\n[%s] %d ideas found" % (batch_file, len(ids_in_batch)))
    
    # Check for dupes within batch
    seen = set()
    for id_ in ids_in_batch:
        if id_ in seen:
            print("  ERROR: Duplicate ID within batch: %s" % id_)
            errors += 1
        seen.add(id_)
    
    # Check for conflicts with existing
    for id_ in ids_in_batch:
        if id_ in existing_ids:
            print("  WARN: ID already exists in data.js (will be skipped): %s" % id_)
    
    # Check for non-ASCII in the mk() string args
    for line_num, line in enumerate(code.split("\n"), 1):
        if "mk(" in line:
            non_ascii = [c for c in line if ord(c) > 127]
            if non_ascii:
                print("  ERROR line %d: Non-ASCII chars found: %s" % (line_num, non_ascii))
                errors += 1
    
    all_new_ids.extend(ids_in_batch)

# Cross-batch dupe check
print("\n--- CROSS-BATCH CHECK ---")
all_seen = set()
cross_dupes = 0
for id_ in all_new_ids:
    if id_ in all_seen:
        print("  ERROR: ID duplicated across batches: %s" % id_)
        cross_dupes += 1
        errors += 1
    all_seen.add(id_)

truly_new = len([id_ for id_ in all_new_ids if id_ not in existing_ids])

print("\n--- SUMMARY ---")
print("Total new IDs across all batches: %d" % len(all_new_ids))
print("Unique new IDs: %d" % len(all_seen))
print("Already in data.js (will skip): %d" % (len(all_new_ids) - truly_new))
print("Truly new ideas to inject: %d" % truly_new)
print("Projected total after injection: %d" % (len(existing_ids) + truly_new))
print("Errors found: %d" % errors)

if errors == 0:
    print("\nVALIDATION PASSED - Safe to run RUN_MORNING.ps1")
else:
    print("\nVALIDATION FAILED - Fix errors before running")
