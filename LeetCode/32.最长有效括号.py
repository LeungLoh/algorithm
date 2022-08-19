#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s = " " + s
        n = len(s)
        dp = [0] * (n)
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2] if s[i - dp[i - 1] - 1] == "(" else 0
        return max(dp)

# @lc code=end
