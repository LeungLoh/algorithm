#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
from typing import *


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0] * (len(matrix[0]) + 1)for _ in range(len(matrix) + 1)]
        res = 0
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                    res = max(res, dp[i][j])
        return res * res


test = Solution()
test.maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])

# @lc code=end
