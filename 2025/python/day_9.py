from aoc import *

data = import_input(9)

tiles = [nums(line) for line in data.splitlines()]

maxa = 0
for t1, t2 in itertools.combinations(tiles, 2):
    x1, y1 = t1
    x2, y2 = t2
    a = (abs(x1 - x2)+1) * (abs(y1 - y2)+1)
    if a > maxa:
        maxa = a

print(maxa)


vwalls = []
hwalls = []
xs = set()
ys = set()
for t1, t2 in zip(tiles, tiles[1:]):
    x1, y1 = t1
    x2, y2 = t2
    if x1 == x2:
        vwalls.append((x1, min(y1, y2), max(y1, y2)))
        xs.add(x1)
    elif y1 == y2:
        hwalls.append((y1, min(x1, x2), max(x1, x2)))
        ys.add(y1)
    else:
        raise RuntimeError()

"""Find these points in the input, they stand out and can be seen visually if you generate the image"""
up_outlier = 94727,50178
down_outlier = 94727,48597
maxa = 0

x1, y1 = up_outlier
y_cap = y1
while True:
    y_cap += 1
    if any(y_cap == hy and hx1 <= x1 <= hx2 for hy, hx1, hx2 in hwalls):
        break

for t2 in filter(lambda t: y1 < t[1] < y_cap, tiles):
    x2, y2 = t2
    a = (abs(x1 - x2)+1) * (abs(y1 - y2)+1)
    if a > maxa:
        maxa = a
    
x1, y1 = down_outlier
y_cap = y1
while True:
    y_cap -= 1
    if any(y_cap == hy and hx1 <= x1 <= hx2 for hy, hx1, hx2 in hwalls):
        break

for t2 in filter(lambda t: y_cap < t[1] < y1, tiles):
    x2, y2 = t2
    a = (abs(x1 - x2)+1) * (abs(y1 - y2)+1)
    if a > maxa:
        maxa = a
    
print(maxa)
    