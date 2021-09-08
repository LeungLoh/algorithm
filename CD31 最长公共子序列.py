"""
描述
给定两个字符串str1和str2，输出连个字符串的最长公共子序列。如过最长公共子序列为空，则输出-1。
输入描述：
输出包括两行，第一行代表字符串str1，第二行代表str2。
输出描述：
输出一行，代表他们最长公共子序列。如果公共子序列的长度为空，则输出-1。
示例1
输入：
1A2C3D4B56
B1D23CA45B6A
输出：
123456
说明：
"123456"和“12C4B6”都是最长公共子序列，任意输出一个。
"""


class Solution:
    def GetSameSubStr(self, str1, str2, n, m):
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if str1[0] == str2[0] else 0
        for i in range(1, n):
            dp[i][0] = 1 if str1[i] == str2[0] or dp[i - 1][0] else 0
        for j in range(1, m):
            dp[0][j] = 1 if str1[0] == str2[j] or dp[0][j - 1] else 0
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if str1[i] == str2[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        length = dp[n - 1][m - 1]
        if length == 0:
            return -1
        res = ""
        i = n - 1
        j = m - 1
        while length:
            if i > 0 and dp[i][j] == dp[i - 1][j]:
                i -= 1
            elif j > 0 and dp[i][j] == dp[i][j - 1]:
                j -= 1
            else:
                res = str1[i] + res
                i -= 1
                j -= 1
                length -= 1
        return res


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    test = Solution()
    print(test.GetSameSubStr(s1, s2, len(s1), len(s2)))
