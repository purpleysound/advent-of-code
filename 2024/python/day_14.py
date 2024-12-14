from aoc import *

data = import_input(14)


seconds = 0
robots = []

for line in data.split("\n"):
    px, py, vx, vy = numsn(line)
    robots.append([(px, py), (vx, vy)])


def print_grid():
    grid = [[" " for _ in range(101)] for _ in range(103)]
    for robot in robots:
        px, py = robot[0]
        grid[py][px] = "█"
    for row in grid:
        print("".join(map(str, row)))
    print("")

                   
def max_length_chain():
    chain = 0
    posses = set(r[0] for r in robots)
    for robot in robots:
        px, py = robot[0]
        q = collections.deque([(px, py)])
        visited = set()
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in dirs8:
                nx, ny = x + dx, y + dy
                if (nx, ny) in posses:
                    q.append((nx, ny))
        chain = max(chain, len(visited))
    return chain

def second():
    for robot in robots:
        robot[0] = ((robot[0][0] + robot[1][0]) % 101, (robot[0][1] + robot[1][1]) % 103)

for _ in range(100):
    second()
    seconds += 1


q = {(True, True): 0, (True, False): 0, (False, True): 0, (False, False): 0}
for robot in robots:
    px, py = robot[0]
    if px > 50:
        if py > 51:
            q[(True, True)] += 1
        elif py < 51:
            q[(True, False)] += 1
    elif px < 50:
        if py > 51:
            q[(False, True)] += 1
        elif py < 51:
            q[(False, False)] += 1
    

p = 1
for v in q.values():
    p *= v

print(p)
while True:
    second()
    seconds += 1
    if max_length_chain() > 200:
        print_grid()
        print(seconds)
        break
