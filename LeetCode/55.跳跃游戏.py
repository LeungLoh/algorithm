#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        sums = nums[0]
        for i in range(1, len(nums)):
            sums -= 1
            if sums < 0:
                return False
            if sums < nums[i]:
                sums = nums[i]
        return True


# @lc code=end
