"""
描述
给定数组arr，arr中所有的值都为正整数且不重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张，再给定一个aim，代表要找的钱数，求组成aim的最少货币数。
输入描述：
输入包括两行，第一行两个整数n（0<=n<=1000）代表数组长度和aim（0<=aim<=5000），第二行n个不重复的正整数，代表arr
输出描述：
输出一个整数，表示组成aim的最小货币数，无解时输出-1.
示例1
输入：
3 20
5 2 3
输出：
4
说明：
20=5*4
示例2
输入：
3 0
5 2 3
输出：
0
示例3
输入：
2 2
3 5
输出：
-1
"""


class Solution:
    def GetMinCoin(self, arr, aim):
        if aim == 0:
            return 0
        dp = [-1] * (aim + 1)
        for i in range(1, aim + 1):
            minvalue = 0
            for item in arr:
                if i == item:
                    dp[i] = 1
                    break
                elif i > item and dp[i - item] != -1:
                    minvalue = min(minvalue, dp[i - item]) if minvalue else dp[i - item]
            if minvalue and dp[i] == -1:
                dp[i] = minvalue + 1
        return dp[-1]


if __name__ == '__main__':
    n, aim = input().split()
    arr = [int(item) for item in input().split()]
    test = Solution()
    print(test.GetMinCoin(arr, int(aim)))
