"""
Given a non-negative index k where k <= 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

Follow up:
    Could you optimize your algorithm to use only O(k) extra space?

Example:
    Input: 3
    Output: [1,3,3,1]

Solution:
    Time complex is not what we care in this problem. Instead, we want to use as less space as possible
    0: 1
    1: 1 1
    2: 1 2 1
    3: 1 3 3 1
    4: 1 4 6 4 1

    From the matrix above, you can see that for row = n, it needs a list which length is n+1
    Besides, we have calculate each row's result based on the last row. For example,
    when looping through row, we can calculate triangle[1] based on row 1 by: triangle[1] = triangle[1] + triangle[1-1],
    which is 2. When looping through row 3, we can calculate triangle[2] based on row 2 by:
    triangle[2] = triangle[2] + triangle[2-1] (which is 3) and triangle[1] by:
    triangle[1] = triangle[1] + triangle[1-1] (which is also 3)
"""


class Solution(object):
    def pascals_triangle_ii(self, rowIndex):
        """
        :param rowIndex: int
        :return: list[int]
        """
        triangle = [1] * (rowIndex + 1)
        for row in range(rowIndex+1):
            for col in reversed(range(1, row)):
                triangle[col] = triangle[col] + triangle[col-1]

        return triangle


s = Solution()
print s.pascals_triangle_ii(6)

