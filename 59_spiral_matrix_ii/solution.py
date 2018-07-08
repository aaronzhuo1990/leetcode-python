"""
Problem:
    Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
    Input: 3
    Output:
    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]

Solution:
    Take num = 4 as example, output is:
    [
        [1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]
    ]
    Filling sequence is:
    1, 4, 7, 10 | 2, 5, 8, 11 | 3, 6, 9, 12 | 13 | 14 | 15 | 16
"""


class Solution(object):
    def generate_matrix(self, num):
        """
        :param num: int
        :return: a mtrix
        """
        matrix = [[0 for i in range(num)] for j in range(num)]
        count = 1
        for i in range(num / 2):
            start = i  # start moves from left to right
            end = num - i - 1  # end moves from right to left
            width = end - start  # width is the gap between start and end
            for j in range(start, end):  # j is used to fill the element between start and end
                offset = j - start
                # Top
                matrix[start][j] = count + (0 * width) + offset
                # Right
                matrix[j][end] = count + 1 * width + offset
                # Bottom
                matrix[end][end - offset] = count + 2 * width + offset
                # Left
                # draw the matrix for num = 4, then you will understand what n * width means
                matrix[end - offset][start] = count + 3 * width + offset
            count += 4 * width
        if num % 2 == 1:
            mid = num / 2
            matrix[mid][mid] = count
        return matrix


s = Solution()
print s.generate_matrix(4)