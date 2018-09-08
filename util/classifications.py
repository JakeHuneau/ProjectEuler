"""
Functions that return bools and check if a number is something
"""

def is_palindrome(n: int) -> bool:
    """
    Checks if a number is palindromic. Meaning it is the same forwards as backwards

    Args:
        n (int): Number to check

    Returns:
        (bool) if n is palindromic
    """
    return str(n) == str(n)[::-1]
