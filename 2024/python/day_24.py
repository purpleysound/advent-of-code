from aoc import *

data = import_input(24)

z = 0

starts, gates = data.split("\n\n")

values = {name: int(value) for name, value in [line.split(": ") for line in starts.split("\n")]}
gates = [line.split(" -> ") for line in gates.split("\n")]
nodes = set()
for line in gates:
    nodes.add(line[1])
    nodes.add(line[0].split(" ")[0])
    nodes.add(line[0].split(" ")[2])


needed_values = nodes - set(values.keys())

changed = True
while changed:
    changed = False
    for gate in gates:
        if gate[1] not in needed_values:
            continue
        a, op, b = gate[0].split(" ")
        if a not in values or b not in values:
            continue
        if op == "AND":
            values[gate[1]] = values[a] & values[b]
        elif op == "OR":
            values[gate[1]] = values[a] | values[b]
        elif op == "XOR":
            values[gate[1]] = values[a] ^ values[b]
        else: raise ValueError("Invalid operation")
        changed = True
        needed_values.remove(gate[1])

old_values = values.copy()
i = 0
z = 0
while f"z{'0' if i < 10 else ''}{i}" in values:
    m = i
    i += 1

for i in range(m, -1, -1):
    z <<= 1
    z += values[f"z{'0' if i < 10 else ''}{i}"]
    i += 1


print(z)

x = 0
while f"x{'0' if i < 10 else ''}{i}" in values:
    m = i
    i += 1

for i in range(m, -1, -1):
    x <<= 1
    x += values[f"x{'0' if i < 10 else ''}{i}"]
    i += 1


y = 0
while f"y{'0' if i < 10 else ''}{i}" in values:
    m = i
    i += 1

for i in range(m, -1, -1):
    y <<= 1
    y += values[f"y{'0' if i < 10 else ''}{i}"]
    i += 1


values = {name: int(value) for name, value in [line.split(": ") for line in starts.split("\n")]}

ideal_gates = ["x00 XOR y00 -> z00", "x00 AND y00 -> c01"]
i = 0
while f"z{'0' if i < 10 else ''}{i}" in values:
    m = i
    i += 1

for i in range(1, m+1):
    cx = values[f"x{'0' if i < 10 else ''}{i}"] if f"x{'0' if i < 10 else ''}{i}" in values else 0
    cy = values[f"y{'0' if i < 10 else ''}{i}"] if f"y{'0' if i < 10 else ''}{i}" in values else 0
    ccarry = values[f"c{'0' if i < 10 else ''}{i}"] if f"c{'0' if i < 10 else ''}{i}" in values else 0

    ideal_gates.append(f"x{'0' if i < 10 else ''}{i} AND y{'0' if i < 10 else ''}{i} -> a{'0' if i < 10 else ''}{i}")
    ideal_gates.append(f"x{'0' if i < 10 else ''}{i} XOR y{'0' if i < 10 else ''}{i} -> b{'0' if i < 10 else ''}{i}")
    ideal_gates.append(f"b{'0' if i < 10 else ''}{i} AND c{'0' if i < 10 else ''}{i} -> d{'0' if i < 10 else ''}{i}")
    ideal_gates.append(f"a{'0' if i < 10 else ''}{i} OR d{'0' if i < 10 else ''}{i} -> c{'0' if i+1 < 10 else ''}{i+1}")
    ideal_gates.append(f"b{'0' if i < 10 else ''}{i} XOR c{'0' if i < 10 else ''}{i} -> z{'0' if i < 10 else ''}{i}")




actual_outputs = {}
ideal_outputs = {}

for gate in gates:
    out = gate[1]
    actual_outputs[out] = gate[0]
  
for gate in ideal_gates:
    out = gate.split(" -> ")[1]
    ideal_outputs[out] = gate.split(" -> ")[0]

aoT = {v: k for k, v in actual_outputs.items()}
ioT = {v: k for k, v in ideal_outputs.items()}
ideal_to_actual = {v: v for v in [l[0] for l in [*map(lambda x: x.split(": "), starts.split("\n")), *[f"z{'0' if i < 10 else ''}{i}" for i in range(0, 44)]]]}

changed = True
while changed:
    changed = False
    for instruction, out in ioT.items():
        a, op, b = instruction.split(" ")
        if a in ideal_to_actual:
            a = ideal_to_actual[a]
        
        if b in ideal_to_actual:
            b = ideal_to_actual[b]
        new_instruction = f"{a} {op} {b}"
        if new_instruction in aoT and out not in ideal_to_actual:
            ideal_to_actual[out] = aoT[new_instruction]
            changed = True
        new_instruction = f"{b} {op} {a}"
        if new_instruction in aoT and out not in ideal_to_actual:
            ideal_to_actual[out] = aoT[new_instruction]
            changed = True

actual_to_ideal = {v: k for k, v in ideal_to_actual.items()}




for i, gate in enumerate(ideal_gates):
    a, op, b = gate.split(" -> ")[0].split(" ")
    out = gate.split(" -> ")[1]
    if a not in ideal_to_actual or b not in ideal_to_actual or out not in ideal_to_actual:
        print(a, op, b, "=", out)
        print(ideal_gates[:i+1])
        print(ideal_to_actual.get(a), ideal_to_actual.get(b), ideal_to_actual.get(out))
        
        break

diffs = z ^ (x + y)
for i in range(0, 44):
    if (diffs >> i) & 1:
        print(i, "is different")
        break
else:
    print("the input has been fixed")
    exit()

print(ideal_to_actual.get(f"a{str(i).zfill(2)}"),
      ideal_to_actual.get(f"b{str(i).zfill(2)}"),
      ideal_to_actual.get(f"c{str(i).zfill(2)}"),
      ideal_to_actual.get(f"c{str(i+1).zfill(2)}"),
      ideal_to_actual.get(f"d{str(i).zfill(2)}"),
      ideal_to_actual.get(f"z{str(i).zfill(2)}")
)

print(old_values[f"x{str(i).zfill(2)}"],
      old_values[f"y{str(i).zfill(2)}"],
      old_values.get(ideal_to_actual.get(f"c{str(i).zfill(2)}")),
      old_values.get(ideal_to_actual.get(f"a{str(i).zfill(2)}")),
      old_values.get(ideal_to_actual.get(f"b{str(i).zfill(2)}")),
      old_values.get(ideal_to_actual.get(f"c{str(i+1).zfill(2)}")),
      old_values.get(ideal_to_actual.get(f"d{str(i).zfill(2)}")),
      old_values.get(ideal_to_actual.get(f"z{str(i).zfill(2)}"))
)


"""Manually inspect how these should be changed to make this work"""
