import sys

scores = {'X' : 1, 'Y' : 2, 'Z' : 3}
outcomes = {
    'A' : {'X' : 3, 'Y' : 6, 'Z' : 0},
    'B' : {'X' : 0, 'Y' : 3, 'Z' : 6},
    'C' : {'X' : 6, 'Y' : 0, 'Z' : 3}
}
choices = {
    'A' : {'X' : 'Z', 'Y' : 'X', 'Z' : 'Y'},
    'B' : {'X' : 'X', 'Y' : 'Y', 'Z' : 'Z'},
    'C' : {'X' : 'Y', 'Y' : 'Z', 'Z' : 'X'}
}

tot = 0
for line in sys.stdin:
    a,b = line.strip().split()
    b = choices[a][b]
    tot += scores[b]
    tot += outcomes[a][b]
print(tot)
