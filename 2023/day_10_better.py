import aoc

data = aoc.import_input(10)
# data = """FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L"""
grid = [list(line) for line in data.split("\n")]
for r, row in enumerate(grid):
    for c, column in enumerate(row):
        if column == "S":
            start = (r, c)
            grid[r][c] = "|" #REAL INPUT
            # grid[r][c] = "7" #TEST INPUT

#dirs are handles in (row, column) format, not (x, y) so they look like (-y, x)
dirs = {"|": [(1, 0), (-1, 0)], "-": [(0,1), (0, -1)], "L": [(-1, 0), (0, 1)], "J": [(-1, 0), (0, -1)], "7": [(1, 0), (0, -1)], "F": [(1, 0), (0, 1)], ".": []}

def bfs(start, grid):
    queue = [start]
    visited = set()
    dist = {start: 0}
    while queue:
        r, c = queue.pop(0)
        visited.add((r, c))
        for dr, dc in dirs[grid[r][c]]:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and grid[nr][nc] != ".":
                queue.append((nr, nc))
                dist[(nr, nc)] = dist[(r, c)] + 1
    return dist, visited

dist, visited = bfs(start, grid)
print(max(dist.values()))

main_loop = visited
max_height = len(grid)
max_width = len(grid[0])
count = 0
# I kinda didn't come up with this myself, i saw someone used "Jordan Curve Theorem" on reddit and i looked it up
# The other solution i did come up with it but its awful so i just wanted to make this to compensate
for r, row in enumerate(grid):
    for c, column in enumerate(row):
        if (r, c) in main_loop:
            continue
        inside = False
        for nr, nc in zip(range(r, max_height+1), range(c, max_width+1)):
            if (nr, nc) in main_loop:
                if grid[nr][nc] in "|-JF":
                    inside = not inside
        count += inside
print(count)