import aoc

data = aoc.import_input(15)
# data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

def funny_hash(string):
    total = 0
    for ch in string:
        total += ord(ch)
        total *= 17
        total %= 256
    return total

total = 0
for thing in data.split(","):
    total += funny_hash(thing)
print(total)



hashmap = {i: [] for i in range(256)}

for thing in data.split(","):
    h = funny_hash(thing[:-2] if "=" in thing else thing[:-1])
    box = hashmap[h]
    if "=" in thing:
        for i, lens in enumerate(box):
            if lens[:-2] == thing[:-2]:
                box.pop(i)
                box.insert(i, thing)
                break
        else:
            box.append(thing)
    elif "-" in thing:
        for lens in box:
            if lens[:-2] == thing[:-1]:
                box.remove(lens)
    else:
        raise ValueError
                    

total = 0
for k, v in hashmap.items():
    for i, item in enumerate(v):
        total += (k+1)*(i+1)*int(item[-1])
print(total)