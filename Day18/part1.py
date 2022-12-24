import sys

s = set()
for line in sys.stdin:
    x,y,z = map(int, line.strip().split(','))
    s.add((x,y,z))

ctr = 0
for x,y,z in s:
    for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        newx,newy,newz = x+dx,y+dy,z+dz
        if (newx,newy,newz) not in s:
            ctr += 1
print(ctr)
