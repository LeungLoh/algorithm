"""
描述
假设有排成一行的N个位置，记为1~N，开始时机器人在M位置，机器人可以往左或者往右走，如果机器人在1位置，
那么下一步机器人只能走到2位置，如果机器人在N位置，那么下一步机器人只能走到N-1位置。规定机器人只能走k步，
最终能来到P位置的方法有多少种。由于方案数可能比较大，所以答案需要对1e9+7取模。
输入描述：
输出包括一行四个正整数N（2<=N<=5000）、M(1<=M<=N)、K(1<=K<=5000)、P(1<=P<=N)。
输出描述：
输出一个整数，代表最终走到P的方法数对10^9+7取模后的值。
示例1
输入：
5 2 3 3
复制
输出：
3
说明：
1).2->1,1->2,2->3

2).2->3,3->2,2->3

3).2->3,3->4,4->3
示例2
输入：
1000 1 1000 1
输出：
591137401
说明：
注意答案要取模
"""


class Solution:
    def GetMaxWay(self, N, M, K, P):
        mod = 1e9 + 7
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        dp[0][P] = 1
        for i in range(1, K + 1):
            for j in range(1, N + 1):
                if j == 1:
                    dp[i][j] = dp[i - 1][j + 1]
                elif j == N:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = int((dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod)
        return dp[K][M]


if __name__ == '__main__':
    N, M, K, P = input().split()
    test = Solution()
    print(test.GetMaxWay(int(N), int(M), int(K), int(P)))
