import sys

nums = []
for line in sys.stdin:
    nums.append(line.strip())

vals = {'2': 2, '1' : 1, '0' : 0, '-' : -1, '=' : -2}

t = 0
for num in nums:
    s = 0
    for c in num:
        s *= 5
        s += vals[c]
    t += s

chars = {-2 : '=', -1 : '-', 0 : '0', 1 : '1', 2 : '2'}

res = ''
while t != 0:
    t += 2
    x = (t % 5) - 2
    t //= 5
    res = chars[x] + res
print(res)
