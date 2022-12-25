import sys
from math import sqrt

KEY = 811589153

cnts = {}
seq = []
for line in sys.stdin:
    n = int(line.strip())
    if n not in cnts: cnts[n] = 0
    seq.append((n*KEY, cnts[n]))
    cnts[n] += 1

s = round(sqrt(len(seq)))

prevs = {}
nexts = {}
for x,y in zip(seq, seq[1:] + seq[:1]):
    prevs[y] = x
    nexts[x] = y

long_prevs = {}
long_nexts = {}
for x,y in zip(seq, seq[s:] + seq[:s]):
    long_prevs[y] = x
    long_nexts[x] = y

for _ in range(10):
    for x in seq:
        # Remove x
        px,nx = prevs[x],nexts[x]
        prevs[nx] = px
        nexts[px] = nx

        ppx = long_prevs[x]
        new_nx = nx
        for _ in range(s):
            long_prevs[new_nx] = ppx
            long_nexts[ppx] = new_nx
            new_nx = nexts[new_nx]
            ppx = nexts[ppx]

        # Find the new position
        y = x[0]
        y %= len(seq)-1

        new_nx = nx
        while y > 0:
            if y >= s:
                new_nx = long_nexts[new_nx]
                y -= s
            else:
                new_nx = nexts[new_nx]
                y -= 1
        new_px = prevs[new_nx]

        # Insert x
        nexts[new_px] = x
        prevs[new_nx] = x
        prevs[x] = new_px
        nexts[x] = new_nx

        ppx = long_prevs[new_nx]
        curx = x
        for _ in range(s+1):
            long_nexts[ppx] = curx
            long_prevs[curx] = ppx
            curx = nexts[curx]
            ppx = nexts[ppx]

x = (0,0)
t = 0
for _ in range(3):
    y = 1000 % len(seq)
    while y > 0:
        if y >= s:
            x = long_nexts[x]
            y -= s
        else:
            x = nexts[x]
            y -= 1
    t += x[0]
print(t)
