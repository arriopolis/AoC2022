print(next(j for s in [open('input.txt').read().strip()] for j in range(14, len(s)) if len(set(s[j-14:j])) == 14))
