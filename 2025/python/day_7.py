from aoc import *

data = import_input(7)


g = grid(data)
for r, row in enumerate(g):
    for c, col in enumerate(row):
        if col == "S":
            start = (r, c)


q = collections.deque()
q.append(start)
beams = set()
visited = set()
hit = set()
while q:
    r, c = q.popleft()
    if r >= len(g):
        continue
    if g[r][c] == "^":
        if (r, c) not in beams:
            beams.add((r, c))
        if (r+1, c-1) not in visited:
            visited.add((r+1, c-1))
            q.append((r+1, c-1))
        if (r+1, c+1) not in visited:
            visited.add((r+1, c+1))
            q.append((r+1, c+1))
    else:
        if (r+1, c) not in visited:
            visited.add((r+1, c))
            q.append((r+1, c))

print(len(beams))

@functools.lru_cache(None)
def search(start):
    if start[0] >= len(g):
        return 1
    r, c = start
    total = 0
    if g[r][c] == "^":
        total += search((r+1, c-1))
        total += search((r+1, c+1))
    else:
        total += search((r+1, c))
    return total

print(search(start))
