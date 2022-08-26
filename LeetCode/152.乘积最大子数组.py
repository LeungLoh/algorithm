#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
from functools import reduce


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_v, min_v, ans = nums[0], nums[0], nums[0]
        for num in nums[1:]:
            mx, mn = max_v, min_v
            max_v = max(num * mx, num * mn, num)
            min_v = min(num * mx, num * mn, num)
            ans = max(ans, max_v)
        return ans
# @lc code=end
