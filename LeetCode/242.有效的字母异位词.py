#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
from collections import *
# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for item in s:
            m1[item] += 1
        for item in t:
            m2[item] += 1

        if len(m1.keys()) != len(m2.keys()):
            return False
        for k, v in m1.items():
            if m2[k] != v:
                return False
        return True
# @lc code=end
