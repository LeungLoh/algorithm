#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
from typing import *
# @lc code=start


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [[0] * k for _ in range(len(prices))]
        sell = [[0] * k for _ in range(len(prices))]

        for i in range(k):
            buy[0][i] = -prices[0]
        for i in range(1, len(prices)):
            buy[i][0] = max(buy[i - 1][0], -prices[i])
            sell[i][0] = max(sell[i - 1][0], buy[i][0] + prices[i])
            for j in range(1, k):
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i][j] + prices[i])
        return sell[-1][-1]


test = Solution()
print(test.maxProfit(2, [2, 4, 1]))
# @lc code=end
