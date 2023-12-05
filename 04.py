import re
input = open("input_04").read()


_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

lines = input.strip().split("\n")
total = 0
for l in lines:
    a, b = l.strip().split(":")
    w, n = b.strip().split(" | ")
    w = [int(v) for v in re.split(" +", w.strip())]
    n = [int(v) for v in re.split(" +", n.strip())]
    count = len(set(w)&set(n))
    v = 0 if count == 0 else 2**(count - 1)
    total += v
print(total)


lines = input.strip().split("\n")
cards = []
for l in lines:
    a, b = l.strip().split(":")
    w, n = b.strip().split(" | ")
    w = [int(v) for v in re.split(" +", w.strip())]
    n = [int(v) for v in re.split(" +", n.strip())]
    count = len(set(w)&set(n))
    cards.append([count, 1])

for (i, card) in enumerate(cards):
    for j in range(card[0]):
        cards[i + j + 1][1]+=card[1]

print(sum([c[1] for c in cards]))
