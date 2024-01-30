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
        p1 = 0
        p2 = 0
        while p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                if p1 >= len(s):
                    return True
            p2 += 1
        return False

# @lc code=end
