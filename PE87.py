from Project_Euler import sieve_of_eratosthenes
from itertools import product
from time import time

t1 = time()
limit = 50_000_000
square_primes = sieve_of_eratosthenes(int(limit ** (1/2)))
cube_primes = sieve_of_eratosthenes(int(limit ** (1/3)))
fourth_primes = sieve_of_eratosthenes(int(limit ** (1/4)))

good_prod = set()

for s, c, f in product(square_primes, cube_primes, fourth_primes):
    prod = s**2 + c**3 + f**4
    if prod < limit:
        good_prod.add(prod)

print(len(good_prod))
print(time()-t1)