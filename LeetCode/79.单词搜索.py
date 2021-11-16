#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False if word else True
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if self.dfs(board, list(word), i, j, n, m):
                    return True
        return False

    def dfs(self, board, word, i, j, n, m):
        if not word:
            return True
        if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != word[0] or board[i][j] == 0:
            return False
        temp = board[i][j]
        board[i][j] = 0

        res = self.dfs(board, word[1:], i + 1, j, n, m) or\
            self.dfs(board, word[1:], i - 1, j, n, m) or\
            self.dfs(board, word[1:], i, j + 1, n, m) or\
            self.dfs(board, word[1:], i, j - 1, n, m)
        board[i][j] = temp
        return res
# @lc code=end
