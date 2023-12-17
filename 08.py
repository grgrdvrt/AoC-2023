import re
import itertools

input = open("input_08").read()

_input = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

_input = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

directions, lines = input.strip().split("\n\n")
directions = [0 if d == "L" else 1 for d in directions]

nodes = {}

for l in lines.strip().split("\n"):
    name, dirs = l.split(" = ")
    l, r = dirs[1:-1].split(", ")
    nodes[name] = (l, r)

place = nodes["AAA"]
print(place)
index = 0
steps = 0
while True:
    nextName = place[directions[index]];
    if nextName == "ZZZ":
        print(steps + 1)
        print(nodes[nextName])
        break
    place = nodes[nextName]
    index = (index + 1) % len(directions)
    steps += 1




    
_input = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

directions, lines = input.strip().split("\n\n")
directions = [0 if d == "L" else 1 for d in directions]

nodes = {}

for l in lines.strip().split("\n"):
    name, dirs = l.split(" = ")
    l, r = dirs[1:-1].split(", ")
    nodes[name] = (l, r)

places = [n[1] for n in nodes.items() if n[0][-1] == "A"]


cyclesLengths  = [-1 for _ in range(len(places))]
for i, place in enumerate(places):
    index = 0
    steps = 0
    while True:
        nextName = place[directions[index]];
        if nextName[-1] == "Z":
            cyclesLengths[i] = steps + 1
            break
        place = nodes[nextName]
        index = (index + 1) % len(directions)
        steps += 1
    
print(cyclesLengths)

from functools import reduce

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)


t = 1
for c in cyclesLengths:
    t *= c
print(t, lcmm(*cyclesLengths))
