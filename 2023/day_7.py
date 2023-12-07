import aoc
import functools

data = aoc.import_input(7)
# data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

def compare_hands(hand1, hand2):
    #returns hand1>hand2
    hand1 = hand1.split()[0]
    hand2 = hand2.split()[0]
    counts1 = [hand1.count(ch) for ch in hand1]
    counts2 = [hand2.count(ch) for ch in hand2]
    mc1 = max(counts1)
    mc2 = max(counts2)
    #more similar cards always better
    if mc1 > mc2:
        return 1
    elif mc1 < mc2:
        return -1
    else:
        assert mc1 == mc2
        if mc1 == 3:
            if 2 in counts1 and 2 not in counts2:
                return 1
            elif 2 in counts2 and 2 not in counts1:
                return -1
        
        if counts1.count(2) == 4 and counts2.count(2) != 4:
            return 1
        if counts2.count(2) == 4 and counts1.count(2) != 4:
            return -1
    #same
    VALUES = {ck: i for i, ck in enumerate("23456789TJQKA")}
    for c1, c2 in zip(hand1, hand2):
        if VALUES[c1] > VALUES[c2]:
            return 1
        elif VALUES[c1] < VALUES[c2]:
            return -1
    return 0

ordered = sorted(data.split("\n"), key=functools.cmp_to_key(compare_hands))
total = 0
for i, line in enumerate(ordered):
    total += (i+1)*int(line.split()[1])
print(total)

# probably could've done part 1 like i do part 2 but that way came to mind first

def hand_key(hand):
    value = 0 #base 13 yippee
    hand = hand.split()[0]
    count = [hand.count(ch) for ch in hand if ch != "J"]+[0] #in case JJJJJ
    mc = max(count)
    jc = hand.count("J")
    if mc+jc == 5:
        value = 6
    elif mc+jc == 4:
        value = 5
    elif mc+jc == 3:
        if not jc:
            if 2 in count:
                value = 4
            else:
                value = 3
        else:
            if count.count(2) == 4:
                value = 4
            else:
                value = 3
    elif mc+jc == 2:
        if not jc:
            if count.count(2) == 4:
                value = 2
            else:
                value = 1
        else:
            value = 1
    #high card stays 0
    value *= 13**6
    VALUES = {ch: i for i, ch in enumerate("J23456789TQKA")}
    for i,ch in enumerate(hand):
        value += VALUES[ch]*13**(5-i) #last 5 digits are base 13 digits of the cards 
    return value
        

ordered = sorted(data.split("\n"), key=hand_key)
total = 0
for i, line in enumerate(ordered):
    total += (i+1)*int(line.split()[1])
print(total)