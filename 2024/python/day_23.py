from aoc import *
import networkx

data = import_input(23)

total = 0


g = networkx.graph.Graph()


for line in data.split("\n"):
    v1, v2 = line.strip().split("-")
    g.add_edge(v1, v2)

components = []
for node1 in g.nodes():
    for node2 in g.neighbors(node1):
        for node3 in g.neighbors(node2):
            if node3 in g.neighbors(node1):  
                component = frozenset([node1, node2, node3])
                if component not in components:
                    components.append(component)

# print(components)
total = len([component for component in components if any(c.startswith("t") for c in component)])


print(total)


max_clique = []
for clique in networkx.find_cliques(g):
    if len(clique) > len(max_clique):
        max_clique = clique

print(",".join(sorted(max_clique)))
