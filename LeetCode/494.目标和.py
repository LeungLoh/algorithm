#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (target + sum(nums)) % 2 != 0 or target + sum(nums) < 0:
            return 0
        pos = (target + sum(nums)) // 2
        dp = [0] * (pos + 1)
        dp[0] = 1
        for num in nums:
            for i in range(pos, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]

# @lc code=end
