#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
import sys
from typing import *
# @lc code=start


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        res = sys.maxsize
        pre = 0
        while right < len(nums):
            if pre < target:
                pre += nums[right]

            while left <= right and pre >= target:
                res = min(res, right - left + 1)
                pre -= nums[left]
                left += 1
            right += 1
        return res if res != sys.maxsize else 0


# test = Solution()
# print(test.minSubArrayLen(4, [1, 4, 4]))
# @lc code=end
