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

xmax,ymax = max(x for x,y in grid),max(y for x,y in grid)

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
        for _ in range(instr):
            dx,dy = heading
            newx,newy = x+dx,y+dy
            newheading = heading

            nowrap = False
            if 50 <= newx <= 99 and newy == -1 and heading == (0,-1):
                newx,newy = 0, 150 + (newx - 50)
                newheading = (1,0)
            elif 100 <= newx <= 149 and newy == -1 and heading == (0,-1):
                newx,newy = newx - 100, 199
                newheading = (0,-1)
            elif newx == 49 and 0 <= newy <= 49 and heading == (-1,0):
                newx,newy = 0, 100 + (49 - newy)
                newheading = (1,0)
            elif newx == 150 and 0 <= newy <= 49 and heading == (1,0):
                newx,newy = 99, 100 + (49 - newy)
                newheading = (-1,0)
            elif 100 <= newx <= 149 and newy == 50 and heading == (0,1):
                newx,newy = 99, 50 + (newx - 100)
                newheading = (-1,0)
            elif newx == 49 and 50 <= newy <= 99 and heading == (-1,0):
                newx, newy = newy - 50, 100
                newheading = (0,1)
            elif newx == 100 and 50 <= newy <= 99 and heading == (1,0):
                newx,newy = 100 + (newy - 50), 49
                newheading = (0,-1)
            elif 0 <= newx <= 49 and newy == 99 and heading == (0,-1):
                newx,newy = 50, 50 + newx
                newheading = (1,0)
            elif newx == -1 and 100 <= newy <= 149 and heading == (-1,0):
                newx,newy = 50, 49 - (newy - 100)
                newheading = (1,0)
            elif newx == 100 and 100 <= newy <= 149 and heading == (1,0):
                newx,newy = 149, 49 - (newy - 100)
                newheading = (-1,0)
            elif 50 <= newx <= 99 and newy == 150 and heading == (0,1):
                newx,newy = 49, 150 + (newx - 50)
                newheading = (-1,0)
            elif newx == -1 and 150 <= newy <= 199 and heading == (-1,0):
                newx,newy = 50 + (newy - 150), 0
                newheading = (0,1)
            elif newx == 50 and 150 <= newy <= 199 and heading == (1,0):
                newx,newy = 50 + (newy - 150), 149
                newheading = (0,-1)
            elif 0 <= newx <= 49 and newy == 200 and heading == (0,1):
                newx,newy = 100 + newx, 0
                newheading = (0,1)
            else:
                nowrap = True

            assert (newx,newy) in grid, f"{newx,newx} is not in the grid. Left from {x,y}."

            if (newx,newy) in walls: break

            x,y = newx,newy
            heading = newheading
    elif instr == 'L':
        heading = turn_left[heading]
    else:
        heading = turn_right[heading]

heading_score = {(1,0) : 0, (0,1) : 1, (-1,0) : 2, (0,-1) : 3}
print(1000 * (y+1) + 4 * (x+1) + heading_score[heading])
