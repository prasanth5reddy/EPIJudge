from test_framework import generic_test


def power(x, y):
    # TODO - you fill in here.
    # ans = 1.0
    # if y < 0:
    #     y, x = -y, 1.0 / x
    # while y:
    #     if y & 1:
    #         ans *= x
    #     x, y = x * x, y >> 1
    # return ans

    # recursion
    if y == 0:
        return 1.0
    if y == 1:
        return x
    if y < 0:
        return pow(1.0 / x, -y)
    else:
        next_pow = pow(x * x, y >> 1)
        return x * next_pow if y & 1 else next_pow


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
