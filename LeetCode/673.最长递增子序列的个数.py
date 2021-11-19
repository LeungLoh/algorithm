#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#

# @lc code=start
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        help = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        help[i] = help[j]
                    elif dp[j] + 1 == dp[i]:
                        help[i] += help[j]
        maxlength = max(dp)
        res = 0
        for i in range(n):
            if dp[i] == maxlength:
                res += help[i]
        return res
# @lc code=end
