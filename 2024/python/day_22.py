from aoc import *

data = import_input(22)

total = 0


def secret(n):
    n64 = n*64
    n = n ^ n64
    n %= 16777216
    n32 = n//32
    n = n ^ n32
    n %= 16777216
    n2048 = n * 2048
    n = n ^ n2048
    n %= 16777216
    return n


for line in data.split("\n"):
    n = int(line)
    for _ in range(2000):
        n = secret(n)
    total += n


print(total)



all_digits = []
all_diffs = []

for line in data.split("\n"):
    digits = []
    n = int(line)
    for _ in range(2000):
        digits.append(n%10)
        n = secret(n)
    digits.append(n%10)
    diffs = [b-a for a, b in zip(digits, digits[1:])]
    all_digits.append(digits)
    all_diffs.append(diffs)


sequences = collections.defaultdict(int)

for digits, diffs in zip(all_digits, all_diffs):
    seen = set()
    for i in range(len(diffs)-3):
        sequence = tuple(diffs[i:i+4])
        if sequence in seen:
            continue
        seen.add(sequence)
        sequences[sequence] += digits[i+4]

print(max(sequences.values()))
