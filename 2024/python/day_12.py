from aoc import *

data = import_input(12)


total = 0
total2 = 0

g = grid(data)
R = len(g)
C = len(g[0])


def flood(r, c, letter, visited):
    if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visited or g[r][c] != letter:
        return set()
    visited.add((r, c))
    return visited | flood(r+1, c, letter, visited) | flood(r-1, c, letter, visited) | flood(r, c+1, letter, visited) | flood(r, c-1, letter, visited)


def area(region):
    return len(region)


def perimeter(region):
    region = list(region)
    perimeter = 0
    for r, c in region:
        if (r+1, c) not in region:
            perimeter += 1
        if (r-1, c) not in region:
            perimeter += 1
        if (r, c+1) not in region:
            perimeter += 1
        if (r, c-1) not in region:
            perimeter += 1
    return perimeter


def sides_count(region):
    region = list(region)
    sides = 0
    perimeter = []
    for r, c in region:
        if (r+1, c) not in region:
            perimeter.append(((r, c), (1, 0)))
        if (r-1, c) not in region:
            perimeter.append(((r, c), (-1, 0)))
        if (r, c+1) not in region:
            perimeter.append(((r, c), (0, 1)))
        if (r, c-1) not in region:
            perimeter.append(((r, c), (0, -1)))
    sides = len(perimeter)
    for p1, p2 in pairs_unique(perimeter):
            if mag1(vector_delta(p1[0], p2[0])) == 1 and p1[1] == p2[1]:
                sides -= 1

    return sides


all_visited = set()
for r in range(R):
    for c in range(C):
        if g[r][c] != ' ' and (r, c) not in all_visited:
            visited = set()
            region = flood(r, c, g[r][c], visited)
            all_visited |= region
            a, p, s = area(region), perimeter(region), sides_count(region)
            total += a*p
            total2 += a*s


print(total)
print(int(total2))
