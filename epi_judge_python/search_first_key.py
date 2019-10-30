from test_framework import generic_test


def search_first_of_k(A, k):
    # Time complexity : O(log n)
    # space complexity : O(1)
    i, j = 0, len(A) - 1
    ans = -1
    while i <= j:
        m = i + (j - i) // 2
        if A[m] < k:
            i = m + 1
        elif A[m] == k:
            ans = m
            j = m - 1
        else:
            j = m - 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
