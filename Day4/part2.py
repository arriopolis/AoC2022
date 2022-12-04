import sys

t = 0
for line in sys.stdin:
    (a,b),(c,d) = map(lambda x : x.split('-'), line.strip().split(','))
    a,b,c,d = map(int, (a,b,c,d))
    if (a <= c and b >= c) or (b >= c and b <= d): t += 1
    else:
        a,b,c,d = c,d,a,b
        if (a <= c and b >= c) or (b >= c and b <= d): t += 1
print(t)
