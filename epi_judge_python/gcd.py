from test_framework import generic_test


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


if __name__ == '__main__':
    exit(generic_test.generic_test_main("gcd.py", 'gcd.tsv', gcd))
