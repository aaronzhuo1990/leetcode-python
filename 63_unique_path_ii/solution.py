"""
Problem:
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
    The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right
    corner of the grid (marked 'Finish' in the diagram below).
    Now consider if some obstacles are added to the grids. How many unique paths would there be?
    An obstacle and empty space is marked as 1 and 0 respectively in the grid.
    Note: m and n will be at most 100.

Example:
    Input:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    Output: 2
    Explanation:
    There is one obstacle in the middle of the 3x3 grid above.
    There are two ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Down -> Down -> Right -> Right

Solution:
    Calculate unique paths when reaching grid[m][n] by grid[m][n] = grid[m][n-1] + grid[m-1][n]
"""


class Solution(object):
    def get_unique_path_num(self, grid):
        """
        :param grid: int[m][n]
        :return: int: number of unique path to grid[m-1][n-1]
        """
        m = len(grid)
        n = len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                else:
                    if row == 0 and col == 0:
                        grid[row][col] = 1
                    elif row == 0:
                        grid[row][col] = grid[row][col-1]
                    elif col == 0:
                        grid[row][col] = grid[row-1][col]
                    else:
                        grid[row][col] = grid[row][col-1] + grid[row-1][col]

        return grid[m-1][n-1]


grid = [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
s = Solution()
# the contents of grid will be changed after executing the following method
print s.get_unique_path_num(grid)