#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lengths = len(s)
        lengtht = len(t)
        dp = [[0] * lengths for i in range(lengths)]
        for j in range(lengtht, lengths):
            if dp[0][j - 1] == 1:
                dp[0][j] == 1
                continue
            for item in t:
                if item not in s[:j]:
                    break
                dp[0][j] = 1
        for i in range(lengths - lengtht):
            for j in range(i + lengtht, lengths):

                # @lc code=end
