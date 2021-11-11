"""
描述
给定数组arr，设数组长度为n，arr中所有的值都为正整数且不重复。每个值代表一种面值的货币，
每种面值的货币可以使用任意张，再给定一个整数aim，代表要找的钱数，求换钱的方法数有多少种。
由于方法的种数比较大，所以要求输出对10^9进行取模后的答案。
输入描述：
输出包括两行，第一行包括两个整数n(0≤n≤1000)和aim(0≤aim≤20000)。第二行包含n个整数，表示arr数组
 ≤1e9)。
输出描述：
输出一个整数，表示换钱的方法数对10^9+7取模后的答案。
示例1
输入：
4 15
5 10 25 1
输出：
6
说明：
5*3=15
10*1+5*1=15
10*1+1*5=15
1*10+5*1=15
5*2+1*5=15
1*15=15
示例2
输入：
5 1000
2 3 5 7 10
复制
输出：
20932712
"""


class Solution:
    def GetChangeCoin(self, n, aim, arr):
        dp = [0] * (aim + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(arr[i], aim + 1):
                dp[j] = int((dp[j] + dp[j - arr[i]]) % (1e9 + 7))
        return dp[-1]


if __name__ == '__main__':
    n, aim = input().split()
    arr = [int(item) for item in input().split()]
    test = Solution()
    print(test.GetChangeCoin(int(n), int(aim), arr))
