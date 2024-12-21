from aoc import *

data = import_input(21)

total = 0
total2 = 0

@functools.cache
def how_to_type_nums(s):
    """+---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+"""
    keypad = {
        '0': (3, 1), '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (0, 0),
        '8': (0, 1), '9': (0, 2), 'A': (3, 2)
    }
    dirs = []
    cur = keypad['A']

    for char in s:
        target = keypad[char]
        while cur[0] > target[0]:
            dirs.append('^')
            cur = (cur[0] - 1, cur[1])
        while cur[0] < target[0]:
            dirs.append('v')
            cur = (cur[0] + 1, cur[1])
        while cur[1] < target[1]:
            dirs.append('>')
            cur = (cur[0], cur[1] + 1)
        while cur[1] > target[1]:
            dirs.append('<')
            cur = (cur[0], cur[1] - 1)
        dirs.append('A')

    return ''.join(dirs)

@functools.cache
def how_to_type_dirs(s, start='A'):
    """    +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+"""
    keypad = {
        '^': (0, 1), 'A': (0, 2), '>': (1, 2),
        '<': (1, 0), 'v': (1, 1)
    }
    dirs = []
    cur = keypad[start]

    for char in s:
        target = keypad[char]
        while cur[0] > target[0]:
            dirs.append('^')
            cur = (cur[0] - 1, cur[1])
        while cur[0] < target[0]:
            dirs.append('v')
            cur = (cur[0] + 1, cur[1])
        while cur[1] < target[1]:
            dirs.append('>')
            cur = (cur[0], cur[1] + 1)
        while cur[1] > target[1]:
            dirs.append('<')
            cur = (cur[0], cur[1] - 1)
        dirs.append('A')

    return ''.join(dirs)

for line in data.split("\n"):
    total += nums(line)[0] * len(how_to_type_dirs(how_to_type_dirs(how_to_type_nums(line))))
print(total)
# this was a total fluke it doesnt even find the shortest path but it worked on my input
# i cheesed 1st place wtf T_T





def get_all_paths(p1, p2, path="", avoid=[]):
    if p1 == p2:
        return [path]
    paths = []
    horiz = ("<", ">")[p2[1] > p1[1]]
    vert = ("^", "v")[p2[0] > p1[0]]
    if p1[1] != p2[1]:
        if horiz == "<" and (p1[0], p1[1] - 1) not in avoid:
            paths += get_all_paths((p1[0], p1[1] - 1), p2, path + horiz, avoid)
        if horiz == ">" and (p1[0], p1[1] + 1) not in avoid:
            paths += get_all_paths((p1[0], p1[1] + 1), p2, path + horiz, avoid)
    if p1[0] != p2[0]:
        if vert == "^" and (p1[0] - 1, p1[1]) not in avoid:
            paths += get_all_paths((p1[0] - 1, p1[1]), p2, path + vert, avoid)
        if vert == "v" and (p1[0] + 1, p1[1]) not in avoid:
            paths += get_all_paths((p1[0] + 1, p1[1]), p2, path + vert, avoid)
    return paths


@functools.cache
def get_all_type_nums(s):
    """+---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+"""
    keypad = {
        '0': (3, 1), '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (0, 0),
        '8': (0, 1), '9': (0, 2), 'A': (3, 2)
    }
    dirs = [""]
    cur = keypad['A']

    for char in s:
        target = keypad[char]
        dirs = [d + p + "A" for d in dirs for p in get_all_paths(cur, target, avoid=[(3, 0)])]
        cur = target

    return dirs


@functools.cache
def get_all_type_dirs(s, start="A"):
    """    +---+---+
        | ^ | A |
    +---+---+---+
    | < | v | > |
    +---+---+---+"""
    keypad = {
        '^': (0, 1), 'A': (0, 2), '>': (1, 2),
        '<': (1, 0), 'v': (1, 1)
    }
    dirs = [""]
    cur = keypad[start]

    for char in s:
        target = keypad[char]
        dirs = [d + p + "A" for d in dirs for p in get_all_paths(cur, target, avoid=[(0, 0)])]
        cur = target

    return dirs


d = {
    c1+c2: [p[1:] for p in get_all_type_dirs(c1+c2, start=c1)] for c1 in "<>^vA" for c2 in "<>^vA"
}

@functools.cache
def get_all_type_dirs_recursive(s, depth):
    if depth == 0:
        return len(s)
    count = 0
    s = "A" + s
    for c1, c2 in zip(s, s[1:]):
        m = float("inf")
        for p in d[c1+c2]:
            m = min(m, get_all_type_dirs_recursive(p, depth-1))
        count += m
    return count


for line in data.split("\n"):
    m = float("inf")
    for p in get_all_type_nums(line):
        m = min(m, get_all_type_dirs_recursive(p, 25))
    total2 += nums(line)[0] * m


print(total2)
