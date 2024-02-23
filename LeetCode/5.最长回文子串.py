#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = s[0]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and (dp[i + 1][j - 1] or j - i == 1):
                    dp[i][j] = True
                    if j - i + 1 > len(res):
                        res = s[i:j + 1]
                else:
                    dp[i][j] = False
        return res

# @lc code=end
