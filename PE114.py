def F(tot_len, min_block):
    sols = 1  # all blank solution

    if min_block > tot_len:
        return sols

    if known[tot_len] != -1:
        return known[tot_len]

    for s in range(tot_len - min_block + 1):
        for b in range(min_block, tot_len - s + 1):
            sols += F(tot_len - s - b - 1, min_block)

    known[tot_len] = sols
    return sols


known = [-1] * 51
print(F(50, 3))
