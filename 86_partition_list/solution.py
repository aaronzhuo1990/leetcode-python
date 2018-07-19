"""
Problem:
    Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
    You should preserve the original relative order of the nodes in each of the two partitions.

Example:
    Input: head = 1->4->3->2->5->2, x = 3
    Output: 1->2->2->4->3->5

Solution:
    Divide the list into two parts (one for < x and another one for >= x) and merge them
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.ne = None


class Solution(object):
    def partition_list(self, linked_list, x):
        """
        :param linked_list: linked list
        :param x: threshold
        :return:
        """

        i = linked_list
        new, new_head, old, old_head = None, None, None, None
        while i is not None:
            if i.val < x:
                if new is None:
                    new_head = new = i
                else:
                    new.ne= i
                    new = i
            else:
                if old is None:
                    old_head = old = i
                else:
                    old.ne = i
                    old = i
            i = i.ne

        new.ne = old_head
        old.ne = None
        return new_head

    def print_list(self, li):
        head = li
        while head is not None:
            print head.val
            head = head.ne


n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(5)
n6 = ListNode(2)
n1.ne = n2
n2.ne = n3
n3.ne = n4
n4.ne = n5
n5.ne = n6

s = Solution()
li = s.partition_list(n1, 3)
s.print_list(li)
