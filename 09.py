import re
import itertools

input = open("input_09").read()

_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

lines = [[int(v) for v in l.split(" ")] for l in input.strip().split("\n")]


t = 0
for l in lines:
    states = [l]
    diffs = l
    while any(diffs):
        diffs = [p[1] - p[0] for p in itertools.pairwise(diffs)]
        states.append(diffs)
    states.reverse()
    for i, s in enumerate(states[1:]):
        states[i + 1].append(states[i + 1][-1] + states[i][-1])
    t += states[-1][-1]
print(t)


lines = [[int(v) for v in l.split(" ")] for l in input.strip().split("\n")]
t = 0
for l in lines:
    states = [l]
    diffs = l
    while any(diffs):
        diffs = [p[1] - p[0] for p in itertools.pairwise(diffs)]
        states.append(diffs)
    states.reverse()
    for i, s in enumerate(states[1:]):
        states[i + 1].insert(0, states[i + 1][0] - states[i][0])
    t += states[-1][0]
print(t)
