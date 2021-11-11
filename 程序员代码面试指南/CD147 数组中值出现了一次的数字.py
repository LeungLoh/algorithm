"""
描述
给定一个数字arr，其中只有有两个数字出现了奇数次，其它数字都出现了偶数次，按照从小到大顺序输出这两个数。
输入描述：
输入包含两行，第一行一个整数n，代表数组arr的长度，第二行n个整数，代表数组arr,arr[i]为32位整数。
输出描述：
输出出现奇数次的两个数，按照从小到大的顺序。
示例1
输入：
4
1 1 2 3
复制
输出：
2 3
示例2
输入：
6
11 22 11 23 23 45
输出：
22 45
"""


class Solution:
    def GetSingleNum(self, arr, n):
        sum = 0
        for v in arr:
            sum ^= v
        firstonebit = sum & (~sum + 1)
        first = 0
        for v in arr:
            if v & firstonebit != 0:
                first ^= v
        second = sum ^ first
        if first > second:
            first, second = second, first
        return first, second


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    test = Solution()
    first, second = test.GetSingleNum(arr, n)
    print(first, second)
