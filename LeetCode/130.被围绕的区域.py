#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            self.dfs(board, i, 0, n, m)
            self.dfs(board, i, m - 1, n, m)
        for j in range(m):
            self.dfs(board, 0, j, n, m)
            self.dfs(board, n - 1, j, n, m)

        for i in range(n):
            for j in range(m):
                self.dfs(board, i, j, n, m, flag='X')

        for i in range(n):
            for j in range(m):
                if board[i][j] == '-':
                    board[i][j] = 'O'

    def dfs(self, board, i, j, n, m, flag='-'):
        if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != 'O':
            return
        board[i][j] = flag
        self.dfs(board, i + 1, j, n, m, flag)
        self.dfs(board, i - 1, j, n, m, flag)
        self.dfs(board, i, j - 1, n, m, flag)
        self.dfs(board, i, j + 1, n, m, flag)


# @lc code=end
