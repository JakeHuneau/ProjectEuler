from random import randint


def peter_total():
    tot = 0
    for i in range(9):
        tot += randint(1, 4)
    return tot


def colin_total():
    tot = 0
    for i in range(6):
        tot += randint(1, 6)
    return tot


tot = 0
games = 1000000
for i in range(games):
    if peter_total() > colin_total():
        tot += 1


print(tot / games)