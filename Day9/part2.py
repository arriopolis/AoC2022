import sys

offsets = {
    'R' : (1,0),
    'D' : (0,-1),
    'U' : (0,1),
    'L' : (-1,0)
}

visited = set([(0,0)])
x,y = 0,0
dxs = [(0,0)]*9
for line in sys.stdin:
    dir,n = line.strip().split()
    n = int(n)
    ox,oy = offsets[dir]

    for _ in range(n):
        x,y = x+ox,y+oy
        for j in range(9):
            dx,dy = dxs[j]
            dx -= ox
            dy -= oy
            prevdx,prevdy = dxs[j-1] if j > 0 else (0,0)
            ddx,ddy = dx-prevdx,dy-prevdy

            if abs(ddx) == 2 or abs(ddy) == 2:
                if ddx == -1: ddx += 1
                if ddy == -1: ddy += 1
                ddx //= 2
                ddy //= 2

            dx,dy = prevdx+ddx, prevdy+ddy
            dxs[j] = (dx,dy)

        lastdx,lastdy = dxs[-1]
        visited.add((x+lastdx,y+lastdy))

print(len(visited))
