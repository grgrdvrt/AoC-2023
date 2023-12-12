import re
import itertools

input = open("input").read()

_input = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

lines = input.strip().split("\n")
emptyCols = [True] * len(lines[0])
emptyLines = [True]*len(lines)
galaxies = []

for j, l in enumerate(lines):
    for i, c in enumerate(l):
        if c == "#":
            emptyLines[j] = False
            emptyCols[i] = False
            galaxies.append((i, j))
emptyLines = [i for i, v in enumerate(emptyLines) if v]
emptyCols = [i for i, v in enumerate(emptyCols) if v]

pairs = set()
for x in galaxies:
    for y in galaxies:
        if x != y and (y, x) not in pairs:
            pairs.add((x, y))

n = 2
n = 1000000
# n = 10
# n = 100
lengths = []
for (a, b) in pairs:
    dist = abs(b[0] - a[0]) + abs(b[1] - a[1])
    for c in emptyCols:
        if min(a[0], b[0]) < c < max(a[0], b[0]):
            dist+=n-1
    for c in emptyLines:
        if min(a[1], b[1]) < c < max(a[1], b[1]):
            dist+=n-1
    lengths.append(dist)

print(sum(lengths))
