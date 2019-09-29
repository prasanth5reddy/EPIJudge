from test_framework import generic_test


def divide(x, y):
    # TODO - you fill in here.
    ans, k = 0, 32
    y_p = y << k
    while x >= y:
        while y_p > x:
            y_p >>= 1
            k -= 1
        ans += 1 << k
        x -= y_p
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_divide.py",
                                       "primitive_divide.tsv", divide))
