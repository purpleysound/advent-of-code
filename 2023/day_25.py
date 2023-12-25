import aoc
from collections import deque, defaultdict

data = aoc.import_input(25)
# with open("inputs/day_25_graph.gv", "w") as f:
#     f.write("graph G{\n")
#     for line in data.split("\n"):
#         node, cons = line.split(": ")
#         cons = cons.split(" ")
#         for con in cons:
#             f.write(f"{node} -- {con}\n")
#     f.write("}")

"""Saw visually using zgrviewer 3 edges were connecting 2 halfs of the graph:
vkb - jzj
hhx - vrx
nvh - grh
after manually removing these from the input:"""
connections = defaultdict(lambda: [])
for line in data.split("\n"):
    key, cons = line.split(": ")
    cons = cons.split(" ")
    for con in cons:
        connections[key].append(con)
        connections[con].append(key)


def get_side_size(start):
    q = deque([start])
    seen = {start}
    while q:
        node = q.popleft()
        for con in connections[node]:
            if con not in seen:
                q.append(con)
                seen.add(con)
    return len(seen)

print(get_side_size("nvh")*get_side_size("grh"))
