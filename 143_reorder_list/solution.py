"""
Problem:
    Given a singly linked list L: L0->L1->...->Ln-1->Ln,
    reorder it to: L0->Ln->L1->Ln-1->L2->Ln2->...

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
    Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:
    Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

Solution:
    Use an array to save correct order and reconnect each list node
"""

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.ne = None


class Solution(object):
    def reorder(self, head):

        # Calculate the length of list
        cursor = head
        length = 0
        while cursor is not None:
            length += 1
            cursor = cursor.ne

        array = [None] * length
        mid = (length-1) / 2
        cursor = head
        even = True if length % 2 == 0 else False

        # Put correct order into the array
        index = n = 0
        while cursor is not None:
            if n <= mid:
                array[index] = cursor
                if n != mid:
                    index += 2
            else:
                if even:
                    array[index+1] = cursor
                else:
                    array[index-1] = cursor

                index -= 2

            n += 1
            cursor = cursor.ne

        # Re-connect each list node
        for i in range(len(array)):
            if i < length-1:
                array[i].ne = array[i+1]
            else:
                array[i].ne = None

        return array[0]


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
li = s.reorder(n1)
print_list(li)

