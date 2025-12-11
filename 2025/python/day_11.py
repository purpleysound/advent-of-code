from aoc import *
import networkx

data = import_input(11)

G = networkx.DiGraph()
for line in data.splitlines():
    node, edges = line.split(": ")
    for edge in edges.split(" "):
        G.add_edge(node, edge)

start = "you"
end = "out"

all_paths = list(networkx.all_simple_paths(G, start, end))
print(len(all_paths))


start = "svr"
mid1 = "fft"
mid2 = "dac"
end = "out"

@functools.lru_cache(None)
def dfs(cur, target, mid1_found, mid2_found):
    if cur == target:
        return 1 if mid1_found and mid2_found else 0
    count = 0
    for neighbor in G.neighbors(cur):
        count += dfs(
            neighbor,
            target,
            mid1_found or (neighbor == mid1),
            mid2_found or (neighbor == mid2),
        )
    return count

total_paths = dfs(start, end, False, False)
print(total_paths)
