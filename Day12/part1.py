import sys

grid = []
for j,line in enumerate(sys.stdin):
    grid.append([])
    for k,c in enumerate(line.strip()):
        if c == 'S':
            x,y = k,j
            h = 0
        elif c == 'E':
            tx,ty = k,j
            h = 25
        else:
            h = ord(c) - ord('a')
        grid[-1].append(h)

h,w = len(grid),len(grid[0])
num_steps = 0
visited = set()
frontier = set([(x,y)])
while frontier:
    num_steps += 1
    visited.update(frontier)
    new_frontier = set()
    for x,y in frontier:
        for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
            newx,newy = x+dx,y+dy
            if not 0 <= newx < w: continue
            if not 0 <= newy < h: continue
            if (newx,newy) in visited: continue
            if grid[newy][newx] - grid[y][x] > 1: continue
            new_frontier.add((newx,newy))
    if (tx,ty) in new_frontier: break
    frontier = new_frontier
print(num_steps)
