import aoc
from collections import deque

data = aoc.import_input(18)
# data = """R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)"""
instructions = data.split("\n")
cur = (0, 0)
edge = set([cur])
dir_dict = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
for instruction in instructions:
    dir_string, scalar, colour = instruction.split(" ")
    dir_vec = dir_dict[dir_string]
    for _ in range(int(scalar)):
        cur = aoc.vector_add(cur, dir_vec)
        edge.add(cur)

xs = [x[0] for x in edge]
maxx, minx = max(xs), min(xs)
ys = [y[1] for y in edge]
maxy, miny = max(ys), min(ys)

def print_grid():
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            if (x,y) in edge:
                print("#", end="")
            else:
                print(".", end="")
        print()
# print_grid()

# Jordan Curve Theorem strikes back

def check_inside(x, y):
    if (x, y) in edge:
        return False
    inside = False
    in_edge = False
    for nx in range(x, maxx+2):
        if (nx, y) in edge:
            in_edge = True
        else:
            if in_edge:
                inside = not inside
            in_edge = False
    return inside

inside = set()
for x in range(minx-1, maxx+2):
    for y in range(miny-1, maxy+2):
        if check_inside(x,y):
            # print(x, y)
            inside.add((x,y))
# doesnt work lmao im just using it to get a guess at an inside coord for flood fill, this works *most* of the time
random_coord = inside.pop()

def flood_fill(start):
    q = deque([start])
    visited = set([start])
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x+dx
            ny = y+dy
            if (nx, ny) in edge or (nx, ny) in visited:
                continue
            visited.add((nx,ny))
            q.append((nx, ny))
    return visited

inside = flood_fill(random_coord)
print(len(edge|inside))





instructions = data.split("\n")
cur = (0, 0)
vertices = [cur]
edge_vertices = 0
dir_dict = {"3": (0, 1), "1": (0, -1), "2": (-1, 0), "0": (1, 0)}
for instruction in instructions:
    _, _, colour = instruction.split(" ")
    magnitude = int(colour[2:7], 16)
    direction = dir_dict[colour[7]]
    cur = aoc.vector_add(cur, aoc.vector_scale(direction, magnitude))
    vertices.append(cur)
    edge_vertices += magnitude
# print(vertices)
    
total = 0
for i in range(len(vertices)-1):
    total += vertices[i][0]*vertices[i+1][1] - vertices[i][1]*vertices[i+1][0]
total_area = abs(total//2)  # Shoelace Formula
print(total_area + edge_vertices//2 + 1)  # Pick's Theorem

