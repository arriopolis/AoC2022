import sys

monkeys = []
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    if line.startswith('Monkey'):
        monkeys.append({'action' : {}, 'num_inspected' : 0})
    elif line.startswith('Starting items:'):
        monkeys[-1]['items'] = list(map(int,line.split(':')[1].strip().split(', ')))
    elif line.startswith('Operation:'):
        monkeys[-1]['operation'] = line.split(':')[1].strip()
    elif line.startswith('Test'):
        test = line.split(':')[1].strip()
        assert test.startswith('divisible by')
        monkeys[-1]['test'] = int(test.split()[-1])
    elif line.startswith('If'):
        val = line.split()[1].strip().rstrip(':')
        assert val in ['true','false']
        action = line.split(':')[1].strip()
        assert action.startswith('throw to monkey')
        monkeys[-1]['action'][val == 'true'] = int(action.split()[-1])

for _ in range(20):
    for m in monkeys:
        items = m['items'].copy()
        m['items'].clear()
        for i in items:
            old = i
            exec(m['operation'])
            i = new // 3
            monkeys[m['action'][i%m['test']==0]]['items'].append(i)
            m['num_inspected'] += 1

num_inspects = [m['num_inspected'] for m in monkeys]
num_inspects.sort(reverse = True)
print(num_inspects[0] * num_inspects[1])
