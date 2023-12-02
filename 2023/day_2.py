import aoc

data = aoc.import_input(2)
games = data.split("\n")
total = 0
max_cubes = {"red": 12, "green": 13, "blue": 14}
for i, game in enumerate(games):
    impossible = False
    sets = game.split(":")[1].split(";")
    for show in sets:
        cubes = show.split(",")
        for count_colour in cubes:
            count, colour = count_colour.strip().split(" ")
            if int(count) > max_cubes[colour]:
                impossible = True
                break
    if not impossible:
        total += i+1
            
print(total)
games = data.split("\n")
total = 0
for game in games:
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    sets = game.split(":")[1].split(";")
    for show in sets:
        cubes = show.split(",")
        for count_colour in cubes:
            count, colour = count_colour.strip().split(" ")
            max_cubes[colour] = max(max_cubes[colour], int(count))
    total += max_cubes["red"]*max_cubes["green"]*max_cubes["blue"]

print(total)