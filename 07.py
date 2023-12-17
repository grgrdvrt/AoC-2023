import re
import itertools

input = open("input_07").read()


_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
cards = "A K Q J T 9 8 7 6 5 4 3 2".split(" ")
cards.reverse()

lines = input.strip().split("\n")
scores = [
    (1, 1, 1, 1, 1),
    (1, 1, 1, 2),
    (1, 2, 2),
    (1, 1, 3),
    (2, 3),
    (1, 4),
    (5,),
];

gamesByHand = {}
for s in scores:
    gamesByHand[s] = []
total = 0
for l in lines:
    hand, bid = l.split(" ")
    b = {};
    for c in cards:
        vals = re.findall(c, hand)
        b[c] = len(vals)
    handType = tuple(sorted([v for v in b.values() if v]))
    gamesByHand[handType].append(([cards.index(c) for c in hand], bid));

for games in gamesByHand:
    gamesByHand[games] = sorted(gamesByHand[games])
    gamesByHand[games]

total = 0
i = 0;
for games in gamesByHand:
    for game in gamesByHand[games]:
        i += 1
        total += i * int(game[1])

print(total)


cards = "A K Q T 9 8 7 6 5 4 3 2 J".split(" ")
cards.reverse()

lines = input.strip().split("\n")
scores = [
    (1, 1, 1, 1, 1),
    (1, 1, 1, 2),
    (1, 2, 2),
    (1, 1, 3),
    (2, 3),
    (1, 4),
    (5,),
];

gamesByHand = {}
for s in scores:
    gamesByHand[s] = []
total = 0
for l in lines:
    hand, bid = l.split(" ")
    b = {};
    for c in cards[1:]:
        vals = re.findall(c, hand)
        b[c] = len(vals)
    
    handType = sorted([v for v in b.values() if v])
    js = len(re.findall("J", hand))
    if len(handType):
        handType[-1] += js
    handType = (5,) if js == 5 else tuple(handType)
    gamesByHand[handType].append(([cards.index(c) for c in hand], bid));

for games in gamesByHand:
    gamesByHand[games] = sorted(gamesByHand[games])
    gamesByHand[games]

total = 0
i = 0;
for games in gamesByHand:
    for game in gamesByHand[games]:
        i += 1
        total += i * int(game[1])

print(total)
