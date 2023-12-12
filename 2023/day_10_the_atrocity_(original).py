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
visited = main_loop.copy()
inside = set()

# def bfs_escape(start, grid, already_visited):
#     queue = [start]
#     visited = set()
#     escaped = False
#     while queue:
#         r, c = queue.pop(0)
#         visited.add((r, c))
#         for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
#             nr, nc = r + dr, c + dc
#             if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
#                 escaped = True
#                 continue
#             if (nr, nc) not in visited and (nr, nc) not in already_visited :
#                 queue.append((nr, nc))
#     return visited, escaped

# for r, row in enumerate(grid):
#     for c, column in enumerate(row):
#         if (r, c) not in visited:
#             new_visited, escaped = bfs_escape((r, c), grid, main_loop|visited)
#             visited |= new_visited
#             if not escaped:
#                 inside |= new_visited

# print(len(inside))


main_loop = visited
visited = main_loop.copy()

def can_go_to(start, end, grid, main_loop, visited, already_visited):
    """need to somehow figure out how to jump off the edge of main_loop onto the correct side but not the incorrect side"""
    if end in already_visited or end in visited:
        return False
    if start not in main_loop:
        return True
    start = r, c
    if start in main_loop:
        for dr, dc in dirs[grid[r][c]]:
            if (r+dr, c+dc) == end:
                return True
    return False

def flood_fill(start, grid, main_loop, already_visited):
    if start in main_loop|already_visited:
        return set()
    queue = [start]
    visited = {start}
    while queue:
        r, c = queue.pop(0)
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]):
                continue
            if can_go_to((r, c), (nr, nc), grid, main_loop, visited, already_visited):
                queue.append((nr, nc))
                visited.add((nr, nc))
    return visited

max_height = len(grid)
max_width = len(grid[0])
outside = set()

for r in range(max_height):
    outside |= flood_fill((r, 0), grid, main_loop, outside)
    outside |= flood_fill((r, max_width-1), grid, main_loop, outside)
for c in range(max_width):
    outside |= flood_fill((0, c), grid, main_loop, outside)
    outside |= flood_fill((max_height-1, c), grid, main_loop, outside)
inside = {(r, c) for r in range(max_height) for c in range(max_width)} - main_loop - outside
# print(len(inside))
# Need to handle squeezing through the pipes

# from colorama import Fore
# for r, row in enumerate(grid):
#     for c, column in enumerate(row):
#         if (r, c) in main_loop:
#             print(Fore.RED + column, end="")
#         elif (r, c) in outside:
#             print(Fore.BLUE + column, end="")
#         else:
#             print(Fore.GREEN + column, end="")
#     print(Fore.RESET)

from PIL import Image, ImageDraw
img_width = 3*max_width
img_height = 3*max_height
img = Image.new("RGB", (img_width, img_height))
draw = ImageDraw.Draw(img)

def draw_shape(r, c, grid):
    letter = grid[r][c]
    letter_to_shape_offsets = {
        "|": [(0, 0), (1, 0), (-1, 0)],
        "-": [(0, 0), (0, 1), (0, -1)],
        "L": [(0, 0), (0, 1), (-1, 0)],
        "J": [(0, 0), (0, -1), (-1, 0)],
        "7": [(0, 0), (0, -1), (1, 0)],
        "F": [(0, 0), (0, 1), (1, 0)]
    }
    offsets = letter_to_shape_offsets[letter]
    for dr, dc in offsets:
        draw.point((img_width-(3*c+dc), 3*r+dr), (255, 0, 0))

def draw_outside(r, c, grid):
    offsets = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for dr, dc in offsets:
        draw.point((img_width-(3*c+dc), 3*r+dr), (0, 0, 0))

def draw_inside(r, c, grid):
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for dr, dc in offsets:
        draw.point((img_width-(3*c+dc), 3*r+dr), (0, 0, 0))
    draw.point((img_width-(3*c), 3*r), (255, 255, 255))


# for r, row in enumerate(grid):
#     for c, column in enumerate(row):
#         if (r, c) in main_loop:
#             # (r, c) = (-y, x)
#             draw_shape(r, c, grid)
#         elif (r, c) in outside:
#             draw_outside(r, c, grid)
#         else:
#             draw_inside(r, c, grid)
# img.show()
# img.save("day_10.png")
"""
I used fill bucket tool to find pixels connected to outside LMAO
In retrospect i couldve expanded the grid to make each square 3x3 then use flood fill
but it probably would've taken a while and this just came to my head and it was rly funny
"""
img = Image.open("day_10_modified.png") 
"""Not included in git repo bc its basically the input but this can be generated by the above commented out code
then using paint bucket tool to convert all outside ones to a different colour then back so only white pixels are inside
if you can do that in 10 seconds ig this counts as a real solution lmao"""
img = img.convert("RGB")
img_width, img_height = img.size
count = 0
for r in range(img_height):
    for c in range(img_width):
        if img.getpixel((c, r)) == (255, 255, 255):
            count += 1
print(count)

