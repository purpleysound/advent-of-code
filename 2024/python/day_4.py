import aoc

data = aoc.import_input(4)

grid = [*map(list, data.split("\n"))]
trans = [*map(list, zip(*grid))]
data2 = "\n".join("".join(x) for x in trans)
size = len(grid[0])

import re
r = "(?=(XMAS|SAMX))"

data3 = "\n".join("".join(x[i:]+["."]+x[:i]) for i, x in enumerate(grid))
grid3 = [*map(list, data3.split("\n"))]
trans3 = [*map(list, zip(*grid3))]
data3 = "\n".join("".join(x) for x in trans3)
data4 = "\n".join("".join(x[size-i:]+["."]+x[:size-i]) for i, x in enumerate(grid))
grid4 = [*map(list, data4.split("\n"))]
trans4 = [*map(list, zip(*grid4))]
data4 = "\n".join("".join(x) for x in trans4)

print(len(re.findall(r, data))+len(re.findall(r, data2))+len(re.findall(r, data3))+len(re.findall(r, data4)))

r = "(?=(M.S.{"+str(size-1)+"}A.{"+str(size-1)+"}M.S|S.M.{"+str(size-1)+"}A.{"+str(size-1)+"}S.M|M.M.{"+str(size-1)+"}A.{"+str(size-1)+"}S.S|S.S.{"+str(size-1)+"}A.{"+str(size-1)+"}M.M))"
data = data.replace("\n", ".")
print(len(re.findall(r, data)))
