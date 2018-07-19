"""
Problem:
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
    Note: Do not modify the linked list.

Follow up:
    Can you solve it without using extra space?

Solution:
    Two pointers: fast and slow
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.ne = None


class Solution(object):
    def detect_cycle(self, linked_list):

        if linked_list is None or linked_list.ne is None:
            return None

        slow = fast = linked_list
        while fast is not None and fast.ne is not None:
            slow = slow.ne
            fast = fast.ne.ne
            if fast == slow:
                return slow

        return None


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.ne = n2
n2.ne = n3
n3.ne = n4
n4.ne = n1
s = Solution()
node = s.detect_cycle(n1)
if node is None:
    print "no cycle"
else:
    print "has cycle"
