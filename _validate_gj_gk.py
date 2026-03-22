import re, os, sys
sys.stdout.buffer.write(b"Starting validation...\n")
sys.stdout.buffer.flush()

DATA_JS = r"D:\projects\mapzimus-board\data.js"
with open(DATA_JS, encoding="utf-8") as f:
    raw = f.read()
existing_ids = set(re.findall(r'id:"([^"]+)"', raw))

batches = ["BATCH_GJ.py", "BATCH_GK.py"]
all_new_ids = []
errors = 0

for batch_file in batches:
    fp = os.path.join(r"D:\projects\mapzimus-board", batch_file)
    with open(fp, encoding="utf-8") as f:
        code = f.read()
    ids_in_batch = re.findall(r'mk\("([^"]+)"', code)
    sys.stdout.buffer.write(f"[{batch_file}] {len(ids_in_batch)} ideas\n".encode())
    seen = set()
    for id_ in ids_in_batch:
        if id_ in seen:
            sys.stdout.buffer.write(f"  ERROR: dupe within batch: {id_}\n".encode())
            errors += 1
        seen.add(id_)
    conflicts = [id_ for id_ in ids_in_batch if id_ in existing_ids]
    if conflicts:
        sys.stdout.buffer.write(f"  WARN: {len(conflicts)} already in data.js\n".encode())
    for line_num, line in enumerate(code.split("\n"), 1):
        if "mk(" in line:
            non_ascii = [c for c in line if ord(c) > 127]
            if non_ascii:
                sys.stdout.buffer.write(f"  ERROR line {line_num}: non-ASCII\n".encode())
                errors += 1
    all_new_ids.extend(ids_in_batch)

# Cross-batch
all_seen = set()
for id_ in all_new_ids:
    if id_ in all_seen:
        sys.stdout.buffer.write(f"  ERROR: cross-batch dupe: {id_}\n".encode())
        errors += 1
    all_seen.add(id_)

truly_new = len([id_ for id_ in all_new_ids if id_ not in existing_ids])
sys.stdout.buffer.write(f"\nTotal: {len(all_new_ids)} | Unique: {len(all_seen)} | New: {truly_new}\n".encode())
sys.stdout.buffer.write(f"Projected: {len(existing_ids) + truly_new}\n".encode())
sys.stdout.buffer.write(f"Errors: {errors}\n".encode())
result = "PASSED" if errors == 0 else "FAILED"
sys.stdout.buffer.write(f"VALIDATION {result}\n".encode())
sys.stdout.buffer.flush()
