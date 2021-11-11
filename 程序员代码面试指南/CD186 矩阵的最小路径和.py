"""
描述
给定一个 n * m 的矩阵 a，从左上角开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，输出所有的路径中最小的路径和。
输入描述：
第一行输入两个整数 n 和 m，表示矩阵的大小。

接下来 n 行每行 m 个整数表示矩阵。
输出描述：
输出一个整数表示答案。
示例1
输入：
4 4
1 3 5 9
8 1 3 4
5 0 6 1
8 8 4 0
输出：
12
"""


class Solution:
    def GetMaxPath(self, arr, n, m):
        dp = [[0] * m for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i == n - 1 and j == m - 1:
                    dp[i][j] = arr[i][j]
                elif i == n - 1:
                    dp[i][j] = arr[i][j] + dp[i][j + 1]
                else:
                    if j == m - 1:
                        dp[i][j] = arr[i][j] + dp[i + 1][j]
                    else:
                        dp[i][j] = arr[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


if __name__ == '__main__':
    n, m = input().split()
    arr = []
    for i in range(int(n)):
        nums = [int(item) for item in input().split()]
        arr.append(nums)
    test = Solution()
    print(test.GetMaxPath(arr, int(n), int(m)))
