"""
Problem:
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum
    of all numbers along its path.
    Note: You can only move either down or right at any point in time.

Example:
    Input:
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1->3->1->1->1 minimizes the sum.

Solution:
    Calculate the minimum path sum for grid[m][n] by: grid[m][n = grid[m][n + min(grid[m][n-1], grid[m-1][n])
"""


class Solution(object):
    def get_min_path_sum(self, grid):
        """
        :param grid: int[m][n]
        :return: int: minimum path sum
        """
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    grid[row][col] = grid[row][col] + grid[row][col-1]
                elif col == 0:
                    grid[row][col] = grid[row][col] + grid[row-1][col]
                else:
                    grid[row][col] = grid[row][col] + min(grid[row][col-1], grid[row-1][col])

        return grid[m-1][n-1]


s = Solution()
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print (s.get_min_path_sum(grid))
