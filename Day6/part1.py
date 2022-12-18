import sys

s = sys.stdin.read().strip()
for j,(a,b,c,d) in enumerate(zip(s[:-3], s[1:-2], s[2:-1], s[3:])):
    if len(set([a,b,c,d])) == 4:
        print(j+4)
        break
