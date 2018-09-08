def F(tot_len, block_size):
    sols = 0  # all blank solution

    if block_size > tot_len:
        return sols

    if known[tot_len] != -1:
        return known[tot_len]

    for s in range(tot_len - block_size + 1):
        sols += 1
        sols += F(tot_len - s - block_size, block_size)

    known[tot_len] = sols
    return sols

known = [-1] * 51
tot = 0
for i in range(2,5):
    tot += F(50, i)
    known = [-1] * 51

print(tot)