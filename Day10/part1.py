import sys

x = 1
num_cycles = 0
i = 0

s = 0
for line in sys.stdin:
    cmds = line.strip().split()
    if cmds[0] == 'noop':
        num_cycles += 1
    elif cmds[0] == 'addx':
        num_cycles += 2
        newx = x + int(cmds[1])
    if num_cycles >= 40*i+20:
        s += (40*i+20)*x
        i += 1
    x = newx

print(s)
