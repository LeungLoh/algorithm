#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
        heights = matrix[0]
        res = self.largestRectangleArea(heights)
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + matrix[i][j] if matrix[i][j] else 0
            res = max(res, self.largestRectangleArea(heights))
        return res

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
