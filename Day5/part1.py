import sys

lines = sys.stdin.readlines()
stacks = {}
while lines[1].rstrip():
    line = lines.pop(0).rstrip()
    ctr = 1
    while line:
        while line.startswith('    '):
            ctr += 1
            line = line[4:]
        if ctr not in stacks: stacks[ctr] = []
        stacks[ctr].insert(0, line[1])
        ctr += 1
        line = line[4:]

for line in lines[2:]:
    _,n,_,s,_,d = line.strip().split()
    n,s,d = map(int, (n,s,d))
    for _ in range(n):
        stacks[d].append(stacks[s].pop())

s = ''
for x,c in sorted(stacks.items()):
    s += c[-1]
print(s)
