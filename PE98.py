"""
https://projecteuler.net/problem=98

:Thoughts:
1. Find all the anagram pairs.
"""
from collections import defaultdict

def is_anagram(word1: str, word2: str) -> bool:
    """Checks if two words are anagrams"""
    return sorted(word1) == sorted(word2)

def find_anagrams() -> dict:
    all_words = open('text_files/p098_words.txt').read().split(',')
    anagrams = defaultdict(list)
    for indx, word in enumerate(all_words):
        for indx2, word2 in enumerate(all_words[indx+1:]):
            if is_anagram(word, word2):
                anagrams[word].append(word2)


if __name__ == '__main__':
    print(find_anagrams())