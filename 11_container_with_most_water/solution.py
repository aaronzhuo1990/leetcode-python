"""
Problem:
    Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

Example:
    Input: [1, 2, 7, 6, 8]
    Output: 14

Solution:
    Two pointers, one points the head while another one points to the tail. Move two pointers and find the max area

"""


class Solution(object):
    def get_max_area(self, height):
        """
        :param height: list[int]
        :return: int
        """
        n = len(height)
        i = 0
        j = n -1
        max_area = 0
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            print i, j, max_area
        return max_area


solution = Solution()
a = [1, 2, 7, 6, 8]
print solution.get_max_area(a)