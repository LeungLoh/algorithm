#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start
class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, self.dfs(grid, i, j))
        return res

    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return 0
        if grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        count = 1
        count += self.dfs(grid, x - 1, y)
        count += self.dfs(grid, x + 1, y)
        count += self.dfs(grid, x, y - 1)
        count += self.dfs(grid, x, y + 1)
        return count

# @lc code=end
