#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = index = len(nums) - 1
        res = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                res[index] = nums[r] * nums[r]
                r -= 1
            else:
                res[index] = nums[l] * nums[l]
                l += 1
            index -= 1
        return res
# @lc code=end
