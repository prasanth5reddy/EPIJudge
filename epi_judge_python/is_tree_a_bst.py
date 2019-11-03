from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    # # My solution (Recursion)
    # # Time complexity : O(n^2) in worst case
    # # Space complexity : O(1)
    # if not tree:
    #     return True
    # is_left = is_right = True
    # if tree.left:
    #     dummy = tree.left
    #     while dummy.right:
    #         dummy = dummy.right
    #     is_left = tree.left.data <= tree.data and dummy.data <= tree.data and is_binary_tree_bst(tree.left)
    # if tree.right:
    #     dummy = tree.right
    #     while dummy.left:
    #         dummy = dummy.left
    #     is_right = tree.data <= tree.right.data and tree.data <= dummy.data and is_binary_tree_bst(tree.right)
    # return is_left and is_right

    # # DFS approach
    # # Time complexity : O(n)
    # # Space complexity : O(h) where h is height of the tree
    # if not tree:
    #     return True
    # if not low_range <= tree.data <= high_range:
    #     return False
    # return is_binary_tree_bst(tree.left, low_range, tree.data) and \
    #        is_binary_tree_bst(tree.right, tree.data, high_range)

    # BFS approach
    # This approach is better when the tree is skewed. Performs early checks near to the root
    # Time complexity : O(n)
    # Space complexity : O(n)
    if not tree:
        return True
    queue = [[tree, (low_range, high_range)]]
    while queue:
        size = len(queue)
        for i in range(size):
            node, (l, h) = queue.pop(0)
            if not l <= node.data <= h:
                return False
            else:
                if node.left:
                    queue.append([node.left, (l, node.data)])
                if node.right:
                    queue.append([node.right, (node.data, h)])
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
