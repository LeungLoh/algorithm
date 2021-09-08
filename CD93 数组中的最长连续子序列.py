"""
描述
给定无序数组arr，返回其中最长的连续序列的长度(要求值连续，位置可以不连续,例如 3,4,5,6为连续的自然数）
输入描述：
输出两行，第一行包括一个整数n,第二行包含n个整数，分别代表arr[i]
输出描述：
输出一个整数，代表最长连续子序列的长度。
示例1
输入：
6
100 4 200 1 3 2
输出：
4
示例2
输入：
3
1 1 1
输出：
1

"""


class Solution:
    def GetMaxLenSublist(self, arr, n):
        arr.sort()
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[j] == arr[i] - 1:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution2:
    def GetMaxLenSublist(self, arr, n):
        dp = {}
        res = 1
        for item in arr:
            if item not in dp.keys():
                dp[item] = 1
                if dp.get(item - 1):
                    res = max(res, self.merge(dp, item - 1, item))
                if dp.get(item + 1):
                    res = max(res, self.merge(dp, item, item + 1))
        return res

    def merge(self, dp, less, more):
        left = less - dp[less] + 1
        right = more + dp[more] - 1
        len = right - left + 1
        dp[left] = len
        dp[right] = len
        return len


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    test = Solution2()
    print(test.GetMaxLenSublist(arr, n))
