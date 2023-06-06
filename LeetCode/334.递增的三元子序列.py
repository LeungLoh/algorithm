#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
class Solution:
    # def increasingTriplet(self, nums: List[int]) -> bool:
    def increasingTriplet(self, nums):
        first = nums[0]
        second = max(nums) + 1
        for num in nums:
            if num > second:
                return True
            if num > first:
                second = num
            if num < first:
                first = num
        return False

# @lc code=end
