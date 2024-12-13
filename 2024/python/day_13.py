from aoc import *
import z3

data = import_input(13)

total = 0
total2 = 0

machines_str = data.split("\n\n")
machines = []
for machine_str in machines_str:
    machine = machine_str.split("\n")
    machine = [nums(machine[0]), nums(machine[1]), nums(machine[2])]
    machines.append(machine)


def solve(machine):
    ax, ay = machine[0]
    bx, by = machine[1]
    px, py = machine[2]
    solver = z3.Solver()
    a = z3.Int("a")
    b = z3.Int("b")
    solver.add(ax*a + bx*b == px)
    solver.add(ay*a + by*b == py)
    if solver.check() == z3.sat:
        return 3*solver.model()[a].as_long() + solver.model()[b].as_long()
    return 0


for machine in machines:
    s = solve(machine)
    total += s
    machine[2] = map(lambda x: x+10000000000000, machine[2])
    s = solve(machine)
    total2 += s


print(total)
print(total2)
