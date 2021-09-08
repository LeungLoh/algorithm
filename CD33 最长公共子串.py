"""
描述
给定两个字符串str1和str2,输出两个字符串的最长公共子串，如果最长公共子串为空，输出-1。
输入描述：
输入包括两行，第一行代表字符串srr1，第二行代表字符串str2。
输出描述：
输出包括一行，代表最长公共子串。
示例1
输入：
1AB2345CD
12345EF
输出：
2345
"""


class Solution:
    def GetSameSubStr(self, s1, s2, n, m):
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if s1[0] == s2[0] else 0
        for i in range(1, n):
            dp[i][0] = 1 if s1[i] == s2[0] else 0
        for j in range(1, m):
            dp[0][j] = 1 if s1[0] == s2[j] else 0

        for i in range(1, n):
            for j in range(1, m):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        index = 0
        maxlength = 0
        for i in range(n):
            for j in range(m):
                if dp[i][j] > maxlength:
                    index = i
                    maxlength = dp[i][j]
        if maxlength == 0:
            return -1
        return s1[index - maxlength + 1:index + 1]


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    test = Solution()
    print(test.GetSameSubStr(s1, s2, len(s1), len(s2)))
