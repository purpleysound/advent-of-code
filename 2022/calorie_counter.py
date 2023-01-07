with open("input.txt", "r") as f:
    calorie_list = "".join(f.readlines())

totals_list = []
current_calories = 0
for line in calorie_list.split("\n"):
    if line == "":
        current_calories = 0
    else:
        current_calories += int(line)
        totals_list.append(current_calories)

totals_list.sort(reverse=True)
print(totals_list[0] + totals_list[1] + totals_list[2])