from aoc import *
import heapq

data = import_input(16)


g = grid(data)
R = len(g)
C = len(g[0])
for r in range(R):
    for c in range(C):
        if g[r][c] == "S":
            start = (r, c)
        if g[r][c] == "E":
            end = (r, c)

total = 0


def bfs():
    q = []
    heapq.heappush(q, (0, start, iright))
    visited = {start: 0}
    min_score = float("inf")
    while q:
        score, (cr, cc), (ldr, ldc) = heapq.heappop(q)
        if (cr, cc) == end:
            min_score = min(min_score, score)
            continue
        nr, nc = cr + ldr, cc + ldc
        if 0 <= nr < R and 0 <= nc < C and g[nr][nc] != "#" and visited.get((nr, nc), float("inf")) >= score + 1:
            heapq.heappush(q, (score + 1, (nr, nc), (ldr, ldc)))
            visited[(nr, nc)] = score + 1
        for dr, dc in {(0, 1), (1, 0), (-1, 0), (0, -1)}.difference({(ldr, ldc), (-ldr, -ldc)}):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < R and 0 <= nc < C and g[nr][nc] != "#" and visited.get((nr, nc), float("inf")) >= score + 1001:
                heapq.heappush(q, (score + 1001, (nr, nc), (dr, dc)))
                visited[(nr, nc)] = score + 1001
    return min_score

min_score = bfs()
print(min_score)


def bfs_find_all():
    q = []
    heapq.heappush(q, (0, start, iright, set()))
    visited = {start: 0}
    nodes = {start, end}
    while q:
        score, (cr, cc), (ldr, ldc), traversed = heapq.heappop(q)
        nr, nc = cr + ldr, cc + ldc
        if (cr, cc) == end and score == min_score:
            nodes |= traversed
            continue
        if 0 <= nr < R and 0 <= nc < C and g[nr][nc] != "#" and visited.get((nr, nc), float("inf")) >= score - 1001:
            heapq.heappush(q, (score + 1, (nr, nc), (ldr, ldc), traversed.union({(nr, nc)})))
            visited[(nr, nc)] = score + 1
        for dr, dc in {(0, 1), (1, 0), (-1, 0), (0, -1)}.difference({(ldr, ldc), (-ldr, -ldc)}):
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < R and 0 <= nc < C and g[nr][nc] != "#" and visited.get((nr, nc), float("inf")) >= score - 1001:
                heapq.heappush(q, (score + 1001, (nr, nc), (dr, dc), traversed.union({(nr, nc)})))
                visited[(nr, nc)] = score + 1001
    return nodes


nodes = bfs_find_all()
print(len(nodes))
