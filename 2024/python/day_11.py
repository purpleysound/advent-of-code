from aoc import *

data = import_input(11)

data = nums(data)

total = 0
total2 = 0


@functools.lru_cache(maxsize=None)
def blink_recursive(num, depth):
    if depth == 0:
        return 1
    digits = len(str(num))
    if num == 0:
        return blink_recursive(1, depth-1)
    elif digits % 2 == 0:
        return blink_recursive(int(str(num)[:digits//2]), depth-1) + blink_recursive(int(str(num)[digits//2:]), depth-1)
    else:
        return blink_recursive(num*2024, depth-1)
    

data.sort()
for num in data:
    total += blink_recursive(num, 25)
    total2 += blink_recursive(num, 75)


print(total)
print(total2)
