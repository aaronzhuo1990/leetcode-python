"""
Problem:
    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

Example:
    Given nums = [1,1,1,2,2,3],
    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
    It doesn't matter what you leave beyond the returned length.
"""


class Solution(object):
    def remove_duplicates(self, array):
        """
        :param array: list[int]: sorted array with duplicates
        :return: list[int]: the array without duplicates, int: length of the array
        """
        n = len(array)

        if n == 0:
            return [], 0

        cursor = 0
        duplicated = False

        for i in range(1, n):
            if array[cursor] == array[i] and not duplicated:
                cursor += 1
                array[cursor] = array[i]
                duplicated = True
            elif array[cursor] != array[i]:
                cursor += 1
                array[cursor] = array[i]
                if duplicated:
                    duplicated = False

        return array[:cursor+1], cursor+1


s = Solution()
print s.remove_duplicates([0, 1, 1, 2, 2, 2, 3])
