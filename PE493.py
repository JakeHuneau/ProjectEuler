# 70 colored balls, 10 of each color (c1, c2, c3, c4, c5, c6, c7)
# Expected number of distinct colors in 20 randomly picked balls
# Find probability of NOT choosing one color: (60 C 20) / (70 C 20)

from Project_Euler import choose

print(7 * (1 - choose(60, 20) / choose(70, 20)))
