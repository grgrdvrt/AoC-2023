import re
import itertools

input = open("input_13").read()

_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""


patterns = input.strip().split("\n\n")

def checkLines(lines):
    for i in range(len(lines) - 1):
        l = min(i + 1, len(lines) - i - 1)
        eq = True
        for j in range(l):
            if lines[i + j + 1] != lines[i - j]:
                eq = False
                break
        if eq: return i + 1
    return None

count = 0
for p in patterns:
    lines = p.strip().split("\n")
    
    c = checkLines(lines)
    if c: count += 100 * c

    trans = []
    for i in range(len(lines[0])):
        trans.append([None]*len(lines))
    for j, l in enumerate(lines):
        for i, c in enumerate(l):
            trans[i][j] = c

    c = checkLines(trans)
    if c: count += c


print(count)

def diffeq(a, b):
    diff = 0
    for i, c in enumerate(a):
        if c != b[i]: diff+=1
    return diff

def checkLines(lines):
    for i in range(len(lines) - 1):
        l = min(i + 1, len(lines) - i - 1)

        diff = 0
        for j in range(l):
            diff += diffeq(lines[i + j + 1], lines[i - j])
        if diff == 1: return i + 1
    return None

count = 0
for p in patterns:
    lines = p.strip().split("\n")
    
    c = checkLines(lines)
    if c: count += 100 * c

    trans = []
    for i in range(len(lines[0])):
        trans.append([None]*len(lines))
    for j, l in enumerate(lines):
        for i, c in enumerate(l):
            trans[i][j] = c

    c = checkLines(trans)
    if c: count += c


print(count)

# 33494 too low
