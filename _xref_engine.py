"""
Cross-Reference Engine: Analyze existing 4497 ideas to find novel correlations
and generate new, highly original XREF ideas by combining datasets that
haven't been combined yet.

Strategy:
1. Extract all unique data sources (tbl) and topics
2. Build a co-occurrence matrix of what's already been combined
3. Find HIGH-POTENTIAL uncombined pairs using semantic similarity
4. Generate XREF ideas from the best novel pairs
"""
import re, os, json, random
from collections import Counter, defaultdict
from itertools import combinations

DATA = os.path.join(os.path.dirname(__file__), 'data.js')

def parse_all():
    with open(DATA, 'r', encoding='utf-8') as f:
        text = f.read()
    entries = []
    for line in text.split('\n'):
        line = line.strip().lstrip(',')
        if not line.startswith('{id:'):
            continue
        e = {}
        for key in ['id','title','sub','type','geo','fmt','section','tbl']:
            m = re.search(r'\b'+key+r':"([^"]*)"', line)
            if m: e[key] = m.group(1)
        entries.append(e)
    return entries

entries = parse_all()
print(f"Loaded {len(entries)} entries")

# Extract unique sections, data sources, formats, and geo scopes
sections = Counter(e.get('section','') for e in entries)
tbls = Counter(e.get('tbl','') for e in entries)
fmts = Counter(e.get('fmt','') for e in entries)
geos = Counter(e.get('geo','') for e in entries)
types = Counter(e.get('type','') for e in entries)

print(f"\nSections: {len(sections)}")
print(f"Unique data sources: {len(tbls)}")
print(f"Types: {dict(types)}")

# Find existing XREF entries to see what's been combined
existing_xrefs = [e for e in entries if e.get('type') == 'XREF']
print(f"\nExisting XREF ideas: {len(existing_xrefs)}")


# Build section-pair co-occurrence to find what cross-section combos are underexplored
section_pairs = Counter()
for e in existing_xrefs:
    title = e.get('title','').lower()
    sub = e.get('sub','').lower()
    sects = set()
    for s in sections:
        if s and (s.lower() in title or s.lower() in sub):
            sects.add(s)
    # Also use the section field itself
    sects.add(e.get('section',''))
    for a, b in combinations(sorted(sects), 2):
        if a and b:
            section_pairs[(a,b)] += 1

# All possible section pairs and their coverage
all_sections = [s for s in sections if s and sections[s] >= 5]
print(f"\nActive sections (5+ entries): {len(all_sections)}")

total_pairs = len(all_sections) * (len(all_sections)-1) // 2
covered_pairs = len(section_pairs)
print(f"Total possible section pairs: {total_pairs}")
print(f"Pairs with existing XREFs: {covered_pairs}")
print(f"Uncovered pairs: {total_pairs - covered_pairs}")

# Find the most INTERESTING uncombined section pairs
# Score by: sum of entry counts (more data = more potential)
uncovered = []
for a, b in combinations(sorted(all_sections), 2):
    if (a,b) not in section_pairs and (b,a) not in section_pairs:
        score = sections[a] + sections[b]
        uncovered.append((score, a, b))
uncovered.sort(reverse=True)

print(f"\nTop 30 uncombined section pairs (by data richness):")
for score, a, b in uncovered[:30]:
    print(f"  {a} x {b} (combined entries: {score})")

# Extract keyword themes from titles for smarter matching
title_words = Counter()
for e in entries:
    for w in re.findall(r'[A-Z][a-z]+|[a-z]+', e.get('title','')):
        if len(w) > 3:
            title_words[w.lower()] += 1

print(f"\nTop 40 title keywords:")
for w, c in title_words.most_common(40):
    print(f"  {w}: {c}")
