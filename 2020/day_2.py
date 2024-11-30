
with open("inputs/day_2.txt") as f:
    data = f.read()

total1 = 0
total2 = 0

for line in data.split("\n"):
    r, l, string = line.split(" ")
    a, b = r.split("-")
    a = int(a)
    b = int(b)
    l = l[:-1]
    if a <= string.count(l) <= b:
        total1 += 1

    if (string[a-1] == l) ^ (string[b-1] == l):
        total2 += 1

print(f"Part 1: {total1}")
print(f"Part 2: {total2}")