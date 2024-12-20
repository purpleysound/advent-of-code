from aoc import *

data = import_input(20)

total = 0
g = grid(data)
R = len(g)
C = len(g[0])

for r, row in enumerate(g):
    for c, cell in enumerate(row):
        if cell == "S":
            start = (r, c)
        if cell == "E":
            end = (r, c)

def bfs(g):
    q = [start]
    dist = {start: 0}
    while q:
        r, c = q.pop(0)
        if (r, c) == end:
            return dist
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and g[nr][nc] != "#" and (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))


base_dist = bfs(g)
path = set(base_dist.keys())
base = base_dist[end]

for r in range(1, R-1):

    for c in range(1, C-1):
        if g[r][c] == "#":
            if all(g[nr][nc] == "#" for nr, nc in  [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] if 0 <= nr < R and 0 <= nc < C):
                continue
            g[r][c] = "."
            if base - bfs(g)[end] >= 100:
                total += 1
            g[r][c] = "#"

print(total)


def get_20_circle(r, c):
    for dr in range(-20, 21):
        for dc in range(-20, 21):
            if abs(dr) + abs(dc) <= 20:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    yield (nr, nc), abs(dr) + abs(dc)

    
total2 = 0

for k, v in base_dist.items():
    for (nr, nc), nd in get_20_circle(*k):
        if (nr, nc) in path and v+nd <= base_dist[(nr, nc)]-100:
            total2 += 1

print(total2)
