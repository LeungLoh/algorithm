#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        kb_map = {}
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                x1 = points[i][0]
                x2 = points[j][0]
                y1 = points[i][1]
                y2 = points[j][1]

                if x1 - x2 != 0:
                    k = (y1 - y2) / (x1 - x2)
                    b = y2 - k * x2
                else:
                    b = float('inf')
                    k = x1

                key = (k, b)
                p1 = (x1, y1)
                p2 = (x2, y2)
                if key in kb_map:
                    if p1 not in kb_map[key]:
                        kb_map[key].add(p1)
                    if p2 not in kb_map[key]:
                        kb_map[key].add(p2)
                else:
                    kb_map[key] = set([p1, p2])

        return len(max(kb_map.values(), key=len)) if kb_map else 1
# @lc code=end
