import aoc
from functools import lru_cache

data = aoc.import_input(4)
# data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
cards = data.split("\n")
for card in cards:
    card = card.split(":")[1]
total = 0
for card in cards:
    winnings, gotten = card.split("|")
    winnings = set(aoc.get_nums(winnings))
    gotten = aoc.get_nums(gotten)
    count = 0
    for num in gotten:
        if num in winnings:
            count += 1
    if count == 0:
        continue
    total += 2**(count-1)
print(total)

@lru_cache
def cacheable(card):
    start, end = card.split(":")
    card_no = int(start[4:])
    winnings, gotten = end.split("|")
    winnings = set(aoc.get_nums(winnings))
    gotten = aoc.get_nums(gotten)
    count = 0
    for num in gotten:
        if num in winnings:
            count += 1
    return card_no, count
    

cards = data.split("\n")
for card in cards:
    card_no, count = cacheable(card)
    for i in range(card_no,card_no+count):
        cards.append(cards[i])
print(len(cards))