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
grid = set([(x,-1) for x in range(7)])

graph = {}

step = 0
i = 0
while True:
    rock = rocks[i%len(rocks)]

    # Check if we have seen this situation before
    state = (i%len(rocks), step%len(push_pattern), tuple(sorted(grid)))
    if state in graph: break

    # If not, then simulate
    dstep = 0
    x,y = 2,3
    while True:
        push = push_pattern[(step + dstep)%len(push_pattern)]
        dx = push_dict[push]
        dstep += 1

        # Try the push
        rock_poss = set([(x+dx+rx, y+ry) for rx,ry in rock])
        if all(0 <= rx < 7 for rx,ry in rock_poss) and not rock_poss.intersection(grid):
            x += dx

        # Try the fall
        rock_poss = set([(x+rx, y-1+ry) for rx,ry in rock])
        if not rock_poss.intersection(grid):
            y -= 1
        else:
            grid.update([(x+rx, y+ry) for rx,ry in rock])
            dymax = max(ry+1 for rx,ry in grid)

            # Strip the grid
            new_grid = set()
            frontier = set([(x, dymax) for x in range(7)])
            visited = set()
            while frontier:
                visited.update(frontier)
                new_frontier = set()
                for x,y in frontier:
                    for dx,dy in [(-1,0),(1,0),(0,-1)]:
                        if not 0 <= x+dx < 7: continue
                        if (x+dx,y+dy) in grid:
                            new_grid.add((x+dx,y+dy-dymax))
                        elif (x+dx,y+dy) not in visited:
                            new_frontier.add((x+dx,y+dy))
                frontier = new_frontier

            graph[state] = (dstep, dymax, new_grid.copy())

            grid = new_grid
            step += dstep
            ymax += dymax

            i += 1
            break

start_state = state
start_i = i
start_ymax = ymax

new_state = None
while new_state != start_state:
    dstep, dymax, new_grid = graph[state]
    step += dstep
    ymax += dymax
    i += 1
    new_state = (i%len(rocks), step%len(push_pattern), tuple(sorted(new_grid)))
    state = new_state

di = i - start_i
dymax = ymax - start_ymax

TARGET = 1000000000000

k = (TARGET - i) // di
i += k * di
ymax += k * dymax

while i < TARGET:
    dstep, dymax, new_grid = graph[state]
    step += dstep
    ymax += dymax
    i += 1
    new_state = (i%len(rocks), step%len(push_pattern), tuple(sorted(new_grid)))
    state = new_state

print(ymax)
