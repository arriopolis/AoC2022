import sys
from functools import cmp_to_key

def compare(a,b):
    if not isinstance(a, list) and not isinstance(b, list):
        return 1 if a < b else -1 if a > b else 0
    if not isinstance(a, list) and isinstance(b, list):
        return compare([a],b)
    if isinstance(a, list) and not isinstance(b, list):
        return compare(a,[b])
    for x,y in zip(a[:len(b)],b):
        res = compare(x,y)
        if res != 0: return res
    return 1 if len(a) < len(b) else -1 if len(a) > len(b) else 0

lines = [
    [[2]],
    [[6]]
]
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    lines.append(eval(line))

lines.sort(key = cmp_to_key(compare), reverse = True)
for j,line in enumerate(lines):
    if line == [[2]]:
        idx1 = j+1
    if line == [[6]]:
        idx2 = j+1
print(idx1*idx2)
