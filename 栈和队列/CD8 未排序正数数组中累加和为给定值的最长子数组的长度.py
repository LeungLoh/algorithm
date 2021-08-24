# -*- encoding: utf-8 -*-
'''
Author: leungloh
Email: liangquanle@360.cn
version: @v1.0
Date: 2021/08/23 17:53:52
'''

"""
描述
给定一个数组arr，该数组无序，但每个值均为正数，再给定一个正数k。求arr的所有子数组中所有元素相加和为k的最长子数组的长度
例如，arr = [1, 2, 1, 1, 1], k = 3
累加和为3的最长子数组为[1, 1, 1]，所以结果返回3
[要求]
时间复杂度为O(n)O(n)，空间复杂度为O(1)O(1)

输入描述：
第一行两个整数N, k。N表示数组长度，k的定义已在题目描述中给出
第二行N个整数表示数组内的数
输出描述：
输出一个整数表示答案
示例1
输入：
5 3
1 2 1 1 1
输出：
3

"""


class Solution:

    def getMaxSublist(self, arr, k):
        res = []
        sum = 0
        maxlength = 0
        for i in arr:
            while(sum + i > k):
                first = res.pop(0)
                sum -= first
            sum += i
            res.append(i)
            if sum == k:
                maxlength = max(maxlength, len(res))
        return maxlength


if __name__ == '__main__':
    N, k = input().split(" ")
    arr = [int(item) for item in input().split(" ")]
    test = Solution()
    print(test.getMaxSublist(arr, int(k)))
