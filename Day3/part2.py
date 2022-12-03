import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())

t = 0
while lines:
    a,b,c = lines[:3]
    s = set(a).intersection(b).intersection(c)
    s = s.pop()
    n = ord(s) - ord('a') + 1 if ord('a') <= ord(s) <= ord('z') else ord(s) - ord('A') + 27
    t += n
    lines = lines[3:]
print(t)
