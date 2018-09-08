"""
Other tools
"""

def factors(n: int) -> set:
    """
    Calculates all the factors of n

    Args:
        n (int)

    Returns:
        (set) of factors
    """
    facts = set()
    for i in range(1, int(n ** 0.5) + 1):
        if not n % i:
            facts.update({i, n//i})
    return facts


def palindromes_under(n: int) -> list:
    """
    Finds all the palindromic numbers under n

    Args:
        n (int): ceiling to palindromes

    Returns:
        (set) of palindromic numbers
    """
    max_length = len(str(n))
    all_palis = []
    for i in range(1, max_length):
        for p in palindromes_of_length(i):
            if p[0] != '0':
                all_palis.append(int(p))
    for p in palindromes_of_length(max_length):
        if int(p) < n and p[0] != '0':
            all_palis.append(int(p))
    return sorted(list(set(all_palis)))


def palindromes_of_length(n: int) -> list:
    """
    Calculates all the palindromes of length n.
    This means the number will have n numbers in it.
    For example, 313 is length 3.

    Args:
        n (int): length of palindromic numbers

    Returns:
        (set) of palindromic numbers
    """
    if n == 1:
        return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if n == 2:
        return ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']

    palis = []
    for p in palindromes_of_length(n - 2):
        palis += [f'{i}{p}{i}' for i in palindromes_of_length(1)]

    return palis
