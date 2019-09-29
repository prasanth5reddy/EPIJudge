from test_framework import generic_test


def multiply(x, y):
    # TODO - you fill in here.
    # adding two numbers without arithmetic
    def add(a, b):
        while b:
            c = a & b
            a, b = a ^ b, c << 1
        return a

    # # adding two numbers without arithmetic - recursion
    # def add(a, b):
    #     if b:
    #         return add(a ^ b, (a & b) << 1)
    #     return a

    ans = 0
    while x:
        if x & 1:
            ans = add(ans, y)
        x = x >> 1
        y = y << 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
