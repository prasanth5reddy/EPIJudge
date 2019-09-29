from test_framework import generic_test


def reverse(x):
    # TODO - you fill in here.
    ans, t = 0, abs(x)
    while t:
        ans = ans * 10 + t % 10
        t //= 10
    return -ans if x < 0 else ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
