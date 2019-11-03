from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    # # Time complexity = O(n m)
    # # Space complexity = O(k) where k is the number of common elements
    # ans = []
    # for i in A:
    #     for j in B:
    #         if i == j and i not in ans:
    #             ans.append(i)
    # return ans

    # # Time complexity = O(n log m)
    # # Space complexity = O(k)
    # ans = []
    # for i in range(len(A)):
    #     if i == 0 or A[i] != A[i - 1]:
    #         l, r = 0, len(B) - 1
    #         while l <= r:
    #             m = l + (r - l) // 2
    #             if A[i] == B[m]:
    #                 ans.append(A[i])
    #                 break
    #             elif A[i] < B[m]:
    #                 r = m - 1
    #             else:
    #                 l = m + 1
    # return ans

    # Time complexity = O(n + m)
    # Space complexity = O(k)
    # Two pointer approach
    ans = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if (i == 0 or A[i] != A[i - 1]) and A[i] == B[j]:
            ans.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return ans

    # # using sets
    # return sorted(set(A).intersection(B))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
