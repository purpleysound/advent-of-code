import aoc

data = aoc.import_input(9)
# data = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

# def new_list(nums):
#     new = []
#     for i in range(len(nums)-1):
#         new.append(nums[i+1]-nums[i])
#     if all(num == 0 for num in new):
#         newnew = new + [0]
#         return nums + [newnew[-1]+nums[-1]]
#     else:
#         newnew = new_list(new)
#         return nums + [newnew[-1]+nums[-1]]

total = 0
for line in data.split("\n"):
    original = aoc.get_nums_negative(line)
    seqs = [original]
    for seq in seqs:
        new = []
        for i in range(len(seq)-1):
            new.append(seq[i+1]-seq[i])
        if all(num == 0 for num in new):
            seqs[-1].append(seqs[-1][-1])
            break
        else:
            seqs.append(new)
    for i in range(len(seqs)-2,-1,-1):
        seqs[i].append(seqs[i][-1]+seqs[i+1][-1])
    total += seqs[0][-1]

print(total)

total = 0
for line in data.split("\n"):
    original = aoc.get_nums_negative(line)
    seqs = [original]
    for seq in seqs:
        new = []
        for i in range(len(seq)-1):
            new.append(seq[i+1]-seq[i])
        if all(num == 0 for num in new):
            seqs[-1].insert(0, seqs[-1][0])
            break
        else:
            seqs.append(new)
    for i in range(len(seqs)-2,-1,-1):
        seqs[i].insert(0, seqs[i][0]-seqs[i+1][0])
    total += seqs[0][0]

print(total)