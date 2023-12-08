import aoc
import itertools

data = aoc.import_input(8)
# data  = """LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

path, nodes = data.split("\n\n")
nodes = nodes.split("\n")
nodes = [node.split(" = ") for node in nodes]
graph = {}
cur = "AAA"
for node in nodes:
    graph[node[0]] = node[1][1:-1].split(", ")

for i, d in enumerate(itertools.cycle(path)):
    dir_idx = 0 if d == "L" else 1
    cur = graph[cur][dir_idx]
    if cur == "ZZZ":
        break
print(i+1)
