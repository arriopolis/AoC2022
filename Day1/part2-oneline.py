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
            sum(sorted(list(map(sum, elves)), reverse = True)[:3])
        ) for elves,items in [([],[])]
    ][-1][-1]
)
