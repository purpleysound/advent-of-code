import aoc
from collections import deque
from copy import deepcopy

data = aoc.import_input(20)
# data = r"""broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a"""
# data = r"""broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output"""
lines = data.split("\n")

class Module:
    def __init__(self, name: str, outputs: list):
        self.name = name
        self.outputs = outputs.copy()
        self.memory = None

    def receive(self, high: bool, sender: str) -> tuple[bool, list[str]]:
        return False, []
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.outputs}, memory={self.memory})"
    
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name and self.memory == other.memory


class FlipFlop(Module):
    def __init__(self, name: str, outputs: list):
        super().__init__(name, outputs)
        self.memory = False
    
    def receive(self, high: bool, sender: str) -> tuple[bool, list[str]]:
        if high:
            return False, []
        self.memory = not self.memory
        return self.memory, self.outputs
    
class Conjunction(Module):
    def __init__(self, name: str, outputs: list):
        super().__init__(name, outputs)
        self.memory: dict[str, bool] = self.initialise_memory()

    def initialise_memory(self):
        memory = {}
        for line in lines:
            module, outs = line.split(" -> ")
            if self.name in outs.split(", "):
                memory[module[1:]] = False
        return memory
    
    def receive(self, high: bool, sender: str) -> tuple[bool, list[str]]:
        self.memory[sender] = high
        if all(self.memory.values()):
            return False, self.outputs
        return True, self.outputs
    
class Broadcaster(Module):
    def __init__(self, name: str, outputs: list):
        super().__init__(name, outputs)
    
    def receive(self, high: bool, sender: str) -> tuple[bool, list[str]]:
        return high, self.outputs
    
modules: dict[str, Module] = {}
empty_module = Module("", [])
for line in lines:
    module, outputs = line.split(" -> ")
    outputs = outputs.split(", ")
    if module == "broadcaster":
        broadcaster = Broadcaster("broadcaster", outputs)
        continue
    mod_type, mod_name = module[0], module[1:]
    if mod_type == "%":
        modules[mod_name] = FlipFlop(mod_name, outputs)
    elif mod_type == "&":
        modules[mod_name] = Conjunction(mod_name, outputs)
    else:
        raise RuntimeError
    

def push_button():
    q = deque([("broadcaster", False, out) for out in broadcaster.outputs])
    lows = 1 # button -low-> broadcaster
    highs = 0
    while q:
        name, high, output = q.popleft()
        if high:
            highs += 1
        else:
            lows += 1
        # print(f"{name} -{['low', 'high'][high]}-> {output}")
        new_high, new_outputs = modules.get(output, empty_module).receive(high, name)
        for out in new_outputs:
            q.append((output, new_high, out))
    return lows, highs

start = deepcopy(modules)
presses = 0
lows = 0
highs = 0
while True:
    dl, dh = push_button()
    lows += dl
    highs += dh
    presses += 1
    new = deepcopy(modules)
    if new == start:
        break
    if presses == 1000:
        break

# print(presses)
print(lows*highs)



def push_button():
    q = deque([("broadcaster", False, out) for out in broadcaster.outputs])
    while q:
        name, high, output = q.popleft()
        if name == "rx" and not high:
            return True
        if high and name in ["jt", "sx", "kb", "ks"] and name not in printed:
            print(f"{name} activated in {presses} presses")
            printed.add(name)

        # print(f"{name} -{['low', 'high'][high]}-> {output}")
        new_high, new_outputs = modules.get(output, empty_module).receive(high, name)
        for out in new_outputs:
            q.append((output, new_high, out))
    return False


presses = 0
printed = set()
modules = start
while True:
    presses += 1
    rx_pressed = push_button()
    if rx_pressed:
        print(presses)
    if len(printed) == 4:
        break

"""kb activated in 3851 presses
sx activated in 3877 presses
ks activated in 4021 presses
jt activated in 4049 presses"""

import math
print(math.lcm(3851, 3877, 4021, 4049))