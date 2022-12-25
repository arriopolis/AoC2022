import sys

lines = []
for line in sys.stdin:
    if not line.strip(): break
    lines.append(line.rstrip('\n'))

grid = set()
walls = set()
for y,r in enumerate(lines):
    for x,c in enumerate(r):
        if c == ' ': continue
        grid.add((x,y))
        if c == '#': walls.add((x,y))

xmins,xmaxs,ymins,ymaxs = {},{},{},{}
for x,y in grid:
    if y not in xmins: xmins[y] = x
    if y not in xmaxs: xmaxs[y] = x
    if x not in ymins: ymins[x] = y
    if x not in ymaxs: ymaxs[x] = y
    xmins[y] = min(xmins[y],x)
    xmaxs[y] = max(xmaxs[y],x)
    ymins[x] = min(ymins[x],y)
    ymaxs[x] = max(ymaxs[x],y)

instr = next(sys.stdin).strip()
instrs = []
s = ''
for c in instr:
    if c in '0123456789':
        s += c
    else:
        if s:
            instrs.append(int(s))
            s = ''
        instrs.append(c)
if s:
    instrs.append(int(s))

x,y = xmins[0],0
heading = (1,0)

turn_right = {(1,0) : (0,1), (0,1) : (-1,0), (-1,0) : (0,-1), (0,-1) : (1,0)}
turn_left = {(0,1) : (1,0), (-1,0) : (0,1), (0,-1) : (-1,0), (1,0) : (0,-1)}

for instr in instrs:
    if isinstance(instr, int):
        dx,dy = heading
        for _ in range(instr):
            newx,newy = x+dx,y+dy
            if (newx,newy) not in grid:
                if heading == (1,0): newx = xmins[newy]
                if heading == (-1,0): newx = xmaxs[newy]
                if heading == (0,1): newy = ymins[newx]
                if heading == (0,-1): newy = ymaxs[newx]
            if (newx,newy) in walls: break
            x,y = newx,newy
    elif instr == 'L':
        heading = turn_left[heading]
    else:
        heading = turn_right[heading]

heading_score = {(1,0) : 0, (0,1) : 1, (-1,0) : 2, (0,-1) : 3}
print(1000 * (y+1) + 4 * (x+1) + heading_score[heading])
