#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * len(prices), [0] * len(prices)]
        dp[1][0] = -prices[0]
        for i in range(1, len(prices)):

            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
            dp[1][i] = max(dp[0][i - 1] - prices[i], dp[1][i - 1])
        return dp[0][-1]
# @lc code=end
