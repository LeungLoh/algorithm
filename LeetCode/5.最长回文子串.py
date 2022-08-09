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
        res = ""
        maxlength=0
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        if j - i == 1:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j-i+1>maxlength:
                    maxlength=j-i+1
                    res=s[i:j+1]
        return res

# @lc code=end
