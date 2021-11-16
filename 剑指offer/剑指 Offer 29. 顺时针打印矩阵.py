"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        left, top, right, buttom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        res = []
        while left < right and top < buttom:
            for i in range(left, right):
                res.append(matrix[top][i])
            for i in range(top, buttom):
                res.append(matrix[i][right])
            for i in range(right, left, -1):
                res.append(matrix[buttom][i])
            for i in range(buttom, top, -1):
                res.append(matrix[i][left])

            left += 1
            top += 1
            right -= 1
            buttom -= 1
        if right > left and top == buttom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
        elif buttom > top and left == right:
            for i in range(top, buttom + 1):
                res.append(matrix[i][left])
        elif left == right and top == buttom:
            res.append(matrix[left][buttom])
        return res
