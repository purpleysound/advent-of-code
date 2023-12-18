import aoc
from heapq import heappush, heappop

data = aoc.import_input(17)
# data = """2413432311323
# 3215453535623
# 3255245654254
# 3446585845452
# 4546657867536
# 1438598798454
# 4457876987766
# 3637877979653
# 4654967986887
# 4564679986453
# 1224686865563
# 2546548887735
# 4322674655533"""

    
grid = [list(r) for r in data.split("\n")]
SIZE = len(grid)
LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)
DIRS = [LEFT, RIGHT, UP, DOWN]

def get_allowed_nodes(r, c, last_dir, last_dir_times, dist, visited):
    for new_dir in DIRS:
        dr, dc = new_dir
        nr = r+dr
        nc = c+dc
        if new_dir == last_dir:
            if last_dir_times == 3:
                continue
            else:
                nlast_dir_times = last_dir_times + 1
        elif new_dir == aoc.vector_scale(last_dir, -1):
            continue
        else:
            nlast_dir_times = 1
        nlast_dir = new_dir
        if (nr, nc, (nlast_dir, nlast_dir_times)) in visited:
            continue
        if nr not in range(SIZE) or nc not in range(SIZE):
            continue
        ndist = dist + int(grid[nr][nc])
        yield nr, nc, (nlast_dir, nlast_dir_times), ndist

def dijkstra():
    unvisited = [(0, (0, 0), (dir, 0)) for dir in DIRS]
    visited = set([(0, 0, (dir, 0)) for dir in DIRS])
    dist_dict = {(0, 0, (dir, 0)): 0 for dir in DIRS}
    while unvisited:
        node = heappop(unvisited)
        dist, (r, c), (last_dir, last_dir_times) = node
        for new_node in get_allowed_nodes(r, c, last_dir, last_dir_times, dist, visited):
            nr, nc, (nlast_dir, nlast_dir_times), ndist = new_node
            heappush(unvisited, (ndist, (nr, nc), (nlast_dir, nlast_dir_times)))
            visited.add(new_node[:3])
            dist_dict[new_node[:3]] = ndist
    return dist_dict


dist = dijkstra()
print(min(dist[x] for x in dist if x[0] == SIZE-1 and x[1] == SIZE-1))



def get_allowed_nodes(r, c, last_dir, last_dir_times, dist, visited):
    for new_dir in DIRS:
        dr, dc = new_dir
        nr = r+dr
        nc = c+dc
        if new_dir == aoc.vector_scale(last_dir, -1):
            continue
        elif new_dir == last_dir:
            if last_dir_times == 10:
                continue
            else:
                nlast_dir_times = last_dir_times + 1
        else:
            if last_dir_times < 4:
                continue
            else:
                nlast_dir_times = 1
        nlast_dir = new_dir
        if (nr, nc, (nlast_dir, nlast_dir_times)) in visited:
            continue
        if nr not in range(SIZE) or nc not in range(SIZE):
            continue
        ndist = dist + int(grid[nr][nc])
        yield nr, nc, (nlast_dir, nlast_dir_times), ndist


def dijkstra():
    unvisited = [(0, (0, 0), (dir, 0)) for dir in DIRS]
    visited = set([(0, 0, (dir, 0)) for dir in DIRS])
    dist_dict = {(0, 0, (dir, 0)): 0 for dir in DIRS}
    while unvisited:
        node = heappop(unvisited)
        dist, (r, c), (last_dir, last_dir_times) = node
        for new_node in get_allowed_nodes(r, c, last_dir, last_dir_times, dist, visited):
            nr, nc, (nlast_dir, nlast_dir_times), ndist = new_node
            heappush(unvisited, (ndist, (nr, nc), (nlast_dir, nlast_dir_times)))
            visited.add(new_node[:3])
            dist_dict[new_node[:3]] = ndist
    return dist_dict

dist = dijkstra()
print(min(dist[x] for x in dist if x[0] == SIZE-1 and x[1] == SIZE-1 and x[2][1]>=4))