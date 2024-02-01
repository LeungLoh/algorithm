#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
from typing import *
# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left, right = 0, n - 1
        top, buttom = 0, n - 1

        while left < right and top < buttom:
            for j in range(right - left):
                temp = matrix[top][left + j]
                matrix[top][left + j] = matrix[buttom - j][left]
                matrix[buttom - j][left] = matrix[buttom][right - j]
                matrix[buttom][right - j] = matrix[top + j][right]
                matrix[top + j][right] = temp
            left += 1
            top += 1
            right -= 1
            buttom -= 1


# test = Solution()
# print(test.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))

# @lc code=end
