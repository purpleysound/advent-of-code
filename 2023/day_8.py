import aoc
import itertools

data = aoc.import_input(8)
# data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

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


def trans(node, dir):
    if dir == "L":
        return graph[node][0]
    else:
        return graph[node][1]
    
curs = [node[0] for node in nodes if node[0][-1] == "A"]
# print(curs)
loop_dict = {} # anode: {znode: (start, step), ...}
for node in curs:
    # check for loop, find loop, store as (start, step)
    cur = node
    loops = {}
    start = 0
    for i, d in enumerate(itertools.cycle(path)):
        dir_idx = 0 if d == "L" else 1
        cur = graph[cur][dir_idx]
        if cur[-1] == "Z":
            if cur in loops:
                if loops[cur][1]:
                    break # started looping twice
                loops[cur] = (loops[cur][0], i+1-loops[cur][0])
            else:
                loops[cur] = (i+1, 0)
                # print(f"found {cur} at {i+1} from {node}")
    loop_dict[node] = loops
#found by printing it that z is one behind a, and loops only contain one z, hence lcm of steps is ans
import math
ints = []
for d in loop_dict.values():
    for i in d.values():
        ints.append(i[0])

print(math.lcm(*ints))