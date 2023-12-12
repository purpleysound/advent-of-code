import aoc

data = aoc.import_input(11)
# data = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""
old = [list(line) for line in data.split("\n")]
new = []
for i, line in enumerate(old):
    new.append(line.copy())
    if "#" not in line:
        # print(f"No galaxies in row {i}")
        new.append(line.copy())

transposed_old = list(map(list, zip(*new)))
transposed_new = []

for i, line in enumerate(transposed_old):
    transposed_new.append(line.copy())
    if "#" not in line:
        # print(f"No galaxies in column {i}")
        transposed_new.append(line.copy())

# print("\n".join("".join(line) for line in transposed_new))

galaxies = []
for r, row in enumerate(transposed_new):
    for c, column in enumerate(row):
        if column == "#":
            galaxies.append((r, c))

total = 0
for i, gal1 in enumerate(galaxies[:-1]):
    for gal2 in galaxies[i+1:]:
        # print(gal1, gal2)
        x1, y1 = gal1
        x2, y2 = gal2
        distx = abs(x2 - x1)
        disty = abs(y2 - y1)
        total += distx + disty

print(total)

# data = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""


old = [list(line) for line in data.split("\n")]
empty_rows = []
for i, line in enumerate(old):
    if "#" not in line:
        # print(f"No galaxies in row {i}")
        empty_rows.append(i)

transposed_old = list(map(list, zip(*new)))
transposed_new = []
empty_columns = []

for i, line in enumerate(transposed_old):
    transposed_new.append(line.copy())
    if "#" not in line:
        # print(f"No galaxies in column {i}")
        empty_columns.append(i)

galaxies = []
for r, row in enumerate(old):
    for c, column in enumerate(row):
        if column == "#":
            galaxies.append((r, c))

total = 0
for i, gal1 in enumerate(galaxies[:-1]):
    for gal2 in galaxies[i+1:]:
        # print(gal1, gal2)
        r1, c1 = gal1
        r2, c2 = gal2
        distr = abs(r2 - r1)
        distc = abs(c2 - c1)
        for empty in empty_rows:
            if empty in range(min(r1, r2), max(r1, r2)):
                distr += 1000000-1
        for empty in empty_columns:
            if empty in range(min(c1, c2), max(c1, c2)):
                distc += 1000000-1
        total += distr + distc
print(total)