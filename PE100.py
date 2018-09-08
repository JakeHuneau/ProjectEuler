# B^2 - B / N^2 - N = 1/2 -> 2B^2 -2B - (N^2 -N) = 0 -> B = (2 + sqrt(4 + 8(N^2 -N))) / 4
# Integer solutions to this are solutions of B where B is number of blue disks
# This didn't work, so just using solution to quadratic diophantine equation
# b(k+1) = 3b(k) + 2 n(k) -2
# n(k+1) = 4b(k) + 3n(k) - 3

def f(x):
    return (2 + (4 + 8 * (x**2 - x)) ** 0.5) / 4


b = 15
n = 21

while n < 1e12:
    b, n = 3 * b + 2 * n - 2, 4 * b + 3 * n - 3

print(n, f(n))
