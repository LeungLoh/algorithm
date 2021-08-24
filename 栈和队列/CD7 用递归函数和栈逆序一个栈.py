# -*- encoding: utf-8 -*-
'''
Author: leungloh
Email: liangquanle@360.cn
version: @v1.0
Date: 2021/08/23 15:55:07
'''

"""
描述
一个栈依次压入1,2,3,4,5，那么从栈顶到栈底分别为5,4,3,2,1。将这个栈转置后，从栈顶到栈底为1,2,3,4,5，也就是实现栈中元素的逆序，但是只能用递归函数来实现，不能用其他数据结构。
输入描述：
输入数据第一行一个整数N为栈中元素的个数。

接下来一行N个整数X_i表示从栈顶依次到栈底的每个元素。
输出描述：
输出一行表示栈中元素逆序后的每个元素
示例1
输入：
5
1 2 3 4 5
复制
输出：
5 4 3 2 1
"""


class Soultion():
    def reverse(self, start, end, s):
        if start < end:
            s[start], s[end] = s[end], s[start]
            self.reverse(start + 1, end - 1, s)
        else:
            return


if __name__ == '__main__':
    test = Soultion()
    n = int(input())
    s = input().split()
    test.reverse(0, n - 1, s)
    print(" ".join(s))
