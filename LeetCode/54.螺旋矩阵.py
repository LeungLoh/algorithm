#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from pickle import MARK


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, buttom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while left < right and top < buttom:
            for j in range(left, right):
                res.append(matrix[top][j])
            for i in range(top, buttom):
                res.append(matrix[i][right])
            for j in range(right, left, -1):
                res.append(matrix[buttom][j])
            for i in range(buttom, top, -1):
                res.append(matrix[i][left])
            left += 1
            top += 1
            right -= 1
            buttom -= 1
        if left == right and top == buttom:
            res.append(matrix[top][left])
        elif left == right:
            for i in range(top, buttom + 1):
                res.append(matrix[i][left])
        elif top == buttom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
        return res

# @lc code=end
