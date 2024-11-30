
with open("inputs/day_3.txt") as f:
    data = f.read()

g = [*map(list, data.split("\n"))]
min_trees = 9999999999999999999

slope = 3
c = 0
trees = 0
for r, row in enumerate(g):
    if g[r][c] == "#":
        trees += 1
    c += slope
    c %= len(g[0])
min_trees = min(min_trees, trees)

print(f"Part 1: {min_trees}")

p = 1
for slope in [1, 3, 5, 7]:
    c = 0
    trees = 0
    for r, row in enumerate(g):
        if g[r][c] == "#":
            trees += 1
        c += slope
        c %= len(g[0])
    p *= trees

slope = 1
c = 0
trees = 0
for r, row in enumerate(g[::2]):
    if g[2*r-1][c] == "#":
        trees += 1
    c += slope
    c %= len(g[0])
p *= trees
print(f"Part 2: {p}")
