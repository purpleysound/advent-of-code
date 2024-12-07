import aoc

data = aoc.import_input(7)

total = 0
total2 = 0


for line in data.split("\n"):
    nums = aoc.get_nums(line)
    target, *operands = nums
    for i in range(2**len(operands)):
        cur = operands[0]
        for j in range(1, len(operands)):
            if i & (1 << j):
                cur += operands[j]
            else:
                cur *= operands[j]
        
        if cur > target:
            continue

        if cur == target:
            total += target
            break
    
    for i in range(3**len(operands)):
        cur = operands[0]
        for j in range(1, len(operands)):
            if i % 3 == 0:
                cur += operands[j]
            elif i % 3 == 1:
                cur *= operands[j]
            else:
                cur = int(str(cur) + str(operands[j]))
            i //= 3

        if cur > target:
            continue
            
        if cur == target:
            total2 += target
            break


print(total)
print(total2)
