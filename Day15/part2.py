import sys

sensors = {}
for line in sys.stdin:
    sensor,beacon = line.strip().split(': ')
    assert sensor.startswith('Sensor at ')
    assert beacon.startswith('closest beacon is at')

    x,y = sensor.split()[-2:]
    assert x.startswith('x=')
    assert y.startswith('y=')
    sensorx = int(x.split('=')[-1].rstrip(','))
    sensory = int(y.split('=')[-1])

    x,y = beacon.split()[-2:]
    assert x.startswith('x=')
    assert y.startswith('y=')
    beaconx = int(x.split('=')[-1].rstrip(','))
    beacony = int(y.split('=')[-1])

    sensors[(sensorx,sensory)] = (beaconx, beacony)

beacons = set(sensors.values())

for y in range(4000001):
    print(y, end = '\r')
    intervals = set()
    for (sx,sy),(bx,by) in sensors.items():
        d = abs(sx-bx) + abs(sy-by)
        dy = abs(sy-y)
        dx = d - dy
        if dx < 0: continue
        intervals.add((sx-dx,sx+dx))

    cur_max = -1
    for xmin,xmax in sorted(intervals):
        if xmin > cur_max + 1 and (cur_max + 1, y) not in beacons:
            res = (cur_max + 1,y)
            print()
            print(res)
        if xmax > cur_max:
            cur_max = xmax

print()
print(res[0] * 4000000 + res[1])
