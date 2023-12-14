import aoc

data = aoc.import_input(13)
# data = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#"""

def get_symmetry(rows) -> int|None:
    for i in range(1, len(rows)):
        left = rows[:i][::-1]
        right = rows[i:]
        for lcol, rcol in zip(left, right):
            if lcol != rcol:
                break
        else:
            return len(left)
    return None
        
def symmetry_value(pattern):
    rows = pattern.split("\n")
    symmetry = get_symmetry(rows)
    if not symmetry:
        transpose = list(map(list, zip(*rows)))
        symmetry = get_symmetry(transpose)
    else:
        symmetry *= 100
    return symmetry   

patterns = data.split("\n\n")
total = 0
for pattern in patterns:
    total += symmetry_value(pattern)
print(total)



def get_smudges(pattern: str):
    # print(pattern)
    for i, ch in enumerate(pattern):
        n = list(pattern)
        if ch == "#":
            n[i] = "."
        elif ch == ".":
            n[i] == "#"
        elif ch == "\n":
            continue
        else:
            raise ValueError
        yield "".join(n)


patterns = data.split("\n\n")
total = 0
for pattern in patterns:
    old_symmetry = symmetry_value(pattern)
    for np in get_smudges(pattern):
        symmetry = symmetry_value(np)
        if symmetry is not None and symmetry != old_symmetry:
            total += symmetry
            break
    else:
        raise RuntimeError
print(total)