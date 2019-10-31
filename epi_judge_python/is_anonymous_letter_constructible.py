from test_framework import generic_test
import collections


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # Time complexity : O(m + n) where m and n are number of characters in letter and magazine respectively
    # Space complexity : O(L) where L is number of distinct characters in letter_text

    # using dict
    letter_counts = {}
    for letter in letter_text:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    for c in magazine_text:
        if not letter_counts:
            return True
        if c in letter_counts:
            letter_counts[c] -= 1
            if letter_counts[c] == 0:
                del letter_counts[c]

    return not letter_counts

    # # using collections.Counter
    # return not (collections.Counter(letter_text) - collections.Counter(magazine_text))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
