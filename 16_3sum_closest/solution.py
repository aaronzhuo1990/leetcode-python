"""
Problem:
    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
    target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

    Given array nums = [-1, 2, 1, -4], and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Solution:
    1. Sort the list
    2. Do the sum of three integers for all the integers in the list and find the closet one
"""


class Solution(object):
    def get_cloest(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: int: The sum of three integers that is closest to the target
        """
        nums.sort()
        total = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for first in range(n-2):
            second = first + 1
            last = n - 1
            while second < last:
                tmp = nums[first] + nums[second] + nums[last]
                if abs(tmp - target) < abs(total - target):
                    total = tmp

                if tmp == target:
                    return tmp
                elif tmp < target:
                    second += 1
                else:
                    last -= 1
            return total


solution = Solution()
a = [1, -13, 5, 27, 20]
print solution.get_cloest(a, 15)
