"""
Problem:
    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

    For example, given the following triangle

    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

    Note:

    Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Solution:
    Calculate minimum
"""


class Solution(object):
    def path_sum(self, triangle):
        path = [triangle[0][0]]
        path_sum = triangle[0][0]

        i = 0
        for j in range(1, len(triangle)):
            if i == 0:
                num = min(triangle[j][:i+2])
            else:
                num = min(triangle[j][i-1:i+2])

            path.append(num)
            path_sum += num
            i = triangle[j].index(num)

        return path, path_sum


triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

s = Solution()
print s.path_sum(triangle)

