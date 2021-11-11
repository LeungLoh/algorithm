#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#

# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        n = len(grid)
        m = len(grid[0])
        res = 1
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        queue = [[0, 0]]
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.pop(0)
                if x == n - 1 and y == m - 1:
                    return res
                for dir in dirs:
                    tmpx = x + dir[0]
                    tmpy = y + dir[1]
                    if tmpx < 0 or tmpx >= n or tmpy < 0 or tmpy >= m or grid[tmpx][tmpy] == 1:
                        continue
                    queue.append([tmpx, tmpy])
                    grid[tmpx][tmpy] = 1
            res += 1

        return -1

# @lc code=end
