print(next(
    ''.join([c[-1] for x,c in sorted(stacks.items())])
    for lines in [open('input.txt').readlines()]
    for stacks in [{}]
    for _ in [[
        None
        for _ in range(len(lines))
        if lines[1].rstrip()
        for _ in [
            (
                stacks.update({ctr[0] : []}) if ctr[0] not in stacks else None,
                stacks[ctr[0]].insert(0, line[1]) if not line[:4] == [' ',' ',' ',' '] else None,
                [line.pop(0) for _ in range(4)],
                ctr.append(ctr.pop()+1)
            )
            for line in [list(lines.pop(0))]
            for ctr in [[1]]
            for _ in range(len(line)//4)
        ]
    ]]
    for _ in [[
        (
            stacks[d].extend(stacks[s][-n:]),
            [stacks[s].pop() for _ in range(n)]
        )
        for line in lines[2:]
        for _,n,_,s,_,d in [line.strip().split()]
        for n,s,d in [map(int, (n,s,d))]
    ]]
))
