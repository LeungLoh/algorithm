#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
from collections import *
# @lc code=start


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}
        for i in range(len(s)):
            if s[i] not in m1 and t[i] not in m2:
                m1[s[i]] = t[i]
                m2[t[i]] = s[i]
            elif m1.get(s[i]) != t[i] or m2.get(t[i]) != s[i]:
                return False
        return True


# test = Solution()
# print(test.isIsomorphic("paper", "title"))
# @lc code=end
