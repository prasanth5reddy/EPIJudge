from test_framework import generic_test


def fibonacci(n):
    # TODO - you fill in here.
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("fibonacci.py", 'fibonacci.tsv',
                                       fibonacci))
