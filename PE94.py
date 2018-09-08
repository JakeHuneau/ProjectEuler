def check_root(x):
    return (3 * x * x + 2 * x - 1) ** 0.5, (3 * x * x - 2 * x - 1) ** 0.5


total_p = 0
#for i in range(5, 333_333_335, 2):
#    x1, x2 = check_root(i)
#    if x1.is_integer():
#        total_p += 3 * i - 1
#    if x2.is_integer():
#        total_p += 3 * i + 1

side0, side, s, p, m = 1, 1, 0, 0, 1
limit = 10**9

while p <= limit: #Pells equation
    side0, side, m = side, 4 * side - side0 + 2 * m, -m
    s += p
    p = 3 * side - m

print(s)