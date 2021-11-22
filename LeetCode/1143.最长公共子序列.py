#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, n):
            dp[i][0] = 1 if text1[i] == text2[0] or dp[i - 1][0] else 0
        for j in range(1, m):
            dp[0][j] = 1 if text1[0] == text2[j] or dp[0][j - 1] else 0
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])
        return dp[-1][-1]
# @lc code=end
