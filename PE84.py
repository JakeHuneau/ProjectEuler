import random


def roll_dice(sides=4):
    return random.randint(1, sides)


def chance(chance_pos, monopoly_pos):
    goto = [0, 10, 11, 24, 39, 5]

    if chance_pos <= 5:
        monopoly_pos = goto[chance_pos]

    if chance_pos in {6, 7}:
        if monopoly_pos == 7:
            monopoly_pos = 15
        elif monopoly_pos == 22:
            monopoly_pos = 25
        elif monopoly_pos == 36:
            monopoly_pos = 5

    if chance_pos == 8:
        if monopoly_pos in {7, 36}:
            monopoly_pos = 11
        elif monopoly_pos == 22:
            monopoly_pos = 28

    if chance_pos == 9:
        monopoly_pos -= 3

    chance_pos = (chance_pos + 1) % 16

    return monopoly_pos, chance_pos


def com_chest(cc_pos, monopoly_pos):
    if cc_pos == 0:
        monopoly_pos = 0

    elif cc_pos == 1:
        monopoly_pos = 10

    cc_pos = (cc_pos + 1) % 16

    return monopoly_pos, cc_pos


landings = dict()  # Number of times landing on each space
for i in range(40):
    landings[i] = 0

monopoly_pos = 0
chance_pos = 0
cc_pos = 0

num_sides = 4
num_rolls = 1000000

for i in range(num_rolls):
    monopoly_pos = (monopoly_pos + roll_dice(num_sides) + roll_dice(num_sides)) % 40

    if monopoly_pos in {7, 22, 36}:
        monopoly_pos, chance_pos = chance(chance_pos, monopoly_pos)

    if monopoly_pos in {2, 17, 33}:
        monopoly_pos, cc_pos = com_chest(cc_pos, monopoly_pos)

    if monopoly_pos == 30:
        monopoly_pos = 10

    landings[monopoly_pos] += 1

sorted_pos = sorted(landings.items(), key=lambda x: x[1])[::-1]
print("Modal string: {}".format(''.join([str(x[0]) for x in sorted_pos[:3]])))
