#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        r = 0
        length = len(nums)
        multiply = 1

        while r < length:
            multiply *= nums[r]
            while multiply >= k and l <= r:
                multiply //= nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res
# @lc code=end
