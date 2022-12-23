import sys

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

lines = []
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    lines.append(eval(line))

assert len(lines)%2 == 0

t = 0
for j,(a,b) in enumerate(zip(lines[::2], lines[1::2])):
    if compare(a,b) == 1:
        t += j+1
print(t)
