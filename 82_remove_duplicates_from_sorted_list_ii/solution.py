"""
Problem:
    Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
    Input: 1->2->3->3->4->4->5
    Output: 1->2->5

Example 2:
    Input: 1->1->1->2->3
    Output: 2->3

Solution:
    Filter out no duplicate elements with a map [key: ne.val, value: counts of ne.val]
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.ne = None


class Solution(object):
    def remove_duplicates(self, head):
        values = {}
        ne = head

        while ne is not None:
            if ne.val not in values:
                values[ne.val] = 1
            else:
                values[ne.val] += 1
            ne = ne.ne

        new_head = cursor = None
        ne = head

        while ne is not None:
            if values[ne.val] == 1:
                if new_head is None:
                    new_head = cursor = ne
                else:
                    cursor.ne = ne
                    cursor = ne
            ne = ne.ne

        return new_head

    def print_list(self, li):
        head = li
        while head is not None:
            print head.val
            head = head.ne


n1 = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(1)
n4 = ListNode(2)
n5 = ListNode(3)
n1.ne = n2
n2.ne = n3
n3.ne = n4
n4.ne = n5

s = Solution()
l = s.remove_duplicates(n1)
s.print_list(l)
