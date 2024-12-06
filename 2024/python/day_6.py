import aoc

data = aoc.import_input(6)
# data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""


total = 0

grid = [*map(list, data.split("\n"))]

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "^":
            start = (r, c)
            break


seen = set()
dir = (-1, 0)
cur = start
seen.add(cur)
while True:
    nr, nc = (cur[0] + dir[0], cur[1] + dir[1])
    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
        break
    if grid[nr][nc] == "#":
        dir = (dir[1], -dir[0])
    else:
        cur = (nr, nc)
    seen.add(cur)

print(len(seen))


def can_escape(grid):
    dir = (-1, 0)
    cur = start
    seen2 = set()
    seen2.add((cur, dir))
    while True:
        nr, nc = (cur[0] + dir[0], cur[1] + dir[1])
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            return True
        if grid[nr][nc] == "#":
            dir = (dir[1], -dir[0])
        else:
            cur = (nr, nc)
        if (cur, dir) in seen2:
            return False
        seen2.add((cur, dir))


for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == ".":
            grid[r][c] = "#"
            if not can_escape(grid):
                total += 1
            grid[r][c] = "."


print(total)
