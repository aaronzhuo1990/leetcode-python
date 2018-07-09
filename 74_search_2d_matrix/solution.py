"""
Problem:
    https://leetcode.com/problems/search-a-2d-matrix/description/

Solution:
    Binary search in 2D matrix
"""


class Solution(object):
    def search(self, matrix, target):
        """
        :param matrix: int[m][n]
        :param target: int
        :return: bool: indicate whether target is found in the matrix
        """

        m = len(matrix)
        n = len(matrix[0])

        col_start = 0
        col_end = m-1
        while col_start <= col_end:
            row = col_start + (col_end - col_start) / 2

            if matrix[row][0] <= target <= matrix[row][n-1]:
                left = 0
                right = n - 1

                while left <= right:
                    mid = left + (right - left) / 2
                    if matrix[row][mid] == target:
                        return True
                    elif target < matrix[row][mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False

            elif target < matrix[row][0]:
                col_end = row - 1
            else:
                col_start = row + 1

        return False


s = Solution()
mx = [[1, 3, 5, 6, 9], [11, 15, 17, 18, 19], [21, 23, 25, 27, 33]]

print s.search(mx, 1)
print s.search(mx, 11)
print s.search(mx, 21)
print s.search(mx, 26)
print s.search(mx, 33)






