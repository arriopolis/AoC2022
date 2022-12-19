import sys

grid = []
for line in sys.stdin:
    grid.append(list(map(int, line.strip())))

score = [[1]*len(grid[0]) for _ in grid]

for _ in range(4):

    # Look at visibility
    for j,r in enumerate(grid):
        num_visible = [0]*10
        for k,c in enumerate(r):
            score[j][k] *= num_visible[c]
            for l in range(c+1):
                num_visible[l] = 1
            for l in range(c+1,10):
                num_visible[l] += 1

    # Rotate over 90 degrees
    grid = list(map(list,zip(*map(reversed,grid))))
    score = list(map(list,zip(*map(reversed,score))))

print(max(sum(score, [])))
