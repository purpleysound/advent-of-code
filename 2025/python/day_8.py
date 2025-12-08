from aoc import *
import networkx

data = import_input(8)

nodes = [nums(line) for line in data.splitlines()]
edges = []
for a, b in itertools.combinations(nodes, 2):
    dist = sum(abs(a[k]-b[k])**2 for k in range(3))
    edges.append((tuple(a), tuple(b), dist))
edges.sort(key=lambda x: x[2])

i = 0
G = networkx.Graph()
for i in range(1000):
    G.add_edge(edges[i][0], edges[i][1])

cliques = list(networkx.connected_components(G))
sizes = sorted([len(c) for c in cliques])

print(sizes[-1]*sizes[-2]*sizes[-3])


while len(list(networkx.connected_components(G))) > 1:
    i += 1
    G.add_edge(edges[i][0], edges[i][1])

print(edges[i][0][0]*edges[i][1][0])
