"""
Problem:
    Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
    Input: 1->1->2
    Output: 1->2

Example 2:
    Input: 1->1->2->3->3
    Output: 1->2->3

Solution:
    Use cursor to remove duplicates
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.ne = None


class Solution(object):
    def remove_duplicates(self, li):
        head = li
        cursor = head.ne

        while cursor is not None:
            if head.val == cursor.val:
                cursor = cursor.ne
            else:
                head.ne = cursor
                head = cursor
                cursor = cursor.ne

        return li

    def print_list(self, li):
        head = li
        while head is not None:
            print head.val
            head = head.ne


n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(3)
n1.ne = n2
n2.ne = n3
n3.ne = n4

s = Solution()
li = s.remove_duplicates(n1)
s.print_list(li)