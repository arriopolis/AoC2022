import sys

t = 0
for line in sys.stdin:
    items = list(line.strip())
    c1,c2 = items[:len(items)//2],items[len(items)//2:]
    s = set(c1).intersection(c2)
    s = s.pop()
    n = ord(s) - ord('a') + 1 if ord('a') <= ord(s) <= ord('z') else ord(s) - ord('A') + 27
    t += n
print(t)
