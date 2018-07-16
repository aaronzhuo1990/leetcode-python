"""
Problem:
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

    You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true

Example 2:
    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

Answer:
    It doesn't affect run time complexity as it only needs an extra branch to delete unnecessary element if found
"""


class Solution(object):
    def search(self, array, target):
        left = 0
        right = len(array) -1

        while left <= right:
            mid = (right - left) / 2 + left
            if array[mid] == target:
                return True
            elif array[mid] > array[right]:
                if array[left] <= target < array[mid]:
                    right = mid - 1  # now the whole left part is sorted
                else:
                    left = mid + 1
            elif array[mid] < array[right]:
                if array[mid] < target <= array[right]:
                    left = mid + 1  # now the whole right part is sorted
                else:
                    right = mid - 1
            else:
                right -= 1 # array[mid] != taget && array[mid] = array[mid], so delete array[right]

        return False


s = Solution()
print s.search([2,5,6,0,0,1,2], 0)
print s.search([2,5,6,0,0,1,2], 3)