import aoc

data = aoc.import_input(1)
total = 0
for line in data.split():
    first = ""
    last = ""
    for char in line:        
        if char.isdigit():
            if not first:
                first = char
            last = char
    
    total += int(first+last)

print(total)


total = 0
words = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}


def ends_in_number(string:str):
    for i in range(len(string)-2):
        if string[i:] in words:
            return string[i:]
    return False


for line in data.split():
    first = ""
    last = ""
    cur_word = ""
    for char in line:        
        if char.isdigit():
            cur_word = ""
            if not first:
                first = char
            last = char
        else:
            cur_word += char
            if word:= ends_in_number(cur_word):
                if not first:
                    first = str(words[word])
                last = str(words[word])

    total += int(first+last)

print(total)