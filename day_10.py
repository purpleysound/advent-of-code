program = """noop
addx 5
addx -2
noop
noop
addx 7
addx 15
addx -14
addx 2
addx 7
noop
addx -2
noop
addx 3
addx 4
noop
noop
addx 5
noop
noop
addx 1
addx 2
addx 5
addx -40
noop
addx 5
addx 2
addx 15
noop
addx -10
addx 3
noop
addx 2
addx -15
addx 20
addx -2
addx 2
addx 5
addx 3
addx -2
noop
noop
noop
addx 5
addx 2
addx 5
addx -38
addx 3
noop
addx 2
addx 5
noop
noop
addx -2
addx 5
addx 2
addx -2
noop
addx 7
noop
addx 10
addx -5
noop
noop
noop
addx -15
addx 22
addx 3
noop
noop
addx 2
addx -37
noop
noop
addx 13
addx -10
noop
addx -5
addx 10
addx 5
addx 2
addx -6
addx 11
addx -2
addx 2
addx 5
addx 3
noop
addx 3
addx -2
noop
addx 6
addx -22
addx 23
addx -38
noop
addx 7
noop
addx 5
noop
noop
noop
addx 9
addx -8
addx 2
addx 7
noop
noop
addx 2
addx -4
addx 5
addx 5
addx 2
addx -26
addx 31
noop
addx 3
noop
addx -40
addx 7
noop
noop
noop
noop
addx 2
addx 4
noop
addx -1
addx 5
noop
addx 1
noop
addx 2
addx 5
addx 2
noop
noop
noop
addx 5
addx 1
noop
addx 4
addx 3
noop
addx -24
noop"""


#part 1
program = program.split("\n")
score = 0
cycle = 1
X = 1

for line in program:
    if line.split(" ")[0] == "noop":
        if cycle % 40 == 20:
            score += X * cycle
        cycle += 1
    else:
        operand = line.split(" ")[1]
        if cycle % 40 == 20:
            score += X * cycle
        cycle += 1
        if cycle % 40 == 20:
            score += X * cycle
        X += int(operand)
        cycle += 1

print(score)
print()
#part 2
score = 0
cycle = 1
X = 1

for line in program:
    if line.split(" ")[0] == "noop":
        if abs(X-(cycle-1)%40) <= 1:
            print("█", end="")
        else:
            print(".", end="")
        if cycle % 40 == 0:
            print()
        cycle += 1
    else:
        operand = line.split(" ")[1]
        if abs(X-(cycle-1)%40) <= 1:
            print("█", end="")
        else:
            print(".", end="")
        if cycle % 40 == 0:
            print()
        cycle += 1
        if abs(X-(cycle-1)%40) <= 1:
            print("█", end="")
        else:
            print(".", end="")
        if cycle % 40 == 0:
            print()
        X += int(operand)
        cycle += 1
