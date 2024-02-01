#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
from collections import *
# @lc code=start


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = defaultdict(int)
        for item in magazine:
            m[item] += 1
        for item in ransomNote:
            if m.get(item, 0) > 0:
                m[item] -= 1
            else:
                return False
        return True
# @lc code=end
