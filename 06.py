import re
import itertools


input = """
Time:        54     94     65     92
Distance:   302   1476   1029   1404
"""

_input = """
Time:      7  15   30
Distance:  9  40  200
"""


t, d = input.strip().split("\n")

times = [int(v) for v in re.findall("\d+", t)]
distances = [int(v) for v in re.findall("\d+", d)]
races = list(zip(times, distances))


total = 1
for (t, d) in races:
    count = 0
    for c in range(t):
        d2 = c * (t - c)
        if d2 > d:
            count += 1
    total *= count
print(total)



time = 54946592
distance = 302147610291404

# time = 71530
# distance = 940200



count = 0
for c in range(time):
    d2 = c * (time - c)
    if d2 > distance:
        count += 1
print(count)
