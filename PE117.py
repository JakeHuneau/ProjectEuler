def F(tot_len, min_block, max_block):
    sols = 1  # all blank solution

    if min_block > tot_len:
        return sols

    if known[tot_len] != -1:
        return known[tot_len]

    for b in range(min_block, max_block + 1):
        for s in range(tot_len - b + 1):
            sols += F(tot_len - s - b, min_block, max_block)

    known[tot_len] = sols
    return sols


known = [-1] * 51
print(F(50, 2, 4))