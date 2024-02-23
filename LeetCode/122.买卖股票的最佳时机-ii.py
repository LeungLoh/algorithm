#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp1 = [0] * len(prices)
        dp2 = [0] * len(prices)
        dp2[0] = -prices[0]
        for i in range(1, len(prices)):
            dp1[i] = max(dp1[i - 1], prices[i] + dp2[i - 1])
            dp2[i] = max(dp2[i - 1], dp1[i - 1] - prices[i])
        return dp1[-1]
# @lc code=end
