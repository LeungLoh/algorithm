#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if not s:
#             return True

#         p1 = 0
#         p2 = 0
#         while p1 < len(s) and p2 < len(t):
#             if s[p1] == t[p2]:
#                 p1 += 1
#                 if p1 == len(s):
#                     return True
#             p2 += 1
#         return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        dp = {i: {c: -1 for c in s}for i in range(n)}
        dp[n - 1][t[-1]] = n - 1
        for i in range(n - 2, -1, -1):
            for j in range(i, n):
                if t[i] == t[j]:
                    dp[i][t[j]] = i
                else:
                    dp[i][j] = dp[i + 1][j]

# @lc code=end
