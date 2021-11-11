"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j):
                    return True
        return False

    def dfs(self, board, word, i, j):
        if not word:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        if board[i][j] == -1:
            return False
        temp = board[i][j]
        board[i][j] = -1
        res = self.dfs(board, word[1:], i + 1, j) or\
            self.dfs(board, word[1:], i - 1, j) or\
            self.dfs(board, word[1:], i, j + 1) or\
            self.dfs(board, word[1:], i, j - 1)
        if not res:
            board[i][j] = temp
        return res
