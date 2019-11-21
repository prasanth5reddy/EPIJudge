from test_framework import generic_test


def has_two_sum(A, t):
    # Time complexity = O(n)
    # Space complexity = O(1)
    i, j = 0, len(A) - 1
    while i <= j:
        s = A[i] + A[j]
        if s == t:
            return True
        elif s < t:
            i += 1
        else:
            j -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
