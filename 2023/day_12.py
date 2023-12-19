import aoc
import itertools

data = aoc.import_input(12)
# data = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1"""
lines = data.split("\n")

def check(springs: str, groups: list[int]):
    springs = springs.split(".")
    springs = [len(s) for s in springs if s != ""]
    if len(springs) != len(groups):
        return False
    for s, g in zip(springs, groups):
        if s != g:
            return False
    return True

def get_all_spring_combs(springs, ndots):
    qs = [i for i, ch in enumerate(springs) if ch == "?"]
    for combination in itertools.combinations(qs, ndots):
        new_springs = ""
        for i, ch in enumerate(springs):
            if ch != "?":
                new_springs += ch
            elif i in combination:
                new_springs += "."
            else:
                new_springs += "#"
        yield new_springs


def combinations(springs, groups):
    nhashes = sum(groups) - springs.count("#")
    ndots = springs.count("?") - nhashes
    count = 0
    for spring in get_all_spring_combs(springs, ndots):
        # print(spring)
        if check(spring, groups):
            count += 1
    return count


total = 0
for line in lines:
    springs, groups = line.split(" ")
    groups = aoc.get_nums(groups)
    # print(springs, groups)
    total += combinations(springs, groups)
print(total)



from functools import lru_cache
import re
RE_HASH_OR_Q = "(\?|#)+"

@lru_cache
def combinations(springs: str, groups: tuple[int]):
    if springs == "":
        return 0 if groups else 1
    if not groups:
        return "#" not in springs
    groups = [num for num in groups if num != 0]
    count = 0
    first = springs[0]
    if first in ".?":
        count += combinations(springs[1:], tuple(groups))
    if first in "?#":
        if groups[0] <= len(springs) and "." not in springs[:groups[0]]:
            if len(springs)==groups[0] or springs[groups[0]] in ".?":
                count += combinations(springs[groups[0]+1:], tuple(groups[1:]))
    return count
 



total = 0
for line in lines:
    springs, groups = line.split(" ")
    groups = aoc.get_nums(groups)
    springs = "?".join([springs]*5)
    groups *= 5
    total += combinations(springs, tuple(groups))
print(total)