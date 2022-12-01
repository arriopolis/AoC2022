print(
    [
        (
            [
                (
                    (
                        elves.append(items.copy()),
                        items.clear()
                    ) if not line.strip() else
                        items.append(int(line.strip()))
                ) for line in open('input.txt')
            ],
            elves.append(items),
            max(list(map(sum, elves))),
        ) for elves,items in [([],[])]
    ][-1][-1]
)
