#
# @lc app=leetcode.cn id=2352 lang=python3
#
# [2352] 相等行列对
#

# @lc code=start
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row = []
        col = defaultdict(int)
        n = len(grid)
        for i in range(n):
            temp = [str(grid[i][j]) for j in range(n)]
            row.append(",".join(temp))
        for j in range(n):
            temp = [str(grid[i][j]) for i in range(n)]
            col[",".join(temp)] += 1
        res = 0
        for item in row:
            if col.get(item):
                res += col[item]
        return res


# @lc code=end
