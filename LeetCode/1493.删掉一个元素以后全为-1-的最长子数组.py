#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#
from typing import *
# @lc code=start


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        zero = 0
        res = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            elif zero == 0:
                zero += 1
                right += 1
            else:
                while nums[left] != 0:
                    left += 1
                left += 1
                zero -= 1
            res = max(res, right - left - 1)
        return res


test = Solution()
test.longestSubarray([1, 1, 0, 0, 1, 1, 1, 0, 1])

# @lc code=end
