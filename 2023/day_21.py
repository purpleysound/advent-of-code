import aoc
from collections import deque

data = aoc.import_input(21)
STEPS = 64-1
# data = """...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ..........."""
# STEPS = 6-1
grid = [list(row) for row in data.split("\n")]
SIZE = len(grid)
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "S":
            grid[r][c] == "."
            start = (r, c)


DIRS = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(start):
    q = deque([(start, STEPS)])
    visited = set()
    reacheable = set()
    while q:
        (r, c), remaining_steps = q.popleft()
        for dr, dc in DIRS:
            nr = r+dr
            nc = c+dc
            ns = remaining_steps-1
            if nr not in range(SIZE) or nc not in range(SIZE):
                continue
            if grid[nr][nc] == "#":
                continue
            if (nr, nc) in visited:
                continue
            if remaining_steps % 2 == 0:
                reacheable.add((nr, nc))
            visited.add((nr,nc))
            if remaining_steps == 0:
                continue
            q.append(((nr, nc), ns))
    return reacheable

def print_reachable(reachable):
    for r in range(SIZE):
        for c in range(SIZE):
            if (r,c) in reachable:
                print("O", end="")
            else:
                print(grid[r][c], end="")
        print()

reachable = bfs(start)
# print_reachable(reachable)
print(len(reachable)) 

# STEPS = 5000
STEPS = 26501365

# From any corner the answer is the same since from a repeated grid it always takes 2 steps to get to a different corner
FROM_CORNER = {True: len(bfs((0, 0))), False: len(bfs((0, 1)))}
#From start is True parity
# print(FROM_CORNER)

def how_far_from_centre_to_corner():
    q = deque([(start, 0)])
    visited = set()
    reacheable = set()
    while q:
        (r, c), remaining_steps = q.popleft()
        for dr, dc in DIRS:
            nr = r+dr
            nc = c+dc
            ns = remaining_steps+1
            if nr not in range(SIZE) or nc not in range(SIZE):
                continue
            if nr in [0, SIZE-1] and nc in [0, SIZE-1]:
                print(f"{(nr, nc)}, at dist {ns}")
            if grid[nr][nc] == "#":
                continue
            if (nr, nc) in visited:
                continue
            # if remaining_steps % 2 == 0:
            #     reacheable.add((nr, nc))
            visited.add((nr,nc))
            # if remaining_steps == 0:
            #     continue
            q.append(((nr, nc), ns))
    # return reacheable 
            
# print(how_far_from_centre_to_corner())
CENTRE_TO_CORNER = SIZE-1 #130
CENTRE_TO_EDGE = SIZE//2 #65
# 26501365 = 65 + 202300*131
# pattern goes like 1, 4; 9, 4; 9, 16; 25, 16? leads up in squares
#at             65 + 131; 65+2*131..
# 202300 is even so (202300+1)**2 Trues and  202300**2 Falses
# then gotta add and subtract cut off corners at end???
# print(FROM_CORNER[True]*((202300+1)**2)+FROM_CORNER[False]*202300**2) #is too high
# cut corners are probably across the "diamond" shape in input bc eric is a silly guy

def bfs(start):
    q = deque([(start, STEPS)])
    visited = set()
    reacheable = set()
    while q:
        (r, c), remaining_steps = q.popleft()
        for dr, dc in DIRS:
            nr = r+dr
            nc = c+dc
            ns = remaining_steps-1
            if grid[nr%SIZE][nc%SIZE] == "#":
                continue
            if (nr, nc) in visited:
                continue
            if remaining_steps % 2 == 0:
                reacheable.add((nr, nc))
            visited.add((nr,nc))
            if remaining_steps == 0:
                continue
            q.append(((nr, nc), ns))
    return reacheable


# for i in range(10):
#     STEPS = 64+i*131 #constant go brr
#     print(len(bfs(start)))
"""
output:
33858
94118
184528
305088
455798
636658
847668
1088828
1360138
"""
# differences: 30110, 60260, 90410, 120560
#second differences: 30150, 30150, 30150 (yippee!!)
#30150 = 2a, a = 15075
#linear (starting at 0) = 33858, 79043, 124228, 169413
#difference = 45185, 45185, 45185 (epic)
# sequence = 15075*n**2 + 45185*n + 33858 (wtf lmao)
#at n = 202300
# print(15075*202300**2 + 45185*202300 + 33858)  # too high :(
# print(15075*202300**2 + 15035*202300 + 3748) # too low lol (i thought i corrected for starting at 0 an extra time)
print(15075*202300**2 + 15114*202300 + 3787) # works bc i did 63 steps previous instead of 64, bc im stupid and accounted for off by 1 error twice