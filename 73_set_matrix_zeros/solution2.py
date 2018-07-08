class Solution(object):
    def sex_matrix_zeros(self, matrix):
        """
        :param matrix: int[m][n]
        :return: modified matrix
        """
        m = len(matrix)
        n = len(matrix[0])
        column_zero = False
        row_zero = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    # Check whether the first row or first column contains zeroes before recording
                    if row_zero is not False and i == 0:
                        row_zero = True
                    if column_zero is not False and j == 0:
                        column_zero = True
                    # Record zeroes using the first row and column
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Fill zeroes except for the first row and column
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0

        # Fill zeros for the first row and column
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if column_zero:
            for i in range(m):
                matrix[i][0] = 0

        return matrix


s = Solution()
m = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print s.sex_matrix_zeros(m)