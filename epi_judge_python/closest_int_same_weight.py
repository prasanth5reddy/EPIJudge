from test_framework import generic_test


def weight(x):
    c = 0
    while x:
        x &= x - 1
        c += 1
    return c


def closest_int_same_bit_count(x):
    # TODO - you fill in here.
    # # Brute force left and right until weight is matched
    # left, right = x - 1, x + 1
    # while weight(left) != weight(x) and weight(right) != weight(x):
    #     left -= 1
    #     right += 1
    # return left if weight(left) == weight(x) else right

    # Logic : Find rightmost two adjacent bits that are different and swap them

    # # O(n) solution where n is integer width
    # num_bits = 64
    # if x == 0 or x == (2 ** num_bits - 1):
    #     # if all are zeros or ones then there is no closest integer with same weight
    #     return
    # for i in range(num_bits - 1):
    #     if (x >> i) & 1 != (x >> (i + 1)) & 1:
    #         x ^= (1 << i) | (1 << (i + 1))
    #         return x

    # O(1) solution
    # t contains 1 if bit at that position is different to its left bit
    t = x ^ (x >> 1)
    # find rightmost 1 bit
    t = t & -t
    # then swap the above bit and its left bit in x
    return x ^ (t | t << 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
    # print(closest_int_same_bit_count(48))
