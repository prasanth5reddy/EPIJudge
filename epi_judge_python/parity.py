from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.

    # O(n)
    # c = 0
    # while x:
    #     c ^= x & 1
    #     x >>= 1
    # return c

    # O(log n)
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
