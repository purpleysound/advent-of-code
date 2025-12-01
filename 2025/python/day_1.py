from aoc import *

data = import_input(1)
# data = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

lines = data.split("\n")
start = 50
zeros = 0

for line in lines:
    d = line[0]
    n = int(line[1:])
    if d == "R":
        start = (start + n) % 100
    elif d == "L":
        start = (start - n) % 100
    if start == 0:
        zeros += 1

print(zeros)


start = 50
zeros = 0
for line in lines:
    d = line[0]
    n = int(line[1:])
    if d == "R":
        for i in range(n):
            start = (start + 1) % 100
            if start == 0:
                zeros += 1
    elif d == "L":
        for i in range(n):
            start = (start - 1) % 100
            if start == 0:
                zeros += 1
    

print(zeros)