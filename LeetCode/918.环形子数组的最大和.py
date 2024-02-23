#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#

# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        res = max(res, max(dp))

        leftmax = [0] * len(nums)
        leftmax[0] = nums[0]
        prefix = nums[0]
        for i in range(1, len(nums)):
            prefix += nums[i]
            leftmax[i] = max(prefix, leftmax[i - 1])
        right = 0
        for i in range(len(nums) - 1, 0, -1):
            right += nums[i]
            res = max(res, right + leftmax[i - 1])
        return res


# @lc code=end
