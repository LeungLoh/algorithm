#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x, y = 0, len(matrix) - 1
        while x < y:
            p1, p2 = x, y
            while p1 < y:
                temp = matrix[x][p1]
                matrix[x][p1] = matrix[p2][x]  # 左上
                matrix[p2][x] = matrix[y][p2]  # 左下
                matrix[y][p2] = matrix[p1][y]  # 右下
                matrix[p1][y] = temp  # 右上
                p1 += 1
                p2 -= 1
            x += 1
            y -= 1

# @lc code=end
