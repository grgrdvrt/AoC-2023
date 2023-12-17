import re
import itertools

input = open("input_14").read()

_input = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""


lines = input.strip().split("\n")

w = len(lines[0])
h = len(lines)

total = 0
for i in range(w):
    c = 0
    for j in range(h):
        v = lines[j][i]
        if v == "#":
            c = 0
        elif v == "O":
            total += len(lines) - j + c
        elif v == ".":
            c += 1
print(total)




squares = []
for j, l in enumerate(lines):
    for i, c in enumerate(l):
        if c == "#":
            squares.append((i, j))


for i in range(w):
    c = 0
    for j in range(h):
        v = lines[j][i]
        if v == "#":
            c = 0
        elif v == "O":
            total += len(lines) - j + c
        elif v == ".":
            c += 1
