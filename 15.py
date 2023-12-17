import re
import itertools

input = open("input_15").read()

input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


string = "HASH"

steps = input.strip().split(",")


def aochash(string):
    val = 0
    for c in string:
        val = ((val + ord(c)) * 17)%256
    return val

total = 0
for s in steps:
    total += aochash(s)
print(total)



# focal length in [0, 9]
boxes = [[] for i in range(256)]
for s in steps:
    m = re.search("(\w+)(-|=)(\d?)", s)
    label, op, fl = m.groups(0)
    boxId = aochash(label)

    if op == "-":
        boxes[boxId] = [l for l in boxes[boxId] if l[0] != label]
    elif op == "=":
        fl = int(fl)
        found = False
        for l in boxes[boxId]:
            if l[0] == label:
                l[1] = fl
                found = True
        if not(found):
            boxes[boxId].append([label, fl])

result = 0
for i, b in enumerate(boxes):
    result += sum([(i + 1) * (j + 1) * l[1] for j, l in enumerate(b)])

print(result)
