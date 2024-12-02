import aoc

data = aoc.import_input(2)
# data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

total = 0
total2 = 0


def check(nums):
    pairs = aoc.pairs_adjacent(nums)
    a, b = next(pairs)
    passed = True
    if a > b:
        inc = False
    else:
        inc = True
    if inc:
        if b-a in (1, 2, 3):
            pass
        else:
            passed = False
    else:
        if a-b in (1, 2, 3):
            pass
        else:
            passed = False
    for a, b in pairs:
        if inc:
            if b-a in (1, 2, 3):
                pass
            else:
                passed = False
        else:
            if a-b in (1, 2, 3):
                pass
            else:
                passed = False 
    
    if passed:
        return 1
    return 0


def remove_one(nums):
    yield nums
    for i in range(len(nums)):
        nnums = nums.copy()
        nnums.pop(i)
        yield nnums


for line in data.split("\n"):
    nums = aoc.get_nums(line)
    total += check(nums)
    for nnums in remove_one(nums):
        if check(nnums):
            total2 += 1
            break


print(total)
print(total2)
