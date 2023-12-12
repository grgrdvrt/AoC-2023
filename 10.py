import re
import itertools

input = open("input").read()

_input = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""


begin = None
lines = input.strip().split("\n")
for j, l in enumerate(lines):
    for i, c in enumerate(l):
        if c == "S":
            begin = (i, j)

# path = [begin]
dir = None
def changeDir(dir, c):
    if c == "J":
        return (0, -1) if dir == (1, 0) else (-1, 0)
    elif c == "7":
        return (0, 1) if dir == (1, 0) else (-1, 0)
    elif c == "F":
        return (0, 1) if dir == (-1, 0) else (1, 0)
    elif c == "L":
        return (0, -1) if dir == (-1, 0) else (1, 0)
    else: return dir

turns = "J7FL"

def readM(pos):
    return lines[pos[1]][pos[0]]

def inMap(pos):
    return pos[0] >= 0 and pos[0] < len(lines[0]) and pos[1] >= 0 and pos[1] < len(lines)

initDirs = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

pos = begin
for d in initDirs:
    np = (pos[0] + d[0], pos[1] + d[1])

    if inMap(np) and (readM(np) in turns):
        dir = d
        break

print(dir)
c = readM(np)
pos = (pos[0] + dir[0], pos[1] + dir[1])
dir = changeDir(dir, c)
print(pos, dir)

count = 1
while readM(pos) != "S":
    pos = (pos[0] + dir[0], pos[1] + dir[1])
    if not(inMap(pos)):print("oops")
    dir = changeDir(dir, readM(pos))
    count += 1
print(count / 2)



print(begin)


_input = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""

_input = """
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""


begin = None
lines = input.strip().split("\n")
for j, l in enumerate(lines):
    for i, c in enumerate(l):
        if c == "S":
            begin = (i, j)
print("begin", begin)

dir = None
def changeDir(dir, c):
    if c == "J":
        return (0, -1) if dir == (1, 0) else (-1, 0)
    elif c == "7":
        return (0, 1) if dir == (1, 0) else (-1, 0)
    elif c == "F":
        return (0, 1) if dir == (-1, 0) else (1, 0)
    elif c == "L":
        return (0, -1) if dir == (-1, 0) else (1, 0)
    else: return dir

pipes = "J7FL|-"

def readM(pos):
    return lines[pos[1]][pos[0]]

def inMap(pos):
    return pos[0] >= 0 and pos[0] < len(lines[0]) and pos[1] >= 0 and pos[1] < len(lines)

initDirs = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

pos = begin
for d in initDirs:
    np = (pos[0] + d[0], pos[1] + d[1])
    print(np, inMap(np), readM(np))

    if inMap(np) and (readM(np) in pipes):
        dir = d
        break
print("initDir", dir)

c = readM(np)
pos = (pos[0] + dir[0], pos[1] + dir[1])
dir = changeDir(dir, c)
print(pos, dir)

found = set([begin, pos])
while readM(pos) != "S":
    pos = (pos[0] + dir[0], pos[1] + dir[1])
    dir = changeDir(dir, readM(pos))
    found.add(pos)


enter = "FL"
exiter = "7J"
count = 0
for j, l in enumerate(lines):
    isIn = False
    nl = (list(l))
    prev = "."
    lastEnter = None
    for i, c in enumerate(l):
        if (i, j) in found:
            if c == "|": isIn = not(isIn)
            elif c in enter:
                lastEnter = c
            elif c in exiter:
                if c == "7" and lastEnter == "L":
                  isIn = not(isIn)
                elif c == "J" and lastEnter == "F":
                  isIn = not(isIn)
        elif isIn:
            count += 1
        # nl[i] = c + str(0 if ((i, j) in found) else (1 if isIn else 0))
        nl[i] = c + str(1 if isIn else 0)
        prev = c
    # print(nl)
print(count)

# 1448 too high
