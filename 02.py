import re
input = open("input").read()

games = input.strip().split("\n")

counts= {"red":12, "green":13, "blue":14}
t = 0
for game in games:
    f = re.findall("(\d+) (red|green|blue)", game)
    valid = True
    for (v, c) in f:
        if int(v) > counts[c]: valid = False
    if valid:
        t += int(re.findall("\d+", game)[0])
print(t)

t = 0
for game in games:
    f = re.findall("(\d+) (red|green|blue)", game)
    counts = {"red":0, "green":0, "blue":0}
    for (v, c) in f:
        counts[c] = max(counts[c], int(v))
    t += counts["red"] * counts["green"] * counts["blue"]
print(t)

# 86400 too high
