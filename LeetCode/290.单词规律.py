#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        fields = s.strip().split(" ")
        while " " in fields:
            fields.remove(" ")
        if len(fields) != len(pattern):
            return False
        m1 = {}
        m2 = {}
        for i, v in enumerate(fields):
            if v not in m1 and pattern[i] not in m2:
                m1[v] = pattern[i]
                m2[pattern[i]] = v
            elif m1.get(v) != pattern[i] or m2.get(pattern[i]) != v:
                return False
        return True

# @lc code=end
