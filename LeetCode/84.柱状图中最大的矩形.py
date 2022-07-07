#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights):
        s = []
        res = 0
        temp = [0] + heights + [0]
        for i in range(len(temp)):
            while s and temp[i] < temp[s[-1]]:
                height = temp[s.pop()]
                res = max(res, height * (i - s[-1] - 1))
            s.append(i)
        return res


# @lc code=end
