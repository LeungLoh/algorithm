#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        pos = sum(nums) // 2
        dp = [0] * (pos + 1)
        dp[0] = 1
        for num in nums:
            for i in range(pos, num - 1, -1):
                dp[i] = dp[i - num]
        return True if dp[-1] else False
# @lc code=end
