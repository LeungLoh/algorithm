"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
"""


class Solution:
    def translateNum(self, num: int) -> int:
        num = str(num)
        n = len(num)
        if n <= 1:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2 if int(num[0] + num[1]) < 26 else 1
        for i in range(2, n):
            if num[i - 1] != '0' and int(num[i - 1] + num[i]) < 26:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
