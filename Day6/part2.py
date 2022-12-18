import sys

s = sys.stdin.read().strip()
for j in range(14, len(s)):
    if len(set(s[j-14:j])) == 14:
        print(j)
        break
