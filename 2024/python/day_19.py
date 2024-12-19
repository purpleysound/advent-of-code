from aoc import *

data = import_input(19)
patterns, wanted = data.split("\n\n")
wanted = wanted.split("\n")
patterns = patterns.split(", ")

total = 0
total2 = 0

@functools.cache
def possible(wanted:str):
    if wanted == "":
        return 1
    total = 0
    for pattern in patterns:
        if wanted.startswith(pattern):
            total += possible(wanted[len(pattern):])
    return total


for w in wanted:
    p = possible(w)
    if p:
        total += 1
    total2 += p

print(total)
print(total2)
