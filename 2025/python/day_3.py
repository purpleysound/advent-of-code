from aoc import *

data = import_input(3)

# data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

banks = [list(map(int, line)) for line in data.splitlines()]
total = 0
l = len(banks[0])
for bank in banks:
    m = max(bank)
    mi = bank.index(m)
    if mi == l - 1:
        n = max(bank[:l - 1])
        total += 10*n + m
    else:
        n = max(bank[mi + 1:])
        total += 10*m + n

print(total)



total = 0
for bank in banks:
    digits = []
    while len(digits) < 12:
        i = len(digits) - 11
        if i == 0:
            m = max(bank)
        else:
            m = max(bank[:i])
        mi = bank.index(m)
        digits.append(m)
        bank = bank[mi + 1:]
        
    number = 0
    for d in digits:
        number = 10*number + d
    total += number

print(total)
