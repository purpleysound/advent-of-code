import aoc

data = aoc.import_input(1)

total = 0
total2 = 0
lefts = []
rights = []
for line in data.split("\n"):
    a, b = aoc.get_nums_negative(line)
    lefts.append(a)
    rights.append(b)

lefts.sort()
rights.sort()
for a, b in zip(lefts, rights):
    total += abs(a-b)
    total2 += a * rights.count(a)

print(total)
print(total2)
