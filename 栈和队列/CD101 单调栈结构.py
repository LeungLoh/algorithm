# -*- encoding: utf-8 -*-
'''
Author: leungloh
Email: liangquanle@360.cn
version: @v1.0
Date: 2021/08/24 11:48:42
'''

"""
描述
给定一个不含有重复值的数组 arr，找到每一个 i 位置左边和右边离 i 位置最近且值比 arr[i] 小的位置。返回所有位置相应的信息。

输入描述：
第一行输入一个数字 n，表示数组 arr 的长度。

以下一行输出 n个数字，表示数组的值。
输出描述：
输出n行，每行两个数字 L 和 R，如果不存在，则值为-1，下标从0开始。
示例1
输入：
7
3 4 1 5 6 2 7
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
        s = list()
        res = [(-1, -1)] * n
        for index in range(n):
            if not s:
                s.append(index)
            else:
                while s and arr[s[-1]] > arr[index]:
                    i = s.pop()
                    l = s[-1] if s else -1
                    r = index
                    res[i] = (l, r)
                s.append(index)
        while s:
            i = s.pop()
            l = s[-1] if s else -1
            res[i] = (l, -1)
        return res


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split(" ")]
    test = Solution()
    res = test.mstack(n, arr)
    for item in res:
        print(item[0], item[1])
