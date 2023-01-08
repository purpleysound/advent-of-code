input = """Sensor at x=3972136, y=2425195: closest beacon is at x=4263070, y=2991690
Sensor at x=3063440, y=2824421: closest beacon is at x=2870962, y=2380928
Sensor at x=982575, y=3224220: closest beacon is at x=883832, y=2000000
Sensor at x=3987876, y=3879097: closest beacon is at x=4101142, y=3623324
Sensor at x=2202219, y=115239: closest beacon is at x=2756860, y=-955842
Sensor at x=2337255, y=2939761: closest beacon is at x=2870962, y=2380928
Sensor at x=1942286, y=3935612: closest beacon is at x=2942943, y=3548053
Sensor at x=228100, y=3955166: closest beacon is at x=-7488, y=4058847
Sensor at x=2114394, y=2368537: closest beacon is at x=2870962, y=2380928
Sensor at x=3658485, y=2855273: closest beacon is at x=4263070, y=2991690
Sensor at x=3731843, y=3995527: closest beacon is at x=4101142, y=3623324
Sensor at x=1311535, y=1294676: closest beacon is at x=883832, y=2000000
Sensor at x=3533617, y=3590533: closest beacon is at x=4101142, y=3623324
Sensor at x=341495, y=287725: closest beacon is at x=110643, y=-1160614
Sensor at x=1533864, y=2131620: closest beacon is at x=883832, y=2000000
Sensor at x=1179951, y=1876387: closest beacon is at x=883832, y=2000000
Sensor at x=3403590, y=1619877: closest beacon is at x=2870962, y=2380928
Sensor at x=2756782, y=3344622: closest beacon is at x=2942943, y=3548053
Sensor at x=14753, y=3818113: closest beacon is at x=-7488, y=4058847
Sensor at x=3808841, y=388411: closest beacon is at x=4559391, y=972750
Sensor at x=3129774, y=3401225: closest beacon is at x=2942943, y=3548053
Sensor at x=2710780, y=3978709: closest beacon is at x=2942943, y=3548053
Sensor at x=88084, y=2475915: closest beacon is at x=883832, y=2000000
Sensor at x=2503969, y=3564612: closest beacon is at x=2942943, y=3548053
Sensor at x=3954448, y=3360708: closest beacon is at x=4101142, y=3623324
Sensor at x=2724475, y=1736595: closest beacon is at x=2870962, y=2380928"""


CHECK_Y = 2000000
from collections import deque

def get_neighbours(node: tuple) -> tuple:
    x, y = node
    return (x+1, y), (x-1, y), (x, y+1), (x, y-1)

def no_beacons(sensor: tuple, beacon: tuple) -> set:
    """Returns a set of coordinates where there cannot be beacons"""
    visited = set()
    queue = deque([sensor])
    while queue:
        node = queue.popleft()
        if node == beacon:
            return visited
        for neighbour in get_neighbours(node):
            if neighbour not in visited and abs(CHECK_Y-neighbour[1]) <= abs(CHECK_Y-node[1]):
                queue.append(neighbour)
                visited.add(neighbour)
    raise AssertionError("Queue emptied and beacon wasn't found")

sensors = []
beacons = []
for line in input.split("\n"):
    line = line.split(" ")
    sensors.append((int(line[2][2:-1]), int(line[3][2:-1])))
    beacons.append((int(line[8][2:-1]), int(line[9][2:-1])))
print("parsed data")
cant = set()
for i, (sensor, beacon) in enumerate(zip(sensors, beacons)):
    print(f"finished {i} out of {len(sensors)}")
    cant.update((location for location in no_beacons(sensor, beacon) if location[1] == CHECK_Y))

print(len(cant))