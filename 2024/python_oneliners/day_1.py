
with open("../inputs/day_1.txt") as f:
    data = f.read()

print(f"Part 1: {sum(map(lambda n: abs(n[1]-n[0]), [*map(list, zip(*[*map(sorted, [*map(list, zip(*[*map(lambda l: [int(l[0]), int(l[1])], map(str.split, data.split("\n")))]))])]))]))}\nPart 2: {sum(map(lambda x: x*[*map(sorted, [*map(list, zip(*[*map(lambda l: [int(l[0]), int(l[1])], map(str.split, data.split("\n")))]))])][1].count(x), [*map(sorted, [*map(list, zip(*[*map(lambda l: [int(l[0]), int(l[1])], map(str.split, data.split("\n")))]))])][0]))}")
