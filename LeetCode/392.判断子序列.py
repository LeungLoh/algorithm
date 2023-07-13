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
        if not s:
            return True
        if not t:
            return False
        n = len(t)
        dp = [[-1] * 26 for i in range(n)]
        dp[-1][ord(t[-1]) - ord('a')] = n - 1
        for i in range(n - 2, -1, -1):
            for j in range(26):
                dp[i][j] = i if ord(t[i]) - ord('a') == j else dp[i + 1][j]
        cur = 0
        for c in s:
            if cur >= n:
                return False
            new_cur = dp[cur][ord(c) - ord('a')]
            if new_cur == -1:
                return False
            cur = new_cur + 1
        return True
# @lc code=end
