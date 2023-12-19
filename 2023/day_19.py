import aoc

data = aoc.import_input(19)
# data = """px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}"""
rules_str, objects_str = data.split("\n\n")
rules_str = rules_str.split("\n")
objects_str = objects_str.split("\n")
rules = dict()
for rule_str in rules_str:
    rule = rule_str.split("{")
    key = rule[0]
    rule = [x.split(":") for x in rule[1][:-1].split(",")]
    rules[key] = rule
# print(rules)

objects = []
for object_str in objects_str:
    objects.append(aoc.get_nums(object_str))

accepted_sum = 0
for object in objects:
    x, m, a, s = object
    cur = "in"
    while cur != "R" and cur != "A":
        rule = rules[cur]
        for r in rule[:-1]:
            if eval(r[0]):  # mmmmm eval
                cur = r[1]
                break
        else:
            cur = rule[-1][0]
    if cur == "A":
        accepted_sum += sum(object)
print(accepted_sum)

del x, m, a, s, cur, rule, r, object, objects_str, rules_str, data, accepted_sum

from collections import deque
q = deque([((1, 4000), (1, 4000), (1, 4000), (1, 4000), "in")])
# x, m, a, s = as (start, stop) range tuples inclusive

def volume(xr, mr, ar, sr):
    return (xr[1] - xr[0] +1) * (mr[1] - mr[0] +1) * (ar[1] - ar[0] +1) * (sr[1] - sr[0] +1)


total = 0
seen = set()
while q:
    item = q.popleft()
    # if item in seen:
    #     continue
    # seen.add(item)
    xr, mr, ar, sr, cur = item
    if cur == "R":
        continue
    if cur == "A":
        total += volume(xr, mr, ar, sr)
        continue
    rule = rules[cur]
    for r in rule[:-1]:
        condition, next_rule = r
        variable_idx = ["x","m","a","s"].index(condition[0])
        var = item[variable_idx]
        start_range, end_range = var
        sign = condition[1]
        comparison_value = int(condition[2:])
        if sign == "<":
            if start_range >= comparison_value:
                continue
            if end_range < comparison_value:
                next_rule = next_rule
                q.append((xr, mr, ar, sr, next_rule))
                break
            else:
                #split range
                left_start = start_range
                left_end = comparison_value - 1
                left_next_rule = next_rule
                left_item = [xr, mr, ar, sr]
                left_item[variable_idx] = (left_start, left_end)
                left_item.append(left_next_rule)
                q.append(tuple(left_item))
                right_start = comparison_value
                right_end = end_range
                right_next_rule = cur
                right_item = [xr, mr, ar, sr]
                right_item[variable_idx] = (right_start, right_end)
                right_item.append(right_next_rule)
                q.append(tuple(right_item))
                break
        elif sign == ">":
            if start_range > comparison_value:
                next_rule = next_rule
                q.append((xr, mr, ar, sr, next_rule))
                break
            if end_range <= comparison_value:
                continue
            else:
                #split range
                left_start = start_range
                left_end = comparison_value
                left_next_rule = cur
                left_item = [xr, mr, ar, sr]
                left_item[variable_idx] = (left_start, left_end)
                left_item.append(left_next_rule)
                q.append(tuple(left_item))
                right_start = comparison_value + 1
                right_end = end_range
                right_next_rule = next_rule
                right_item = [xr, mr, ar, sr]
                right_item[variable_idx] = (right_start, right_end)
                right_item.append(right_next_rule)
                q.append(tuple(right_item))
                break
    else:
        next_rule = rule[-1][0]
        q.append((xr, mr, ar, sr, next_rule))
        continue

print(total)