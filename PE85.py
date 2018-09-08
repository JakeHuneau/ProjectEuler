nearest_area = 1
nearest_num = 2e6
for i in range(1, 100):
    for j in range(1, 100):
        num = (i ** 2 + i) * (j ** 2 + j) / 4
        if abs(2e6 - num) < nearest_num:
            nearest_area = i * j
            nearest_num = abs(2e6 - num)
print(nearest_area, nearest_num)
