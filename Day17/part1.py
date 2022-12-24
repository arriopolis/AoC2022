import sys

push_pattern = sys.stdin.read().strip()

rocks = [
    set([(0,0), (1,0), (2,0), (3,0)]),
    set([(0,1), (1,0), (1,1), (1,2), (2,1)]),
    set([(0,0), (1,0), (2,0), (2,1), (2,2)]),
    set([(0,0), (0,1), (0,2), (0,3)]),
    set([(0,0), (0,1), (1,0), (1,1)])
]
push_dict = {
    '>' : 1,
    '<' : -1
}

ymax = 0
grid = set()

step = 0
for i in range(2022):
    rock = rocks[i%len(rocks)]
    x,y = 2,ymax+3

    while True:
        push = push_pattern[step%len(push_pattern)]
        dx = push_dict[push]
        step += 1

        # Try the push
        rock_poss = set([(x+dx+rx, y+ry) for rx,ry in rock])
        if all(0 <= rx < 7 for rx,ry in rock_poss) and not rock_poss.intersection(grid):
            x += dx

        # Try the fall
        rock_poss = set([(x+rx, y-1+ry) for rx,ry in rock])
        if all(ry >= 0 for rx,ry in rock_poss) and not rock_poss.intersection(grid):
            y -= 1
        else:
            grid.update([(x+rx, y+ry) for rx,ry in rock])
            ymax = max(ry+1 for rx,ry in grid)
            break

print(ymax)
