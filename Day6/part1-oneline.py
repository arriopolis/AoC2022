print(next(j for s in [open('input.txt').read().strip()] for j in range(4, len(s)) if len(set(s[j-4:j])) == 4))
