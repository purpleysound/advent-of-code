
with open("inputs/day_2.txt") as f:
    data = f.read()

total1 = 0
total2 = 0
for line in data.split("\n"):
    nums = [*map(int, line.split())]
    total1 += max(nums) - min(nums)
    for num in nums:
        for num2 in nums:
            if num == num2:
                continue
            div, mod = divmod(num, num2)
            if mod == 0:
                total2 += div

print(f"Part 1: {total1}")
print(f"Part 2: {total2}")
