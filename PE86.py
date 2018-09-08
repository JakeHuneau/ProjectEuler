import numpy as np
from Project_Euler import memoize


@memoize
def is_square(x):
    return np.sqrt(x).is_integer()


l = 2  # length
count = 0
target = 1_000_000
while count < target:
    l += 1
    for i in range(3, 2*l):
        if is_square(i * i + l * l):
            count += min(i, l+1) - (i+1)//2

print(l)

#Use A143714