import re
input = open("input_05").read()
import itertools


_input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

groups = input.strip().split("\n\n")
seeds = [int(s) for s in re.findall("\d+", groups[0])]

groups = [[[int(v) for v in l.strip().split(" ")] for l in g.strip().split("\n")[1:]] for g in groups[1:]]
print(groups)


for i, s in enumerate(seeds):
    for g in groups:
        for r in g:
            if r[1] <= s < (r[1] + r[2]):
                prevS = s
                s = r[0] + (s - r[1])
                break
    seeds[i] = s


print(min(seeds))




groups = input.strip().split("\n\n")
seedRanges = [int(s) for s in re.findall("\d+", groups[0])]
seedRanges = [(seedRanges[2*i],seedRanges[2*i] + seedRanges[2*i + 1] - 1) for i in range(len(seedRanges) // 2)]

groups = [[[int(v) for v in l.strip().split(" ")] for l in g.strip().split("\n")[1:]] for g in groups[1:]]

for i, g in enumerate(groups):
    changedSeeds = set()
    for r in g:
        nr = set()
        for sr in seedRanges:
            a, b, c, d = sr[0], sr[1], r[1], r[1] + r[2] - 1
            if b < c:
                unchanged, changed = [(a, b)], None
            elif a < c and c <= b <= d:
                unchanged, changed = [(a, c - 1)], (c, b)
            elif a < c and d < b:
                unchanged, changed = [(a, c - 1), (d + 1, b)], (c, d)
            elif c <= a <= d and c <= b <= d:
                unchanged, changed = [], (a, b)
            elif c <= a <= d and d < b:
                unchanged, changed = [(d + 1, b)], (a, d)
            if a > d:
                unchanged, changed = [(a, b)], None

            if changed:
                a = changed[0] - c + r[0]
                b = changed[1] - c + r[0]
                if b - a:
                    changedSeeds.add((a, b))
            for u in unchanged:
                if u[1] - u[0]:
                    nr.add(u)

        seedRanges = nr
    seedRanges = changedSeeds | seedRanges
    

print(min([p[0] for p in seedRanges]))
