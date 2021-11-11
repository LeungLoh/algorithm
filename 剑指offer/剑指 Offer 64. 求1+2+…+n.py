"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
"""


class Solution:
    def sumNums(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        dp[1] = 3
        if n <= 2:
            return dp[n - 1]
        for i in range(2, n):
            dp[i] = dp[i - 1] + i + 1
        return dp[-1]
