import aoc
import re

data = aoc.import_input(3)

total = 0
total2 = 0


muls = re.findall(r"(mul\(\d+,\d+\))|(don\'t\(\))|(do\(\))", data)
# print(muls)
on = True
for mul in muls:
    nums, dont, do = mul
    if dont:
        on=False
    if do:
        on=True
    if nums:
        a, b = aoc.get_nums(nums)
        total += a*b
        if on:
            total2 += a*b


print(total)
print(total2)
