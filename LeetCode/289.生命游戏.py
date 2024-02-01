#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
from typing import *
# @lc code=start


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changed = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                sum_1 = 0

                top = i - 1 if i > 0 else i
                buttom = i + 1 if i < len(board) - 1 else i
                left = j - 1 if j > 0 else j
                right = j + 1 if j < len(board[0]) - 1 else j
                for k in range(top, buttom + 1):
                    for t in range(left, right + 1):

                        v = board[k][t]
                        if (k, t) in changed:
                            v = 1 if board[k][t] == 0 else 0
                        if v == 1 and (i != k or j != t):
                            sum_1 += 1
                if board[i][j] == 1 and (sum_1 < 2 or sum_1 > 3):
                    board[i][j] = 0
                    changed.add((i, j))
                elif board[i][j] == 0 and sum_1 == 3:
                    board[i][j] = 1
                    changed.add((i, j))


# test = Solution()
# print(test.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))

# @lc code=end
