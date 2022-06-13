#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from pickle import MARK


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        top, left = 0, 0
        buttom, right = len(matrix) - 1, len(matrix[0]) - 1
        while left < right and top < buttom:
            for i in range(left, right):
                res.append(matrix[top][i])
            for j in range(top, buttom):
                res.append(matrix[j][right])
            for i in range(right, left, -1):
                res.append(matrix[buttom][i])
            for j in range(buttom, top, -1):
                res.append(matrix[j][left])
            left += 1
            top += 1
            right -= 1
            buttom -= 1
        if left < right and top == buttom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
        elif top < buttom and left == right:
            for i in range(top, buttom + 1):
                res.append(matrix[i][left])
        elif left == right and top == buttom:
            res.append(matrix[top][left])
        return res


# @lc code=end
