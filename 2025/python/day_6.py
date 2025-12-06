from aoc import *

data = import_input(6)
lines = data.splitlines()
ops = lines.pop().split()

g = [nums(line) for line in lines]
g = [*map(list, zip(*g))]

total = 0
for r, op in zip(g, ops):
    if op == "+":
        total += sum(r)
    elif op == "*":
        total += functools.reduce(lambda x, y: x * y, r, 1)

print(total)


g = [*map(list, zip(*data.splitlines()))]
problems = []
p = []
for line in g:
    if all(ch == " " for ch in line):
        problems.append(p)
        p = []
    else:
        p.append("".join(line))
problems.append(p)

total = 0
for p in problems:
    op = p[0][-1]
    l = map(lambda x: int(x[:-1].strip()), p)
    if op == "+":
        total += sum(l)
    elif op == "*":
        total += functools.reduce(lambda x, y: x * y, l, 1)

print(total)
