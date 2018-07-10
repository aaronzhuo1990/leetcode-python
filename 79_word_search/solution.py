"""
Problem:
    https://leetcode.com/problems/word-search/description/

Example:
    board =
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    Given word = "ABCCED", return true.
    Given word = "SEE", return true.
    Given word = "ABCB", return false.

Solution: Use DFS to search all the possibilities

"""


class Solution(object):
    def word_search(self, board, word):
        """
        :param board: char[m][n]
        :param word: string, search word
        :return: bool: whether word is found or not
        """

        m = len(board)
        n = len(board[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if self.search(board, word, visited, i, j):
                    return True

        return False

    def search(self, board, word, visited, i, j):
        """
        :param board: char[m][n]
        :param word: string, search word
        :param visited: matrix used to detect whether board[x][y] has been visited
        :param i: row index
        :param j: column index
        :return: bool: indicates whether word is found or not
        """

        if len(word) == 0:
            return True

        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0] or visited[i][j] == 1:
            return False

        visited[i][j] = 1

        found = self.search(board, word[1:], visited, i+1, j) or self.search(board, word[1:], visited, i-1, j) or \
                self.search(board, word[1:], visited, i, j+1) or self.search(board, word[1:], visited, i, j-1)

        visited[i][j] = 0

        return found


b = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E'],
]
s = Solution()
print s.word_search(b, 'BCC')
print s.word_search(b, 'BCCS')
print s.word_search(b, 'ABFCEH')
