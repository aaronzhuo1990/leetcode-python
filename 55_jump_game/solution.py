"""
Problem:
    Given an array of non-negative integers, you are initially positioned at the first index of the array.
    Each element in the array represents your maximum jump length at that position.
    Determine if you are able to reach the last index.

Example 1:
    Input: [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
    Input: [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum
    jump length is 0, which makes it impossible to reach the last index.

Solution:
    Just record the maximum remaining steps when moving forward. When maximum = 0, it means it won't be able to
    reach the last element
"""


class Solution(object):
    def jump_game(self, nums):
        """
        :param nums: list[int]
        :return: bool, detect whether can reach the last element in the list
        """
        n = len(nums)
        if n == 1:
            return True

        remain = 0
        for i in range(1, n):
            remain = max(remain, nums[i-1]) - 1 # Calculate the maximum steps when moving forward
            if remain < 0:
                return False

        return True


s = Solution()
print s.jump_game([2,3,1,1,4])
print s.jump_game([3,2,1,0,4])

