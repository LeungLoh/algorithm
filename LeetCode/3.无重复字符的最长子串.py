#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        res = 0
        index = 0
        for i in range(len(s)):
            if s[i] in m.keys():
                index = max(m[s[i]] + 1, index)
            res = max(res, i - index + 1)
            m[s[i]] = i
        return res

# @lc code=end
