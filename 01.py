import re
input = open("input").read().strip()

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
s = 0
for l in input.strip().split("\n"):
    p = re.compile("(?=(\d|one|two|three|four|five|six|seven|eight|nine))");
    n = [v for v in p.findall(l) if v != ""]
    a, b = n[0], n[-1];
    if a in nums:
        a = nums.index(a) + 1
    if b in nums:
        b = nums.index(b) + 1
    val = int(str(a) + str(b))
    s += val
print(s)
