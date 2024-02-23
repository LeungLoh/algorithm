#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += self.dfs(grid, i, j, len(grid), len(grid[0]))
        return res

    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
            return 0
        grid[i][j] = "0"
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i, j - 1, m, n)
        self.dfs(grid, i, j + 1, m, n)
        return 1

# @lc code=end
