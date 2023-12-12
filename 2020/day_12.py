with open("inputs/day_12.txt") as f:
    data = f.read()

lines = data.split("\n")
cur = 0 + 0j
cards = {"N": 1j, "E": 1+0j, "S": -1j, "W": -1+0j}
rot = {"L": 1j, "R": -1j}
forwards = 1+0j
for line in lines:
    key, num = line[0], int(line[1:])
    if key in cards:
        cur += cards[key]*num
    elif key in rot:
        for i in range(num//90):
            forwards *= rot[key]
    else:
        cur += forwards*num
print(abs(cur.real)+abs(cur.imag))