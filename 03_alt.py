
import re
input = open("input").read()

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

lines = input.strip().split("\n")

# sum all numbers that touch a symbol

def rectsIntersect(r1, r2):
    ax, ay, bx, by = r1
    cx, cy, dx, dy = r2
    return cx <= bx and dx >= ax and cy <= by and dy >= ay

def expandRect(rect, margin):
    ax, ay, bx, by = rect
    return [ax - margin, ay - margin, bx + margin, by + margin]

def collect(pattern):
    result = []
    for (y, l) in enumerate(lines):
        for m in re.finditer(pattern, l):
            a, b = m.span()
            result.append((m.group(0), [a, y, b-1, y]))

    return result

nums = [(int(n), expandRect(r, 1)) for (n, r) in collect("\d+")]
symbols = collect("[^0-9^.]")
total = sum([n for (n, r) in nums if any([rectsIntersect(r, r2) for (s, r2) in symbols])])


nums = [(int(n), expandRect(r, 1)) for (n, r) in collect("\d+")]
stars = collect("\*")
total = 0
for _, r1 in stars:
    v = []
    for num, r2 in nums:
        if rectsIntersect(r1, r2):
            v.append(num)
    if len(v) == 2:
        total += v[0] * v[1]

print(total)
