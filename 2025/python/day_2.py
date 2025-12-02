from aoc import *

data = import_input(2)
# data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124"""

range_texts = data.split(",")
ranges = map(nums, range_texts)

invalid_sum = 0

for a, b in ranges:
    if len(str(a)) == 1:
        test = 0
    else:
        test = int(str(a)[:len(str(a)) // 2])
    upper = int(str(b)[:len(str(b)) // 2 ])

    while True:
        consider = int(str(test)*2)
        if consider > b:
            break
        if consider >= a:
            invalid_sum += consider
        test += 1

print(invalid_sum)



ranges = map(nums, range_texts)
invalid_sum = 0
for a, b in ranges:
    seen = set()
    for i in range(2, len(str(b)) + 1):
        test = 1
        while True:
            consider = int(str(test)*i)
            if consider > b:
                break
            if consider >= a and consider not in seen:
                invalid_sum += consider
                seen.add(consider)
            test += 1

print(invalid_sum)   
