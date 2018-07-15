"""
Problem:
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Solution:
    I don't know how to describe it, see the code
"""


class Solution(object):
    def search(self, array, target):
        left = 0
        right = len(array) -1

        while left <= right:
            mid = (right - left) / 2 + left
            if array[mid] == target:
                return mid
            elif array[mid] > array[right]:
                if array[left] <= target < array[mid]:
                    right = mid - 1  # now the whole left part is sorted
                else:
                    left = mid + 1
            else:
                if array[mid] < target <= array[right]:
                    left = mid + 1  # now the whole right part is sorted
                else:
                    right = mid - 1

        return -1


s = Solution()
a = [4,5,6,7,0,1,2]
print s.search(a, 6)
print s.search(a, 3)