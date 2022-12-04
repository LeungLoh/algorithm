#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start

# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if not s and not p:
#             return True
#         if s and not p:
#             return False
#         if not s and p:
#             if p[0] == "*":
#                 return self.isMatch(s, p[1:])
#             else:
#                 return False
#         if p[0] == "*":
#             while len(p) > 1 and p[1] == "*":
#                 p = p[1:]
#             return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
#         if s[0] == p[0] or p[0] == '?':
#             return self.isMatch(s[1:], p[1:])
#         return False


# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         if not s and not p:
#             return True
#         if s and not p:
#             return False
#         newp = [p[0]]
#         for i in range(1, len(p)):
#             if p[i] == "*" and p[i - 1] == "*":
#                 continue
#             newp.append(p[i])
#         p = newp
#         if not s and p:
#             return True if len(p) == 1 and p[0] == "*" else False
#         dp = [[0] * len(p) for _ in range(len(s))]
#         if s[0] == p[0] or p[0] == "?" or p[0] == "*":
#             dp[0][0] = 1
#         for i in range(1, len(s)):
#             dp[i][0] = 1 if p[0] == "*" else 0
#         for j in range(1, len(p)):
#             if p[j] == "*":
#                 dp[0][j] = dp[0][j - 1]
#             elif p[j] == "?" or s[0] == p[j]:
#                 if p[j - 1] == "*":
#                     dp[0][j] = 1 if j == 1 else 0
#         for j in range(1, len(p)):
#             for i in range(1, len(s)):
#                 if p[j] == "*":
#                     dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
#                 elif s[i] == p[j] or p[j] == "?":
#                     dp[i][j] = dp[i - 1][j - 1]

#         return True if dp[-1][-1] else False
#p[j-1]=="*" dp[i][j]==dp[i-1][j] or dp[j-1][i]
#p[j-1]==s[i-1] or s[i]=="?" dp[i][j]==dp[i-1][j-1]
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ns = len(s)
        np = len(p)
        dp = [[0] * (np + 1) for _ in range(ns + 1)]
        dp[0][0] = True
        for j in range(1, np + 1):
            if p[j - 1] == "*":
                dp[0][j] = 1
            else:
                break
        for j in range(1, np + 1):
            for i in range(1, ns + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
        return True if dp[-1][-1] else False
# @lc code=end
