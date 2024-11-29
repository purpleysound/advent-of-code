import re

def import_input(day):
    with open(f"../inputs/day_{str(day)}.txt", "r") as f:
        data = f.read()
    return data

def vector_add(v1, v2):
    return tuple(map(sum, zip(v1, v2)))

def vector_scale(v, s):
    return tuple(x*s for x in v)

def get_digits(string:str):
    return list(map(int, re.findall(r"\d", string)))

def get_nums(string:str):
    """Returns a list of all numbers in a string"""
    return list(map(int, re.findall(r"\d+", string)))

def get_nums_negative(string:str):
    """Returns a list of all numbers in a string, including but not exclusive to negative numbers"""
    return list(map(int, re.findall(r"-?\d+", string)))

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


if __name__ == "__main__":
    import os
    os.mkdir("../inputs")
    for i in range(1, 26):
        d = f"day_{str(i)}.py"
        with open(d, "w") as f:
            f.write(f"""import aoc\n\ndata = aoc.import_input({str(i)})\n""")
        with open(f"../inputs/day_{str(i)}.txt", "w") as f:
            f.write("")
    