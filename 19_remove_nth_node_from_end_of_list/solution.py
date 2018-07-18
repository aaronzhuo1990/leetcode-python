"""
Problem:
    Given a linked list, remove the n-th node from the end of list and return its head.

Example:
    Given linked list: 1->2->3->4->5, and n = 2.
    After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
    Given n will always be valid.

Follow up:
    Could you do this in one pass?

Solution:
    Well it will super easy if uses array to simulate linked list
"""


class Solution(object):
    def remove_node(self, linked_list, n):
        del linked_list[len(linked_list) - n]
        return linked_list


a = [1, 2, 3, 4, 5]
s = Solution()
print s.remove_node(a, 3)