from test_framework import generic_test

lookup_table = []
for i in range(2 ** 16):
    p = 0
    while i:
        p ^= 1
        # this will erase the lowest set bit
        i &= i - 1
    lookup_table.append(p)


def parity(x):
    # TODO - you fill in here.

    # # O(n)
    # c = 0
    # while x:
    #     c ^= x & 1
    #     x >>= 1
    # return c

    # O(n/L) using look up table
    # mask_size = 16
    # bit_mask = 0xFFFF
    # return lookup_table[x >> (3 * mask_size)] ^ lookup_table[(x >> (2 * mask_size)) & bit_mask] ^ lookup_table[
    #     (x >> mask_size) & bit_mask] ^ lookup_table[x & bit_mask]

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
