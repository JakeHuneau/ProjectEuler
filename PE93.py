from operator import add, sub, mul, truediv
from itertools import combinations, permutations, product


def seq_len(seq, curr=1):
    while curr in seq:
        curr += 1
    return curr


possible = combinations(range(1, 10), 4)
longest_seq = 0
longest_set = ''
for p in possible:
    arrangements = permutations(p)
    seqs = set()
    for a in arrangements:
        ops = product([add, sub, mul, truediv], repeat=3)
        for op in ops:
            seqs.add(op[0](op[1](a[0], a[1]), op[2](a[2], a[3])))  # (a.b).(c.d)
            seqs.add(op[0](op[1](op[2](a[0], a[1]), a[2]), a[3]))  # ((a.b).c).d
    if seq_len(seqs) > longest_seq:
        longest_seq = seq_len(seqs)
        longest_set = ''.join(str(i) for i in p)

print(longest_set, longest_seq)