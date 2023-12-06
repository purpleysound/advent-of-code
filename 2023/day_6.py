import aoc
import math
import functools

data = aoc.import_input(6)
# data = """Time:      7  15   30
# Distance:  9  40  200"""
times, distances = map(aoc.get_nums, data.split("\n"))
# total = 1
# for T, s in zip(times, distances):
#     t0 = (T-math.sqrt(T**2 - 4*s))/(2)
#     t1 = (T+math.sqrt(T**2 - 4*s))/(2)
#     print(math.ceil(t0), math.floor(t1))
#     print(math.floor(t1)-math.ceil(t0))
#     total *= math.floor(t1)-math.ceil(t0)+1
# print(total)
total = 1
def count_wins(T, s):
    count = 0
    for i in range(T):
        speed = i
        count += speed*(T-i) > s
    return count


for T, s in zip(times, distances):
    total *= count_wins(T,s)
print(total)

times = int(functools.reduce(lambda x, y: str(x)+str(y), times))
distances = int(functools.reduce(lambda x, y: str(x)+str(y), distances))
print(count_wins(times, distances))