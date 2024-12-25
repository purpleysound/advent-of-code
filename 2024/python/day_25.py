from aoc import *

data = import_input(25)


total = 0


gs = []

for gstring in data.split("\n\n"):
    gs.append([*map(list, zip(*grid(gstring)))])


keys = []
holes = []

for g in gs:
    key_bool = g[0][0] == "#"
    depths = []
    for row in g:
        depths.append(row.count("#")-1)
    if key_bool:
        keys.append(depths)
    else:
        holes.append(depths)
    

for key in keys:
    for hole in holes:
        if all(k + h <= 5 for k, h in zip(key, hole)):
            total += 1

print(total)
