import sys

WALL = 0
SAND = 1

grid = {}
for line in sys.stdin:
    vertices = line.strip().split(' -> ')
    vertices = [tuple(map(int, v.split(','))) for v in vertices]
    for (x1,y1),(x2,y2) in zip(vertices[:-1], vertices[1:]):
        dx,dy = x2-x1,y2-y1
        if dx != 0: dx //= abs(dx)
        if dy != 0: dy //= abs(dy)
        while (x1,y1) != (x2,y2):
            grid[(x1,y1)] = WALL
            x1 += dx
            y1 += dy
    grid[vertices[-1]] = WALL

ymax = max(y for x,y in grid.keys())

ctr = -1
stop = True
while stop:
    x,y = 500,0
    while True:
        if (x,y+1) not in grid:
            y += 1
        elif (x-1,y+1) not in grid:
            y += 1
            x -= 1
        elif (x+1,y+1) not in grid:
            y += 1
            x += 1
        else:
            grid[(x,y)] = SAND
            break

        if y > ymax:
            stop = False
            break
    ctr += 1
print(ctr)
