from aoc import *

data = import_input(10)
# data = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""

g = grid(data)
R = len(g)
C = len(g[0])

def get_adjacent(r, c):
    return [vadd((r, c), (dr, dc)) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= r + dr < R and 0 <= c + dc < C and int(g[r + dr][c + dc]) - int(g[r][c]) == 1]


def bfs(r, c):
    q = [(r, c)]
    seen = set()
    nines = set()
    while q:
        r, c = q.pop(0)
        if int(g[r][c]) == 9:
            nines.add((r, c))
        if (r, c) in seen:
            continue
        seen.add((r, c))
        for nr, nc in get_adjacent(r, c):
            if (nr, nc) not in seen:
                q.append((nr, nc))
    return nines


def count_ways_to_nines(r, c):
    q = [(r, c)]
    seen = set()
    ways = {}
    ways[(r, c)] = 1
    while q:
        r, c = q.pop(0)
        for nr, nc in get_adjacent(r, c):
            if (nr, nc) not in seen:
                q.append((nr, nc))
                seen.add((nr, nc))
            if (nr, nc) in ways:
                ways[(nr, nc)] += ways[(r, c)]
            else:
                ways[(nr, nc)] = ways[(r, c)]
    return {k: v for k, v in ways.items() if int(g[k[0]][k[1]]) == 9}


total = 0
total2 = 0


for r, row in enumerate(g):
    for c, ch in enumerate(row):
        if ch == '0':
            total += len(bfs(r, c))
            total2 += sum(count_ways_to_nines(r, c).values())

print(total)
print(total2)
