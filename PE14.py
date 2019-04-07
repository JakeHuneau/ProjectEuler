"""
Longest collatz sequence of starting number under 1 million.

n -> n/2 (even n)
n -> 3n + 1 (odd n)

:thoughts:
Just cache the length of a sequence in a dict so not to repeat stuff
"""
from util.algorithms import next_collatz


def pe14():
    collatz_len = dict()  # {num: length of sequence}
    for i in range(1, 1_000_000):
        curr = i
        count = 0
        while curr != 1:
            if curr in collatz_len:
                count += collatz_len[curr]
                break
            curr = next_collatz(curr)
            count += 1
        collatz_len[i] = count
    print(max(collatz_len, key=lambda key: collatz_len[key]))


if __name__ == '__main__':
    pe14()
