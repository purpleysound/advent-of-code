heightmap = """abaaaaaaaaccccccccccccccccccaaaaaccccaaaaaaccccccccccccccccccccccaaaaaaaaaacccccccccccccccccccccccccccccccaaaaaccccccccccccccccccccccccccccccccccccccccccaaaaaa
abaaaaaaaacccccccccccccccccccaaaaaccccaaaacccccaaaacccccccccccccccaaaaaaaaaacccccccccccccccccccccccccccccaaaaaaccccccccccccccccccccccccccccccccccccccccccccaaaa
abccaaaaaaccccccccccccccccccaaaaaaccccaaaaccccaaaaaccccccccccaaaaaaaaaaaaaaacccccccccccccccccccccccccccccaaaacccccccccccccccccccccccccccccaaaccccccccccccccaaaa
abcaaaaaaaccccccccccccccccccaaaaccccccaccaccccaaaaaacccccccccaaaaaaaaaaaaaaacccccccccccccccccccccacccccccccaacccccccccccccccccccccccccccccaaaccccccccccccccaaaa
abccaacccaccccccccccccccccccccaaacccccccccccccaaaaaaccccccccccaaaaaaaaacaaacccccccccccccccccccaaaacccccccccccccccccccccccccaacccccccaaccccaaacccccccccccccaaaaa
abcaaaaaacccccccccccccccccccccccccccccccccccccaaaaaccccccccccaaaaaaaaaaccccaacaaccccccccccccccaaaaaacccccccccccccccccccccccaacccccccaaaacaaaaccccccccccccccaccc
abccaaaaacccccccccccccccccccccccccccccccccccaaccaaacccccccccaaaaaaaaaaaacccaaaaccccccccccccccccaaaaacccccccccccccccaacaaaaaaacccccccaaaaaaaaacccccccccccccccccc
abccaaaaaacccccccccccccccccccccccccccccaaacaaaccccccccccccccaaaaaaaaaaacccaaaaacccccccccccccccaaaaacccccccccccccaaaaaccaaaaaaaaccccccaaaaaalllllllcccaacccccccc
abccaaaaaaccccccaaaaacccccccccaaaccccccaaaaaaaccccccccccccccaaacaaacaaacccaaaaaaccccccccccccccaccaaccccccccccccccaaaaacaaaaaaaaajkkkkkkkkkklllllllccccaaaaacccc
abccaaaaacccccccaaaaacccccccccaaaaccccccaaaaaaccccccccaacaacccccaaacccccccacaaaaccccccccaaaccccccccccccccccccccccaaaaaccaaaaaaajjkkkkkkkkkkllssllllcccaaaaacccc
abcccaaaaccccccaaaaaacccccccccaaaaccccccaaaaaaaaccccccaaaaacccccaaccccccccccaacccccccccaaaacccccccccccccccaaccccaaaaaccaaaaaacjjjjkkkkkkkkssssssslllccaaaaccccc
abcccccccccccccaaaaaacccccccccaaaccccccaaaaaaaaacaaccccaaaaacccccccccccccccaaccccccccccaaaaccccccccccccccaaacccccccaaccaaaaaajjjjrrrrrrsssssssssslllcccaaaccccc
abcccccccccccccaaaaaacccccccccccccccccaaaaaaaaaaaaaaacaaaaaacccccccccccaaacaacccccccccccaaaccccaaacccccaaaaaaaaccccccccaacaaajjjrrrrrrrsssssuusssslmcccaaaacccc
abcccccccccccccccaacccccccccccccccaacaaaacaaaccaaaaaacaaaaccccccccccccccaaaaaccccccccccccccccccaaaaacccaaaaaaaaccccccccccccaajjjrrrruuurssuuuuvsqqmmcddaaaacccc
abccccccccccccccccccccccccccccccccaaaaacccaaacccaaaaccccaaccccccccccccccaaaaaaacccccccccccccccaaaaaaccccaaaaaacccccccccccccccjjrrruuuuuuuuuuuuvvqqmmmdddccccccc
abcccccccccccccccccccccccacccccccccaaaaaccaaacccaaaaccccccccccccccccccccaaaaaaacccccccccccccccaaaaaaccccaaaaaacccccccccaaccccjjjrrtuuuuuuuuyyvvvqqmmmddddcccccc
abccccccccccccccccccccaaaaccccccccaaaaaacccccaacaccacccccccccccccccccccaaaaaaccccccccccccccccccaaaaaccccaaaaaaccccccccaaaccccjjjrrttuxxxuuxyyyvvqqmmmmdddcccccc
abcccccccccaacccccccccaaaaaaccccccaaaaccccccaaaccccccccccccccccccccccccaacaaaccccccccccccccccccaacaaccccaaccaaccccaaaaaaaccccjjjrrtttxxxxxyyyyvvqqqmmmddddccccc
abccccccccaaaacccccccccaaaacccccccccaaccccccaaacaaaccccccccccccccccccaaccccaacccccccccccccccccccccccccccccccccccccaaaaaaaaaacijjqrtttxxxxxyyyvvvqqqqmmmdddccccc
abcccccacaaaaaccccccccaaaaaccccccccccccccaaaaaaaaaacccccccccccccccccaaaccccccccccccccccccccccccccccccccccccccccccccaaaaaaaaaciiiqqqttxxxxxyyyvvvvqqqqmmmdddcccc
SbcccccaaaaaaaaaacccccaacaaccccccccccccccaaaaaaaaaccccccccccccccaaacaaacccccccccccccccccccccccccccccccccccccccccccccaaaaaaaciiiqqqtttxxxEzzyyyyvvvqqqmmmdddcccc
abcccccaaaaaaaaaaccccccccccccaaccccccccccccaaaaaccccccccccccccccaaaaaaaaaacccccccaacccccccccccccaacccccccccccccccccaaaaaaccciiiqqqttxxxxyyyyyyyyvvvqqqmmmeddccc
abcccccccaaaaaacccccccccccaaaaccccccccccaaaaaaaaacccccccaaaacccccaaaaaaaaacccccaaaaccccccccccaacaaaccccccccccccccccaaaaaaaciiiqqqtttxxyyyyyyyyyvvvvqqqnnneeeccc
abcccccccaaaaaacccccccccccaaaaaaccccccccaaaaaaaaaaccccccaaaaccccccaaaaaaaccccccaaaaaaccccccccaaaaacccccccccccccccccaaccaaaciiiqqtttxxxxwwyyywwvvvvrrrnnnneeeccc
abcccccccaaaaaaccccccccccccaaaaacccccccaaaaaaacaaaccccccaaaacccccaaaaaacccccccccaaaaccccccccccaaaaaaccccaaccccccccccccccaaciiqqqtttxxxwwwyywwwwvvrrrrnnneeecccc
abccccccaaaaaaaaccccccccccaaaaaccccccccaaaaaaccccccccccccaaacccccaaaaaaacccccccaaaaaccccccccaaaaaaaaacccaaccccccccccccccccciiqqqtttttwwswwyywwrrrrrrnnnneeecccc
abccccccccccccacccccccccccaccaaccccaaccaaaaaacccccccccccaccccccccaaacaaacccccccaacaaccccccccaaaaacaaaaaaaacccccccccaacccccciiqqqqttssssswwwwwrrrrnnnnnneeeecccc
abcccccccccccccccccccccccccccccaaaaaaccccaacccccccaaacaaacccccccccccccaacaaacccccccccccccccccccaaaccaaaaaaaaccccaacaacccccciiiqqpppsssssswwwwrrrnnnnneeeeeccccc
abcccccccccccccccccccccccccccccaaaaaaaccccccccccccaaaaaaaccccccccccccccccaaacccccccccccccccccccaaaccaaaaaaaaacccaaaaacccccchhhhppppppppssswwwrroonnfeeeeacccccc
abccccccccccccccccccccaaaaaccccaaaaaaaaccccccccccccaaaaaaccccccccccccccaaaaaaaacccccccccccccccccccccaaaaaaaaaccccaaaaaaccccchhhhhpppppppsssssrroonfffeeaaaacccc
abccccccccccccccccccccaaaaacccccaaaaaaaccccccccccccaaaaaaaaccccccccccccaaaaaaaacccccccccccccccccccccaaaaaacccccaaaaaaaacccccchhhhhhhppppsssssrooofffffaaaaacccc
abcccccaacaaacccccccccaaaaaacccaaaaaacccccccccccccaaaaaaaaacccccccccccccaaaaacccccccccccccccccccccccaaaaaaaccccaaaaaccaccccccchhhhhhhhpppssssrooofffcaaaaaccccc
abcccccaaaaaacccccccccaaaaaacccaaaaaaccccccccccccaaaaaaaaaacccccccccccccaaaaaaccccccccccccccccccccccaccaaaccccccacaaaccaacccccccchhhhhgppooooooofffcaaaaacccccc
abcccccaaaaaacccccccccaaaaaaccccccaaacaacccccccccaaacaaaccccccccccaaacccaaaaaaccccccccccccccccccccccccccaaacccccccaaacaaaccccccccccchgggoooooooffffcaaaaaaccccc
abaccccaaaaaaaccccccccccaaccccccccaaaaaacccccccccccccaaaccccccccccaaaaccaaaccacaacaacccccccccccccccccccccccccccccccaaaaaaaaccccccccccggggoooooffffccaccaaaccccc
abacccaaaaaaaaccccccccccccccccccccaaaaaccccccccccccccaacccccccaaacaaaacccaaccccaaaaacccccccccccccccccccaacaacccccccaaaaaaaacccccccccccggggggggfffcccccccccccccc
abacccaaaaaaaaccccccccaaacccccccccaaaaaaccccccccccccccccccccccaaacaaaacaaaaccccaaaaaaccccccccaaccccccccaaaaaccccccccaaaaaaacccccccccccaaggggggffcccccccccccccca
abcccccccaaacccccccccaaaaaaccccccaaaaaaaacccccccccccccccccccaaaaaaaaaaaaaaaccccaaaaaaccccccacaaaacccccccaaaaacccccccaaaaaccccccccccccaaacgggggaccccccccccccccaa
abcccccccaaccccccccccaaaaaaccccccaaaaaaaacccccccaaacccccccccaaaaaaaaaaaaaaaacccaaaaaaccccccaaaaaaccccccaaaaaaccccccaaaaaaacccccccccccaaaccccaaaccccccccccaaacaa
abcccccccccccccccccccaaaaaccccccccccaaccccccccaaaaaccccccccccaaaaaaaaaaaaaaaaccccaaaccccccccaaaacccccccaaaaccccccccccccaaccccccccccccccccccccccccccccccccaaaaaa
abccccccccccccccccccccaaaaacccccccccaaccccccccaaaaaacccccccccaaaaaaaaaaaaaaaacccccccccccccccaaaacccccccccaacccccccccccccccccccccccccccccccccccccccccccccccaaaaa"""

heightmap = heightmap.split("\n")
for i, row in enumerate(heightmap):
    heightmap[i] = list(row)

for i, row in enumerate(heightmap):
    for j, letter in enumerate(row):
        if letter == "S":
            start = (i,j)
            heightmap[i][j] = "a"
        if letter == "E":
            end = (i,j)
            heightmap[i][j] = "z"

from collections import deque, defaultdict

def get_neighbours(node: tuple) -> list:
    x, y = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

def BFS(start_node: tuple) -> int:
    queue = deque()
    current_x, current_y = start_node
    queue.append(start_node)
    distance = defaultdict(lambda: 10000)
    distance[start_node] = 0
    while queue:
        current_x, current_y = queue.popleft()
        if (current_x, current_y) == end:
            return distance[end]
        for neighbour in get_neighbours((current_x, current_y)):
            new_x, new_y = neighbour
            if new_x not in range(len(heightmap)) or new_y not in range(len(heightmap[0])):
                continue
            if ord(heightmap[new_x][new_y]) <= ord(heightmap[current_x][current_y])+1:
                current_distance = distance[(current_x, current_y)] + 1 
                if current_distance+1 < distance[neighbour]:
                    queue.append((new_x, new_y))
                    distance[neighbour] = current_distance
    
    return "didn't reach goal"

print(BFS(start))

def BFS2(start_node: tuple) -> int:
    As = [(x, y) for y, letter in enumerate(row) for x, row in enumerate(heightmap) if heightmap[x][y] == "a"]
    queue = deque()
    current_x, current_y = start_node
    queue.append(start_node)
    distance = defaultdict(lambda: 10000)
    distance[start_node] = 0
    while queue:
        current_x, current_y = queue.popleft()
        if (current_x, current_y) in As:
            return distance[((current_x, current_y))]
        for neighbour in get_neighbours((current_x, current_y)):
            new_x, new_y = neighbour
            if new_x not in range(len(heightmap)) or new_y not in range(len(heightmap[0])):
                continue
            if ord(heightmap[new_x][new_y]) >= ord(heightmap[current_x][current_y])-1:
                current_distance = distance[(current_x, current_y)] + 1 
                if current_distance+1 < distance[neighbour]:
                    queue.append((new_x, new_y))
                    distance[neighbour] = current_distance
        
print(BFS2(end))
