#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
from typing import *
# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1 = [0] * len(prices)
        sell1 = [0] * len(prices)
        buy2 = [0] * len(prices)
        sell2 = [0] * len(prices)
        buy1[0] = -prices[0]
        buy2[0] = -prices[0]
        for i in range(1, len(prices)):
            buy1[i] = max(buy1[i - 1], -prices[i])
            sell1[i] = max(sell1[i - 1], buy1[i - 1] + prices[i])
            buy2[i] = max(buy2[i - 1], sell1[i - 1] - prices[i])
            sell2[i] = max(sell2[i - 1], buy2[i - 1] + prices[i])
        print(buy1)
        print(buy2)
        return sell2[-1]


test = Solution()
print(test.maxProfit([2, 4, 1]))
# @lc code=end
