from aoc import *

data = import_input(4)
# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

g = grid(data)
total = 0
for r, row in enumerate(g):
    for c, ch in enumerate(row):
        if ch == ".":
            continue
        neighbours = 0
        for dr, dc in dirs8:  
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= len(g) or nc < 0 or nc >= len(g[0]):
                continue
            if g[nr][nc] == "@":
                neighbours += 1
        if neighbours < 4:            
            total += 1

print(total)


g = grid(data)
total = 0
def cycle():
    ct = 0
    ng = [r[:] for r in g]
    changed = False
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            if ch == ".":
                continue
            neighbours = 0
            for dr, dc in dirs8:  
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= len(g) or nc < 0 or nc >= len(g[0]):
                    continue
                if g[nr][nc] == "@":
                    neighbours += 1
            if neighbours < 4:            
                ct += 1
                ng[r][c] = "."
                changed = True
                # print_(r,c)
    return ct, ng, changed

while True:
    ct, g, changed = cycle()
    total += ct
    if not changed:
        break

print(total)
