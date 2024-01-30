#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from typing import *
# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        res = 0
        for i in range(len(height)):
            while s and height[s[-1]] <= height[i]:
                index = s.pop()
                if s:
                    left = s[-1]
                    right = i
                    res += (right - left - 1) * (min(height[left], height[right]) - height[index])
            s.append(i)
        return res


# test = Solution()
# print(test.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# @lc code=end
