import sys

x = 1
num_cycles = 0

grid = [[]]
for line in sys.stdin:
    cmds = line.strip().split()

    new_cycles = num_cycles
    if cmds[0] == 'noop':
        new_cycles += 1
    elif cmds[0] == 'addx':
        new_cycles += 2
        newx = x + int(cmds[1])

    for c in range(num_cycles,new_cycles):
        if c%40 == 0:
            grid.append([])
        grid[-1].append('#' if abs((c%40)-x)<=1 else '.')
    num_cycles = new_cycles
    x = newx

for g in grid:
    print(''.join(g))
