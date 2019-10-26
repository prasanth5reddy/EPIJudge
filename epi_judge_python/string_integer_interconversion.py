from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x):
    # TODO - you fill in here.
    sign = ''
    if x < 0:
        sign, x = '-', -x
    ans = []
    if x == 0:
        ans.append('0')
    while x > 0:
        ans.append(chr(ord('0') + x % 10))
        x //= 10

    return sign + ''.join(reversed(ans))


def string_to_int(s):
    # TODO - you fill in here.
    ans, sign = 0, 1
    if s[0] == '-':
        sign = -1
    else:
        ans = ord(s[0]) - 48
    for d in s[1:]:
        ans = ans * 10 + ord(d) - 48
    return sign * ans


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
