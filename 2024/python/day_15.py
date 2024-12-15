from aoc import *

data = import_input(15)


total = 0

g = grid(data.split("\n\n")[0])
R = len(g)
C = len(g[0])

walls = []
boxes = []
robot = None
for r, row in enumerate(g):
    for c, ch in enumerate(row):
        if ch == "#":
            walls.append((r, c))
        elif ch == "O":
            boxes.append((r, c))
        elif ch == "@":
            robot = (r, c)


dirs = {"^": iup, "v": idown, "<": ileft, ">": iright}


def can_push(box, d):
    nr, nc = vadd(box, d)
    if nr not in range(R) or nc not in range(C):
        return False
    if (nr, nc) in walls:
        return False
    if (nr, nc) in boxes:
        return can_push((nr, nc), d)
    return True


def print_grid():
    for r in range(R):
        for c in range(C):
            if (r, c) in walls:
                printv("#", end="")
            elif (r, c) in boxes:
                printv("O", end="")
            elif (r, c) == robot:
                printv("@", end="")
            else:
                printv(".", end="")
        printv()


for d in data.split("\n\n")[1].replace("\n", ""):
    d = dirs[d]
    if can_push(robot, d):
        chain = [robot]
        robot = vadd(robot, d)
        while True:
            nr, nc = vadd(chain[-1], d)
            if (nr, nc) in boxes:
                chain.append((nr, nc))
            else:
                break
        chain = chain[1:]
        for box in chain:
            boxes.remove(box)
            box = vadd(box, d)
            boxes.append(box)

for r, c in boxes:
    total += 100*r + c
print(total)



gs = data.split("\n\n")[0]
gs = gs.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
g = grid(gs)
R = len(g)
C = len(g[0])

walls = []
boxes = []
robot = None
total = 0
for r, row in enumerate(g):
    for c, ch in enumerate(row):
        if ch == "#":
            walls.append((r, c))
        elif ch == "[":
            boxes.append((r, c))
        elif ch == "@":
            robot = (r, c)


def can_push_as_box(box, d):
    nr, nc = vadd(box, d)
    result = True
    affected = [box]
    if nr not in range(R) or nc not in range(C):
        return False, affected
    if d == iright and nc+1 not in range(C):
        return False, affected
    if (nr, nc) in walls or (nr, nc+1) in walls:
        return False, affected
    if (nr, nc) in boxes:
        new_result, new_affected = can_push_as_box((nr, nc), d)
        affected += new_affected
        result &= new_result
    if d in (iup, idown) and (nr, nc-1) in boxes:
        new_result, new_affected = can_push_as_box((nr, nc-1), d)
        affected += new_affected
        result &= new_result
    if d in (iup, idown) and (nr, nc+1) in boxes:
        new_result, new_affected = can_push_as_box((nr, nc+1), d)
        affected += new_affected
        result &= new_result
    if d == ileft and (nr, nc-1) in boxes:
        new_result, new_affected = can_push_as_box((nr, nc-1), d)
        affected += new_affected
        result &= new_result
    if d == iright and (nr, nc+1) in boxes:
        new_result, new_affected = can_push_as_box((nr, nc+1), d)
        affected += new_affected
        result &= new_result
    return result, affected


def can_push_as_robot(robot, d):
    nr, nc = vadd(robot, d)
    result = True
    affected = []
    if nr not in range(R) or nc not in range(C):
        return False, affected
    if (nr, nc) in walls:
        return False, affected
    if (nr, nc) in boxes:
        new_result, new_affected = can_push_as_box((nr, nc), d)
        affected += new_affected
        result &= new_result
    if (nr, nc-1) in boxes:
        new_result, new_affected = can_push_as_box((nr, nc-1), d)
        affected += new_affected
        result &= new_result
    return result, affected


def print_grid():
    b = False
    for r in range(R):
        for c in range(C):
            if b:
                b = False
                continue
            if (r, c) in walls:
                printv("#", end="")
            elif (r, c) in boxes:
                printv("[]", end="")
                b = True
            elif (r, c) == robot:
                printv("@", end="")
            else:
                printv(".", end="")
        printv()
    printv()


for d in data.split("\n\n")[1].replace("\n", ""):
    d = dirs[d]
    result, affected = can_push_as_robot(robot, d)
    if result:
        robot = vadd(robot, d)
        for box in set(affected):
            boxes.remove(box)
            box = vadd(box, d)
            boxes.append(box)


for r, c in boxes:
    total += 100*r + c
print(total)
