#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for j in range(n):
            for i in range(n - j):
                if s[i] == s[i + j]:
                    dp[i][i + j] = dp[i + 1][i + j - 1] if j > 1 else 1
        res = ""
        for i in range(n):
            for j in range(n):
                if dp[i][j] == 1 and len(res) < (j - i + 1):
                    res = s[i:j + 1]
        return res

# @lc code=end
