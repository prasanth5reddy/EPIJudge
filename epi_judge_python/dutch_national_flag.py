import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index, A):
    # TODO - you fill in here.
    # # Time complexity : O(n)
    # # Space complexity : O(n)
    # lt, eq, gt = [], [], []
    # for i in A:
    #     if i < A[pivot_index]:
    #         lt.append(i)
    #     elif i == A[pivot_index]:
    #         eq.append(i)
    #     else:
    #         gt.append(i)
    # return lt + eq + gt

    # # Time complexity : O(n^2)
    # # Space complexity : O(1)
    # for i in range(len(A)):
    #     for j in range(i + 1, len(A)):
    #         if A[j] < A[pivot_index]:
    #             A[i], A[j] = A[j], A[i]
    #             break
    #
    # for i in range(len(A) - 1, -1, -1):
    #     for j in range(i - 1, -1, -1):
    #         if A[j] > A[pivot_index]:
    #             A[i], A[j] = A[j], A[i]
    #             break
    # return A

    # # Time complexity : O(n)
    # # Space complexity : O(1)
    # # Two passes
    # small = 0
    # for i in range(1, len(A)):
    #     if A[i] < A[pivot_index]:
    #         A[i], A[small] = A[small], A[i]
    #         small += 1
    # big = len(A) - 1
    # for i in reversed(range(len(A))):
    #     if A[i] > A[pivot_index]:
    #         A[i], A[big] = A[big], A[i]
    #         big -= 1
    # return A

    # Time complexity : O(n)
    # Space complexity : O(1)
    # Single pass
    small, equal, greater = 0, 0, len(A) - 1
    while equal < greater:
        if A[equal] < A[pivot_index]:
            A[small], A[equal] = A[equal], A[small]
            small += 1
            equal += 1
        elif A[equal] == A[pivot_index]:
            equal += 1
        else:
            A[greater], A[equal] = A[equal], A[greater]
            greater -= 1
    return A


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
