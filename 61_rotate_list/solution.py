"""
Problem:
    Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
    Input: 0->1->2->NULL, k = 4
    Output: 2->0->1->NULL
    Explanation:
    rotate 1 steps to the right: 2->0->1->NULL
    rotate 2 steps to the right: 1->2->0->NULL
    rotate 3 steps to the right: 0->1->2->NULL
    rotate 4 steps to the right: 2->0->1->NULL

Solution:
    Record position of old head, old tail, find the new head and new tail, and then rotate the list
"""

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.ne = None


class Solution(object):
    def rotate_list(self, li, k):
        """
        :param li: linked list with integer
        :param k: int
        :return: rotated list
        """
        # Calculate length of linked list
        n = 0
        head = li
        tail = None
        while head is not None:
            n += 1
            tail = head
            head = head.ne

        next_head_index = n - (k%n)

        if next_head_index != n:
            p = 0
            head = li
            while head is not None:
                if p != next_head_index-1:
                    p += 1
                    head = head.ne
                    continue
                else:
                    new_tail = head
                    new_head = head.ne

                    new_tail.ne = None
                    tail.ne = li
                    return new_head
        else:
            return li

    def print_list(self, li):
        head = li
        while head is not None:
            print head.val
            head = head.ne


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.ne = n2
n2.ne = n3
n3.ne = n4
n4.ne = n5

s = Solution()
s.print_list(s.rotate_list(n1, 0))
