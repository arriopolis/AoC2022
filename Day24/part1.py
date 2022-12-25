import sys

lines = []
for line in sys.stdin:
    lines.append(list(line.strip()))

h,w = len(lines)-2,len(lines[0])-2

grid = [[set() for _ in range(w)] for _ in range(h)]
for y,r in enumerate(lines):
    for x,c in enumerate(r):
        if c == '>': grid[y-1][x-1].add((1,0))
        if c == '<': grid[y-1][x-1].add((-1,0))
        if c == 'v': grid[y-1][x-1].add((0,1))
        if c == '^': grid[y-1][x-1].add((0,-1))

offsets = [(0,0),(-1,0),(1,0),(0,-1),(0,1)]
avail = set([(0,-1)])

t = 0
while (w-1,h) not in avail:
    t += 1

    new_grid = [[set() for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            for dx,dy in grid[y][x]:
                newx,newy = (x+dx)%w,(y+dy)%h
                new_grid[newy][newx].add((dx,dy))
    grid = new_grid

    new_avail = set()
    for x,y in avail:
        for dx,dy in offsets:
            newx,newy = x+dx,y+dy
            if not (0 <= newx < w and 0 <= newy < h) and (newx,newy) not in [(0,-1),(w-1,h)]: continue
            if 0 <= newx < w and 0 <= newy < h and len(grid[newy][newx]) > 0: continue
            new_avail.add((newx,newy))
    avail = new_avail
print(t)
