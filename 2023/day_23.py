import aoc
from collections import deque

data = aoc.import_input(23)
# data = """#.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#"""
grid = [list(row) for row in data.split("\n")]
# print(len(grid), len(grid[0]))
SIZE = len(grid)
START = (0, 1)
END = (SIZE-1, SIZE-2)
SLOPES = {">": [(0, 1)],"<": [(0, -1)],"v": [(1, 0)],"^": [(-1, 0)]}
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def get_neighbours(cur_pos, visited):
    r, c = cur_pos
    ch = grid[r][c]
    for dr, dc in SLOPES.get(ch, DIRS): #possible directions
        nr = r+dr
        nc = c+dc
        if nr not in range(SIZE) or nc not in range(SIZE):
            continue
        if grid[nr][nc] == "#":
            continue
        if (nr, nc) in visited:
            continue
        yield (nr, nc)
        

def dfs():
    visited = set([START])
    q = deque([(START, 0, visited)])
    max_depth = 0
    while q:
        cur_pos, cur_depth, visited = q.pop()
        if cur_pos == END:
            max_depth = max(cur_depth, max_depth)
        for new_pos in get_neighbours(cur_pos, visited):
            new_visited = visited.copy()
            new_visited.add(new_pos)
            q.append((new_pos, cur_depth+1, new_visited))
    return max_depth

        
max_depth = dfs()
print(max_depth)





def get_neighbours(cur_pos, visited):
    r, c = cur_pos
    ch = grid[r][c]
    for dr, dc in DIRS: #possible directions
        nr = r+dr
        nc = c+dc
        if nr not in range(SIZE) or nc not in range(SIZE):
            continue
        if grid[nr][nc] == "#":
            continue
        if (nr, nc) in visited:
            continue
        yield (nr, nc)


def find_edges():
    q = deque([(START, START, 0)])
    # (cur, last junction, steps since last junction)
    visited = set([START])
    edges: list[list[tuple[int, int], tuple[int, int], int]] = []
    while q:
        cur, last_junction, steps = q.popleft()
        neighbours = list(get_neighbours(cur, visited))
        new_steps = steps + 1
        if len(neighbours) >= 2 or cur == END:
            edges.append([last_junction, cur, new_steps])
            last_junction = cur
            new_steps = 0
        for new_pos in neighbours:
            visited.add(new_pos)
            q.append((new_pos, last_junction, new_steps))
    return edges


def find_edges():
    EMPTY = set()
    junctions = [START, END]
    for r in range(SIZE):
        for c in range(SIZE):
            if len(list(get_neighbours((r, c), EMPTY))) >= 3:
                junctions.append((r, c))
    edge_dict = {}
    for junction in junctions:
        q = deque([(junction, 0)])
        visited = set([junction])
        ends = []
        while q:
            cur, dist = q.popleft()
            new_dist = dist+1
            for neighbour in get_neighbours(cur, visited):
                visited.add(neighbour)
                if neighbour in junctions:
                    ends.append((neighbour, new_dist))
                    continue
                q.append((neighbour, new_dist))
        edge_dict[junction] = ends
    return edge_dict


EDGES = find_edges()
# print(EDGES) 
# print(END)


def get_neighbours(cur_pos, visited):
    for next_node, distance in EDGES[cur_pos]:
        if next_node in visited:
            continue
        yield next_node, distance


def dfs():
    visited = set([START])
    q = deque([(START, 0, visited)])
    max_depth = 0
    while q:
        cur_pos, cur_depth, visited = q.pop()
        if cur_pos == END:
            max_depth = max(cur_depth, max_depth)
        for new_pos, dist in get_neighbours(cur_pos, visited):
            new_visited = visited.copy()
            new_visited.add(new_pos)
            q.append((new_pos, cur_depth+dist, new_visited))
    return max_depth

print(dfs())
