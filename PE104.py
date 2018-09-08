from Project_Euler import is_pandigital

k = 2
f0 = 1
f1 = 1

while not is_pandigital(str(f1)[:9]) or not is_pandigital(str(f1)[-9:]):
    f1, f0 = f1 + f0, f1
    k += 1
    if k == 329468:
        print('too far')

print(k)