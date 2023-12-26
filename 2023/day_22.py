import aoc

data = aoc.import_input(22)
# data = """1,0,1~1,2,1
# 0,0,2~2,0,2
# 0,2,3~2,2,3
# 0,0,4~0,2,4
# 2,0,5~2,2,5
# 0,1,6~2,1,6
# 1,1,8~1,1,9"""

ranges = []
for line in data.split("\n"):
    ranges.append(list(map(aoc.get_nums_negative, line.split("~"))))  # ranges inclusive both ends
# print(ranges)
    
ranges.sort(key=lambda x: x[0][2]) #lowest up
# print(ranges)

supporting = {i: [] for i in range(len(ranges))}
supported_by = {i: [] for i in range(len(ranges))}

def check_below(start, end):
    assert start[2] <= end[2] #if this fails i will be unhappy
    csx, csy, _ = start
    cex, cey, _ = end
    below = []
    for i, (other_start, other_end) in enumerate(ranges):
        if other_end[2] != start[2]-1:
            continue
        osx, osy, _ = other_start
        oex, oey, _ = other_end
        if (osx <= csx <= oex or osx <= cex <= oex or csx <= osx <= cex or csx <= oex <= cex) and (osy <= csy <= oey or osy <= cey <= oey or csy <= osy <= cey or csy <= oey <= cey):  # what a lovely condition
            below.append(i)
    return below




for i, (start, end) in enumerate(ranges):
    while start[2] > 1:
        below = check_below(start, end)
        if len(below) == 0:
            start[2] -= 1
            end[2] -= 1
        else:
            supported_by[i] = below
            break
    
for brick, supports in supported_by.items():
    for support in supports:
        supporting[support].append(brick)


cant_disintergrate = set()
for brick, what_its_supporting in supporting.items():
    for new_brick in what_its_supporting:
        if len(supported_by[new_brick]) == 1:
            # print(f"brick {brick} can be disintergrated")
            cant_disintergrate.add(brick)
            break
    
# print(cant_disintergrate)
print(len(ranges)-len(cant_disintergrate))



from functools import lru_cache

@lru_cache
def fall_from_breaking(brick: int, gone: tuple):  # so much redundancy from rewriting it many times
    what_its_supporting = list(filter(lambda x: x not in gone, supporting[brick]))
    if len(what_its_supporting) == 0:
        return gone
    new_gone = list(gone)
    to_check = []
    for above in what_its_supporting:
        whats_supporting_it = list(filter(lambda x: x not in gone, supported_by[above]))
        if len(whats_supporting_it) == 0:
            # print(f"when {new_gone} is gone, {above} falls")
            new_gone.append(above)
            to_check.append(above)
    # print(to_check, gone)
    for check in to_check:
        new_gone = fall_from_breaking(check, tuple(new_gone))
    return new_gone


count = 0
for brick, what_its_supporting in supporting.items():
    would_fall = fall_from_breaking(brick, (brick,))
    # print(brick, would_fall)
    count += len(would_fall)-1
print(count)