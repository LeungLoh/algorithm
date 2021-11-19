"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。


"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        res = 1
        i, j, k = 0, 0, 0
        for index in range(n):
            v = min(dp[i] * 2, dp[j] * 3, dp[k] * 5)
            if v == dp[i] * 2:
                i += 1
            if v == dp[j] * 3:
                j += 1
            if v == dp[k] * 4:
                k += 1
            dp[index] = v
        return dp[-1]
