from itertools import combinations


def valid_combo(dice1, dice2):  # Checks that the square can be made
    return all(dig1 in dice1 and dig2 in dice2 or dig2 in dice1 and dig1 in dice2 for dig1, dig2 in squares)


squares = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (3, 6), (4, 6), (6, 4), (8, 1)]
dice = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 6], 6))  # List of all dice combos


count = 0

for i, d1 in enumerate(dice):
    for d2 in dice[:i]:  # all dice before d1 in the list
        if valid_combo(d1, d2):
            count += 1

print(count)
