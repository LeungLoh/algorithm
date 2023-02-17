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
        top, buttom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []
        while left < right and top < buttom:
            i, j = top, left
            while j < right:
                res.append(matrix[top][j])
                j += 1
            while i < buttom:
                res.append(matrix[i][right])
                i += 1
            while j > left:
                res.append(matrix[buttom][j])
                j -= 1
            while i > top:
                res.append(matrix[i][left])
                i -= 1
            top += 1
            buttom -= 1
            left += 1
            right -= 1
        if left == right and top == buttom:
            res.append(matrix[left][top])
        elif left < right and top == buttom:
            while left <= right:
                res.append(matrix[top][left])
                left += 1
        elif top < buttom and left == right:
            while top <= buttom:
                res.append(matrix[top][left])
                top += 1
        return res


# @lc code=end
