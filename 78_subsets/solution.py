"""
Problem:
    https://leetcode.com/problems/subsets/description/

Example:
    Input: nums = [1,2,3]
    Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

Solution:
    subset([3]) == [[], [3]]
    subset([2, 3]) == [[], [2], [2, 3], [3]]
    subset([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    So we have to calculate subset recursively
"""


class Solution(object):
    def subsets(self, nums):
        nums.sort()
        return self._subsets(nums, len(nums))

    def _subsets(self, ss, n):
        if n == 0:
            return [[]]
        else:
            res = [[]]
            for i in range(len(ss)):
                rest_subsets = self._subsets(ss[i + 1:], n - 1)
                for subset in rest_subsets:
                    subset.insert(0, ss[i])
                res += rest_subsets
            return res


s = Solution()
print s.subsets([1, 2, 3])

