import sys

monkeys = {}
for line in sys.stdin:
    name, op = line.strip().split(': ')
    monkeys[name] = op

def evaluate(name):
    expression = monkeys[name]
    parts = expression.split()
    if len(parts) == 1:
        return expression

    for x in parts[::2]:
        val = evaluate(x)
        expression = expression.replace(x, val)
    expression = str(eval(expression.replace('/','//')))
    monkeys[name] = expression
    return expression

print(evaluate('root'))
