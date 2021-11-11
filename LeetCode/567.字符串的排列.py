#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
from typing import _SpecialForm


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        while r <= len(s2):
            if self.check(s1, s2[l:r]):
                return True
            l += 1
            r += 1
        return False

    def check(self, s1, s2):
        s1 = ''.join(sorted(s1))
        s2 = ''.join(sorted(s2))
        return s1 == s2
# @lc code=end
