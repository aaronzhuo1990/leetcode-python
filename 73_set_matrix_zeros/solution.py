"""
Problem:
    https://leetcode.com/problems/set-matrix-zeroes/description/

Solution:
    Record the position of elements which values are zero and then fill zero for corresponding row and column
"""


class Solution(object):
    def set_matrix_zeros(self, matrix):
        """
        :param matrix: int[m][n]
        :return: modified matrix
        """
        m = len(matrix)  # row number
        n = len(matrix[0])  # column number
        pos = []  # keep the element which value is zero

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    pos.append((row, col))

        for t in pos:
            row, col = t

            # fill zero for the row
            for i in range(col):
                matrix[row][i] = 0
            for j in range(col+1, n):
                matrix[row][j] = 0

            # fill zero for the col
            for k in range(row):
                matrix[k][col] = 0
            for l in range(row+1, m):
                matrix[l][col] = 0

        return matrix


s = Solution()
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print s.set_matrix_zeros(matrix)