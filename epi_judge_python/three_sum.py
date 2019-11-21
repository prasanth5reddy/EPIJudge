from test_framework import generic_test


def has_three_sum(A, t):
    # Time complexity = O(n^2)
    # Space complexity = O(1)
    A.sort()
    for i in range(len(A)):
        j, k = i, len(A) - 1
        while j <= k:
            s = A[i] + A[j] + A[k]
            if s == t:
                return True
            elif s < t:
                j += 1
            else:
                k -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
