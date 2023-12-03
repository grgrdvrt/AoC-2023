import re
input = open("input").read()
from collections import defaultdict

_input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
p = re.compile("\d|\.")
def isSpec(c):
    return not(p.match(c))

lines = input.strip().split("\n")

total = 0
for (j, l) in enumerate(lines):
    num = ""
    isInNumber = False
    symbols = []
    for (i, c) in enumerate(l):
        if re.match("\d", c):
            num = num + c
            isInNumber = True
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if a == 0 and b == 0:continue
                    if j + a < 0 or j + a >= len(lines):continue
                    if i + b < 0 or i + b >= len(l):continue
                    if isSpec(lines[j + a][i + b]):
                        symbols.append(lines[j + a][i + b])
        else:
            if isInNumber and symbols:
                total += int(num)
            num = ""
            symbols = []
            isInNumber = False
    if isInNumber and symbols:
        total += int(num)

print(total)


total = 0
table = defaultdict(list)
for (j, l) in enumerate(lines):
    num = ""
    isInNumber = False
    symbols = []
    for (i, c) in enumerate(l):
        if re.match("\d", c):
            num = num + c
            isInNumber = True
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if a == 0 and b == 0:continue
                    if j + a < 0 or j + a >= len(lines):continue
                    if i + b < 0 or i + b >= len(l):continue
                    if lines[j + a][i + b] == "*":
                        symbols.append((j + a, i + b))
        else:
            if isInNumber and symbols:
                table[symbols[0]].append(int(num))
            num = ""
            symbols = []
            isInNumber = False
    if isInNumber and symbols:
        table[symbols[0]].append(int(num))
print(table)
for key in table:
    if len(table[key]) == 2:
        total += table[key][0] * table[key][1]

print(total)

#1 18min34s
#2 8min42s
#total 27min16s
