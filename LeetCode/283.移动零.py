#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums):
            while i < len(nums) - 1 and nums[i] == 0:
                i += 1
            nums[j] = nums[i]
            i += 1
            j += 1
        for i in range(j, len(nums)):
            nums[i] = 0


# @lc code=end
