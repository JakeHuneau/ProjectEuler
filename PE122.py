def sum_to_n(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail

def all_sums(n):
    for i in range(n//2, n+1):
        for j in sum_to_n(n, i):
            yield j

steps = dict()
steps[1] = 1
steps[2] = 1
steps[3] = 2
steps[4] = steps[2] + steps[2]
steps[5] = steps[4] + steps[1]
steps[6] = steps[3] + steps[3]
for i in range(7, 10):

print(steps)