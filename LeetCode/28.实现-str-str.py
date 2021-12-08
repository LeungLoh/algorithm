#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        n = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0] and haystack[i:i + n] == needle:
                return i
        return -1

# @lc code=end
