"""
Problem:
    Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
    a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
    The solution set must not contain duplicate quadruplets.

Example:

    Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

    A solution set is:
    [
        [-1,  0, 0, 1],
        [-2, -1, 1, 2],
        [-2,  0, 0, 2]
    ]

Solution:
    1. Sort the list
    2. Use four pointers to loop through the list, it is safe to skip the element which has the same value with next
    element.
"""


class solution(object):
    def get_four_sums(self, nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        result = []
        n = len(nums)
        nums.sort()
        for first in range(n-3):
            # Skip the same value to save some time
            if first > 0 and nums[first] == nums[first -1]:
                continue

            for second in range(first+1, n-2):
                third = second + 1
                last = n - 1
                while third < last:
                    tmp = nums[first] + nums[second] + nums[third] + nums[last]
                    if tmp == target:
                        result.append([nums[first], nums[second], nums[third], nums[last]])
                        third += 1
                        last -= 1
                        while third < last and nums[third] == nums[third-1]:
                            third += 1
                        while third < last and nums[last] == nums[last+1]:
                            last -= 1
                    elif tmp < target:
                        third += 1
                    else:
                        last -= 1
        return result


nums = [1, 0, -1, 0, -2, 2]
s = solution()
print s.get_four_sums(nums, 0)