import re
import itertools

input = open("input_12").read()

_input = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""


lines = input.strip().split("\n")



# count = 0
# for l in lines:
#     status, groups = l.split(" ")
#     groups = tuple([int(v) for v in groups.strip().split(",")])
#     uPos = [i for i, c in enumerate(status) if c == "?"]
#     c = len(uPos)
#     for i in range(2**c):
#         s = list(status)
#         for j, p in enumerate(uPos):
#             s[p] = "#" if i & 2**j else "."
#         if tuple(len(g) for g in re.split("\.+", "".join(s)) if g) == groups:
#             count += 1

# print(count)


# from one pattern, generate all the matching arrangements
# do we have to generate all? can we just count


for l in lines:
    status, groups = l.split(" ")
    groups = tuple([int(v) for v in groups.strip().split(",")])
    s = [g for g in re.split("\.+", status) if g]
    print(s, groups)


# from one pattern, generate all the matching arrangements
# do we have to generate all? can we just count
