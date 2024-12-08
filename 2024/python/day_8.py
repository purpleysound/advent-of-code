import aoc
from collections import defaultdict
from itertools import combinations

data = aoc.import_input(8)

total = 0
total2 = 0

grid = [*map(list, data.split("\n"))]
R = len(grid)
C = len(grid[0])

locs = defaultdict(list)

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != ".":
            locs[ch].append((r, c))

unique = set()
unique2 = set()

for k, v in locs.items():
    for pair in combinations(v, 2):
        r1, c1 = pair[0]
        r2, c2 = pair[1]
        dr, dc = r2 - r1, c2 - c1

        if r1 - dr in range(R) and c1 - dc in range(C):
            unique.add((r1 - dr, c1 - dc))
        if r2 + dr in range(R) and c2 + dc in range(C):
            unique.add((r2 + dr, c2 + dc))

        unique2.add((r1, c1))
        unique2.add((r2, c2))
        while r1 - dr in range(R) and c1 - dc in range(C):
            r1 -= dr
            c1 -= dc
            unique2.add((r1, c1))
        while r2 + dr in range(R) and c2 + dc in range(C):
            r2 += dr
            c2 += dc
            unique2.add((r2, c2))

print(len(unique))
print(len(unique2))
