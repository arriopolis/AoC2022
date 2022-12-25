import sys

monkeys = {}
for line in sys.stdin:
    name, op = line.strip().split(': ')
    monkeys[name] = op

left,right = monkeys['root'].split(' + ')
monkeys['root'] = left + ' = ' + right

def evaluate(name):
    if name == 'humn': return 'humn'

    expression = monkeys[name]
    parts = expression.split()
    if len(parts) == 1:
        return expression

    success = True
    for x in parts[::2]:
        val = evaluate(x)
        if val == x:
            success = False
        else:
            expression = expression.replace(x, val)

    if success:
        expression = str(eval(expression.replace('/','//')))
        monkeys[name] = expression
        return expression
    else:
        monkeys[name] = expression
        return name

evaluate('root')

name = 'root'
res = None
while name != 'humn':
    expression = monkeys[name]
    left,op,right = expression.split()

    if all(c in '-0123456789' for c in left):
        n = int(left)
        new_name = right
        unknown_right = True
    else:
        n = int(right)
        new_name = left
        unknown_right = False

    if op == '=':
        res = n
    elif op == '+':
        res -= n
    elif op == '*':
        res //= n
    elif op == '-':
        if not unknown_right:
            res += n
        else:
            res = n-res
    elif op == '/':
        if not unknown_right:
            res *= n
        else:
            res = n//res

    name = new_name
print(res)
