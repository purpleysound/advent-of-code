from aoc import *
import z3

data = import_input(10)
# data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


def p1bfs(goal, buttons):
    start = tuple([False] * len(goal))
    queue = collections.deque([(start, 0)])
    seen = {start}
    while queue:
        state, dist = queue.popleft()
        if list(state) == goal:
            return dist
        for b in buttons:
            new_state = list(state)
            for i in b:
                new_state[i] = not new_state[i]
            new_state = tuple(new_state)
            if new_state not in seen:
                seen.add(new_state)
                queue.append((new_state, dist + 1))
    

def p2z3(target_voltages, buttons):
    s = z3.Optimize()
    b_vars = [z3.Int(f'b_{i}') for i in range(len(buttons))]
    for i, t in enumerate(target_voltages):
        s.add(t == sum(b_vars[j] for j in range(len(buttons)) if i in buttons[j]))
    for var in b_vars:
        s.add(var >= 0)
    s.minimize(sum(b_vars))
    if s.check() == z3.sat:
        m = s.model()
        return sum(m[var].as_long() for var in b_vars)


total1 = 0
total2 = 0
for line in data.splitlines():
    goal, *buttons, voltages = line.split()
    goal = goal[1:-1]
    goal = [c == '#' for c in goal]
    buttons = [nums(b) for b in buttons]
    voltages = tuple(nums(voltages))
    total1 += p1bfs(goal, buttons)
    total2 += p2z3(voltages, buttons)

print(total1)
print(total2)
