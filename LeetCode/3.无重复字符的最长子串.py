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
            if m.get(s[i]) != None:
                index = max(index, m[s[i]] + 1)
            res = max(res, i - index + 1)
            m[s[i]] = i
        return res

# @lc code=end
