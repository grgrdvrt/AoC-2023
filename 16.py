import re
import itertools

input = open("input_16").read()

_input = """
.|...=....
|.-.=.....
.....|-...
........|.
..........
.........=
..../.==..
.-.-/..|..
.|....-|.=
..//.|....
"""

left = (-1, 0)
right = (1, 0)
up = (0, -1)
down = (0, -1)

map = input.strip().split("\n")
w, h = len(map[0]), len(map)

def move(pos, vel):
    return (pos[0] + vel[0], pos[1] + vel[1])

def inMap(pos):
    x, y = pos
    return x >= 0 and x < w and y >= 0 and y < h

beams = [[(0, 0), right]]
energized = set([beams[0][0]])

def addBeam(pos, vel):
    beam = [move(pos, vel), vel]
    if inMap(beam[0]):
        energized.add(beam[0])
        beams.append(beam)

# left -> down -> right -> up
# -1, 0 -> 0, 1 -> 1, 0 -> 0, -1
def rotateLeft(vec): return (vec[1], -vec[0])

# left -> up -> right -> down
# -1, 0 -> 0, -1 -> 1, 0 -> 0, 1
def rotateRight(vec): return (-vec[1], vec[0])


def printMap():
    for y in range(h):
        l = []
        for x in range(w):
            if (x, y) in energized:
                l.append("#")
            else:
                l.append(map[y][x])

        print("".join(l))

seen = set()

while beams:
    for beam in beams:
        pos, vel = beam
        if (pos, vel) in seen:
            beams.remove(beam)
            continue
        seen.add((pos, vel))

        c = map[pos[1]][pos[0]]
        # print(c)
        # printMap()

        if c == ".":
            beam[0] = move(pos, vel)
        elif c == "\\":
            vel = rotateRight(vel) if vel[1] == 0 else rotateLeft(vel)
            beam[0], beam[1] = move(pos, vel), vel
        elif c == "/":
            vel = rotateLeft(vel) if vel[1] == 0 else rotateRight(vel)
            beam[0], beam[1] = move(pos, vel), vel
        elif c == "|":
            if vel[1] == 0:
                vel = (0, -1)
                beam[0], beam[1] = move(pos, vel), vel
                addBeam(pos, (0, 1))
            else: beam[0] = move(pos, vel)
        elif c == "-":
            if vel[0] == 0:
                vel = (-1, 0)
                beam[0], beam[1] = move(pos, vel), vel
                addBeam(pos, (1, 0))
            else: beam[0] = move(pos, vel)

        if inMap(beam[0]):
            energized.add(beam[0])
        else:
            beams.remove(beam)

print("total", len(energized))







beams = []
energized = set()

def addBeam(pos, vel):
    beam = [move(pos, vel), vel]
    if inMap(beam[0]):
        energized.add(beam[0])
        beams.append(beam)



def printMap():
    for y in range(h):
        l = []
        for x in range(w):
            if (x, y) in energized:
                l.append("#")
            else:
                l.append(map[y][x])

        print("".join(l))

seen = set()

sTop = [[(i, 0), (0, 1)] for i in range(w)]
sBottom = [[(i, h-1), (0, -1)] for i in range(w)]
sLeft = [[(0, i), (0, 1)] for i in range(h)]
sRight = [[(w - 1, i), (0, -1)] for i in range(h)]

starts = sTop + sBottom + sLeft + sRight

result = 0
for s in starts:
    beam = []
    energized = set()

    beams.append(s)
    energized.add(beams[0][0])

    while beams:
        for beam in beams:
            pos, vel = beam
            if (pos, vel) in seen:
                beams.remove(beam)
                continue
            seen.add((pos, vel))

            c = map[pos[1]][pos[0]]

            if c == ".":
                beam[0] = move(pos, vel)
            elif c == "\\":
                vel = rotateRight(vel) if vel[1] == 0 else rotateLeft(vel)
                beam[0], beam[1] = move(pos, vel), vel
            elif c == "/":
                vel = rotateLeft(vel) if vel[1] == 0 else rotateRight(vel)
                beam[0], beam[1] = move(pos, vel), vel
            elif c == "|":
                if vel[1] == 0:
                    vel = (0, -1)
                    beam[0], beam[1] = move(pos, vel), vel
                    addBeam(pos, (0, 1))
                else: beam[0] = move(pos, vel)
            elif c == "-":
                if vel[0] == 0:
                    vel = (-1, 0)
                    beam[0], beam[1] = move(pos, vel), vel
                    addBeam(pos, (1, 0))
                else: beam[0] = move(pos, vel)

            if inMap(beam[0]):
                energized.add(beam[0])
            else:
                beams.remove(beam)
    result = max(result, len(energized))
print(result)
