from test_framework import generic_test


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_balanced_binary_tree(tree):
    # compute if tree is balanced and its height at the same time
    # Time complexity : O(n) where n is number of nodes
    # Space complexity : O(h) where h is the height of the tree
    def is_balanced(node):
        if not node:
            return [True, -1]
        is_balanced_left, height_left = is_balanced(node.left)
        is_balanced_right, height_right = is_balanced(node.right)
        if not is_balanced_left or not is_balanced_right or abs(height_left - height_right) > 1:
            return [False, 0]
        return [True, max(height_left, height_right) + 1]

    return is_balanced(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
