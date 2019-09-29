from test_framework import generic_test
import math
from reverse_digits import reverse


def is_palindrome_number(x):
    # TODO - you fill in here.
    # # using string manipulation
    # return str(x) == str(x)[::-1]

    # # using integer reverse
    # if x < 0:
    #     return False
    # return x == reverse(x)

    # checking lsd and msd
    if x <= 0:
        return x == 0
    n_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (n_digits - 1)
    for i in range(n_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
