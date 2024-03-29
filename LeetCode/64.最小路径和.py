#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
# dfs timeout
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m = len(grid) - 1
#         n = len(grid[0]) - 1
#         return self.dfs(0, 0, m, n, 0, grid)

#     def dfs(self, i, j, m, n, res, grid):
#         if i == m and j == n:
#             return res + grid[i][j]
#         if i == m:
#             return self.dfs(i, j + 1, m, n, res + grid[i][j], grid)
#         if j == n:
#             return self.dfs(i + 1, j, m, n, res + grid[i][j], grid)
#         return min(self.dfs(i + 1, j, m, n, res + grid[i][j], grid), self.dfs(i, j + 1, m, n, res + grid[i][j], grid))


# dp


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp = [[0] * len(grid[0])for _ in range(len(grid))]
        # dp[0][0]=grid[0][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

# @lc code=end
