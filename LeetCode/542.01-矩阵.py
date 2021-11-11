#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        queue = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = sys.maxsize
        temp = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            i, j = queue.pop(0)
            for node in temp:
                x = i + node[0]
                y = j + node[1]
                if x < 0 or x >= n or y < 0 or y >= m or mat[x][y] <= mat[i][j] + 1:
                    continue
                mat[x][y] = mat[i][j] + 1
                queue.append((x, y))
        return mat


# @lc code=end
