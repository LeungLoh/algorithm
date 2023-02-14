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
            for j in range(left, right):
                res.append(matrix[top][j])
            for i in range(top, buttom):
                res.append(matrix[i][right])
            for j in range(right, left, -1):
                res.append(matrix[buttom][j])
            for i in range(buttom, top, -1):
                res.append(matrix[i][left])
            top += 1
            left += 1
            buttom -= 1
            right -= 1

        if left == right and top == buttom:
            res.append(matrix[left][top])
        if left == right and top < buttom:
            for i in range(top, buttom + 1):
                res.append(matrix[i][left])
        if left < right and top == buttom:
            for j in range(left, right + 1):
                res.append(matrix[top][j])
        return res


# @lc code=end
