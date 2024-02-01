#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        change = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0 and (i, j) not in change:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            change.add((k, j))
                        matrix[k][j] = 0
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            change.add((i, k))
                        matrix[i][k] = 0


# @lc code=end
