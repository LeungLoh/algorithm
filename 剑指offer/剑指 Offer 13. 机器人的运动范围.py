"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        maritx = [[0] * n for _ in range(m)]
        return self.dfs(maritx, 0, 0, k)

    def dfs(self, maritx, i, j, k):
        if i < 0 or i >= len(maritx) or j < 0 or j >= len(maritx[0]) or maritx[i][j] == -1:
            return 0
        if not self.checkk(i, j, k):
            return 0
        res = 1
        maritx[i][j] = -1
        res += self.dfs(maritx, i + 1, j, k)
        res += self.dfs(maritx, i - 1, j, k)
        res += self.dfs(maritx, i, j + 1, k)
        res += self.dfs(maritx, i, j - 1, k)
        return res

    def checkk(self, x, y, k):
        res = 0
        while x:
            res += x % 10
            x = int(x / 10)
        while y:
            res += y % 10
            y = int(y / 10)
        return res <= k
