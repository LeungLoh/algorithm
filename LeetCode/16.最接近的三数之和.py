#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
import sys
from typing import *


class Solution:
    def length(self, a, b):
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            return abs(a - b)
        else:
            return abs(a) + abs(b)

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        nums = sorted(nums)
        res = sys.maxsize
        for i in range(length - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if self.length(temp, target) < self.length(res, target):
                    res = temp
                if temp > target:
                    r -= 1
                elif temp < target:
                    l += 1
                else:
                    return target
        return res


# test = Solution()
# print(test.threeSumClosest([-1, 2, 1, -4], 1))
# @lc code=end
