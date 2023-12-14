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

def get_symmetry(rows, errors) -> int|None:
    count = 0
    for i in range(1, len(rows)):
        left = rows[:i][::-1]
        right = rows[i:]
        for lcol, rcol in zip(left, right):
            for a, b in zip(lcol, rcol):
                if a != b:
                    count += 1
        if count == errors:
            return len(left)
        count = 0
    return None
        
def symmetry_value(pattern, errors):
    rows = pattern.split("\n")
    symmetry = get_symmetry(rows, errors)
    if not symmetry:
        transpose = list(map(list, zip(*rows)))
        symmetry = get_symmetry(transpose, errors)
    else:
        symmetry *= 100
    return symmetry   

patterns = data.split("\n\n")
total = 0
for pattern in patterns:
    total += symmetry_value(pattern, 0)
print(total)

total = 0
for pattern in patterns:
    total += symmetry_value(pattern, 1)
print(total)