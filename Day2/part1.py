import sys

scores = {'X' : 1, 'Y' : 2, 'Z' : 3}
outcomes = {
    'A' : {'X' : 3, 'Y' : 6, 'Z' : 0},
    'B' : {'X' : 0, 'Y' : 3, 'Z' : 6},
    'C' : {'X' : 6, 'Y' : 0, 'Z' : 3}
}

tot = 0
for line in sys.stdin:
    a,b = line.strip().split()
    tot += scores[b]
    tot += outcomes[a][b]
print(tot)
