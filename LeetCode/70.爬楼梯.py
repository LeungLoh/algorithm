#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         return self.dfs(n)

#     def dfs(self, n):
#         if n <= 2:
#             return n
#         return self.dfs(n-1)+self.dfs(n-2)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
# @lc code=end
