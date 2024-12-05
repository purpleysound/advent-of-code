import aoc
from functools import cmp_to_key

data = aoc.import_input(5)

total = 0
total2 = 0

rules_text, pages = data.split("\n\n")
rules = []
wrongs = []

for line in rules_text.split("\n"):
    nums = aoc.get_nums(line)
    rules.append((nums[0], nums[1]))

for line in pages.split("\n"):
    nums = aoc.get_nums(line)
    for i, num in enumerate(nums):
        valid = True
        for rule in rules:
            if num in rule and any(x in nums[:i]+nums[i+1:] for x in rule):
                a, b = rule
                if a == num:
                    if nums.index(b) < i:
                        valid = False
                        break
                else:
                    if nums.index(a) > i:
                        valid = False
                        break
        else:
            continue
        break
    if valid:
        total += nums[(len(nums)+1)//2 - 1]
    else:
        wrongs.append(nums)

print(total)

def cmp(a, b):
    for rule in rules:
        if a in rule and b in rule:
            if a == rule[0]:
                return -1
            else:
                return 1


for wrong in wrongs:
    valid = False
    wrong.sort(key=cmp_to_key(cmp))
    total2 += wrong[(len(wrong)+1)//2 - 1]


print(total2)
