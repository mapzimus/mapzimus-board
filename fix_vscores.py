"""
fix_vscores.py - Recompute all V-scores from the formula
Run: python fix_vscores.py && python maintain.py && git add . && git commit -m "Recompute all V-scores from formula - fix +1.6 mean drift, correct top-3 over-score by 6-8pts" && git push

V-Score formula:
  emotional   * 2.5  (highest weight - human impact story)
  relatability* 2.0  (high - do people feel this?)
  surprise    * 1.5  (counterintuitive?)
  tension     * 1.5  (political/social stakes)
  visual      * 1.0  (does it make a good map/chart?)
  data_ready  * 1.0  (can we actually build it?)
  originality * 0.5  (lowest - has anyone done this before?)

Max possible: 100
"""
import re

def compute_vs(sc):
    return round(
        sc.get('emotional', 0)    * 2.5 +
        sc.get('relatability', 0) * 2.0 +
        sc.get('surprise', 0)     * 1.5 +
        sc.get('tension', 0)      * 1.5 +
        sc.get('visual', 0)       * 1.0 +
        sc.get('data_ready', 0)   * 1.0 +
        sc.get('originality', 0)  * 0.5
    )

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find every idea line and update its vs
pattern = re.compile(
    r'(\{id:"[^"]+?".*?sc:\{)(emotional:\d+,relatability:\d+,surprise:\d+,tension:\d+,visual:\d+,data_ready:\d+,originality:\d+)(\},vs:)(\d+)(,tags:)',
    re.DOTALL
)

changes = []
no_match = []
total = 0

def replacer(m):
    global total
    total += 1
    sc_str = m.group(2)
    stated_vs = int(m.group(4))

    sc = {}
    for pair in re.finditer(r'(\w+):(\d+)', sc_str):
        sc[pair.group(1)] = int(pair.group(2))

    computed = compute_vs(sc)
    delta = stated_vs - computed

    if delta != 0:
        id_match = re.search(r'\{id:"([^"]+)"', m.group(1))
        id_val = id_match.group(1) if id_match else '?'
        changes.append({
            'id': id_val,
            'stated': stated_vs,
            'computed': computed,
            'delta': delta
        })
        return m.group(1) + m.group(2) + m.group(3) + str(computed) + m.group(5)

    return m.group(0)

new_content = pattern.sub(replacer, content)

# Report
print(f"Total ideas processed: {total}")
print(f"Ideas with V-score changes: {len(changes)}")
if changes:
    mean_delta = sum(c['delta'] for c in changes) / len(changes)
    print(f"Mean delta in changed ideas: {mean_delta:+.1f}")
    print()

    # Biggest corrections
    print(f"{'ID':<48} {'Old':>4} {'New':>4} {'Chg':>4}")
    print("-" * 65)

    by_abs = sorted(changes, key=lambda x: abs(x['delta']), reverse=True)
    for c in by_abs[:30]:
        arrow = 'v' if c['delta'] > 0 else '^'
        print(f"  {c['id']:<46} {c['stated']:>4} -> {c['computed']:>4}  ({arrow}{abs(c['delta'])})")

    if len(by_abs) > 30:
        print(f"  ... and {len(by_abs)-30} more small corrections")

    print()
    print("Breakdown:")
    over  = [c for c in changes if c['delta'] > 0]
    under = [c for c in changes if c['delta'] < 0]
    print(f"  Reduced (were over-scored): {len(over)}")
    print(f"  Increased (were under-scored): {len(under)}")
    print()

    # Distribution of deltas
    from collections import Counter
    delta_dist = Counter(c['delta'] for c in changes)
    print("Delta distribution:")
    for d in sorted(delta_dist.keys()):
        bar = '#' * delta_dist[d]
        print(f"  {d:+3d}: {bar} ({delta_dist[d]})")

# Write corrected file
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print()
print(f"Written. Now run: python maintain.py && git add . && git commit -m 'Recompute all V-scores from formula' && git push")
