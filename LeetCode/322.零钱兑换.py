#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != -1:
                    dp[i] = min(dp[i - coin] + 1, dp[i]) if dp[i] != -1 else dp[i - coin] + 1
        return dp[-1]
# @lc code=end
