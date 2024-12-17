from aoc import *

data = import_input(17)

a, b, c, *program = nums(data)

pc = 0
output = []

operands = [lambda: 0, lambda: 1, lambda: 2, lambda: 3, lambda: a, lambda: b, lambda: c]

def adv(operand):
    global a, b, c, pc
    operand = operands[operand]()
    a = a // 2**operand
    

def bxl(operand):
    global a, b, c, pc
    b = b ^ operand
    

def bst(operand):
    global a, b, c, pc
    operand = operands[operand]()
    b = operand % 8
    

def jnz(operand):
    global a, b, c, pc
    if a != 0:
        pc = operand-2
        

def bxc(operand):
    global a, b, c, pc
    b = b ^ c
    

def out(operand):
    global a, b, c, pc, output
    operand = operands[operand]()
    output.append(operand%8)
    

def bdv(operand):
    global a, b, c, pc
    operand = operands[operand]()
    b = a // 2**operand
    

def cdv(operand):
    global a, b, c, pc
    operand = operands[operand]()
    c = a // 2**operand
    


ops = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]


def run(test_a):
    global a, b, c, pc, output
    a = test_a
    pc = 0
    output = []
    while pc < len(program):
        op, operand = program[pc], program[pc+1]
        ops[op](operand)
        pc += 2
    return output


print(",".join(map(str, run(a))))
# a, b, c, *program = nums(data)


"""
program does:
b = a % 8
b ^= 7
c = a//2**b
a = a//2**3
b ^= c
b ^= 7
out b
restart if a != 0
"""

target = program.copy()

import z3

def program_z3(a):
    b = c = 0
    constraints = []
    for i in range(16):
        b = a % 8
        b = b ^ 7
        c = z3.LShR(a, b)
        a = z3.LShR(a, 3)
        b = b ^ c
        b = b ^ 7
        constraints.append(b%8 == target[i])
        if a == 0:
            break
    return constraints

a = z3.BitVec('a', 51)
solver = z3.Solver()
solver.add(program_z3(a))

solutions = []
while solver.check() == z3.sat:
    model = solver.model()
    a_value = model[a].as_long()
    solutions.append(a_value)
    solver.add(a != a_value)

print(min(solutions))
