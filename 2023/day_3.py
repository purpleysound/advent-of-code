import aoc

data = aoc.import_input(3)
# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""
data = data.strip().split('\n')
for row in data: 
    row = list(row)

def get_neighbours(row, column):
    offset = [-1, 0, 1]
    for i in offset:
        for j in offset:
            if row+i < 0 or column+j < 0 or row+i >= len(data) or j > len(data[0]):
                continue
            if i == 0 and j == 0:
                continue
            yield (row + i, column + j)

def get_number(row, column):
    check_row = data[row]
    num = ""
    rc_pairs = []
    for i, char in enumerate(check_row):
        if char.isdigit():
            num += char
            rc_pairs.append((row, i))
        else:
            if i >= column:
                return int(num), rc_pairs
            else:
                rc_pairs = []
                num = ""
    if i >= column:
        return int(num), rc_pairs
    else:
        raise ValueError("No number found")

total = 0

for i, row in enumerate(data):
    for j, column in enumerate(row):
        # columns = char
        if column == '.':
            continue
        if column.isdigit():
            continue
        else:
            seen_rc_pairs = []
            for neighbour in get_neighbours(i,j):
                nr, nc = neighbour
                if (nr, nc) in seen_rc_pairs:
                    continue
                if data[nr][nc].isdigit():
                    num, rc_pairs = get_number(nr, nc)
                    seen_rc_pairs += rc_pairs
                    total += num
                    

print(total)

total = 0
for i, row in enumerate(data):
    for j, column in enumerate(row):
        # columns = char
        if column == "*":
            seen_rc_pairs = []
            nums = []
            for neighbour in get_neighbours(i,j):
                nr, nc = neighbour
                if (nr, nc) in seen_rc_pairs:
                    continue
                if data[nr][nc].isdigit():
                    num, rc_pairs = get_number(nr, nc)
                    nums.append(num)
                    seen_rc_pairs += rc_pairs
            if len(nums) == 2:
                total += nums[0] * nums[1]
print(total)