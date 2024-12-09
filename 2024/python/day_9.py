import aoc

data = aoc.import_input(9)
data = [*map(int, data)]

total = 0
total2 = 0


disk = [[i//2]*ch if i%2 == 0 else "."*ch for i, ch in enumerate(data)]
flat = [item for sublist in disk for item in sublist]
flat2 = flat.copy()


while True:
    dot = flat.index(".")
    for i, val in enumerate(flat[::-1]):
        if val != ".":
            i = len(flat) - i -1
            break
    if i > dot:
        flat[dot], flat[i] = flat[i], flat[dot]
    else:
        break


for i, num in enumerate(flat):
    if num == ".":
        break
    total += i*num

print(total)

last = flat2[0]
len_group = 0
dot_groups = []
first_dot = 0
for i, val in enumerate(flat2):
    if val == last and val == ".":
        len_group += 1
    elif val != last and last == ".":
        dot_groups.append((first_dot, len_group))
        len_group = 0
    elif val != last and val == ".":
        first_dot = i
        len_group += 1
    last = val


for num in range(flat2[-1], 0, -1):
    first_index = flat2.index(num)
    length_group = flat2.count(num)
    for i, (index, length) in enumerate(dot_groups):
        if index < first_index and length >= length_group:
            flat2[index:index+length_group] = [num]*length_group
            flat2[first_index:first_index+length_group] = ["."]*length_group
            dot_groups[i] = (index+length_group, length-length_group)
            break

for i, num in enumerate(flat2):
    if num == ".":
        continue
    total2 += i*num

print(total2)
