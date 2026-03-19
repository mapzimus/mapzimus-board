with open(r'D:\projects\mapzimus-board\maintain.py','r',encoding='utf-8') as f: c=f.read()

# Add topics auto-assignment call inside add_clarity() so new batches get tagged
# Find the print statement at the end of add_clarity and insert the topics call before it
old = "    print(f'  [add_clarity] New clarity added: {added} | V-score recomputed: {recomputed}')"
new = """    # Also assign topics[] for any idea missing them
    from backfill_topics import assign_topics as _at
    topics_added = 0
    new_lines2 = []
    for line in new_lines:
        if (line.startswith(',{id:') or line.startswith('{id:')) and ',topics:[' not in line:
            topics = _at(line)
            topics_str = ',topics:[' + ','.join('"'+t+'"' for t in topics) + ']'
            for anchor in [',status:',',notes:',',tags:']:
                if anchor in line:
                    line = line.replace(anchor, topics_str + anchor, 1)
                    break
            topics_added += 1
        new_lines2.append(line)
    if topics_added:
        with open('data.js','w',encoding='utf-8') as f:
            f.write('\\n'.join(new_lines2))
    print(f'  [add_clarity] New clarity added: {added} | V-score recomputed: {recomputed} | Topics tagged: {topics_added}')"""

if old in c:
    c = c.replace(old, new)
    with open(r'D:\projects\mapzimus-board\maintain.py','w',encoding='utf-8') as f: f.write(c)
    print('maintain.py updated - topics auto-tagged on new batches')
else:
    print('Pattern not found - maintain.py unchanged')
    # Show where add_clarity ends
    idx = c.find('add_clarity')
    print(repr(c[idx:idx+200]))
