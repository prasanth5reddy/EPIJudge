from test_framework import generic_test


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def merge_two_sorted_lists(L1, L2):
    # TODO - you fill in here.
    # Iterative
    # Time complexity : O(n + m)
    # Space complexity : O(1)
    ans = ListNode(-1)
    dummy = ans
    while L1 and L2:
        if L1.data < L2.data:
            dummy.next, L1 = L1, L1.next
        else:
            dummy.next, L2 = L2, L2.next
        dummy = dummy.next
    dummy.next = L1 or L2
    return ans.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
