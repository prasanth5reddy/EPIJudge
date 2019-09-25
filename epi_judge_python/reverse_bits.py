from test_framework import generic_test

mask_size = 16
lookup_reverse = []
for b in range(2 ** mask_size):
    lt, rt = 0, mask_size - 1
    while lt < rt:
        if (b >> lt) & 1 != (b >> rt) & 1:
            b ^= (1 << lt) | (1 << rt)
        lt += 1
        rt -= 1
    lookup_reverse.append(b)


def reverse_bits(x):
    # TODO - you fill in here.

    # # O(n)
    # ans, c = 0, 0
    # while x:
    #     ans <<= 1
    #     ans |= x & 1
    #     x = x >> 1
    #     c += 1
    # while c < 64:
    #     ans <<= 1
    #     c += 1
    # return ans

    # # O(n) using swap_bits.py
    # i, j = 0, 63
    # while i < j:
    #     if (x >> i) & 1 != (x >> j) & 1:
    #         bit_mask = (1 << i) | (1 << j)
    #         x ^= bit_mask
    #     i += 1
    #     j -= 1
    # return x

    # # O(n/L) using lookup table
    bit_mask = 0xFFFF
    return lookup_reverse[x & bit_mask] << (3 * mask_size) | lookup_reverse[(x >> mask_size) & bit_mask] << (
            2 * mask_size) | lookup_reverse[(x >> (2 * mask_size)) & bit_mask] << mask_size | lookup_reverse[
               (x >> (3 * mask_size)) & bit_mask]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
