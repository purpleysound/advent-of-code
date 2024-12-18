from aoc import *

data = import_input(18)

R = 71
C = 71

walls = []
for line in data.split("\n"):
    walls.append(tuple(nums(line)))


def get_neighbours(r, c, num_walls):
    for dr, dc in dirs4:
        nr, nc = r + dr, c + dc
        if nr in range(R) and nc in range(C) and (nr, nc) not in walls[:num_walls]:
            yield nr, nc


def bfs(num_walls):
    q = collections.deque([(0, 0)])
    dist = {(0, 0): 0}
    while q:
        r, c = q.popleft()
        if (r, c) == (R - 1, C - 1):
            return dist[(r, c)]
        for nr, nc in get_neighbours(r, c, num_walls):
            if (nr, nc) not in dist:
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))

print(bfs(1024))

def binary_search():
    low = 0
    high = len(walls)
    while low < high:
        mid = (low + high) // 2
        if bfs(mid) is None:
            high = mid
        else:
            low = mid + 1
    return low

i = binary_search()
print(walls[i-1])
