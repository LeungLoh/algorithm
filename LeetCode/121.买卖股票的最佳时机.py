#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        dp[-1] = prices[-1]
        res = 0
        for i in range(len(prices) - 2, -1, -1):
            dp[i] = max(prices[i], dp[i + 1])
            res = max(res, dp[i] - prices[i])
        return res
# @lc code=end
