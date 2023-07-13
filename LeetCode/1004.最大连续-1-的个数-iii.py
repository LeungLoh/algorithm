#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from typing import *
# @lc code=start


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        zero = 0
        res = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            elif zero < k:
                zero += 1
                right += 1
            else:
                while nums[left] != 0:
                    left += 1
                zero -= 1
                left += 1
            res = max(res, right - left)
        return res


test = Solution()
test.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
# @lc code=end
