#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
from collections import *
# @lc code=start


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = defaultdict(set)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                if x2 - x1 != 0:
                    k = (y2 - y1) / (x2 - x1)
                    b = y1 - k * x1
                else:
                    b = float('inf')
                    k = x1
                key = (k, b)
                m[key].add((x1, y1))
                m[key].add((x2, y2))
        return len(max(m.values(), key=len)) if m else 1

# @lc code=end
