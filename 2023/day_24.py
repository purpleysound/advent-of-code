import aoc
import numpy as np
from itertools import combinations

data = aoc.import_input(24)
lower, upper = 200000000000000, 400000000000000
# data = """19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3"""
# lower, upper = 7, 27

hailstones = []
for line in data.split("\n"):
    line = aoc.get_nums_negative(line)
    pos = line[:2]
    vel = line[3:5]
    hailstones.append((pos, vel))


def check_intersection(p1, v1, p2, v2):
    x1, y1 = p1
    x2, y2 = p2
    lambdax, lambday = v1
    mux, muy = v2
    scalar_matrix = np.array([[lambdax, -mux],
                               [lambday, -muy]])
    answers = np.array([x2-x1, y2-y1])
    try:
        lambd, mu = np.linalg.solve(scalar_matrix, answers)
    except np.linalg.LinAlgError:
        return False
    if lambd < 0 or mu < 0:
        return False
    return x1 + lambd*lambdax, y1+lambd*lambday

count = 0
for idx, jdx in combinations(range(len(hailstones)), 2):
    p1, v1 = hailstones[idx]
    p2, v2 = hailstones[jdx]
    intersect = check_intersection(p1, v1, p2, v2)
    # print(intersect)
    if not intersect:
        continue
    ix, iy = intersect
    if lower <= ix <= upper and lower <= iy <= upper:
        count += 1
        # print(f" particles {p1} @ {v1} and {p2} @ {v2} intersected at {ix, iy}")


print(count)





hailstones = []
for line in data.split("\n"):
    line = aoc.get_nums_negative(line)
    pos = line[:3]
    vel = line[3:]
    hailstones.append((pos, vel))


def check_intersection(p1, v1, p2, v2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    lambdax, lambday, lambdaz = v1
    mux, muy, muz = v2
    scalar_matrix = np.array([[lambdax, -mux],
                               [lambday, -muy],
                               [lambdaz, -muz]])
    answers = np.array([x2-x1, y2-y1, z2-z1])
    try:
        lambd, mu = np.linalg.solve(scalar_matrix, answers)
    except np.linalg.LinAlgError:
        return False
    return (x1 + lambd*lambdax, y1+lambd*lambday, z1+lambd*lambdaz), lambd


import z3
px, py, pz, vx, vy, vz = z3.Ints("px py pz vx vy vz")
solver = z3.Solver()
for hailstone in hailstones[:3]:
    pos_vec, mov_vec = hailstone
    hpx, hpy, hpz = map(z3.IntVal, pos_vec)
    hvx, hvy, hvz = map(z3.IntVal, mov_vec)
    t = z3.FreshInt("t")
    solver.add(px+t*vx==hpx+t*hvx, py+t*vy==hpy+t*hvy, pz+t*vz==hpz+t*hvz)

solver.check()
m = solver.model()
print(m[px]+m[py]+m[pz])