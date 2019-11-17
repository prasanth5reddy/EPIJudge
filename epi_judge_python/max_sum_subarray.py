from test_framework import generic_test


def find_maximum_subarray(A):
    if len(A) == 0:
        return 0
    max_cur, max_so_far = 0, 0
    for i in range(len(A)):
        max_cur = max(A[i], A[i] + max_cur)
        max_so_far = max(max_so_far, max_cur)
    return max_so_far


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
