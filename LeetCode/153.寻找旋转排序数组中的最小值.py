#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
from typing import *
# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


test = Solution()
test.findMin([4, 5, 6, 7, 0, 1, 2])
# @lc code=end
