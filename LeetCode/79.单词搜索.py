#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from typing import *
# @lc code=start


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i, v in enumerate(board):
            for j, _ in enumerate(v):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word):
                        return True
        return False

    def dfs(self, board, i, j, word):
        if not word:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == -1:
            return False

        c = board[i][j]
        board[i][j] = -1
        if c == word[0]:
            if self.dfs(board, i + 1, j, word[1:]):
                return True
            if self.dfs(board, i - 1, j, word[1:]):
                return True
            if self.dfs(board, i, j + 1, word[1:]):
                return True
            if self.dfs(board, i, j - 1, word[1:]):
                return True
        board[i][j] = c
        return False


test = Solution()
test.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
# @lc code=end
