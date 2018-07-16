"""
Problem:
    Given inorder and postorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.

    For example, given

    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    Return the following binary tree:

        3
       / \
      9  20
        /  \
       15   7

Solution:
    construct tree's left tree and right tree recursively
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def construct(self, in_order, post_order):
        """
        :param in_order: list[int]: tree in order
        :param post_order: list[int]: tree in post order
        :return: a tree
        """

        if not in_order or not post_order:
            return None
        root_val = post_order[-1]
        root_index = in_order.index(root_val)
        root = TreeNode(x=root_val)
        root.left = self.construct(in_order[:root_index], post_order[:root_index])
        root.right = self.construct(in_order[root_index+1:], post_order[root_index: -1])

        return root

    def print_tree(self, tree):
        if tree is None:
            return
        print(tree.val)
        if tree.left:
            self.print_tree(tree.left)
        if tree.right:
            self.print_tree(tree.right)


in_o = [9,3,15,20,7]
post_o = [9,15,7,20,3]
s = Solution()
tree = s.construct(in_order=in_o, post_order=post_o)
s.print_tree(tree)
