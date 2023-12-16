import aoc

data = aoc.import_input(16)
# data = r""".|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|...."""
grid = [list(r) for r in data.split("\n")]
LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)
VERT = [UP, DOWN]
HORIZ = [LEFT, RIGHT]
SIZE = len(grid)

def get_next_tiles(r, c, d):
    to_consider = []
    add = lambda nd: (*aoc.vector_add((r, c), nd), nd)  # cba to write this out every time, ik this is bad shhh
    match grid[r][c]:
        case ".":
            #forward
            to_consider.append(add(d))
        case "-":
            if d in HORIZ:
                to_consider.append(add(d))
            elif d in VERT:
                to_consider.append(add(LEFT))
                to_consider.append(add(RIGHT))
            else:
                raise RuntimeError
        case "|":
            if d in VERT:
                #forward
                to_consider.append(add(d))
            elif d in HORIZ:
                to_consider.append(add(UP))
                to_consider.append(add(DOWN))
            else:
                raise RuntimeError
        case "/":
            if d == RIGHT:
                to_consider.append(add(UP))
            elif d == UP:
                to_consider.append(add(RIGHT))
            elif d == LEFT:
                to_consider.append(add(DOWN))
            elif d == DOWN:
                to_consider.append(add(LEFT))
            else:
                raise RuntimeError
        case "\\":  # grrrrr (also why tf doesnt r"\" work </3)
            if d == RIGHT:
                to_consider.append(add(DOWN))
            elif d == UP:
                to_consider.append(add(LEFT))
            elif d == LEFT:
                to_consider.append(add(UP))
            elif d == DOWN:
                to_consider.append(add(RIGHT))
            else:
                raise RuntimeError
        case _:
            raise RuntimeError
    considered = []
    for move in to_consider:
        if move[0] in range(SIZE) and move[1] in range(SIZE):
            considered.append(move)
    return considered            


def traverse(start):
    queue = [start]
    energised = {start[:2]}
    visited = set(queue)
    while queue:
        r, c, d = queue.pop()
        for nr, nc, (nd) in get_next_tiles(r, c, d):
            if (nr, nc, nd) not in visited:
                queue.append((nr, nc, nd))
                visited.add((nr, nc, nd))
                energised.add((nr, nc))
    return energised

def print_grid(energised):
    import colorama
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if (r, c) in energised:
                print(colorama.Fore.RED+ch, end="")
            else:
                print(colorama.Fore.RESET+ch, end="")
        print(colorama.Fore.RESET)

energised = traverse((0, 0, RIGHT))
# print_grid(energised)
print(len(energised))



most = 0
for r in range(SIZE):
    most = max(most, len(traverse((r, 0, RIGHT))))
    most = max(most, len(traverse((r, SIZE-1, LEFT))))
for c in range(SIZE):
    most = max(most, len(traverse((0, c, DOWN))))
    most = max(most, len(traverse((SIZE-1, c, UP))))
print(most)