import sys

grid = []
for line in sys.stdin:
    grid.append(list(map(int, line.strip())))

visible = [[False]*len(grid[0]) for _ in grid]

for _ in range(4):

    # Look at visibility
    for j,r in enumerate(grid):
        m = -1
        for k,c in enumerate(r):
            if c > m: visible[j][k] = True
            m = max(m,c)

    # Rotate over 90 degrees
    grid = list(map(list,zip(*map(reversed,grid))))
    visible = list(map(list,zip(*map(reversed,visible))))

print(sum(sum(visible, [])))
