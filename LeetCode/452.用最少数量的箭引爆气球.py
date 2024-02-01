#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import *
# @lc code=start


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        _points = sorted(points, key=lambda x: (x[0], x[1]))
        res = [_points[0]]
        for i in range(1, len(_points)):
            last = res[-1]
            if last[1] >= _points[i][0]:
                last[0] = max(_points[i][0], last[0])
                last[1] = min(_points[i][1], last[1])
                res.pop()
                res.append(last)
            else:
                res.append(_points[i])
        return len(res)


test = Solution()
test.findMinArrowShots([[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]])
# @lc code=end
