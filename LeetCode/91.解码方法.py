#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        n = len(s)
        dp = [0] * n
        dp[0] = 1
        if s[1] == "0":
            dp[1] = 1 if int(s[0] + s[1]) <= 26 else 0
        else:
            dp[1] = 2 if int(s[0] + s[1]) <= 26 else 1

        for i in range(2, n):
            if s[i - 1] == "0" and s[i] == "0":
                dp[i] = 0
            elif s[i - 1] == "0" and s[i] != "0":
                dp[i] = dp[i - 1]
            elif s[i - 1] != "0" and s[i] == "0":
                dp[i] = dp[i - 2] if int(s[i - 1] + s[i]) <= 26 else 0
            else:
                dp[i] = dp[i - 1] + dp[i - 2] if int(s[i - 1] + s[i]) <= 26 else dp[i - 1]

        return dp[-1]
# @lc code=end
