import aoc

data = aoc.import_input(14)
# data = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#...."""

rows = data.split("\n")
SIZE = len(rows)

def transpose(rows: list[str]) -> list[str]:
    return list(map("".join, zip(*rows)))

def up(rows: list[str]) -> list[str]:
    columns = transpose(rows)
    columns = [column.split("#") for column in columns]
    for column in columns:
        for i, group in enumerate(column):
            column[i] = "".join(sorted(list(group), reverse=True))
    columns = ["#".join(column) for column in columns]
    return transpose(columns)

total = 0
for i, row in enumerate(up(rows)):
    total += row.count("O")*(SIZE-i)
print(total)



def up(rows: list[str]) -> list[str]:
    columns = transpose(rows)
    columns = [column.split("#") for column in columns]
    for column in columns:
        for i, group in enumerate(column):
            column[i] = "".join(sorted(list(group), reverse=True))
    columns = ["#".join(column) for column in columns]
    return transpose(columns)

def down(rows: list[str]) -> list[str]:
    columns = transpose(rows)
    columns = [column.split("#") for column in columns]
    for column in columns:
        for i, group in enumerate(column):
            column[i] = "".join(sorted(list(group)))
    columns = ["#".join(column) for column in columns]
    return transpose(columns)

def left(rows: list[str]) -> list[str]:
    rows = [row.split("#") for row in rows]
    for row in rows:
        for i, group in enumerate(row):
            row[i] = "".join(sorted(list(group), reverse=True))
    rows = ["#".join(row) for row in rows]
    return rows

def right(rows: list[str]) -> list[str]:
    rows = [column.split("#") for column in rows]
    for row in rows:
        for i, group in enumerate(row):
            row[i] = "".join(sorted(list(group)))
    rows = ["#".join(column) for column in rows]
    return rows

def cycle(rows: list[str]) -> list[str]:
    rows = up(rows)
    rows = left(rows)
    rows = down(rows)
    rows = right(rows)
    return rows

def print_rows(rows: list[str]) -> None:
    print("\n".join(rows)+"\n")

def get_load(rows: list[str]) -> int:
    total = 0
    for i, row in enumerate(rows):
        total += row.count("O")*(SIZE-i)
    return total

rows = data.split("\n")
SIZE = len(rows)
# for _ in range(3):
#     rows = cycle(rows)
#     print_rows(rows)

cycles = 0
states = [rows]

while True:
    rows = cycle(rows)
    cycles += 1
    try:
        i = states.index(rows)
        # print(f"Found cycle at {i} and {cycles}")
        break
    except ValueError:
        pass
    states.append(rows)

d = cycles - i
cycles_needed = ((1000000000-i)%d)+i
# print(cycles_needed)
rows = data.split("\n")
SIZE = len(rows)
for _ in range(cycles_needed):
    rows = cycle(rows)
print(get_load(rows))
