print(sum(scores[b] + outcomes[a][b] for scores,outcomes in [({'X' : 1, 'Y' : 2, 'Z' : 3},{'A' : {'X' : 3, 'Y' : 6, 'Z' : 0},'B' : {'X' : 0, 'Y' : 3, 'Z' : 6},'C' : {'X' : 6, 'Y' : 0, 'Z' : 3}})] for line in open('input.txt') for a,b in [line.strip().split()]))