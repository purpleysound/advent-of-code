import re
import math
import pyperclip
import functools
import itertools
import collections


printv = print_ = print


def import_input(day):
    with open(f"../inputs/day_{str(day)}.txt", "r") as f:
        data = f.read()
    return data

ii = ii_ = import_input


def vector_add(v1, v2):
    return tuple(map(sum, zip(v1, v2)))

vadd = vadd_ = vector_add


def vector_scale(v, s):
    return tuple(x*s for x in v)

vs = vs_ = vector_scale


def get_digits(string:str):
    return list(map(int, re.findall(r"\d", string)))

digits = digits_ = get_digits

def get_nums(string:str):
    """Returns a list of all numbers in a string"""
    return list(map(int, re.findall(r"\d+", string)))

nums = nums_ = get_nums

def get_nums_negative(string:str):
    """Returns a list of all numbers in a string, including but not exclusive to negative numbers"""
    return list(map(int, re.findall(r"-?\d+", string)))

numsn = numsn_ = get_nums_negative

def pairs_adjacent(iterable):
    iterable = iter(iterable)
    prev = next(iterable)
    for item in iterable:
        yield prev, item
        prev = item

def pairs_unique(iterable):
    iterable = list(iterable)
    for idx, item in enumerate(iterable):
        for jtem in iterable[idx+1:]:
            yield item, jtem

def pairs_all(iterable, stop_i_equals_i=True):
    iterable = list(iterable)
    for idx, item in enumerate(iterable):
        for jdx, jtem in enumerate(iterable):
            if stop_i_equals_i and idx==jdx:
                continue
            yield item, jtem


def grid(data):
    return [*map(list, data.split("\n"))]

grid_ = grid

def int_grid(data):
    return [*map(lambda x: list(map(int, x)), data.split("\n"))]

igrid = ig = ig_ = int_grid

def mag1(point):
    return sum(map(abs, point))

m1 = m1_ = mag1_ = mag1

def mag22(point):
    return sum(x*x for x in point)

m22 = m22_ = mag22_ = mag22

def mag2(point):
    return math.sqrt(mag22(point))

m2 = m2_ = mag2_ = mag2

def vector_delta(p1, p2):
    return tuple(x-y for x, y in zip(p2, p1))

vd = vd_ = vector_delta

def dist1(p1, p2):
    return mag1(vector_delta(p1, p2))

d1 = d1_ = dist1_ = dist1

def dist22(p1, p2):
    return mag22(vector_delta(p1, p2))

d22 = d22_ = dist22_ = dist22

def dist2(p1, p2):
    return mag2(vector_delta(p1, p2))

d2 = d2_ = dist2_ = dist2

def printg(grid):
    for row in grid:
        print("".join(row))

printg_ = printg

def print(*args, sep=" ", end="\n", file=None, flush=False):
    printv(*args, sep=sep, end=end, file=file, flush=flush)
    pyperclip.copy(sep.join(map(str, args)))

printc = print


cup = cup_ = (0, 1)
cdown = cdown_ = (0, -1)
cleft = cleft_ = (-1, 0)
cright = cright_ = (1, 0)

iup = iup_ = (-1, 0)
idown = idown_ = (1, 0)
ileft = ileft_ = (0, -1)
iright = iright_ = (0, 1)

dirs4 = dirs4_ = [iup, idown, ileft, iright]
dirs8 = dirs8_ = [(r, c) for r in (-1, 0, 1) for c in (-1, 0, 1) if (r, c) != (0, 0)]

def zero(n):
    return tuple(0 for _ in range(n))

z = z_ = zero

l = l_ = list()


if __name__ == "__main__":
    import os
    os.mkdir("../inputs")
    for i in range(10, 26):
        d = f"day_{str(i)}.py"
        with open(d, "w") as f:
            f.write(f"""from aoc import *\n\ndata = import_input({str(i)})\n\n\n""")
        with open(f"../inputs/day_{str(i)}.txt", "w") as f:
            f.write("")
    