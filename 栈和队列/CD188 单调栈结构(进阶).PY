# -*- encoding: utf-8 -*-
'''
Author: leungloh
Email: liangquanle@360.cn
version: @v1.0
Date: 2021/08/24 16:11:00
'''


"""
描述
给定一个可能含有重复值的数组 arr，找到每一个 i 位置左边和右边离 i 位置最近且值比 arr[i] 小的位置。返回所有位置相应的信息。
输入描述：
第一行输入一个数字 n，表示数组 arr 的长度。
以下一行输入 n 个数字，表示数组的值
输出描述：
输出n行，每行两个数字 L 和 R，如果不存在，则值为 -1，下标从 0 开始。
示例1
输入：
7
3 4 1 5 6 2 7
复制
输出：
-1 2
0 2
-1 -1
2 5
3 5
2 -1
5 -1
"""


class Solution:
    def mstack(self, n, arr):
        res = [[-1, -1] for i in range(n)]
        s = []
        for index in range(n):
            while s and arr[s[-1]] > arr[index]:
                res[s.pop()][1] = index
            if s:
                res[index][0] = s[-1] if arr[index] != arr[s[-1]] else res[s[-1]][0]
            s.append(index)
        return res


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split(" ")]
    test = Solution()
    res = test.mstack(n, arr)
    for item in res:
        print(item[0], item[1])
