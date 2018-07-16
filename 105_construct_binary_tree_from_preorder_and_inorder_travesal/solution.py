"""
Problem:
    Given preorder and inorder traversal of a tree, construct the binary tree.

    Note:
    You may assume that duplicates do not exist in the tree.

For example, given

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
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
    def construct(self, pre_order, in_order):
        """
        :param pre_order: list[int]: tree in pre order
        :param in_order: list[int]: tree in order
        :return: a tree
        """
        if len(in_order) == 0:
            return None
        root_val = pre_order.pop(0)
        root_index = in_order.index(root_val)
        root = TreeNode(x=root_val)
        root.left = self.construct(pre_order, in_order[:root_index])
        root.right = self.construct(pre_order, in_order[root_index+1:])

        return root

    def print_tree(self, tree):
        if tree is None:
            return
        print(tree.val)
        if tree.left:
            self.print_tree(tree.left)
        if tree.right:
            self.print_tree(tree.right)


pre_order = [3,9,20,15,7]
in_order = [9,3,15,20,7]
s = Solution()
tree = s.construct(pre_order=pre_order, in_order=in_order)
s.print_tree(tree=tree)