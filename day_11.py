"""Monkey 0:
  Starting items: 74, 64, 74, 63, 53
  Operation: new = old * 7
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 1:
  Starting items: 69, 99, 95, 62
  Operation: new = old * old
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 5

Monkey 2:
  Starting items: 59, 81
  Operation: new = old + 8
  Test: divisible by 7
    If true: throw to monkey 4
    If false: throw to monkey 3

Monkey 3:
  Starting items: 50, 67, 63, 57, 63, 83, 97
  Operation: new = old + 4
  Test: divisible by 13
    If true: throw to monkey 0
    If false: throw to monkey 7

Monkey 4:
  Starting items: 61, 94, 85, 52, 81, 90, 94, 70
  Operation: new = old + 3
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 3

Monkey 5:
  Starting items: 69
  Operation: new = old + 5
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 2

Monkey 6:
  Starting items: 54, 55, 58
  Operation: new = old + 7
  Test: divisible by 11
    If true: throw to monkey 1
    If false: throw to monkey 5

Monkey 7:
  Starting items: 79, 51, 83, 88, 93, 76
  Operation: new = old * 3
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 6"""
import sys
sys.set_int_max_str_digits(1000000)

class Monkey:
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.monkey_business = 0
    
    def inspect(self):
        for i, item in enumerate(self.items[:]):
            old_item = item
            self.monkey_business += 1
            item = eval(str(item)+self.operation)
            if item % self.test == 0:
                self.items.remove(old_item)
                monkeys[self.if_true].items.append(item)
            else:
                self.items.remove(old_item)
                monkeys[self.if_false].items.append(item)

monkeys = []
monkeys.append(Monkey([74, 64, 74, 63, 53], "*7", 5, 1, 6))
monkeys.append(Monkey([69, 99, 95, 62], "**2", 17, 2, 5))
monkeys.append(Monkey([59, 81], "+8", 7, 4, 3))
monkeys.append(Monkey([50, 67, 63, 57, 63, 83, 97], "+4", 13, 0, 7))
monkeys.append(Monkey([61, 94, 85, 52, 81, 90, 94, 70], "+3", 19, 7, 3))
monkeys.append(Monkey([69], "+5", 3, 4, 2))
monkeys.append(Monkey([54, 55, 58], "+7", 11, 1, 5))
monkeys.append(Monkey([79, 51, 83, 88, 93, 76], "*3", 2, 0, 6))

for _ in range(10000):
    for monkey in monkeys:
        monkey.inspect()

monkey_businesses = [monkey.monkey_business for monkey in monkeys]
monkey_businesses.sort(reverse=True)
score = monkey_businesses[0]*monkey_businesses[1]
print(score)