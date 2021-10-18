"""
描述
给定一个数组arr，返回子数组的最大累加和
例如，arr = [1, -2, 3, 5, -2, 6, -1]，所有子数组中，[3, 5, -2, 6]可以累加出最大的和12，所以返回12.
[要求]
时间复杂度为O(n)O(n)，空间复杂度为O(1)O(1)

输入描述：
第一行一个整数N。表示数组长度
接下来一行N个整数表示数组内的元素
输出描述：
输出一个整数表示答案
示例1
输入：
7
1 -2 3 5 -2 6 -1 
复制
输出：
12
"""


class Solution:
    def GetSumMaxSub(self, arr, n):
        dp = [arr[i] for i in range(n)]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + arr[i], dp[i])
        return max(dp)


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    test = Solution()
    print(test.GetSumMaxSub(arr, n))
