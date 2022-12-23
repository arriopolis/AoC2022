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

y = 2000000
intervals = set()
for (sx,sy),(bx,by) in sensors.items():
    d = abs(sx-bx) + abs(sy-by)
    dy = abs(sy-y)
    dx = d - dy
    if dx < 0: continue
    intervals.add((sx-dx,sx+dx))

t = 0
cur_max = float('-inf')
for xmin,xmax in sorted(intervals):
    if xmin > cur_max:
        t += xmax - xmin + 1
        cur_max = xmax
    elif xmax > cur_max:
        t += xmax - cur_max
        cur_max = xmax

beacons = set(sensors.values())
for bx,by in beacons:
    if by == y and any(xmin <= bx <= xmax for xmin,xmax in intervals):
        t -= 1
print(t)
