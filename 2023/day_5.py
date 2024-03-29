import aoc
import itertools

data = aoc.import_input(5)
# data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

seeds, *ranges = data.split("\n\n")
seeds = aoc.get_nums(seeds)
list_of_list_of_maps = []
for map_range in ranges:
    list_of_list_of_maps.append(list(map(tuple, map(aoc.get_nums, map_range.split("\n")[1:]))))

lowest = 9999999999999
for seed in seeds:
    #check which range it is in
    #find end value
    #loop over whole list_of_maps until end of list
    #store min final value
    current_val = seed
    for list_of_maps in list_of_list_of_maps:
        for mapp in list_of_maps:
            dest_start, source_start, length = mapp
            if source_start <= current_val <= source_start+length:
                current_val = dest_start+(current_val-source_start)
                break
    lowest = min(lowest, current_val)

print(lowest)




def finish_range(seed_range, depth=0):
    current_range = seed_range
    for i, list_of_maps in enumerate(list_of_list_of_maps[depth:]):
        for mapp in list_of_maps:
            dest_start, source_start, length = mapp
            # if current_range = (3, 4)
            # start = 3, end = 6 == 3+4-1
            current_start, current_length = current_range
            #totally in
            if source_start <= current_start <= source_start+length and source_start <= current_start+current_length <= source_start+length:
                current_start = dest_start+(current_start-source_start)
                current_range = (current_start, current_length)
                break
            #partially in one side
            #  10 2 3
            # (3, 4)
            # 3 4 5 6 -> 11 12 5 6 
            #left side in, right side out
            if source_start <= current_start <= source_start+length and not (source_start <= current_start+current_length <= source_start+length):
                in_start = dest_start+(current_start-source_start)
                in_length = source_start+length-current_start
                in_range = (in_start, in_length)
                not_in_start = source_start+length+1
                not_in_length = current_length-in_length
                not_in_range = (not_in_start, not_in_length)
                return min(finish_range(in_range, depth=i+depth+1), finish_range(not_in_range, depth=i+depth))
            #right side in, left side out
            # 10 5 3
            # (3, 4)
            # 3 4 5 6 -> 3 4 10 11
            if not (source_start <= current_start <= source_start+length) and source_start < current_start+current_length <= source_start+length:
                in_start = dest_start
                in_length = current_start+current_length-source_start
                in_range = (in_start, in_length)
                not_in_start = current_start
                not_in_length = current_length-in_length
                not_in_range = (not_in_start, not_in_length)
                return min(finish_range(in_range, depth=i+depth+1), finish_range(not_in_range, depth=i+depth))
            #partially in 2 sides
            # 10 5 3
            # (3, 7)
            # 3, 4, 5, 6, 7, 8, 9 -> 3, 4, 10, 11, 12, 8, 9
            if current_start < source_start and current_start+current_length > source_start+length:
                #left side
                left_start = current_start  
                left_length = source_start-current_start
                left_range = (left_start, left_length)
                #middle
                middle_start = dest_start
                middle_length = length
                middle_range = (middle_start, middle_length)
                #right side
                right_start = source_start+length+1
                right_length = current_length-left_length-length
                right_range = (right_start, right_length)
                return min(finish_range(left_range, depth=i+depth), finish_range(middle_range, depth=i+depth+1), finish_range(right_range, depth=i+depth))
            #not in

    return current_range[0]


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch

lowest = 99999999999999999

seed_ranges = batched(seeds, 2)
for seed_range in seed_ranges:
    lowest = min(lowest, finish_range(seed_range))
print(lowest)