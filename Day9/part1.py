import sys

offsets = {
    'R' : (1,0),
    'D' : (0,-1),
    'U' : (0,1),
    'L' : (-1,0)
}

visited = set([(0,0)])
x,y = 0,0
dx,dy = 0,0
for line in sys.stdin:
    dir,n = line.strip().split()
    n = int(n)
    ox,oy = offsets[dir]

    for _ in range(n):
        x,y = x+ox,y+oy
        dx,dy = dx-ox,dy-oy

        if abs(dx) == 2 or abs(dy) == 2:
            if dx == -1: dx += 1
            if dy == -1: dy += 1
            dx //= 2
            dy //= 2

        visited.add((x+dx,y+dy))

print(len(visited))
