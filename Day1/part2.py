import sys

elves = []
items = []
for line in sys.stdin:
    if not line.strip():
        elves.append(items)
        items = []
    else:
        items.append(int(line.strip()))
elves.append(items)
calories = list(map(sum, elves))

calories.sort(reverse = True)
print(sum(calories[:3]))
