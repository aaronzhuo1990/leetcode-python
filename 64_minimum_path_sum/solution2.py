

class Solution(object):
    def get_min_path_sum(self, grid):
        """
        :param grid: int[m][n]
        :return: int: minimum path sum
        """
        m = len(grid)
        n = len(grid[0])
        t = [[-1 for i in range(n)] for j in range(m)]
        return self.min_path_sum_aux(grid, m - 1, n - 1, t)

    def min_path_sum_aux(self, grid, x, y, t):
        if x == 0 and y == 0:
            return grid[x][y]
        elif t[x][y] != -1:
            return t[x][y]
        elif x == 0 and y > 0:
            t[x][y] = grid[x][y] + self.min_path_sum_aux(grid, x, y - 1, t)
            return t[x][y]
        elif x > 0 and y == 0:
            t[x][y] = grid[x][y] + self.min_path_sum_aux(grid, x - 1, y, t)
            return t[x][y]
        else:
            a = self.min_path_sum_aux(grid, x - 1, y, t)
            b = self.min_path_sum_aux(grid, x, y - 1, t)
            t[x][y] = grid[x][y] + min(a, b)
            return t[x][y]


s = Solution()
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1], [4, 2, 1]]
print (s.get_min_path_sum(grid))