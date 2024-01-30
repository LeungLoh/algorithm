#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp_left = [1] * len(nums)
        dp_right = [1] * len(nums)
        for i in range(1, len(nums)):
            dp_left[i] = nums[i - 1] * dp_left[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            dp_right[i] = nums[i + 1] * dp_right[i + 1]
        res = []
        for i in range(len(nums)):
            res.append(dp_left[i] * dp_right[i])
        return res


# @lc code=end
