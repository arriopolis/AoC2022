import sys

grid = []
for line in sys.stdin:
    grid.append(line.strip())

elves = set()
for y,r in enumerate(grid):
    for x,c in enumerate(r):
        if c == '#':
            elves.add((x,y))

offsets = list((x,y) for x in range(-1,2) for y in range(-1,2) if not x == y == 0)

proposals = [(0,-1), (0,1), (-1,0), (1,0)]

round = 0
change = True
while change:
    round += 1
    proposal_pos = {}
    for x,y in elves:
        # Check if there is insentive to move
        if all((x+dx,y+dy) not in elves for dx,dy in offsets): continue

        # Make a proposal
        for px,py in proposals:
            if px == 0 and any((x+dx, y+py) in elves for dx in range(-1,2)): continue
            if py == 0 and any((x+px, y+dy) in elves for dy in range(-1,2)): continue
            if (x+px, y+py) not in proposal_pos: proposal_pos[(x+px,y+py)] = set()
            proposal_pos[(x+px,y+py)].add((x,y))
            break

    # Execute proposals
    change = False
    for (x,y),s in proposal_pos.items():
        if len(s) == 1:
            oldx,oldy = s.pop()
            elves.remove((oldx,oldy))
            elves.add((x,y))
            change = True

    # Cycle proposal directions
    proposals = proposals[1:] + proposals[:1]

print(round)
