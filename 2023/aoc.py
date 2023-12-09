import re

def import_input(day):
    with open(f"inputs/day_{str(day)}.txt", "r") as f:
        data = f.read()
    return data

def vector_add(v1, v2):
    return tuple(map(sum, zip(v1, v2)))

def vector_scale(v, s):
    return tuple(x*s for x in v)

def get_nums(string:str):
    """Returns a list of all numbers in a string"""
    return list(map(int, re.findall(r"\d+", string)))

def get_nums_negative(string:str):
    """Returns a list of all numbers in a string, including but not exclusive to negative numbers"""
    return list(map(int, re.findall(r"-?\d+", string)))

if __name__ == "__main__":
    import os
    os.mkdir("inputs")
    for i in range(1, 26):
        d = f"day_{str(i)}.py"
        with open(d, "w") as f:
            f.write(f"""import aoc\n\ndata = aoc.import_input({str(i)})\n""")
        with open(f"inputs/day_{str(i)}.txt", "w") as f:
            f.write("")
        

        