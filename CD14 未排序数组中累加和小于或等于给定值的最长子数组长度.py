"""
描述
给定一个无序数组arr，其中元素可正、可负、可0。给定一个整数k，求arr所有的子数组中累加和小于或等于k的最长子数组长度
例如：arr = [3, -2, -4, 0, 6], k = -2. 相加和小于等于-2的最长子数组为{3, -2, -4, 0}，所以结果返回4
[要求]
时间复杂度为O(n)，空间复杂度为O(n)

输入描述：
第一行两个整数N, k。N表示数组长度，k的定义已在题目描述中给出
第二行N个整数表示数组内的数
输出描述：
输出一个整数表示答案
示例1
输入：
5 -2
3 -2 -4 0 6
输出：
4
"""


class Solution:

    def getMaxSublist(self, arr, n, k):
        m = {0: -1}
        sums = 0
        res = 0
        for i in range(n):
            sums += arr[i]
            if sums not in m.keys():
                m[sums] = i
            for k, v in m.items():
                if sums - k <= k:
                    res = max(res, i - v)
        return res


if __name__ == '__main__':
    N, k = input().split(" ")
    arr = [int(item) for item in input().split(" ")]
    test = Solution()
    print(test.getMaxSublist(arr, int(N), int(k)))
