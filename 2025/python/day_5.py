from aoc import *

data = import_input(5)

range_texts, ids_texts = data.split("\n\n")
ranges = [range(a,b+1) for a,b in (nums(line) for line in range_texts.split("\n"))]
ids = nums(ids_texts)

total = 0
for i in ids:
    for r in ranges:
        if i in r:
            total += 1
            break

print(total)


ranges = [(a, b) for a,b in (nums(line) for line in range_texts.split("\n"))]
ranges.sort()
merged = [ranges.pop(0)]
for r in ranges:
    last = merged[-1]
    if r[0] <= last[1]:
        merged[-1] = (last[0], max(last[1], r[1]))
    else:
        merged.append(r)

total = 0
for r in merged:
    total += r[1] - r[0] + 1

print(total)
