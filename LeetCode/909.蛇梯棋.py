#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#
from typing import *
import sys
# @lc code=start


class Solution:
    def __init__(self) -> None:
        self.visited = set()

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        queue = [1]
        res = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                if cur == n * n:
                    return res
                for step in range(1, 7):
                    new_id = cur + step
                    if new_id == n * n:
                        queue.append(new_id)
                        break
                    elif new_id > n * n:
                        break
                    if new_id in self.visited:
                        continue
                    self.visited.add(new_id)
                    if new_id % n == 0:
                        i = n - new_id // n
                        j = 0 if (n - i) % 2 == 0 else n - 1
                    else:
                        i = n - new_id // n - 1
                        j = n - new_id % n if (n - i) % 2 == 0 else new_id % n - 1

                    if board[i][j] == -1:
                        queue.append(new_id)
                    else:
                        queue.append(board[i][j])
            res += 1
        return -1


test = Solution()
# print(test.snakesAndLadders([[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]))
# print(test.snakesAndLadders([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -
#   1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))
# @lc code=end
