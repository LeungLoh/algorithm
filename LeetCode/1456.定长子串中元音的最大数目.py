#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        windows = 0
        yuanyin = set(['a', 'e', 'i', 'o', 'u'])
        for i in range(k):
            if s[i] in yuanyin:
                windows += 1
        res = windows
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in yuanyin:
                windows -= 1
            if s[i + k - 1] in yuanyin:
                windows += 1
            res = max(res, windows)
        return res
# @lc code=end
