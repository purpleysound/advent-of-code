from aoc import *
import PIL.Image

data = import_input(9)

tiles = [nums(line) for line in data.splitlines()]

maxx = max(x for x, y in tiles)
maxy = max(y for x, y in tiles)

Image = PIL.Image.new("RGB", (maxx//100 + 1, maxy//100 + 1), "white")

for t1, t2 in zip(tiles, tiles[1:]):
    x1, y1 = t1
    x2, y2 = t2
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            Image.putpixel((x1//100, y//100), (0, 255, 0))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            Image.putpixel((x//100, y1//100), (0, 255, 0))
    else:
        raise RuntimeError()
    Image.putpixel((x1//100, y1//100), (255, 0, 0))

Image.save("day_9_image_squished.png")
