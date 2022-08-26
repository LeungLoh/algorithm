#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, len(board), len(board[0]), word):
                    return True
        return False

    def dfs(self, board, i, j, m, n, word):
        if not word:
            return True
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j]=0
        res = self.dfs(board, i + 1, j, m, n, word[1:]) or self.dfs(board, i - 1, j, m, n, word[1:]) or \
            self.dfs(board, i, j + 1, m, n, word[1:]) or self.dfs(board, i, j - 1, m, n, word[1:])
        board[i][j] = temp
        return res
# @lc code=end
