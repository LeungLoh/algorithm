#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if word1[0] == word2[0] else 0
        for i in range(1, n):
            dp[i][0] = 1 if word1[i] == word2[0] or dp[i - 1][0] else 0
        for j in range(1, m):
            dp[0][j] = 1 if word1[0] == word2[j] or dp[0][j - 1]else 0
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

        return n + m - dp[-1][-1] * 2
# @lc code=end
