#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [0] * n
        minprice = prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i] - minprice)
            minprice = min(minprice, prices[i])
        return dp[-1]

# @lc code=end
