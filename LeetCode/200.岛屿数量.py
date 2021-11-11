#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j, n, m)
        return res

    def dfs(self, grid, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j, n, m)
        self.dfs(grid, i - 1, j, n, m)
        self.dfs(grid, i, j + 1, n, m)
        self.dfs(grid, i, j - 1, n, m)


# @lc code=end
