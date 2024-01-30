#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
from typing import *
# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        left = 0
        res = 0
        for i, v in enumerate(s):
            if m.get(v) != None:
                left = max(left, m[v] + 1)
            res = max(res, i - left + 1)
            m[v] = i
        return res if res != 0 else len(s)


# test = Solution()
# print(test.lengthOfLongestSubstring("pwwkew"))
# @lc code=end
