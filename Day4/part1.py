import sys

t = 0
for line in sys.stdin:
    (a,b),(c,d) = map(lambda x : x.split('-'), line.strip().split(','))
    a,b,c,d = map(int, (a,b,c,d))
    if (a <= c and b >= d) or (c <= a and d >= b): t += 1
print(t)
