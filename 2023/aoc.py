
def import_input(day):
    with open(f"inputs/day_{str(day)}.txt", "r") as f:
        data = f.read()
    return data


if __name__ == "__main__":
    import os
    os.mkdir("inputs")
    for i in range(1, 26):
        d = f"day_{str(i)}.py"
        with open(d, "w") as f:
            f.write(f"""import aoc\n\ndata = aoc.import_input({str(i)})\n""")
        with open(f"inputs/day_{str(i)}.txt", "w") as f:
            f.write("")
        

        