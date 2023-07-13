#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
from typing import *


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        res = sum(nums[:k])
        windows = res
        for left in range(1, n - k + 1):
            right = left + k - 1
            windows = windows + nums[right] - nums[left - 1]
            res = max(res, windows)
        return res / k


# @lc code=end
