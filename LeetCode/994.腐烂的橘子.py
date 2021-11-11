#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        res = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
        temp = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.pop(0)
                for node in temp:
                    x = i + node[0]
                    y = j + node[1]
                    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 1:
                        continue
                    grid[x][y] = 2
                    queue.append((x, y))
            res += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return res - 1 if res else res

# @lc code=end
