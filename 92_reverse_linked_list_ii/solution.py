"""
Problem:
    Reverse a linked list from position m to n. Do it in one-pass.

    Note: 1 <= m <= n <= length of list.

Example:
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL

Solution:
    Use an array as a stack to record (n-m+1) / 2 of elements which need to change values
"""


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.ne = None


class Solution(object):
    def revert(self, head, m, n):
        tmp = []
        change = (n-m+1) / 2
        mid = (n-m)/2 + m

        cursor = head
        index = 1
        while cursor is not None:
            if m <= index <= mid:
                if len(tmp) < change:
                    tmp.append(cursor)
            elif index > mid:
                if len(tmp) > 0:
                    pre = tmp.pop()
                    tmp_val = pre.val
                    pre.val = cursor.val
                    cursor.val = tmp_val
                else:
                    break

            cursor = cursor.ne
            index += 1

        return head


def print_list(head):
    cursor = head
    while cursor is not None:
        print cursor.val
        cursor = cursor.ne


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
li = s.revert(n1, 2, 4)
print_list(li)

