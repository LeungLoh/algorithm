# -*- encoding: utf-8 -*-
'''
Author: leungloh
Email: liangquanle@360.cn
version: @v1.0
Date: 2021/08/23 18:15:08
'''

"""
描述
给定一个无序数组arr, 其中元素可正、可负、可0。给定一个整数k，求arr所有子数组中累加和为k的最长子数组长度
输入描述：
第一行两个整数N, k。N表示数组长度，k的定义已在题目描述中给出
第二行N个整数表示数组内的数
输出描述：
输出一个整数表示答案
示例1
输入：
5 0
1 -2 1 1 1
复制
输出：
3
"""


class Solution:

    def getMaxSublist(self, arr, n, k):
        sums = 0
        m = {0: -1}
        res = 0
        for i in range(n):
            sums += arr[i]
            if sums not in m.keys():
                m[sums] = i
            if sums - k in m:
                res = max(res, i - m[sums - k])
        return res


if __name__ == '__main__':
    N, k = input().split(" ")
    arr = [int(item) for item in input().split(" ")]
    test = Solution()
    print(test.getMaxSublist(arr, int(N), int(k)))
