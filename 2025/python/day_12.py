from aoc import *

data = import_input(12)

*p_text, s_text = data.split("\n\n")
patterns = [list(map(list, p.split("\n")[1:])) for p in p_text] 

sizes = []
for p in patterns:
    sizes.append(sum(row.count("#") for row in p))

total = 0
for s in s_text.split("\n"):
    size_text, ids_text = s.split(":")
    w, h = nums(size_text)
    ids = nums(ids_text)
    if 9*sum(ids) <= w*h:
        total += 1

print(total)
