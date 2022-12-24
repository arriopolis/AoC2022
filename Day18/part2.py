import sys

s = set()
for line in sys.stdin:
    x,y,z = map(int, line.strip().split(','))
    s.add((x,y,z))

xmin,xmax = min(x for x,y,z in s),max(x for x,y,z in s)
ymin,ymax = min(y for x,y,z in s),max(y for x,y,z in s)
zmin,zmax = min(z for x,y,z in s),max(z for x,y,z in s)

outside = set()
frontier = set([(xmin-1,ymin-1,zmin-1)])
while frontier:
    outside.update(frontier)
    new_frontier = set()
    for x,y,z in frontier:
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
            newx,newy,newz = x+dx,y+dy,z+dz
            if not xmin-1 <= newx <= xmax+1: continue
            if not ymin-1 <= newy <= ymax+1: continue
            if not zmin-1 <= newz <= zmax+1: continue
            if (newx,newy,newz) not in s and (newx,newy,newz) not in outside:
                new_frontier.add((newx,newy,newz))
    frontier = new_frontier

ctr = 0
for x,y,z in s:
    for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        newx,newy,newz = x+dx,y+dy,z+dz
        if (newx,newy,newz) in outside:
            ctr += 1
print(ctr)
